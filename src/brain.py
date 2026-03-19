from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Você é um assistente estilo Jarvis.

Interprete comandos do usuário e responda SOMENTE com ações quando necessário:

ADD_TASK: tarefa
ADD_GOAL: meta
ADD_EVENT: evento
GET_WEATHER: cidade

Se não for ação, responda normalmente sendo útil e direto.
"""

def think(messages):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.4
    )
    return response.choices[0].message.content