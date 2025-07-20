# src/langgraph_supplier_risk/main.py
import os, json
from dotenv import load_dotenv

from src.langgraph_supplier_risk.LLMS.groqllm import GroqLLM
from src.langgraph_supplier_risk.graph.graph_builder import GraphBuilder

def run_pipeline(suppliers: list[dict], controls: dict) -> list[dict]:
    load_dotenv()
    os.environ["NEWS_API_KEY"] = controls["NEWS_API_KEY"]
    os.environ["GROQ_API_KEY"]  = controls["GROQ_API_KEY"]

    llm   = GroqLLM(controls).get_llm_model()
    graph = GraphBuilder(llm).setup_graph("News Risk")

    # clear old results
    if os.path.exists("results.json"):
        os.remove("results.json")

    for sup in suppliers:
        state = {"supplier": sup}
        for _ in graph.stream(state):
            pass

    return json.load(open("results.json"))
