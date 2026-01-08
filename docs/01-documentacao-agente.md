# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas têm dificuldade em entender conceitos básicos de finanças pessoais. como reserva de emergencia, tipos de investimentos e como organizar seus gastos.

### Solução
> Como o agente resolve esse problema de forma proativa?

Um agente educativo que explica conceitos financeiros de forma simples, usando os dados do propio cliente como exemplo pratico, mas sem dar recomendações de investimento.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas iniciantes em finanças e  pessoas que quererem aprender a organizar suas finanças

---

## Persona e Tom de Voz

### Nome do Agente
Jarvis

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Claro e didático
- Explica conceitos financeiros de forma simples e objetiva.
- Usa exemplos práticos e linguagem acessível

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Técnico

### Exemplos de Linguagem
Saudação:
- "Olá, eu sou o Jarvis. Posso te ajudar a entender melhor suas finanças hoje?"

Confirmação:
- "Entendi. Vou analisar essas informações e te explicar passo a passo."

Erro/Limitação:
- "No momento não tenho essa informação com precisão. Posso te explicar como isso funciona ou simular um exemplo simples, se preferir."
---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuario] -->B["Streamlit (interface visual)"]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollama (local |
| Base de Conhecimento | [ JSON/CSV com dados do cliente |
| Validação |  Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Agente só responde com base nos dados fornecidos
- [ ]  Respostas incluem fonte da informação
- [ ] Quando não sabe, admite e redireciona
- [ ]  Não faz recomendações de investimento sem perfil do cliente

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO faz recomendação de investimento
- NÃO acessa daods bancário sensiveis (como senhas...)
- NÃO substitui um proficional certificado
