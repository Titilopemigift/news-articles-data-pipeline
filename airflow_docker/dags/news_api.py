import pandas as pd
import psycopg2
import requests
from airflow.models import Variable

api_key = Variable.get("API_KEY")
db_host = Variable.get("DB_HOST")
db_name = Variable.get("DB_NAME")
db_user = Variable.get("DB_USER")
db_pass = Variable.get("DB_PASS")


NEWS_URL = "https://newsapi.org/v2/top-headlines"
COUNTRY = "us"
CATEGORY = "technology"


def fetch_news_data():
    """
    Fetch top headlines from News API and return as a clean Pandas DataFrame.
    """
    params = {
        "apiKey": api_key,
        "country": COUNTRY,
        "category": CATEGORY,
        "pageSize": 50
    }
    response = requests.get(NEWS_URL, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return pd.DataFrame()
    data = response.json()
    articles = data.get("articles", [])
    news_data = []
    for article in articles:
        news_data.append({
            "source": article.get("source", {}).get("name"),
            "author": article.get("author"),
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
            "published_at": article.get("publishedAt"),
            "content": article.get("content")
        })

    return pd.DataFrame(news_data)


def load_to_rds(df):
    """
    Load DataFrame into the RDS PostgreSQL database.
    """
    conn = psycopg2.connect(
        host=db_host,
        dbname=db_name,
        user=db_user,
        password=db_pass
    )
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO news_articles (source, author,
            title,description,url,published_at,content)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, tuple(row))
    conn.commit()
    cur.close()
    conn.close()


def run_pipeline():
    df_news_data = fetch_news_data()
    load_to_rds(df_news_data)

    return "Pipeline completed successfully"
