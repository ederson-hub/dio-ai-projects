# 🍕 Assistente de Delivery com Amazon Bedrock e AWS Step Functions

## 📌 Sobre o Projeto

Este projeto demonstra a construção de um **Assistente Inteligente de Delivery** utilizando serviços de Inteligência Artificial Generativa da AWS.

O fluxo utiliza o **Amazon Bedrock** para gerar recomendações personalizadas de refeições e a **AWS Step Functions** para orquestrar todo o processo de conversação, permitindo criar um assistente capaz de sugerir pratos, bebidas, sobremesas e outras combinações de acordo com as preferências do cliente.

---

## Arquitetura

```
Usuário
   │
   ▼
AWS Step Functions
   │
   ▼
Amazon Bedrock
(Claude 3 Haiku)
   │
   ▼
Resposta Gerada
   │
   ▼
Cliente
```

---

## Serviços Utilizados

- Amazon Bedrock
- AWS Step Functions
- Amazon Claude 3 Haiku
- IAM
- CloudWatch (Logs)

---

## Objetivo

Criar um fluxo automatizado capaz de:

- Receber solicitações do cliente
- Enviar prompts para um modelo de IA no Amazon Bedrock
- Gerar sugestões personalizadas
- Retornar recomendações em linguagem natural

Exemplo de perguntas:

- Quero um jantar romântico.
- Sugira uma bebida para acompanhar uma pizza.
- Qual sobremesa combina com um hambúrguer?
- Monte um combo vegetariano.

---

## Fluxo da Solução

1. O usuário envia uma solicitação.
2. A AWS Step Functions inicia a execução.
3. O estado **InvokeModel** envia o prompt para o Amazon Bedrock.
4. O modelo Claude 3 Haiku processa a solicitação.
5. A resposta é retornada para a máquina de estados.
6. O resultado é entregue ao usuário.

---

## Exemplo de Prompt

```
Estou programando um jantar romântico.

Nesse jantar irei pedir um macarrão.

Me dê uma lista com:

- bebida
- entrada
- sobremesa
```

---

## Exemplo de Resposta

```
🍷 Bebida
Vinho Tinto Cabernet Sauvignon

🥗 Entrada
Bruschetta Italiana

🍰 Sobremesa
Petit Gateau com Sorvete de Baunilha
```

---

## Estrutura da Step Function

```
Initialize
      │
      ▼
InvokeModel (Amazon Bedrock)
      │
      ▼
Process Result
      │
      ▼
Success
```

---

## Exemplo do Payload

```json
{
  "ModelId": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-haiku-20240307-v1:0",
  "Body": {
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "text": "Sugira um jantar romântico com massa."
          }
        ]
      }
    ],
    "inferenceConfig": {
      "maxTokens": 500
    }
  },
  "ContentType": "application/json",
  "Accept": "application/json"
}
```

---

## Pré-requisitos

- Conta AWS
- Amazon Bedrock habilitado
- Acesso ao modelo Claude 3 Haiku
- Permissões IAM para:
  - Bedrock
  - Step Functions
  - CloudWatch Logs

---

## Permissões IAM

A role da Step Function deve possuir permissões semelhantes a:

```json
{
    "Effect": "Allow",
    "Action": [
        "bedrock:InvokeModel"
    ],
    "Resource": "*"
}
```

---

## Tecnologias

| Tecnologia | Descrição |
|------------|-----------|
| Amazon Bedrock | IA Generativa |
| Claude 3 Haiku | Modelo LLM |
| AWS Step Functions | Orquestração |
| IAM | Controle de acesso |
| CloudWatch | Monitoramento |

---

## Possíveis Melhorias

- Histórico de conversa
- Memória de contexto
- Integração com Amazon DynamoDB
- Integração com API Gateway
- Integração com AWS Lambda
- Consulta ao cardápio em banco de dados
- Recomendações baseadas em preferências do cliente
- Integração com sistemas de pagamento
- Integração com aplicativos de delivery

---

## Benefícios

- Arquitetura serverless
- Escalabilidade automática
- Fácil manutenção
- Alta disponibilidade
- Baixa necessidade de infraestrutura
- IA Generativa integrada

---

## Resultado Esperado

O assistente é capaz de compreender solicitações em linguagem natural e gerar recomendações contextualizadas utilizando os modelos fundacionais do Amazon Bedrock.

---

## Autor

Desenvolvido como projeto de estudo utilizando serviços de IA Generativa da AWS.