from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.ollama import ChatOllama
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_openai import ChatOpenAI

from configs import config

# Initialize the Tavily Search tool with a maximum of 2 search results
tool = TavilySearchResults(max_results=2)
tools = [tool]


# Function to generate the chat chain for code generation tasks
def generate_chain(llmtype, model):
    llm = ChatOpenAI(model="gpt-4o-mini")
    if "openai" in llmtype:
        llm = ChatOpenAI(model=model)
        # Define the text prompt for the AI coding co-pilot
        llm_with_tools = llm.bind_tools(tools)
    else:
        llm = ChatOllama(model=model)
        llm_with_tools = llm

    prompt = """
    You are a Senior Full stack developer Agent for a Software development company. Your goal is to generate code from the 
    tasks given to you. The code will be used by developers to deliver the project.
    
    You will go through the BRD, tasks and create the test cases from the context provided below.
    
    The following are the constraints for the code generation:
    - You will generate the code based on the type of the task. 
    - The framework for frontend (UI) and backend (API) will be in Typescript as part of Next JS framework.
    - The code will stick to best practices by following Clean code, and Gang Of Four design patterns.
    - If the task is to generate a flow diagram or design the architecture, then use mermaid format
    - If the task is to work with database tables, then MySQL is the database language
    - You don't have to create the entire project but only the component JSX and the API endpoint controller code as necessary.
   
    
    If you have the final answer or deliverable,
    prefix your response with FINAL ANSWER so the team knows to stop. Display the final solution/answer after the 
    FINAL ANSWER response and terminate the program. Here is the context below: 
    Here is the business related document: {brd} 
    Here is the problem below:
    """

    # Create a prompt template for the chat model with the system message and a placeholder for human messages
    chat_prompt = ChatPromptTemplate.from_messages([
        ('system', prompt),  # The system message with the text prompt
        MessagesPlaceholder("messages")  # Placeholder for human messages to be injected
    ])

    # Combine the prompt template and the language model with tools into a chain
    return chat_prompt | llm_with_tools
