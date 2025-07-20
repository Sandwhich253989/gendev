from datetime import datetime  # Import datetime module for timestamp operations

from agents.dev_agent.graph_router import create_graph  # Import create_graph function from graph_router
from util.db_manager import connect_db  # Import connect_db function from db_manager
from configs import config  # Import config for configuration access
from agents.time import timestamp  # Import timestamp from time module


# Function to fetch problem details for a given task_id
def get_problem(task_id, sqlite_conn):
    sqlite_cursor = sqlite_conn.cursor()
    try:
        # Fetch project_id and BRD from project and task tables
        sqlite_cursor.execute(f"SELECT task.project_id, brd FROM project, task WHERE task_id={task_id}")
        proj_id, brd = sqlite_cursor.fetchone()

        # Fetch task details like task_id, task_description, and task_type
        sqlite_cursor.execute("SELECT task.task_id, task.task_description, task.task_type FROM task "
                              "WHERE project_id=? AND task.task_id=?", (proj_id, task_id))
        task_id, task_desc, task_type = sqlite_cursor.fetchone()

        # Fetch all test cases associated with the task_id
        sqlite_cursor.execute(
            f"SELECT task_id, test_case_description,test_steps,expected_result FROM test_case WHERE task_id={task_id}")
        test_cases = sqlite_cursor.fetchall()

        result = task_desc + "\nType:" + task_type + ".\n"
        for row in test_cases:
            _, test_case, test_steps, expected_result = row
            result += " " + test_case + "\n" + test_steps + "\n" + expected_result + "\n"

        return result, brd  # Return concatenated task details and BRD
    except Exception as e:
        raise e


# Function to run the graph process for a given task_id
def run_dev_agent_taskid(task_id, sqlite_conn, llmtype, model):
    graph = create_graph()  # Create the state graph using create_graph function
    content, brd = get_problem(task_id, sqlite_conn)  # Get problem details and BRD for the task_id
    events = graph.stream({"messages": [("user", content)], "brd": brd, "llmtype": llmtype, "model": model},
                          stream_mode="values")

    # DEBUG
    for event in events:
        event["messages"][-1].pretty_print()  # Print the last message in each event

    code = event["messages"][-1].content  # Retrieve the content of the second last message (the generated code)

    store_code(task_id, code, sqlite_conn)  # Store the generated code in the database
    return code  # Return the generated code


# Function to run the development agent for a given project_id
def dev_agent_run(proj_id, sqlite_conn, llmtype, model):
    sqlite_cursor = sqlite_conn.cursor()
    project = {"project_id": proj_id, "code": []}  # Temporary dictionary to store project_id and generated code
    try:
        # Fetch all task_ids associated with the given project_id
        sqlite_cursor.execute(f"SELECT task_id FROM task WHERE project_id={proj_id}")
        task_ids = sqlite_cursor.fetchall()

        # Iterate through each task_id and run the graph process to generate code
        for i in task_ids:
            code = run_dev_agent_taskid(i[0], sqlite_conn, llmtype, model)  # Generate code for the current task_id
            project["code"].append({
                "task_id": i[0],
                "code": code,
            })
        return project  # Return the temporary dictionary containing project_id and generated code
    except Exception as e:
        print(e)


# Function to store the generated code in the database for a given task_id
def store_code(task_id, code, sqlite_conn):
    sqlite_cursor = sqlite_conn.cursor()
    try:
        # Write the generated code to a file for testing purposes
        file = open("agents/dev_agent/code.md", 'w')
        file.write(code)
        file.close()
        # Check if code already exists for the given task_id
        sqlite_cursor.execute("SELECT code, created_date FROM code WHERE task_id=?", (task_id,))
        result = sqlite_cursor.fetchone()
        current_time = timestamp.get_timestamp()  # Get current timestamp using timestamp module

        if result is None:
            # Insert new row if task_id does not exist in code table
            sqlite_cursor.execute(
                "INSERT INTO code (code_id, task_id, code, created_date, modified_date) VALUES (?,?,?,?,?)",
                (None, task_id, code, current_time, current_time)
            )
            sqlite_conn.commit()
        else:
            # Update existing row if task_id exists in code table
            sqlite_cursor.execute(
                "UPDATE code SET code=?, modified_date=? WHERE task_id=?",
                (code, current_time, task_id)
            )
            sqlite_conn.commit()

        # Update task status to 'Completed' after storing code
        sqlite_cursor.execute("UPDATE task SET status='Completed' WHERE task_id=?", (task_id,))
        sqlite_conn.commit()
    except Exception as e:
        raise e

# Example usage: Run development agent for project with project_id 3
# dev_agent_run(3)
