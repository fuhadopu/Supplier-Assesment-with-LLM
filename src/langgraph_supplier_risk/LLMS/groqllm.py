# src/langgraph_supplier_risk/LLMS/groqllm.py
import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, controls: dict):
        self.controls = controls

    def get_llm_model(self):
        api_key = self.controls.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
        model   = self.controls.get("selected_groq_model")
        if not api_key:
            st.error("❌ Groq API key is missing.")
            return None
        return ChatGroq(api_key=api_key, model=model)
