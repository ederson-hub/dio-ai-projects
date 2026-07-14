from strands import Agent
from strands_tools import calculator
from bedrock_agentcore import BedrockAgentCoreApp

SYSTEM_PROMPT = (
    "Voce e um assistente util para poder realizar calculos. "
    "use a ferramenta de calculadora para realizar os calculos que forem solicitados."
)

MODEL_ID = "us.amazon.nova-premier-v1:0"

agent = Agent(system_prompt=SYSTEM_PROMPT, model_id=MODEL_ID, tools=[calculator])

# Inicializa o Bedrock AgentCore
app = BedrockAgentCoreApp()

# Ponto de entrada do agente
@app.entrypoint
def invoke(payload, context):
    prompt = payload.get("prompt") or "Olá"
    result = agent(prompt)
    
    return {
        "response": result.message.content[0].text
    }

if __name__ == "__main__":
    app.run()