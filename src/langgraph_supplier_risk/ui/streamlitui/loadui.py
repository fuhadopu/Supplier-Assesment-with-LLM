import streamlit as st
from src.langgraph_supplier_risk.ui.config import UIConfig

class LoadStreamlitUI:
    def __init__(self):
        self.conf     = UIConfig()
        self.controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.conf.get_page_title(), layout="wide")
        st.title(self.conf.get_page_title())

        with st.sidebar:
            self.controls["selected_llm"] = st.selectbox(
                "LLM", self.conf.get_llm_options()
            )
            if self.controls["selected_llm"] == "Groq":
                self.controls["selected_groq_model"] = st.selectbox(
                    "Groq Model", self.conf.get_groq_model_options()
                )
                self.controls["GROQ_API_KEY"] = st.text_input(
                    "Groq API Key", type="password"
                )
            self.controls["NEWS_API_KEY"] = st.text_input(
                "NewsAPI Key", type="password"
            )

            names = st.text_input(
                "Suppliers (comma‑sep)", "Pegatron Corp, Luxshare ICT"
            )
            self.controls["suppliers"] = [
                {"name": n.strip()} for n in names.split(",") if n.strip()
            ]

        return self.controls

