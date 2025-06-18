from langchain.tools import tool
from utils.gemini_api import call_gemini

@tool
def predict_hamiltonicity(image_path: str) -> str:
    return call_gemini("hamiltonicity_model", image_path)

@tool
def count_nodes(image_path: str) -> str:
    return call_gemini("node_count_model", image_path)

@tool
def count_edges(image_path: str) -> str:
    return call_gemini("edge_count_model", image_path)

@tool
def detect_planarity(image_path: str) -> str:
    return call_gemini("planarity_model", image_path)
