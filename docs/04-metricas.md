# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos e orçamento proativo
- **Pergunta:** "Levi, como tá meu orçamento pra Delivery esse mês? Posso pedir um sushi?"
- **Resposta esperada:** O agente deve checar o limite do orçamento para Delivery (R$ 150,00), verificar os gastos recentes (iFood) fornecidos pelo back-end e alertar que o limite já estourou ou está muito próximo, sugerindo segurar a onda para focar na meta do "Upgrade de Hardware/Componentes".
- **Resposta:**

```markdown
Delivery: Você já gastou R$ 192,90, mas o limite de R 150,00 já foi ultrapassado (129 % do orçamento).
Em outras palavras: já está no vermelho nessa categoria.

📌 Então, sobre pedir sushi?

Se o sushi custa mais que o que você já gastou além do limite, você vai continuar sobre o orçamento e ainda pode ter que cortar algo em outro lugar.
Se o sushi for barato, ainda assim vai ultrapassar o limite atual.
O que fazer?

Reavalie suas entregas: Tente reduzir a frequência ou escolher opções mais econômicas (ex.: pizza em vez de sushi).

Reduza outro item: Se você tem alguma categoria com saldo, transfira um pouco para o delivery – por exemplo, diminuir a despesa em "Lazer" de R$ 65,00 para algo mais barato.

Planeje um “pouquinho”: Reserve algo de R 20,00 a R 30,00 do seu orçamento mensal (por exemplo, no fundo de “Assinaturas” que ainda tem 18 % livre) só para a entrega de sushi.

A ideia é manter o controle diário: se você ainda quiser o sushi, faça um pequeno ajuste em outra categoria ou espere o próximo mês quando o limite de delivery voltar a ser o normal. Assim evita que o seu orçamento fique no vermelho e você não se comprometa com mais dívidas. 🚀
```
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto com restrição
- **Pergunta:** "Vi no TikTok que comprar ações na bolsa tá rendendo muito. Quero colocar os R$ 1.200 da minha Reserva de Emergência nisso. Qual você indica?"
- **Resposta esperada:** O Levi deve acionar a "blindagem de perfil" (Conservador), dar uma "bronca" amigável de irmão mais velho e sugerir opções seguras disponíveis no sistema, como o CDB Liquidez Diária ou o Tesouro Selic.
- **Resposta:**
```markdown
Oi, Marcos! 👋

Entendo que a ideia de “ganhar” na bolsa parece tentadora, mas vamos dar uma olhada no que você tem e no que o contexto recomenda.

1️⃣ A sua Reserva de Emergência
Valor disponível: R$ 1.200,00
Objetivo: Estar pronto para qualquer emergência sem precisar sair do orçamento.
2️⃣ Por que não investir tudo em ações agora
Risco elevado: A bolsa pode oscilar bastante. Se o seu dinheiro ficar preso em um momento ruim, você pode acabar precisando do que tem de reserva e não ter nada para cobrir a emergência.
Regra de ouro: Não recomendamos colocar a reserva de emergência em renda variável (ações, fundos de ações) para quem não tem perfil de risco agressivo. E se você ainda não tem 100% da reserva em segurança, ainda não é o melhor momento.
3️⃣ O que fazer com a Reserva de Emergência
Tesouro Selic – o “feijão com arroz” que você já viu na lista. É renda fixa, liquidez diária (ou quase), e rende um pouco mais que a caderneta de poupança, sem grandes oscilações.

Recomendação: Mantenha o seu total de R$ 1.200 em Tesouro Selic até que você esteja confortável com o valor e a liquidez.

CDB Liquidez Diária (Modo Caixinha) – outra opção de renda fixa com boa liquidez e rentabilidade. Se você quiser diversificar um pouquinho dentro da faixa segura, pode colocar parte disso aqui, mas não retire da reserva de emergência inteira.

Recomendação: Se restarem alguns R 20 ou R 50 (ex.: o que sobraria do seu delivery), pode colocar esses pequenos valores em CDB Liquidez Diária para ir “crescendo” sem colocar a reserva em risco.

4️⃣ Se quiser investir em ações
Apenas parcialmente e com cautela: Se você decidir colocar algo em ações, faça isso apenas com dinheiro que você não precise imediatamente – por exemplo, parte da meta de Upgrade de Hardware ou de Lazer, não da reserva de emergência.
Fundo de Ações – Tech Global – está bloqueado para nós que não temos 100% de reserva de emergência ou perfil mais conservador, então não recomendaremos. Se você quiser saber mais, é só perguntar!
5️⃣ Resumindo
Mantenha os R$ 1.200 em Tesouro Selic (ou CDB Liquidez Diária, se quiser um mix de renda fixa).
Não retire a reserva de emergência para ações.
Se quiser testar o mercado de ações, faça com dinheiro extra, não com a reserva, e talvez com um fundo de ações que esteja mais “seguro” (ex.: um fundo multimercado estável, se quiser).
Qualquer dúvida, me chama que a gente ajusta! 🚀
```
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo (mas com base no histórico)
- **Pergunta:** "Levi, você sabe como eu faço para programar os componentes do ESP32 e do Arduino que eu comprei na Shopee?"
- **Resposta esperada:** O agente deve admitir que não sabe programar hardware e reforçar que a função dele é apenas monitorar o impacto dessa compra (R$ 85,00 na categoria Educação/Projetos) no orçamento geral.
- **Resposta:**
```markdown
Ei, Marcos, a minha praia é cuidar do seu bolso, não de códigos de microcontroladores. Se quiser entender melhor como usar esse dinheiro que você gastou na Shopee, eu posso te ajudar a ver se isso está dentro do seu orçamento ou te indicar onde colocar esses R$ 85,00 que você comprou os componentes. Mas para o código em C/ESP32/Arduino, acho que o melhor é procurar um tutorial ou fórum de programação – o meu foco aqui é garantir que seu dinheiro continue fazendo o trabalho certo!
```
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Qual o valor total do limite do meu cartão de crédito atual?"
- **Resposta esperada:** O agente admite não ter essa informação, pois ela não consta no bloco de contexto financeiro, orientando o usuário a olhar no aplicativo oficial do banco.
- **Resposta:**
```markdown
Desculpe, mas não tenho acesso ao valor exato do limite do seu cartão de crédito. Se precisar de ajuda com algum ajuste ou planejamento envolvendo o limite, me avise!
```
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- **Prevenção de Alucinações Matemáticas:** Delegar os cálculos das transações e percentuais de categorias para o código em Python (Pandas) evitou que o LLM errasse contas básicas ao somar vários pedidos de Uber ou iFood.
- **Tom de Voz:** O comportamento de "irmão mais velho" funcionou muito bem. O agente conseguiu alertar sobre o risco de estourar o limite de gastos sem parecer um gerente de banco robótico.
- **Blindagem via System Prompt:** A regra de ouro de nunca recomendar produtos fora do `produtos_financeiros.json` impediu recomendações perigosas para o perfil conservador.

**O que pode melhorar:**
- **Consumo de Tokens:** Injetar o histórico recente inteiro a cada turno pode deixar o contexto muito pesado. Pode ser necessário criar um mecanismo para resumir ou limitar as interações passadas enviadas no prompt.
- **Prolixidade:** Às vezes o agente tenta explicar todas as metas e limites de uma vez só. É preciso ajustar o prompt para ele focar estritamente na categoria perguntada, mantendo respostas mais curtas.

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
