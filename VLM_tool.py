from langchain.tools import tool
from PIL import Image

@tool
def describe_image(image_path: str) -> str:
    from openai import OpenAI
    client = OpenAI()
    with open(image_path, "rb") as img:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": [
                    {"type": "text", "text": "Describe the image."},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_img}"}}
                ]}
            ]
        )
    return response.choices[0].message.content
