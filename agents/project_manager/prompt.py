import re
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models.ollama import ChatOllama
from langchain_anthropic import ChatAnthropic
from datetime import datetime

from langchain_openai import ChatOpenAI


def get_plan(llmtype, model):
    llm = ChatOpenAI(model="gpt-4o-mini")
    if "openai" in llmtype:
        llm = ChatOpenAI(model=model)
    else:
        llm = ChatOllama(model=model)
    prompt = """
    remember!ONLY GIVE THE JSON TEXT NOTHING ELSE NO ```json ```
    You are a Project manager agent for a Software development company. Your goal is to create project plan from the
    Business Requirement Document (BRD). The project plan will be used by Developers and QA to deliver the project.
    
    You will go through the BRD and create the tasks from the user stories mentioned.
    
    The following are the constraints for the task creation:
    - The tasks will be split with actual description of the business feature that the user story is trying to achieve.
    - The tasks may be categorised into Architecture, Front end Development, API development, Table creation when necessary.
    - There can be more than 1 task per user story depending on the above categories.
    - You will estimate the time take to complete each task assuming the task is performed by a 3 years experienced full stack
    developer who has 8 hours in a work day.
    -  today's date is {date}. today's time is {time} You will start estimating the date or time from today and the estimate from above.
    - For each task , indicate the expected completion date/time (
    expected_completion_date) , estimated time of completion in hrs from the current date (
    estimated_time_completion_hrs) ,task_description, task_type. Describe your plans with rich details.only display 
    all of these texts in json format, nothing else.
    ONLY GIVE IN JSON FORMAT DONT INCLUDE TEXT LIKE ```json , just the json  is enough
    
    for example:
    in your generation ,it should start with curly brackets opener not ```json and should end with curly bracket closer not ```
    Here is the context/content:
    
    Task: {task}"""

    prompt_template = ChatPromptTemplate.from_messages([("user", prompt)])
    prompt_template = prompt_template.partial(date=datetime.now(), time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    planner = prompt_template | llm
    return planner
