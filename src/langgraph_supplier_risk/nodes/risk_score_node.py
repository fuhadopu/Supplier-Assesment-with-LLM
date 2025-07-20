import json, streamlit as st, re, time
from langchain.schema import SystemMessage, HumanMessage
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from src.langgraph_supplier_risk.utils.normalize import clamp_score

# ---------- 1. define expected fields ----------
schemas = [
    ResponseSchema(name="score",     description="overall risk, integer 1‑5"),
    ResponseSchema(name="rationale", description="one‑sentence explanation"),
]
parser  = StructuredOutputParser.from_response_schemas(schemas)
fmt_instructions = parser.get_format_instructions()

SYSTEM = (
    "You are a supply‑chain risk analyst.\n"
    f"{fmt_instructions}\n"
    "Rate overall risk and give one‑sentence rationale.\n"
)

class RiskScoreNode:
    def __init__(self, llm, retry=1):    # retry once by default
        self.llm   = llm
        self.retry = retry

    # ---------- 2. helper ----------
    def _build_messages(self, supplier, articles):
        bullet_text = "\n".join(f"- {a['title']}: {a['desc']}" for a in articles)
        return [
            SystemMessage(content=SYSTEM),
            HumanMessage(content=f"Supplier: {supplier}\n\nNews:\n{bullet_text}"),
        ]

    # ---------- 3. main ----------
    def process(self, state: dict) -> dict:
        raw   = state["raw_news"]
        msgs  = self._build_messages(raw["supplier"], raw["articles"])

        for attempt in range(self.retry + 1):
            resp  = self.llm.invoke(msgs)
            text  = resp.content.strip()

            # remove ```json fences if present
            if text.startswith("```"):
                text = re.sub(r"^```[a-zA-Z]*\s*|\s*```$", "", text, flags=re.DOTALL)

            try:
                parsed = parser.parse(text)
                parsed["score"] = clamp_score(parsed["score"])
                parsed["supplier"] = raw["supplier"]
                state["risk"] = parsed
                return state                                     # success
            except Exception as e:
                st.warning(f"Groq JSON parse failed (try {attempt+1}): {e}")
                time.sleep(0.5)

        # if all retries fail
        st.error("LLM kept refusing JSON format; defaulting score=1.")
        state["risk"] = {"supplier": raw["supplier"], "score": 1, "rationale": ""}
        return state
