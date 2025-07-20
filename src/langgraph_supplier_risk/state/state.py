# src/langgraph_supplier_risk/state/state.py
from typing_extensions import TypedDict

class State(TypedDict):
    supplier: dict
    raw_news: dict
    risk: dict
    result_path: str

