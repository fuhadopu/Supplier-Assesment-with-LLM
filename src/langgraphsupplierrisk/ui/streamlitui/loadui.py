# src/langgraph_supplier_risk/ui/streamlitui/loadui.py
import streamlit as st
from ..config import UIConfig

class LoadStreamlitUI:
    def __init__(self):
        self.config = UIConfig()
        self.controls = {}

    def load_streamlit_ui(self):
        # Page setup
        st.set_page_config(
            page_title=self.config.get_page_title(), layout="wide"
        )
        st.header(self.config.get_page_title())

        # Sidebar controls
        with st.sidebar:
            # LLM selectors
            self.controls["selected_llm"] = st.selectbox(
                "Select LLM", self.config.get_llm_options()
            )
            if self.controls["selected_llm"] == "Groq":
                self.controls["selected_groq_model"] = st.selectbox(
                    "Groq Model", self.config.get_groq_model_options()
                )
                self.controls["GROQ_API_KEY"] = st.text_input(
                    "Groq API Key", type="password"
                )
            # News API key
            self.controls["NEWS_API_KEY"] = st.text_input(
                "NewsAPI Key", type="password"
            )
            # Suppliers list
            names = st.text_input(
                "Suppliers (comma‑sep)", "Pegatron Corp, Luxshare ICT"
            )
            self.controls["suppliers"] = [
                {"name": n.strip()} for n in names.split(",") if n.strip()
            ]

        return self.controls
