from langchain.tools import tool
import google.generativeai as genai


def call_gemini(model_name, image_path):
    model = genai.GenerativeModel(model_name=model_name)
    with open(image_path, "rb") as img_file:
        response = model.generate_content([
            {"type": "image", "data": img_file.read()},
            {"type": "text", "text": f"Analyze the graph for {model_name.replace('_', ' ')}."}
        ])
    return response.text

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
