import json
import pandas as pd
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

perfil = json.load(open('data/perfil_investidor.json',))
transacoes = pd.read_csv('data/transacoes.csv')
historico = pd.read_csv('data/historico_atendimento.csv')
produtos = json.load(open('data/produtos_financeiros.json',))

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, profissão: {perfil['profissao']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}
TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}
ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}
PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

SYSTEM_PROMPT ="""Você é o Jarvis, um educador financeiro claro e didático.
OBJETIVO:
Ensinar conceitos de finanças pessoais de forma prática e aplicada, usando os dados do cliente como exemplos reais sempre que possível, para que ele consiga entender e aplicar no dia a dia.
REGRAS:
- Sempre baseie suas respostas nos dados fornecidos pelo cliente.
- Nunca invente informações financeiras.
- Se não souber algo, admita e ofereça alternativas ou caminhos para o cliente buscar a informação.
- Explique cada conceito passo a passo, usando exemplos práticos do cotidiano do cliente sempre que possível.
- Priorize clareza e simplicidade, evitando jargões complexos sem explicação.
- Sempre destaque os impactos positivos e negativos das decisões financeiras.
- Incentive hábitos de planejamento, controle e tomada de decisão consciente.
- Responda de forma empática, respeitando a situação e o nível de conhecimento financeiro do cliente.
- Estruture explicações com tópicos, exemplos e comparações quando necessário para facilitar a compreensão.
- Foque em criar aprendizado ativo, estimulando o cliente a refletir e aplicar os conceitos na própria vida.
- Não responda perguntas que não estejam relacionadas ao tema de finanças pessoais, educação financeira ou organização financeira. Caso a pergunta fuja desse contexto, informe educadamente que o assunto está fora do escopo.
"""

def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    CONTEXTO DO CLIENTE:
     {contexto}
    Pergunta: {msg}"""   
    r = requests.post(OLLAMA_URL, json={"model":MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

st.title("Jarvis - Seu Educador Financeiro Virtual")
if pergunta := st.chat_input("Faça sua pergunta sobre finanças: "):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
