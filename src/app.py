import json 
import requests
import pandas as pd
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# carregar dados
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# construção do system prompt 
def construir_system_prompt():
    system_prompt = """
    Você é o Levi, um agente financeiro inteligente focado em ajudar jovens profissionais e estudantes a gerenciar seu orçamento e atingir metas. 
    Sua personalidade é como a de um "irmão mais velho": você é empático, realista, direto ao ponto e usa uma linguagem acessível, sem jargões financeiros complexos (como CDI ou IPCA, a menos que perguntado). Você foca em micro-gestão do dia a dia.

    OBJETIVO:
    Analisar os dados de limite de orçamento e transações recentes fornecidos no contexto para dar conselhos práticos, proativos e evitar que o usuário gaste mais do que ganha.

    REGRAS ESTABELECIDAS:
    1. BASE DE DADOS: Você só pode usar as informações financeiras que estão no bloco [CONTEXTO] (limites, metas e gastos). Nunca invente valores ou transações.
    2. MATEMÁTICA: Não faça cálculos complexos. Confie nos valores totais e nas porcentagens já calculadas e fornecidas no [CONTEXTO].
    3. RECOMENDAÇÕES DE PRODUTOS: Se o usuário pedir onde guardar dinheiro, consulte a lista de produtos no contexto. Respeite RIGOROSAMENTE o campo "restricao_sistema". Nunca sugira renda variável para um perfil Conservador.
    4. TOM DE VOZ: Seja encorajador. Se precisar dar uma bronca sobre gastos excessivos, sugira uma alternativa mais barata logo em seguida.
    5. FORA DO ESCOPO: O seu escopo é ESTRITAMENTE financeiro. Se o usuário fizer perguntas técnicas sobre programação, eletrônica (como usar um ESP32/Arduino), receitas, esportes ou qualquer outro assunto que não seja dinheiro, orçamento, produtos financeiros ou as metas cadastradas, VOCÊ DEVE RECUSAR A RESPOSTA. Diga de forma amigável que o seu foco é apenas cuidar do bolso dele.

    EXEMPLO DE RESPOSTA FORA DO ESCOPO:
    Usuário: "Levi, me ajuda a fazer o código em C para piscar um LED no ESP32?"
    Levi: "Cara, minha praia é planilha e orçamento, não código em C! Meu negócio é monitorar aqueles R$ 85,00 que você gastou na Shopee comprando esses componentes e garantir que isso não atrapalhe a sua meta do mês. Pra programar isso aí, vou ficar te devendo!"
    """
    return system_prompt

# construção do contexto
def construir_contexto(perfil, transaçoes, historico, produtos):
    
    # Processa os dataframes e JSONs para criar uma string de contexto enxuta para o LLM.
    
    # informacoes básicas do usuário
    nome = perfil.get("nome", "Usuário")
    metas = "\n".join([f"- {m['nome']}: R$ {m['valor_atual']}/{m['valor_alvo']}" for m in perfil.get("metas_ativas", [])])

    gastos_categoria = transacoes.groupby('categoria')['valor'].sum().to_dict()

    alertas_orcamento = ""
    limites = perfil.get("orcamento_mensal", {})
    
    mapa_categorias = {
        "limite_delivery": "Delivery",
        "limite_transporte_app": "Transporte App",
        "limite_assinaturas": "Assinaturas",
        "limite_lazer": "Lazer"
    }    

    for chave_limite, nome_categoria in mapa_categorias.items():
        limite_valor = limites.get(chave_limite, 0)
        gasto_atual = gastos_categoria.get(nome_categoria, 0)
        
        if limite_valor > 0:
            porcentagem = (gasto_atual / limite_valor) * 100
            alertas_orcamento += f"- {nome_categoria}: Gasto R$ {gasto_atual:.2f} de R$ {limite_valor:.2f} ({porcentagem:.0f}% utilizado)\n"
            
    
    lista_produtos = "\n".join([
        f"- {p['nome']} ({p['categoria']}): {p.get('dica_do_levi', p.get('alerta_do_levi', 'Sem comentário adicional.'))} [Restrição: {p.get('restricao_sistema', 'Nenhuma')}]" 
        for p in produtos
    ])
    
    ultimos_papos = historico.tail(3)
    historico_str = "\n".join([f"- {row['data']} | Tema: {row['tema']} | Resumo: {row['resumo']}" for _, row in ultimos_papos.iterrows()])
        
    contexto_final = f"""
[DADOS DO CLIENTE]
Nome: {nome}
    
[METAS ATIVAS]
{metas}

[STATUS DO ORÇAMENTO]
{alertas_orcamento}

[PRODUTOS FINANCEIROS DISPONÍVEIS PARA RECOMENDAÇÃO]
{lista_produtos}
    
[HISTÓRICO RECENTE DE ATENDIMENTO]
{historico_str}
"""
    return contexto_final


def perguntar(msg):
    prompt = f"""
    {system_pronto}
    
    Contexto do cliente:
    {contexto_pronto}
    
    Pergunta: {msg}
    """
    
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']


contexto_pronto = construir_contexto(perfil, transacoes, historico, produtos)
system_pronto = construir_system_prompt()

# INTERFACE
st.title("Levi, Seu consultor de gastos e financias!")

if pergunta := st.chat_input("Digite sua dúvida aqui..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        resposta_bruta = perguntar(pergunta)
        
        resposta_formatada = resposta_bruta.replace("R$", "R\\$")
        
        st.chat_message("assistant").write(resposta_formatada)
