# app.py
import os
import streamlit as st
from dotenv import load_dotenv

from src.langgraph_supplier_risk.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph_supplier_risk.ui.streamlitui.display_result import DisplayResultStreamlit
from src.langgraph_supplier_risk.main import run_pipeline

def main():
    load_dotenv()
    ui = LoadStreamlitUI()
    controls = ui.load_streamlit_ui()

    if st.sidebar.button("Run Assessment"):
        # Run the core pipeline
        results = run_pipeline(controls["suppliers"], controls)
        # Show the table + JSON
        DisplayResultStreamlit(controls["suppliers"]).display_result_on_ui()

if __name__ == "__main__":
    main()
