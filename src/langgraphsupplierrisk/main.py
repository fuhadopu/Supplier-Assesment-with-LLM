# src/langgraph_supplier_risk/main.py
import os, json
from dotenv import load_dotenv
from .graph.graph_builder import GraphBuilder
from .ui.config import UIConfig

def run_pipeline(suppliers: list[dict], controls: dict):
    # 1. Load secrets
    load_dotenv()
    os.environ.update({
        "NEWS_API_KEY": controls["NEWS_API_KEY"],
        "GROQ_API_KEY":  controls["GROQ_API_KEY"]
    })

    # 2. Build LLM + Graph
    from .LLMS.groqllm import GroqLLM
    llm   = GroqLLM(controls).get_llm_model()
    graph = GraphBuilder(llm).setup_graph("News Risk")

    # 3. Clear results
    if os.path.exists("results.json"):
        os.remove("results.json")

    # 4. Execute per-supplier
    for sup in suppliers:
        state = {"supplier": sup}
        for _ in graph.stream(state):
            pass

    # 5. Return parsed results
    return json.load(open("results.json"))

if __name__ == "__main__":
    # simple CLI test
    example_suppliers = [{"name":"Pegatron Corp"},{"name":"Luxshare ICT"}]
    example_controls = UIConfig().load_from_env()
    results = run_pipeline(example_suppliers, example_controls)
    print(json.dumps(results, indent=2))
