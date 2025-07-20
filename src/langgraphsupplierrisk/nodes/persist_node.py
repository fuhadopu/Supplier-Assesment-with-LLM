# src/langgraph_supplier_risk/nodes/persist_node.py
import json, os
from src.langgraph_supplier_risk.utils.normalize import normalize_score

class PersistNode:
    """Normalizes and saves the result to results.json."""
    def process(self, state: dict) -> dict:
        r = state["risk"]
        r["SRI"] = normalize_score(r["score"])
        path = "results.json"
        all_ = json.load(open(path)) if os.path.exists(path) else []
        all_.append(r)
        with open(path, "w") as f:
            json.dump(all_, f, indent=2)
        state["result_path"] = path
        return state
