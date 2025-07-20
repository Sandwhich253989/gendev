import json

from agents.QA_agent.graph_router import construct_graph
from agents.time.timestamp import get_timestamp
from util.db_manager import connect_db


def get_tasks(proj_id, sqlite_conn):
    """
    Retrieves plans (task details) for a given project ID from the database.

    Args:
    - proj_id (int): Project ID for which plans are fetched.

    Returns:
    - dict: Dictionary containing task details (task_id, task_description, task_type).
    """
    tasks = {"tasks": []}
    sqlite_cursor = sqlite_conn.cursor()
    try:
        sqlite_cursor.execute("SELECT task_id, task_description, task_type FROM task WHERE project_id=?",
                              (proj_id,))
        rows = sqlite_cursor.fetchall()
        for row in rows:
            task_id, task_description, task_type = row
            tasks["tasks"].append({"task_id": task_id, "task_description": task_description, "task_type": task_type})
        return tasks
    except Exception as e:
        raise e


def run_qa_agent(proj_id, assigned_to, sqlite_conn, llmtype, model):
    graph = construct_graph()
    tasks = str(get_tasks(proj_id, sqlite_conn))
    events = graph.stream({"messages": [("user", tasks)], "plan": tasks, "llmtype": llmtype, "model": model},
                          stream_mode="values")

    # DEBUG
    for event in events:
        event["messages"][-1].pretty_print()

    store_test_cases(event["messages"][-1].content, assigned_to, sqlite_conn, proj_id)
    return event["messages"][-1].content


def store_test_cases(jtest_case, assigned_to, sqlite_conn, proj_id):
    # Write test cases content to a JSON file for testing purposes
    try:
        sqlite_cursor = sqlite_conn.cursor()
        file = open("agents/QA_agent/plan_test_cases.json", 'w')
        file.write(jtest_case)
        test_case_ids = []

        sqlite_cursor.execute("SELECT task_id FROM task WHERE project_id=?", (proj_id,))
        result = sqlite_cursor.fetchall()
        for task_id in result:
            sqlite_cursor.execute("SELECT test_case_id FROM test_case WHERE task_id=?", (task_id[0],))
            test_case_id_fetch = sqlite_cursor.fetchall()
            for test_case_id in test_case_id_fetch:
                test_case_ids.append(test_case_id[0])

        current_time = get_timestamp()  # Get current timestamp using timestamp module

        jtest_case = json.loads(jtest_case)

        if not test_case_ids:
            print("NOT TEST CASE IDS")
            for tasks in jtest_case["tasks"]:
                for testcase in tasks["test_cases"]:
                    sqlite_cursor.execute(
                        "INSERT INTO test_case (test_case_id, task_id, test_case_description, assigned_to, "
                        "test_case_type,test_steps,expected_result)"
                        "VALUES (?,?,?,?,?,?,?)",
                        (None, tasks["task_id"], testcase["description"], assigned_to, testcase["type"],
                         testcase["test_steps"], testcase["expected_result"]))
                    sqlite_conn.commit()
        else:
            # Update existing row if test_case_id exists in test_case table
            print("YES TEST CASE IDS")
            ind = 0
            for task in jtest_case["tasks"]:
                for testcase in task["test_cases"]:
                    sqlite_cursor.execute(
                        "UPDATE test_case SET test_case_description=?, assigned_to=?,test_case_type=?,test_steps=?,"
                        f"expected_result=?, modified_date=? WHERE test_case_id={test_case_ids[ind]}",
                        (testcase["description"], assigned_to, testcase["type"],
                         testcase["test_steps"], testcase["expected_result"], current_time)
                    )
                    sqlite_conn.commit()
                    ind += 1

    finally:
        file.close()

# Example usage:
# run_graph(4, "v")
