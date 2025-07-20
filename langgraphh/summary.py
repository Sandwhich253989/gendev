from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models.ollama import ChatOllama
from langchain_openai import ChatOpenAI


def summarize_chain(llmtype,model):
    llm = ChatOpenAI(model="gpt-4o-mini")
    if "openai" in llmtype:
        llm = ChatOpenAI(model=model)
    else:
        llm = ChatOllama(model=model)
    text_prompt = """
You are an agent , who is required to Summarize gathered requirements into a clear prompt:

Project Overview: Briefly describe the project.
Example: "Develop a customer engagement mobile app."

Goals: State the main goals.
Example: "Improve customer engagement and streamline inventory."

Features: List key features.
Example: "Real-time sales dashboard, email reminders, appointment booking."

Use Cases: Describe main use cases.
Example: "Managers check sales; customers book appointments."

Constraints: Note constraints and deadlines.
Example: "Budget: $50,000. Deadline: End of Q3."

Clarifications: Include specific clarifications.
Example: "Real-time updates every minute; CRM integration."


here is the context below : 
        """
    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = ChatPromptTemplate.from_messages([
        ('system', text_prompt),
        ('human', '{messages}')
    ])

    chain = prompt | llm
    return chain
