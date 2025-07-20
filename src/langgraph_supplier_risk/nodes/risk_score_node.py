# src/langgraph_supplier_risk/nodes/risk_score_node.py
import json
import streamlit as st


SYSTEM_PROMPT = """
You are a supply‑chain risk analyst.
Based on these news items for {supplier}, rate risk 1–5 and give a 1‑sentence rationale.
Respond in JSON: {{ "supplier":str, "score":int, "rationale":str }}
"""

class RiskScoreNode:
    def __init__(self, llm):
        self.llm = llm

    def process(self, state: dict) -> dict:
        raw = state["raw_news"]
        prompt = SYSTEM_PROMPT.format(supplier=raw["supplier"])
        content = "\n".join(f"- {a['title']}: {a['desc']}" for a in raw["articles"])
        resp = self.llm.invoke(f"{prompt}\n\nNews:\n{content}")
        text = getattr(resp, "text", resp)
        try:
            scores = json.loads(text)
        except Exception as e:
            st.error(f"⚠️ Failed to parse LLM JSON: {e}")
            scores = {"supplier": raw["supplier"], "score": 1, "rationale": ""}
        state["risk"] = scores
        return state

