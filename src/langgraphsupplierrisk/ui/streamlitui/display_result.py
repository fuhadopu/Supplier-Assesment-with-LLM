# src/langgraph_supplier_risk/ui/streamlitui/display_result.py
import streamlit as st
import pandas as pd
import json

class DisplayResultStreamlit:
    def __init__(self, suppliers: list):
        self.suppliers = suppliers

    def display_result_on_ui(self):
        st.header("News‑Based Risk Results")
        # Load only the last N results
        try:
            all_res = json.load(open("results.json"))
        except FileNotFoundError:
            st.error("No results found. Please run the assessment.")
            return

        # Display table
        df = pd.DataFrame([
            {
                "Supplier": r["supplier"],
                "Score (1–5)": r["score"],
                "Rationale": r["rationale"],
                "SRI (0–1)":   r["SRI"]
            }
            for r in all_res[-len(self.suppliers):]
        ])
        st.dataframe(df)
        # Raw JSON
        st.markdown("#### Raw JSON Outputs")
        for r in all_res[-len(self.suppliers):]:
            st.json(r)
