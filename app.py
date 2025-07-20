import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import streamlit as st
from dotenv import load_dotenv

from src.langgraph_supplier_risk.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph_supplier_risk.main import run_pipeline
from src.langgraph_supplier_risk.ui.streamlitui.display_result import DisplayResultStreamlit

def main():
    load_dotenv()
    ui = LoadStreamlitUI()
    controls = ui.load_streamlit_ui()

    if st.sidebar.button("Run Assessment"):
        results = run_pipeline(controls["suppliers"], controls)
        DisplayResultStreamlit(controls["suppliers"]).display_result_on_ui()

if __name__ == "__main__":
    main()

