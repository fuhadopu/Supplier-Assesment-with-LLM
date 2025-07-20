# src/langgraph_supplier_risk/apis/news_api.py
import os, requests, datetime

def fetch_news(supplier: str, days: int = 14) -> dict:
    key = os.getenv("NEWS_API_KEY")
    since = (
        datetime.date.today() - datetime.timedelta(days=days)
    ).isoformat()
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={supplier}&from={since}&sortBy=popularity&apiKey={key}"
    )
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    articles = resp.json().get("articles", [])[:5]
    return {
        "supplier": supplier,
        "articles": [
            {"title": a["title"], "desc": a.get("description","")}
            for a in articles
        ],
    }
