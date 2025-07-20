from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models.ollama import ChatOllama
from langchain_community.chat_models.ollama import ChatOllama


# Function to create a chain for generating a Business Requirement Document (BRD)
def brd_chain():
    # Define the text prompt for the business analytics agent
    text_prompt = """
You are an expert business analytics agent for a Software development company that is tasked to create a comprehensive Business Requirement Document (BRD).

Identify the project's business goals and objectives.
Detail the target audience and their needs.
Outline the functionalities and features required to achieve the goals in detail and organize them by module or feature.
Specify any non-functional requirements, such as performance, security, and usability.
Include user stories or use cases to illustrate the desired functionality.
Define success metrics to measure the project's effectiveness.
(Optional) If applicable, include any existing system information or limitations.
Generate a workflow if applicable of the platform journey in mermaid format.
here is the context below:
    """

    # Initialize the language model (ChatGPT) with the specified model
    llm = ChatOllama(model="mistral")

    # Create a prompt template for the chat model
    prompt = ChatPromptTemplate.from_messages([
        ('system', text_prompt),  # The system message with the text prompt
        ('human', '{messages}')  # Placeholder for human messages to be injected
    ])

    # Combine the prompt template and the language model into a chain
    chain = prompt | llm

    # Return the created chain
    return chain
