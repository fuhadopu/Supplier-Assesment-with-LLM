# src/langgraph_supplier_risk/nodes/data_acq_node.py
from src.langgraph_supplier_risk.apis.news_api import fetch_news

class DataAcqNode:
    """Fetches news for a supplier."""
    def process(self, state: dict) -> dict:
        supplier = state["supplier"]["name"]
        state["raw_news"] = fetch_news(supplier)
        return state
