# src/langgraph_supplier_risk/graph/graph_builder.py
from langgraph.graph import StateGraph, START, END
from src.langgraph_supplier_risk.state.state import State
from src.langgraph_supplier_risk.nodes.data_acq_node import DataAcqNode
from src.langgraph_supplier_risk.nodes.risk_score_node import RiskScoreNode
from src.langgraph_supplier_risk.nodes.persist_node import PersistNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm   = llm
        self.graph = StateGraph(State)

    def setup_graph(self, usecase: str):
        if usecase == "News Risk":
            da = DataAcqNode()
            rs = RiskScoreNode(self.llm)
            pv = PersistNode()
            self.graph.add_node("acq",   da.process)
            self.graph.add_node("score", rs.process)
            self.graph.add_node("save",  pv.process)
            self.graph.add_edge(START,   "acq")
            self.graph.add_edge("acq",    "score")
            self.graph.add_edge("score",  "save")
            self.graph.add_edge("save",   END)
        return self.graph.compile()

