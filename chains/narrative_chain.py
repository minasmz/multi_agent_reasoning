from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import google.generativeai as genai

narrative_prompt = PromptTemplate.from_template(
    """
    Given the following graph analysis results:
    - Hamiltonicity: {ham}
    - Node Count: {nodes}
    - Edge Count: {edges}
    - Planarity: {planarity}

    Write a natural language explanation of the graph's properties and what they imply about its structure.
    """
)

llm = genai.GenerativeModel(model_name="gemini-narrator")
narrative_chain = LLMChain(llm=llm, prompt=narrative_prompt)
