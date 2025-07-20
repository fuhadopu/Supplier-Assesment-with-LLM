# src/langgraph_supplier_risk/nodes/data_acq_node.py
from langgraph_supplier_risk.apis.news_api import fetch_news

class DataAcqNode:
    def process(self, state: dict) -> dict:
        name = state["supplier"]["name"]
        state["raw_news"] = fetch_news(name)
        return state

