# API Conversacional com RAG para Dados Climáticos

Projeto pessoal de estudo e experimentação com APIs em Python, modelos generativos e a arquitetura RAG (*Retrieval-Augmented Generation*). A proposta é construir uma API conversacional que permita consultar dados climáticos armazenados em um banco de dados (Brazilian Daily Weather Gridded Data - BR-DWGD).

## Estado atual

Esta é uma versão inicial do projeto. A API recebe uma pergunta em linguagem natural e usa o Google Gen AI SDK para gerar uma consulta SQL direcionada ao banco `dados_br_dwgd`.

Por enquanto, a aplicação **não se conecta ao banco de dados** (pois este ainda será criado), não executa a consulta gerada e ainda não implementa recuperação de contexto (RAG). A integração com os dados e o fluxo de recuperação fazem parte dos próximos passos de estudo.

## Pacotes utilizados

- Python
- FastAPI e Pydantic
- Google Gen AI SDK (`google-genai`)
- Gemini, para geração de consultas SQL

## Requisitos

- Python 3.10 ou superior
- Uma chave de API do Gemini, disponível no [Google AI Studio](https://aistudio.google.com/app/apikey)

## Configuração

No Linux ou macOS, crie e ative um ambiente virtual e instale as dependências:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install fastapi uvicorn google-genai
```

Configure a chave para a sessão atual do terminal sem colocá-la no código ou em arquivos versionados:

```bash
read -rsp "Cole sua chave Gemini: " GEMINI_API_KEY
echo
export GEMINI_API_KEY
```

Inicie o servidor na raiz do projeto:

```bash
uvicorn climate_data_assistant:app --reload
```

A documentação interativa do FastAPI ficará disponível em <http://127.0.0.1:8000/docs>.

## Endpoint

### `POST /chat`

Recebe uma pergunta sobre os dados climáticos:

```json
{
  "message": "Qual foi a temperatura média em janeiro?"
}
```

Exemplo de resposta:

```json
{
  "mensagem_original": "Qual foi a temperatura média em janeiro?",
  "query_gerada": "SELECT AVG(temperatura) FROM ..."
}
```

A consulta retornada é texto gerado pelo modelo: ela não é executada nem validada contra o banco de dados.

## Próximos passos de estudo

- Conectar a API a um banco de dados climáticos e documentar seu esquema.
- Criar um fluxo de ingestão e recuperação de contexto para implementar RAG.
- Validar e restringir consultas SQL antes de qualquer execução.
- Adicionar testes para o endpoint e para a integração com o modelo.
- Tratar configuração, erros e observabilidade da aplicação.
