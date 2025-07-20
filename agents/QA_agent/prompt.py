from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models.ollama import ChatOllama
from langchain_openai import ChatOpenAI


def get_test_case(llmtype, model):
    llm = ChatOpenAI(model="gpt-4o-mini")
    if "openai" in llmtype:
        llm = ChatOpenAI(model=model)
    else:
        llm = ChatOllama(model=model)
    """
        Generates test cases for each plan described in JSON format.

        Returns:
        - chain: Used for generating test cases using an AI model.
    """
    prompt = """
    You are a Senior Quality Assurance Agent for a Software development company. Your goal is to create test cases from the 
    tasks given to you. The test cases will be used by QA to ensure the quality of the project.
    
    You will go through the tasks and create the test cases from the tasks mentioned.
    
    The following are the constraints for the test case creation:
    - Read the task description and the task type and create the test case description for the QA to test in manually.
    - The test case description should not be a mere replication of the task description but rather a detailed test case 
      on how the task will be tested.
    - Write the test steps that will help the QA to reproduce the scenario. Give sample values whenever necessary.
    - Write the test case type - positive and negative.
    - Write the expected result with actual value as given in the sample.
    - The format is as per the example provided below.
    
    Only display the test_cases with description that's all. Display all of these in only json format . 
    no extra unnecessary extra text like 'here are the test cases'. Wrap them all in json. also make sure to include 
    task_id in it. GIVE THE JSON FORMAT ONLY
    
    only display 
    all of these texts in json format, nothing else.
    ONLY GIVE IN JSON FORMAT DONT INCLUDE TEXT LIKE ```json , just the json  is enough

    for example: in your generation ,it should start with curly brackets opener not ```json and should end with curly 
    bracket closer not ```
    
    Note that the test cases shouldn't be mentioned in the test case description.
    
    for example : ⦃ "tasks":[ ⦃"test_cases":[⦃ "description":"...description...","type":"positive or negative" , 
    "test_steps":"Go to...", "expected_result": "..content.."⦄,.....],
     
     .
     .
     .
     .
     
    ]⦄
    it goes on
    "description": " give all of the points here" .
    dont try to create a new object for each test_case description
    make the test_case description as brief as possible with minimum 30 words for each plan
    remember , "test_steps" result should be in a string , not a list
    remember to close all curly brackets
    
    strictly follow the format given my be in the examples . no invalid characters allowed . do not even remove the plural forms
    plan:{plan}"""

    prompt_template = ChatPromptTemplate.from_messages([("user", prompt)])
    planner = prompt_template | llm
    return planner
