# src/langgraph_supplier_risk/utils/normalize.py
def normalize_score(score: int) -> float:
    """Map 1–5 → 0.0–1.0."""
    return round((score - 1) / 4, 3)
