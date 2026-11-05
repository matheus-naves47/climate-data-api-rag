# Importações
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

# A chave é lida da variável de ambiente GEMINI_API_KEY.
# No terminal, export GEMINI_API_KEY="chave"

client = genai.Client()

model_name = "gemini-3.8-flash"

# Define o aplicativo
app = FastAPI(title="Assistente de Dados Climáticos",
              description="API simples para consultar dados climáticos.",
              version="1.0.0")

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
def answer_question(user_message: UserMessage):
    # 1. Criar o prompt )

    prompt = f"""
    Você é um assistente de análise de dados, responsável por retornar informações sobre dados climáticos de acordo com a solicitação do usuário.
    
    A solicitação do usuário é: "{user_message.message}"

    Escreva apenas uma consulta SQL válida que possa ser executada em um banco de dados chamado 'dados_br_dwgd'  para obter os dados climáticos solicitados.

    Não inclua explicações, apenas a consulta SQL. A consulta deve ser escrita em uma única linha.
    """

    # 2. Solicitar a geração do conteúdo

    gemini_response = client.models.generate_content(
        model=model_name,
        contents=prompt,
    )
    if gemini_response.text is None:
        raise HTTPException(
            status_code=502,
            detail="O Gemini não retornou conteúdo textual.",
        )
    generated_query = gemini_response.text.strip()

    # 3. Retornar a consulta SQL gerada
    return{
        "mensagem_original": user_message.message,
        "query_gerada": generated_query
    }