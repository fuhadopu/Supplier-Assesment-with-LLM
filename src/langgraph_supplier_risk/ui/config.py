# src/langgraph_supplier_risk/ui/config.py
import configparser, pathlib

class UIConfig:
    def __init__(self, ini_path=None):
        self.ini = configparser.ConfigParser()
        ini = ini_path or (pathlib.Path(__file__).parent / "uiconfigfile.ini")
        self.ini.read(ini)

    def get_page_title(self):
        return self.ini["DEFAULT"]["PAGE_TITLE"]

    def get_llm_options(self):
        return [x.strip() for x in self.ini["DEFAULT"]["LLM_OPTIONS"].split(",")]

    def get_usecase_options(self):
        return [x.strip() for x in self.ini["DEFAULT"]["USECASE_OPTIONS"].split(",")]

    def get_groq_model_options(self):
        return [x.strip() for x in self.ini["DEFAULT"]["GROQ_MODEL_OPTIONS"].split(",")]

    def load_from_env(self):
        import os
        return {
            "GROQ_API_KEY":       os.getenv("GROQ_API_KEY",""),
            "NEWS_API_KEY":       os.getenv("NEWS_API_KEY",""),
            "selected_llm":       self.get_llm_options()[0],
            "selected_groq_model":self.get_groq_model_options()[0],
            "selected_usecase":   self.get_usecase_options()[0]
        }
