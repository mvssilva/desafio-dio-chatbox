# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Lembrar de combinados passados (ex: "Semana passada você prometeu segurar no iFood, lembra?"). |
| `perfil_investidor.json` | JSON | Identificar a renda mensal, metas de curto prazo (ex: viagem, comprar notebook) e limites de gastos por categoria. |
| `produtos_financeiros.json` | JSON | Sugerir apenas produtos de altíssima liquidez para a construção da reserva de emergência. |
| `transacoes.csv` | CSV | Analisar a frequência e o volume de gastos nas categorias "vilãs" (Delivery, App de Transporte, Assinaturas). |
---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui:

- Para que o agente consiga gerar os alertas proativos de orçamentos, os dados mockados originais foram expandidos com os seguintes atributos:
1. Adição de Categorias no transacoes.csv: Adicionada uma coluna Categoria para classificar os gastos (ex: Lazer, Alimentação, Transporte, Moradia, Assinaturas). Isso permite que o agente identifique para onde o dinheiro está vazando.
2. Definição de Limites no perfil_investidor.json: Foi criado um novo bloco de dados chamado orcamento_mensal, contendo tetos de gastos. Exemplo: "limite_delivery": 200.00.
3. Data e Hora nas Transações: Inclusão de timestamps realistas para permitir alertas contextuais (ex: identificar que é sexta-feira à noite e o usuário já está perto do limite de lazer).

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os dados estáticos (perfil e produtos) são carregados via JSON no início da sessão. Os dados dinâmicos (transações e histórico) são processados via código Python (utilizando Pandas) sempre que o usuário envia uma mensagem ou quando o sistema roda uma verificação de rotina para alertas proativos.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Não enviamos o CSV inteiro para o LLM. Para evitar alucinações matemáticas e economizar tokens, a aplicação faz a totalização dos gastos via código e injeta dinamicamente apenas o resumo do contexto no System Prompt.
O LLM recebe apenas a "fotografia" do momento: quanto o usuário já gastou, qual é o limite da categoria e qual a meta em risco.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.
[CONTEXTO FINANCEIRO ATUALIZADO]
Cliente: Marcos
Status do Mês: Dia 22 (Restam 8 dias para o salário)
Saldo Atual em Conta: R$ 450,00
Meta Principal Ativa: "Reserva para Viagem fim do ano" (Progresso: 40%)

--- ALERTA DE ORÇAMENTO (CALCULADO VIA SISTEMA) ---
Categoria: Delivery / iFood
- Limite Mensal: R$ 250,00
- Gasto Acumulado: R$ 230,00 (92% utilizado)
- Última transação: R$ 45,00 em 21/10 (Hamburgueria)

[MENSAGEM DO USUÁRIO]
"Lira, tô com preguiça de cozinhar hoje, rola pedir uma pizza?"

