# src/langgraph_supplier_risk/graph/graph_builder.py
from langgraph.graph import StateGraph, START, END
from src.langgraph_supplier_risk.state.state import State
from src.langgraph_supplier_risk.nodes import (
    DataAcqNode, RiskScoreNode, PersistNode
)

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph_builder = StateGraph(State)

    def build_news_risk_graph(self):
        da = DataAcqNode()
        rs = RiskScoreNode(self.llm)
        pv = PersistNode()
        self.graph_builder.add_node("acq",   da.process)
        self.graph_builder.add_node("score", rs.process)
        self.graph_builder.add_node("save",  pv.process)
        self.graph_builder.add_edge(START,   "acq")
        self.graph_builder.add_edge("acq",    "score")
        self.graph_builder.add_edge("score",  "save")
        self.graph_builder.add_edge("save",   END)

    def setup_graph(self, usecase: str):
        if usecase == "News Risk":
            self.build_news_risk_graph()
            return self.graph_builder.compile()
