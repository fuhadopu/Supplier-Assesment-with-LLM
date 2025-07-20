# src/langgraph_supplier_risk/apis/news_api.py
import os, requests
from datetime import date, timedelta

def fetch_news(supplier: str, days: int = 14) -> dict:
    key = os.getenv("NEWS_API_KEY")
    since = (date.today() - timedelta(days=days)).isoformat()
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={supplier}&from={since}&sortBy=popularity&apiKey={key}"
    )
    r = requests.get(url, timeout=15); r.raise_for_status()
    arts = r.json().get("articles", [])[:5]
    return {
        "supplier": supplier,
        "articles": [{"title": a["title"], "desc": a.get("description","")} for a in arts]
    }
