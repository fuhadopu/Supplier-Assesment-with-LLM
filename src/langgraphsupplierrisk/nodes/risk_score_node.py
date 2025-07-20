# src/langgraph_supplier_risk/nodes/risk_score_node.py
import json
from streamlit import st

SYSTEM_PROMPT = """
You are a supply‑chain risk analyst.
Based on the following news headlines/descriptions for {supplier},
assign a risk score from 1 (low) to 5 (high) and give a 1‑sentence rationale.
Respond in valid JSON: {{ "supplier":str, "score":int, "rationale":str }}
"""

class RiskScoreNode:
    def __init__(self, llm):
        self.llm = llm

    def process(self, state: dict) -> dict:
        raw = state["raw_news"]
        prompt = SYSTEM_PROMPT.format(supplier=raw["supplier"])
        content = "\n".join(
            f"- {a['title']}: {a['desc']}" for a in raw["articles"]
        )
        resp = self.llm.invoke(prompt + "\n\nNews:\n" + content)
        try:
            scores = json.loads(resp)  # parse JSON
        except Exception as e:
            st.error(f"Failed to parse LLM response: {e}")
            scores = {"supplier": raw["supplier"], "score": 1, "rationale": ""}
        state["risk"] = scores
        return state
