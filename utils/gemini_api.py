import google.generativeai as genai
import base64

def call_gemini(model_name, image_path):
    model = genai.GenerativeModel(model_name=model_name)

    with open(image_path, "rb") as img_file:
        image_bytes = img_file.read()
        base64_img = base64.b64encode(image_bytes).decode("utf-8")

    response = model.generate_content([
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_img}"}},
        {"type": "text", "text": f"Analyze the graph for {model_name.replace('_', ' ')}."}
    ])

    return response.text
