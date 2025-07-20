<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">GENDEV</h1>
</p>
<p align="center">
    <em>Efficient Dev. SolutionsSlogan: Unlock Conversational Potential!</em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=default&logo=JSON&logoColor=white" alt="JSON">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#overview)
- [ Features](#features)
- [ Repository Structure](#repository-structure)
- [ Modules](#modules)
- [ Agents Overview](#agents-overview)
- [ Getting Started](#getting-started)
  - [ Installation](#installation)
  - [ Usage](#usage)
  - [ Tests](#tests)
- [ API Endpoints](#api-endpoints)
- [ Project Roadmap](#project-roadmap)
- [ Contributing](#contributing)
- [ License](#license)
- [ Acknowledgments](#acknowledgments)
</details>
<hr>

##  Overview

GenDev-Interactive Conversational Graph Project OverviewGenDev is an innovative Python project designed to facilitate more effective conversations between agents and users through an interactive conversational graph. This project generates summarized versions of conversations dynamically, taking into account the progression of conversations based on defined context patterns. Its main components include the state manager for handling task details and the summary generator to offer concise information about each context.The GenDev project interacts with a Postman collection for API calls, managing database schema using SQLite scripts (create_db_code, create_table_project, create_table_task, create_table_test_cases), and offering utility functions via db_manager and display_tables modules. These components contribute to efficient handling of conversational tasks, API interactions, and database management in GenDevs broader architecture.

---

##  Features



---

##  Repository Structure

```sh
└── GenDev/
    ├── agents
    │   ├── business_analytics_agent
    │   ├── dev_agent
    │   ├── one_singular_agent.py
    │   ├── project_manager
    │   ├── QA_agent
    │   └── time
    ├── configs
    │   └── config.py
    ├── fastapi_routers
    │   ├── __init__.py
    │   ├── brd
    │   ├── dev
    │   ├── display
    │   ├── pm
    │   ├── qa
    │   └── requirements
    ├── langgraphh
    │   ├── context.py
    │   ├── graph_router.py
    │   ├── main.py
    │   ├── state.py
    │   └── summary.py
    ├── postman_collection
    │   └── gendev.postman_collection.json
    ├── README.md
    ├── requirements.txt
    ├── main.py
    ├── sql_scripts
    │   ├── create_db_code.sql
    │   ├── create_table_project.sql
    │   ├── create_table_task.sql
    │   └── create_table_test_cases.sql
    ├── sqlite3_db
    │   ├── agent.db
    │   └── chat-history.sqlite
    └── util
        ├── db_manager.py
        └── display_tables.py
```

---

##  Modules

<details closed><summary>agents</summary>

| File                                                  | Summary                                                                                                                                                                                                                                                                                                                       |
| ---                                                   | ---                                                                                                                                                                                                                                                                                                                           |
| [one_singular_agent.py](agents/one_singular_agent.py) | This script serves as a central conductor, activating agents tailored for business analytics, project management, QA, and development within a given project. By calling appropriate functions, it synchronizes the workflows of each agent, ensuring efficient and coordinated execution across multiple domains. (50 words) |

</details>

<details closed><summary>agents.business_analytics_agent</summary>

| File                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [graph_router.py](agents/business_analytics_agent/graph_router.py) | This `graph_router.py` script builds and configures the state graph for the Business Analytics Agent, enhancing communication within the language-based system by defining and connecting nodes based on business rule data chains (brd_node). This facilitates seamless interaction between different components of our AI solution.                                                                                                                                  |
| [main.py](agents/business_analytics_agent/main.py)                 | Generates a Business Requirements Document (BRD) from user input by analyzing the given summary through a graph-based model and stores the output BRD in the project database. This agent within the GenDev repository facilitates streamlining project planning by leveraging automated analysis of business requirements.                                                                                                                                            |
| [prompt.py](agents/business_analytics_agent/prompt.py)             | In this repository, the file `agents/business_analytics_agent/prompt.py` provides functionality for creating a chain of commands, specifically designed to generate a comprehensive Business Requirement Document (BRD) for software projects. This chain leverages the OpenAI language model and offers prompts tailored for a business analytics agent. The output from this process contributes to a detailed blueprint essential for successful project execution. |
| [state.py](agents/business_analytics_agent/state.py)               | Manages and processes data for the Business Analytics Agent.**The `state.py` file defines the data structure used to store and manage messages within the Business Analytics Agent of GenDev repository. It leverages the langgraph' library's message handling function, ensuring efficient communication between modules.                                                                                                                                            |

</details>

<details closed><summary>agents.dev_agent</summary>

| File                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [functions.py](agents/dev_agent/functions.py)       | In this Python file (`dev_agent/functions.py`), a function called `generate_chain()` is created within the Dev Agent of a software development projects codebase. This function sets up an artificial intelligence (AI) chat tool, binding a Tavily Search tool and ChatGPT model.The purpose of this AI is to act as a coding copilot for developers. Given context from business requirements documents (BRD) and task descriptions, it generates the necessary code components within Typescript, following best practices such as Clean Code, Gang Of Four design patterns, and more, according to the provided constraints. |
| [graph_router.py](agents/dev_agent/graph_router.py) | Manages communication between development agents and language model using a state graph in real-time interactions. It constructs nodes for generating responses and tool calls, routes the state based on message content, and builds the state graph dynamically. This contributes to the seamless flow of dialogues within the parent projects intelligent development assistant architecture.                                                                                                                                                                                                                                 |
| [main.py](agents/dev_agent/main.py)                 | This main.py script initiates a development agent within a larger GenDev repository, focusing on automating code generation for given tasks in a project. It fetches problem descriptions and test cases for specific task IDs, generates code using state graphs, stores the produced code in the database, and updates the task status accordingly. This results in completed code ready for testing or use in further stages of software development.                                                                                                                                                                         |
| [state.py](agents/dev_agent/state.py)               | This file (state.py) defines a data structure for an agents state, managing its messages, code logs, and board status within the GenDev project. By using a TypedDict with Langgraphs graph integration (add_messages), it ensures seamless communication among various components, enhancing the overall system's flexibility.                                                                                                                                                                                                                                                                                                  |

</details>

<details closed><summary>agents.project_manager</summary>

| File                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [graph_router.py](agents/project_manager/graph_router.py) | In this GenDev project, the graph_router.py file defines an integral part of the agent architecture. It constructs and manages the state graph for the Project Manager Agent, allowing it to dynamically generate action plans from given tasks in a conversational AI context, according to project configurations.                                                                                                                                                                                                                                                                   |
| [main.py](agents/project_manager/main.py)                 | Get_brd, fetching BRD content for a specific project ID; 2) run_pm_agent, executing a graph process based on a projects BRD content and storing the generated plan within the database; 3) store_plan, responsible for storing the generated plan JSON data in the database. These functionalities streamline communication between the project manager agent and other components within the GenDev architecture, facilitating effective project management.                                                                                                                          |
| [plan.json](agents/project_manager/plan.json)             | This `plan.json` file outlines a projects task schedule within the GenDev repository. It details four distinct tasks including Table Creation, API Development, Front End Development, and Architecture Integration, all targeting the insurance quote application with scheduled completion dates and estimated hours required.                                                                                                                                                                                                                                                       |
| [prompt.py](agents/project_manager/prompt.py)             | This Python script, `agents/project_manager/prompt.py`, serves as a blueprint for a Project Manager Agent within the GenDev project. Its main purpose is to construct a plan for software development projects from Business Requirement Documents (BRDs). It accomplishes this by creating tasks with rich descriptions, categorizing them, and estimating time completion based on the assumption of an experienced full-stack developer working 8 hours a day. The resulting project plan is provided in JSON format to facilitate efficient execution by development and QA teams. |
| [state.py](agents/project_manager/state.py)               | The `state.py` module in the project_manager agent, within the larger GenDev repository, manages and organizes the state of a project. It defines a class named `State`, which encapsulates key details like the plan in string format and a list of messages derived from the language graph. This organization aids efficient tracking and communication of project progress.                                                                                                                                                                                                        |

</details>

<details closed><summary>agents.QA_agent</summary>

| File                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [graph_router.py](agents/QA_agent/graph_router.py) | In this open-source project, the Python script `graph_router.py` located within the `QA_agent` directory serves as a graph construction module. It creates a testing scenario by invoking test cases from the specified agent. By compiling these individual test case functions into a graph structure, it enables automated testing and verification processes, fostering better Quality Assurance practices in the project.                                  |
| [main.py](agents/QA_agent/main.py)                 | This Main module in the QA_agent directive fetches task plans for a specified project from a local database. It constructs a graph using these tasks and streams data based on the graph. The run_qa_agent function gathers test cases and stores them within the SQLite database, updating or adding as required.                                                                                                                                              |
| [prompt.py](agents/QA_agent/prompt.py)             | This code file, located at `agents/QA_agent/prompt.py`, serves as a tool for generating test cases by creating prompts for an AI model within the GenDev repository. Specifically, it creates concise and structured test cases in JSON format, derived from project plans provided, to assist Quality Assurance agents with their testing efforts. These generated test cases help ensure that software developed meets specified standards before deployment. |
| [state.py](agents/QA_agent/state.py)               | Manages QA agents state within project architecture, storing essential information like messages, test cases, and plans as typed dicts for easy processing by the language graph module, facilitating efficient test case execution and analysis.                                                                                                                                                                                                               |

</details>

<details closed><summary>agents.time</summary>

| File                                     | Summary                                                                                    |
| ---                                      | ---                                                                                        |
| [timestamp.py](agents/time/timestamp.py) | M:S format, providing a timestamp for various system interactions across this application. |

</details>

<details closed><summary>configs</summary>

| File                           | Summary                                                                                                                                                                                                                                                                                              |
| ---                            | ---                                                                                                                                                                                                                                                                                                  |
| [config.py](configs/config.py) | Configures and manages environment variables for multiple APIs and services within this GenDev project, such as LangChain, OpenAI, Anthropic, Tavily, Bing, and others. It streamlines API access by setting essential keys, facilitating seamless integration across various agent functionalities. |

</details>

<details closed><summary>main.py</summary>

| File                               | Summary                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                | ---                                                                                                                                                                                                                                                                                                                                                                                        |
| [main.py](main.py) | This repository structure hosts various agents like business analytics, development, QA, etc., with main.py orchestrating API routing for fast and efficient interactions. By integrating different routers, such as upload file, get plan, and display tables, the application centralizes data retrieval and streamlines access across its modules, enhancing usability and flexibility. |

</details>

<details closed><summary>fastapi_routers.brd</summary>

| File                                                 | Summary                                                                                                                                                                                                                                                                                                                                          |
| ---                                                  | ---                                                                                                                                                                                                                                                                                                                                              |
| [upload_file.py](fastapi_routers/brd/upload_file.py) | This Fastapi router facilitates file uploading and text input for generating Business Report Documents (BRDs) directly into the GenDev database. The upload_file.py code handles both uploaded files and user-provided text, leveraging a custom `gen_brd` function and connecting with the SQLite database to store generated BRDs efficiently. |

</details>

<details closed><summary>fastapi_routers.dev</summary>

| File                                           | Summary                                                                                                                                                                                                                                                            |
| ---                                            | ---                                                                                                                                                                                                                                                                |
| [gen_code.py](fastapi_routers/dev/gen_code.py) | Generates custom software codes for various projects based on provided task/project IDs within the specified database using APIs. Provides error handling and logging, ensuring seamless execution for optimal workflow within GenDevs fastapi-based architecture. |

</details>

<details closed><summary>fastapi_routers.display</summary>

| File                                           | Summary                                                                                                                                                                                                                                                                             |
| ---                                            | ---                                                                                                                                                                                                                                                                                 |
| [tables.py](fastapi_routers/display/tables.py) | In this FastAPI router, functions are defined to display data from various tables (projects, tasks, test cases, codes) either as a whole or by specific IDs. It ensures efficient and error-handled table visualization in the web application of this GenDev project architecture. |

</details>

<details closed><summary>fastapi_routers.pm</summary>

| File                                          | Summary                                                                                                                                                                                                                                                                                                     |
| ---                                           | ---                                                                                                                                                                                                                                                                                                         |
| [get_plan.py](fastapi_routers/pm/get_plan.py) | This `get_plan.py` fastAPI route retrieves project plans by triggering the Project Manager agent within the system. By invoking the agent with specified project ID and assigned user, it collects and stores generated tasks in the database, ensuring efficient resource allocation for ongoing projects. |

</details>

<details closed><summary>fastapi_routers.qa</summary>

| File                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [get_test_cases.py](fastapi_routers/qa/get_test_cases.py) | In this FastAPI router, a function called `get_test_cases()` is defined that communicates with the QA agent and generates test cases for a specific project based on its id (`proj_id`) and assigned user (`assigned_to`). Upon successful generation, the test cases are stored in the local database. On encountering any errors during this process, it logs an error message along with an identification code to help trace issues later. |

</details>

<details closed><summary>fastapi_routers.requirements</summary>

| File                                          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                           | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [req.py](fastapi_routers/requirements/req.py) | The `fastapi_routers/requirements/req.py` file creates an endpoint (`/requirements/query/`) for querying requirements within the API, using data provided by users in the `Requirements` model. The code leverages a graph function from the `langgraphh` module to process the queries and returns the generated response to users, while handling any errors by logging them and returning an appropriate message. In the broader context of this repository, this file contributes to providing a seamless user experience for requesting requirements within the architecture defined by this GenDev project. |

</details>

<details closed><summary>langgraphh</summary>

| File                                          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                           | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [context.py](langgraphh/context.py)           | The context.py file within the langgraphh module serves as a foundation for a sophisticated chatbot designed to elicit, document, and clarify detailed project requirements from users through iterative conversations. This scripts primary goal is to achieve an unambiguous understanding of user needs, ensuring no misinterpretation arises by utilizing structured steps to engage in open-ended discussions, delving into specific features, clarifying doubts, exploring use cases, identifying constraints, and systematically documenting requirements. The outcome of the script is a concise summary of discussed requirements for future reference. |
| [graph_router.py](langgraphh/graph_router.py) | Generate and summary, dynamically evaluating the conversations progress through conditional edges. The final output is an organized, summarized version of the entire discourse based on defined context patterns.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [main.py](langgraphh/main.py)                 | This main file, located within the langgraphh module, triggers the construction of an interactive conversational graph. It processes user-initiated queries by streaming them through the constructed graph, receiving responses from integrated agents for further analysis. Ultimately, it returns the final content of the processed query, enhancing the projects language-based services.                                                                                                                                                                                                                                                                   |
| [state.py](langgraphh/state.py)               | Manages project state by storing relevant data, including messages, task status, plan, steps, results, and chat history. This class interacts with other modules for efficient handling of conversational tasks within the broader GenDev architecture.                                                                                                                                                                                                                                                                                                                                                                                                          |
| [summary.py](langgraphh/summary.py)           | An overview, goals, key features, use cases, constraints, and clarifications for the given context. In essence, it consolidates essential project information into a cohesive, succinct format for easy understanding.                                                                                                                                                                                                                                                                                                                                                                                                                                           |

</details>

<details closed><summary>postman_collection</summary>

| File                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [gendev.postman_collection.json](postman_collection/gendev.postman_collection.json) | Fetch project details by its ID 6" under the gen-code-by-proj-id API endpoint with no response expected.-Submit user requirement text for a customizable motor insurance app via the requirements/query endpoint, with no response expected.-Upload text about project overview, goals, features, use cases, constraints regarding custom motor insurance quotes web application with no response expected.In summary: Three API interactions take place in this data. The first request fetches project details by ID 6", the second action submits a description of a customizable motor insurance application as user requirements, and finally, an overview of a potential custom motor insurance quotes web app is uploaded. |

</details>

<details closed><summary>sql_scripts</summary>

| File                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                           |
| [create_db_code.sql](sql_scripts/create_db_code.sql)                   | In this SQL repository, youll find a script that **creates the code' table** essential for storing, organizing, and managing various pieces of written code related to specific tasks within the project's context. This database structure is instrumental in facilitating collaboration and efficient tracking of development progress.                                                     |
| [create_table_project.sql](sql_scripts/create_table_project.sql)       | Defines database schema for projects within GenDev, including project_id, brd, and created_date columns, ensuring data consistency for every project registered.                                                                                                                                                                                                                              |
| [create_table_task.sql](sql_scripts/create_table_task.sql)             | In this SQL script, we define the Task table that stores task-related information within our projects database. Each row contains details like ID, project ID, description, estimate, status, assigned team member, type, and timestamps for creation and modification. The Project ID is linked to the Project table for effective project-task association in our application architecture. |
| [create_table_test_cases.sql](sql_scripts/create_table_test_cases.sql) | In this project, the provided SQL script (sql_scripts/create_table_test_cases.sql) establishes a Test Cases table within the projects SQLite database, linking test cases to specific tasks through foreign keys, facilitating efficient tracking and management of software testing processes.                                                                                               |

</details>

<details closed><summary>util</summary>

| File                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [db_manager.py](util/db_manager.py)         | Database connectivity in this multi-agent Python project, using SQLite as the underlying database system. The `db_manager.py` module ensures seamless and consistent interaction with the SQLite database instances. It provides a function to connect to databases, offering flexibility in handling multiple projects. Optionally, it offers a create-table function for setting up database structure according to specific project requirements.                                                                                                                                                                                                                                                                                |
| [display_tables.py](util/display_tables.py) | This script contains functions to manage and display data related to projects and codes in an SQLite database. It initializes an empty dictionary for storing code data indexed by task ID, and a similar one for project data indexed by project ID. Functions are provided to add new code records (with the given code_id, code, and dates) to the relevant task ID record in the code dictionary, and similarly for projects. There is also a function to fetch and display all rows from the code or project table matching a given ID, filling the respective dictionaries accordingly. This setup facilitates organizing related data (like codes for each project) into convenient structures for later analysis or output. |

</details>

---
# Agents Overview

The GenDev project consists of four main agents: Business Analytics Agent (BRD), Project Manager Agent, QA Agent, and Dev Agent. These agents work together to streamline software development projects, from requirement gathering to code generation and testing.

## Business Analytics Agent (BRD)

The Business Analytics Agent is responsible for generating a Business Requirements Document (BRD) from user input. It analyzes the given summary through a graph-based model and stores the output BRD in the project database. This agent plays a crucial role in project planning, ensuring that business requirements are well-defined and communicated to the development team.

## Project Manager Agent

The Project Manager Agent takes the generated BRD and creates a project plan, including task schedules and resource allocation. It uses a graph-based model to dynamically generate action plans from given tasks in a conversational AI context. The agent stores the generated plan in the database, making it accessible to the development and QA teams.

## QA Agent

The QA Agent is responsible for testing and verifying the generated code. It fetches task plans from the database, constructs a graph, and generates test cases based on the project plan. The agent stores the test cases in the database, updating or adding as required. This ensures that the developed software meets the specified standards before deployment.

## Dev Agent

The Dev Agent is a coding copilot for developers, generating code components based on the project plan and business requirements. It uses a state graph to manage communication with the language model and generates code in accordance with best practices, such as Clean Code and Gang of Four design patterns. The agent stores the generated code in the database, making it accessible and easy to fetch for the developers.

## Relationships between Agents

The agents are interconnected, with each agent building upon the output of the previous one:

1. The Business Analytics Agent generates a BRD, which is used by the Project Manager Agent to create a project plan.
2. The Project Manager Agent's output is used by the Dev Agent to generate code components.
3. The Dev Agent's output is tested and verified by the QA Agent, ensuring that the developed software meets the specified standards.

By working together, these agents enable efficient and coordinated execution across multiple domains, streamlining software development projects from requirement gathering to deployment.

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the GenDev repository:
>
> ```console
> $ git clone https://github.com/impelox-ai/GenDev.git
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd GenDev
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run GenDev using the command below:
> ```console
> $ fastapi run .\main.py
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

### API Endpoints

#### 1. Requirements Query
- **URL:** `http://localhost:8000/requirements/query`
- **Method:** `POST`
- **Description:** Send a query related to requirements.
- **Request Body:** (raw json)
  - `query`: The query text.
  - `thread_id`: The ID of the thread.
  - `llmtype`: The type of the LLM to use. (ollama/openai)
  - `model`: The name of the model


- **Sample Input:**
  ```json
  {
    "query":"make a project on generating readme files from git repository",
    "thread_id":"6",
    "llmtype":"openai",
    "model":"gpt-4o-mini"
  }
  ```
- **Sample Response Output:**
  ```json
  {
    "user": "make a project on generating readme files from git repository",
    "genai_response": "Great! Let's start by understanding your overarching goals for the project on generating README files from a Git repository.**Open-Ended Start:** What are the primary objectives you aim to achieve with this project?"
  }
  ```
#### 2. Upload Text
- **URL:** `http://localhost:8000/upload/text`
- **Method:** `POST`
- **Description:** Upload requirements text to the server.
- **Request Body:**
  - `text`: The text content to be uploaded.
  ```json
  {
    "text":"Project Overview:\nDevelop a Python software that generates random numbers for a dice game.\n\nGoals:\nThe primary goal is to create a simple Python program that generates random numbers between 1 and a certain number (e.g., 6) when a user enters a dice roll command.\n\nFeatures:\n\n* Generates a random number between 1 and a certain number (e.g., 6) when a user enters a dice roll command.\n* Does not include additional features or functionalities, such as scoring rules or graphical interfaces.\n\nUse Cases:\nA user enters a dice roll command to generate a random number for a game.\n\nConstraints:\n\n* Budget: N/A\n* Deadline: N/A\n\nClarifications:\nThe program should only generate random numbers for a dice game and does not require any additional features."
  }
  ```
- **Output structure**
  ```json
  {
  "result": "Successfully generated and stored the BRD doc in database", 
  "text": "Project Overview:\nDevelop a Python software that generates random numbers for a dice game.\n\nGoals:\nThe primary goal is to create a simple Python program that generates random numbers between 1 and a certain number (e.g., 6) when a user enters a dice roll command.\n\nFeatures:\n\n* Generates a random number between 1 and a certain number (e.g., 6) when a user enters a dice roll command.\n* Does not include additional features or functionalities, such as scoring rules or graphical interfaces.\n\nUse Cases:\nA user enters a dice roll command to generate a random number for a game.\n\nConstraints:\n\n* Budget: N/A\n* Deadline: N/A\n\nClarifications:\nThe program should only generate random numbers for a dice game and does not require any additional features."
  }
  ```
#### 3. Upload Document
- **URL:** `http://localhost:8000/upload/document/`
- **Method:** `POST`
- **Description:** Upload a document to the server.
- **Request Body:**
  - `file`: The file to be uploaded.

#### 4. Display Table by Name
- **URL:** `http://localhost:8000/display/table/{table_name}`
- **Method:** `GET`
- **Description:** Display the content of a table by its name.


- **Sample Input:**
  ```http request
  http://localhost:8080/display/table/task
  ```
- **Sample Response output:**
  ```json
  {
    "proj_id_6": [
        {
            "task_id": 40,
            "task_description": "Customize quote creation steps",
            "estimate": "2024-07-17 19:22:08",
            "estimated_time": "16",
            "status": "not completed",
            "assigned_to": "\"me\"",
            "task_type": "Architecture",
            "created_date": "2024-07-05 12:12:36",
            "modified_date": "2024-07-12 19:17:41"
        },
        {
            "task_id": 41,
            "task_description": "Allow users to input car's age for accurate insurance quotes",
            "estimate": "2024-07-18 19:22:08",
            "estimated_time": "8",
            "status": "not completed",
            "assigned_to": "\"me\"",
            "task_type": "Front end Development",
            "created_date": "2024-07-05 12:12:36",
            "modified_date": "2024-07-12 19:17:41"
        },
    ],
    "proj_id_7": [
        {
            "task_id": 55,
            "task_description": "Develop the Python software that generates random numbers for a dice game based on user input.",
            "estimate": "2024-08-02 13:43:16",
            "estimated_time": "12",
            "status": "Completed",
            "assigned_to": "\"me\"",
            "task_type": "Front end Development",
            "created_date": "2024-07-25 05:43:34",
            "modified_date": "2024-07-25 05:43:34"
        },
        {
            "task_id": 56,
            "task_description": "Implement the logic for generating random numbers within a specified range (e.g., between 1 and 6)",
            "estimate": "2024-08-02 13:43:16",
            "estimated_time": "5",
            "status": "Completed",
            "assigned_to": "\"me\"",
            "task_type": "API development",
            "created_date": "2024-07-25 05:43:34",
            "modified_date": "2024-07-25 05:43:34"
        },
    ]
  }
  ```
- **Response Visualization:** 
  ```html
  <style type="text/css">
      .tftable {font-size:14px;color:#333333;width:100%;border-width: 1px;border-color: #87ceeb;border-collapse: collapse;}
      .tftable th {font-size:18px;background-color:#87ceeb;border-width: 1px;padding: 8px;border-style: solid;border-color: #87ceeb;text-align:left;}
      .tftable tr {background-color:#ffffff;}
      .tftable td {font-size:14px;border-width: 1px;padding: 8px;border-style: solid;border-color: #87ceeb;}
      .tftable tr:hover {background-color:#e0ffff;}
  </style>
  <table class="tftable" border="1">
      <tr>
          <th>Task ID</th>
          <th>Task Description</th>
          <th>Estimate</th>
          <th>Estimated Time</th>
          <th>Status</th>
          <th>Assigned To</th>
          <th>Task Type</th>
          <th>Created Date</th>
          <th>Modified Date</th>
      </tr>
      {{#each response.proj_id_4}}
          <tr>
              <td>{{task_id}}</td>
              <td>{{task_description}}</td>
              <td>{{estimate}}</td>
              <td>{{estimated_time}}</td>
              <td>{{status}}</td>
              <td>{{assigned_to}}</td>
              <td>{{task_type}}</td>
              <td>{{created_date}}</td>
              <td>{{modified_date}}</td>
          </tr>
      {{/each}}
  </table>
  ```

#### 5. Display Table by Name and ID
- **URL:** `http://localhost:8000/display/table-by-id/?table_name={table_name}&index={index}`
- **Method:** `GET`
- **Description:** Display the content of a table by its name and a specific ID.
- **Query Parameters:**
  - `table_name`: The name of the table.
  - `index`: The specific ID within the table. For example , 1. if the table name is project or task , input the proj_id index . 2. If the table name is test_case or code , input the task id index to display all test_cases.
  

- **Sample Input**:
  ```text
  http://localhost:8000/display/table-by-id/?table_name=test_case&index=40
  ```
- **Sample Response Output**
  ```json
  {
    "task_id_40": [
        {
            "test_case_id": 128,
            "test_case_description": "Test customizable quote creation steps for insurers",
            "assigned_to": "\"me\"",
            "created_date": "2024-07-05 12:13:30",
            "modified_date": "2024-07-08 14:50:08",
            "test_case_type": "positive",
            "test_steps": "1. Navigate to the quote creation page\n2. Input different values for customization\n3. Save the customized quote",
            "expected_result": "The customized quote is successfully saved with the input values"
        },
        {
            "test_case_id": 129,
            "test_case_description": "Test customizable quote creation steps for insurers with invalid input",
            "assigned_to": "\"me\"",
            "created_date": "2024-07-05 12:13:30",
            "modified_date": "2024-07-08 14:50:08",
            "test_case_type": "negative",
            "test_steps": "1. Navigate to the quote creation page\n2. Input invalid values for customization\n3. Save the quote",
            "expected_result": "An error message is displayed indicating invalid input"
        }
    ]
  }
  ```
#### 6. Generate Tasks
- **URL:** `http://localhost:8000/pm/get-plan/?proj_id=7&assigned_to="me"`
- **Method:** `GET`
- **Description:** Generate tasks for a specific project.
- **Query Parameters:**
  - `proj_id`: The ID of the project.
  - `assigned_to`: The assignee for the tasks.
  - `llmtype`: The type of the LLM to use. (ollama/openai)
  - `model`: The name of the model
- **Sample Input:**
  ```http request
  http://localhost:8000/pm/get-plan/?proj_id=7&assigned_to="me"&llmtype=openai&model=gpt-4o-mini
  ```
- **Sample Response Output:**
  ```json
  {
    "result": "Generated and stored the plan in database successfully",
    "plan": [
        {
            "task_description": "Design the architecture for the Python program that generates random numbers for the dice game.",
            "task_type": "Architecture",
            "estimated_time_completion_hrs": 4,
            "expected_completion_date": "2024-07-26T15:12:47"
        },
        {
            "task_description": "Implement the core function that generates a random number between 1 and a defined maximum (e.g., 6) when the 'roll' command is issued.",
            "task_type": "API development",
            "estimated_time_completion_hrs": 6,
            "expected_completion_date": "2024-07-27T15:12:47"
        },
        {
            "task_description": "Create a simple text-based user interface that allows users to enter the 'roll' command.",
            "task_type": "Front end Development",
            "estimated_time_completion_hrs": 4,
            "expected_completion_date": "2024-07-27T15:12:47"
        },
        {
            "task_description": "Test the random number generation functionality to ensure it meets performance requirements (response time < 1 second).",
            "task_type": "QA",
            "estimated_time_completion_hrs": 3,
            "expected_completion_date": "2024-07-28T15:12:47"
        },
        {
            "task_description": "Provide documentation for the program, including clear instructions for use and expected outputs.",
            "task_type": "Documentation",
            "estimated_time_completion_hrs": 2,
            "expected_completion_date": "2024-07-28T15:12:47"
        }
    ]
  } 
  ```
- **Response Visualization:**
  ```html
  <style type="text/css">
      .tftable {font-size:14px;color:#333333;width:100%;border-width: 1px;border-color: #87ceeb;border-collapse: collapse;}
      .tftable th {font-size:18px;background-color:#87ceeb;border-width: 1px;padding: 8px;border-style: solid;border-color: #87ceeb;text-align:left;}
      .tftable tr {background-color:#ffffff;}
      .tftable td {font-size:14px;border-width: 1px;padding: 8px;border-style: solid;border-color: #87ceeb;}
      .tftable tr:hover {background-color:#e0ffff;}
  </style>
  <table class="tftable" border="1">
      <tr>
          <th>Expected Completion Date</th>
          <th>Estimated Time (hrs)</th>
          <th>Task Description</th>
          <th>Task Type</th>
      </tr>
      {{#each response.plan}}
          <tr>
              <td>{{expected_completion_date}}</td>
              <td>{{estimated_time_completion_hrs}}</td>
              <td>{{task_description}}</td>
              <td>{{task_type}}</td>
          </tr>
      {{/each}}
  </table>
  ```

#### 7. Generate Test Cases
- **URL:** `http://localhost:8000/qa/get-test-cases/?proj_id=7&assigned_to="me"`
- **Method:** `GET`
- **Description:** Generate test cases for a specific project.
- **Query Parameters:**
  - `proj_id`: The ID of the project.
  - `assigned_to`: The assignee for the test cases.
  - `llmtype`: The type of the LLM to use. (ollama/openai)
  - `model`: The name of the model
  

- **Sample Input:**
  ```http request
  http://localhost:8000/qa/get-test-cases/?proj_id=7&assigned_to="me"&llmtype=openai&model=gpt-4o-mini
  ```
- **Sample Response Output:**
  ```json
   {
    "result": "Generated and stored the test cases in database successfully",
    "plan": [
        {
            "task_id": 55,
            "test_cases": [
                {
                    "description": "Verify that the architecture design of the Python program includes clear modules and components for random number generation in the dice game, ensuring scalability and maintainability.",
                    "type": "positive",
                    "test_steps": "Review the architecture document for the Python program and ensure it outlines modules such as Random Number Generator, User Interface, and Game Logic with clear interactions.",
                    "expected_result": "Architecture document includes defined modules and interactions."
                }
            ]
        },
        {
            "task_id": 56,
            "test_cases": [
                {
                    "description": "Test the core function that generates a random number to ensure it correctly returns a value between 1 and the defined maximum when the 'roll' command is issued.",
                    "type": "positive",
                    "test_steps": "Invoke the core function with a maximum value of 6 and issue the 'roll' command. Check if the returned value is between 1 and 6.",
                    "expected_result": "Returned value is between 1 and 6."
                },
                {
                    "description": "Ensure that the core function does not return values outside the defined range when the 'roll' command is issued.",
                    "type": "negative",
                    "test_steps": "Invoke the core function with a maximum value of 6 and call the 'roll' command multiple times. Record the output values and check for any values less than 1 or greater than 6.",
                    "expected_result": "No output values are less than 1 or greater than 6."
                }
            ]
        },
        {
            "task_id": 57,
            "test_cases": [
                {
                    "description": "Evaluate the text-based user interface to confirm that it correctly accepts the 'roll' command from users and provides appropriate feedback.",
                    "type": "positive",
                    "test_steps": "Access the user interface and enter the 'roll' command. Observe the response from the system to ensure it indicates the number generated.",
                    "expected_result": "System provides feedback with the generated number."
                }
            ]
        },
        {
            "task_id": 58,
            "test_cases": [
                {
                    "description": "Conduct a performance test on the random number generation functionality to confirm it meets the requirement of a response time of less than 1 second.",
                    "type": "positive",
                    "test_steps": "Initiate the random number generation and measure the time taken to respond after issuing the 'roll' command. Perform this multiple times to ensure consistency.",
                    "expected_result": "All response times are less than 1 second."
                },
                {
                    "description": "Test the random number generation functionality to ensure it does not exceed the performance requirement of response time < 1 second under load.",
                    "type": "negative",
                    "test_steps": "Simulate multiple simultaneous 'roll' commands and measure the response times. Check if any response times exceed 1 second.",
                    "expected_result": "No response times exceed 1 second under load."
                }
            ]
        },
        {
            "task_id": 59,
            "test_cases": [
                {
                    "description": "Review the documentation provided for the program to ensure that it includes clear instructions for use and expected outputs for the random number generation functionality.",
                    "type": "positive",
                    "test_steps": "Read through the documentation and verify that it contains step-by-step instructions for issuing the 'roll' command and explains the expected outcomes.",
                    "expected_result": "Documentation includes clear instructions and expected outputs."
                }
            ]
        }
    ]
  } 
  ```
#### 8. Generate Code from Task ID
- **URL:** `http://localhost:8000/dev/gen-code-by-task-id?task_id=55&llmtype=ollama&model=mistral`
- **Method:** `GET`
- **Description:** Generate code from a specific task ID.
- **Query Parameters:**
  - `task_id`: The ID of the task.
  - `llmtype`: The type of the language model.
  - `model`: The model name.


- **Sample input:**
  ```http request
  http://localhost:8000/dev/gen-code-by-task-id?task_id=55&llmtype=ollama&model=mistral
  ```
- **Sample Response Output:**
  ```json
  {
    "result": "Generated and stored the code in database successfully",
    "code": " FINAL ANSWER:\nHere is an outline for the architecture design of the Python program for the dice game, adhering to the specified constraints and ensuring scalability and maintainability:\n\n1. Modules and Components:\n   - `random_number_generator`: This module will contain a class responsible for generating random numbers. It will include methods like `roll()` that return a random number within the defined range (e.g., 1-6).\n   - `user_interface`: This module will handle user interactions and display relevant information, such as the generated dice roll result.\n   - `game_logic`: This module will manage the game rules and keep track of the game state. It will interact with the `random_number_generator` and `user_interface` modules.\n\n2. Testing:\n   - In the test suite for the Python program, create a test case to verify that the core function in the `random_number_generator` module correctly returns a value between 1 and the defined maximum when the 'roll' command is issued. You can do this by using an assertion like:\n\n```python\ndef test_roll():\n    rand = RandomNumberGenerator()\n    result = rand.roll(max=6)\n    assert 1 <= result <= 6\n```\n\n3. Execution:\n   - To invoke the core function with a maximum value of 6 and issue the 'roll' command, you can use the following code snippet in your `user_interface` module:\n\n```python\ndef play():\n    rand = RandomNumberGenerator()\n    result = rand.roll(max=6)\n    print(f\"Dice roll result: {result}\")\n```\n\nIn the main function or a separate entry point, you can call the `play()` method to start the game:\n\n```python\nif __name__ == \"__main__\":\n    play()\n```"
  }
  ```

#### 9. Generate Code from Project ID
- **URL:** `http://localhost:8000/dev/gen-code-by-proj-id?proj_id=7&llmtype=ollama&model=mistral`
- **Method:** `GET`
- **Description:** Generate code from a specific project ID.
- **Query Parameters:**
  - `proj_id`: The ID of the project.
  - `llmtype`: The type of the language model.
  - `model`: The model name.

---
##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://local/GenDev/issues)**: Submit bugs found or log feature requests for the `GenDev` project.
- **[Submit Pull Requests](https://local/GenDev/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://local/GenDev/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your local account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/impelox-ai/GenDev.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to local**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://local{/GenDev/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=GenDev">
   </a>
</p>
</details>


## Star history
<p align="center">
<img src="https://star-history.com/#impelox-ai/GenDev.git" alt="none"/>
</p>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
