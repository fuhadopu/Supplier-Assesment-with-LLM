import streamlit as st
import pandas as pd
import json

class DisplayResultStreamlit:
    def __init__(self, suppliers: list):
        self.suppliers = suppliers

    def display_result_on_ui(self):
        try:
            all_res = json.load(open("results.json"))
        except FileNotFoundError:
            st.error("No results—run assessment first.")
            return

        df = pd.DataFrame([
            {
                "Supplier":   r["supplier"],
                "Score (1–5)":r["score"],
                "Rationale":  r["rationale"],
                "SRI (0–1)":  r["SRI"]
            } for r in all_res[-len(self.suppliers):]
        ])
        st.header("News‑Based Risk Results")
        st.dataframe(df)
        st.markdown("#### Raw JSON")
        for r in all_res[-len(self.suppliers):]:
            st.json(r)
