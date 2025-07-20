from util.db_manager import connect_db


# Function to display all tasks in the task table
def display_task_table():
    # Connect to the SQLite database
    with connect_db(r"sqlite3_db/agent.db") as sqlite_conn:
        sqlite_cursor = sqlite_conn.cursor()
        # Execute SQL query to select all records from the task table
        sqlite_cursor.execute("SELECT * FROM task")
        rows = sqlite_cursor.fetchall()

    task_data = {}

    # Process each row from the result set
    for row in rows:
        (task_id, proj_id, task_description, estimate, estimated_time, status, assigned_to, task_type, created_date,
         modified_date) = row
        # Check if the project ID key exists in the dictionary, if not, create it
        if f"proj_id_{proj_id}" not in task_data:
            task_data[f"proj_id_{proj_id}"] = []

        # Append the task details to the corresponding project ID
        task_data[f"proj_id_{proj_id}"].append({
            "task_id": task_id,
            "task_description": task_description,
            "estimate": estimate,
            "estimated_time": estimated_time,
            "status": status,
            "assigned_to": assigned_to,
            "task_type": task_type,
            "created_date": created_date,
            "modified_date": modified_date
        })

    return task_data


# Function to display tasks by project ID
def display_task_table_by_id(proj_id):
    # Connect to the SQLite database
    with connect_db(r"sqlite3_db/agent.db") as sqlite_conn:
        sqlite_cursor = sqlite_conn.cursor()
        # Execute SQL query to select all records from the task table where project ID matches
        sqlite_cursor.execute("SELECT * FROM task WHERE project_id=?", (proj_id,))
        rows = sqlite_cursor.fetchall()

    task_data = {f"proj_id_{proj_id}": []}

    # Process each row from the result set
    for row in rows:
        (task_id, _, task_description, estimate, estimated_time, status, assigned_to, task_type, created_date,
         modified_date) = row

        # Append the task details to the corresponding project ID
        task_data[f"proj_id_{proj_id}"].append({
            "task_id": task_id,
            "task_description": task_description,
            "estimate": estimate,
            "estimated_time": estimated_time,
            "status": status,
            "assigned_to": assigned_to,
            "task_type": task_type,
            "created_date": created_date,
            "modified_date": modified_date
        })

    return task_data


# Function to display all test cases in the test_case table
def display_test_case_table():
    # Connect to the SQLite database
    with connect_db(r"sqlite3_db/agent.db") as sqlite_conn:
        sqlite_cursor = sqlite_conn.cursor()
        # Execute SQL query to select all records from the test_case table
        sqlite_cursor.execute("SELECT * FROM test_case")
        rows = sqlite_cursor.fetchall()

    test_case_data = {}

    # Process each row from the result set
    for row in rows:
        (test_case_id, task_id, test_case_description, assigned_to, created_date, modified_date, test_case_type) = row
        # Check if the task ID key exists in the dictionary, if not, create it
        if f"task_id_{task_id}" not in test_case_data:
            test_case_data[f"task_id_{task_id}"] = []

        # Append the test case details to the corresponding task ID
        test_case_data[f"task_id_{task_id}"].append({
            "test_case_id": test_case_id,
            "test_case_description": test_case_description,
            "test_case_type": test_case_type,
            "assigned_to": assigned_to,
            "created_date": created_date,
            "modified_date": modified_date
        })

    return test_case_data


# Function to display test cases by task ID
def display_test_case_table_by_id(task_id):
    # Connect to the SQLite database
    with connect_db(r"sqlite3_db/agent.db") as sqlite_conn:
        sqlite_cursor = sqlite_conn.cursor()
        # Execute SQL query to select all records from the test_case table where task ID matches
        sqlite_cursor.execute("SELECT * FROM test_case WHERE task_id=?", (task_id,))
        rows = sqlite_cursor.fetchall()

    test_case_data = {f"task_id_{task_id}": []}

    # Process each row from the result set
    for row in rows:
        (test_case_id, _, test_case_description, assigned_to, created_date, modified_date,test_case_type,test_steps,expected_result) = row

        # Append the test case details to the corresponding task ID
        test_case_data[f"task_id_{task_id}"].append({
            "test_case_id": test_case_id,
            "test_case_description": test_case_description,
            "assigned_to": assigned_to,
            "created_date": created_date,
            "modified_date": modified_date,
            "test_case_type":test_case_type,
            "test_steps":test_steps,
            "expected_result":expected_result
        })

    return test_case_data


# Function to display all code snippets in the code table
def display_code_table():
    # Connect to the SQLite database
    with connect_db(r"sqlite3_db/agent.db") as sqlite_conn:
        sqlite_cursor = sqlite_conn.cursor()
        # Execute SQL query to select all records from the code table
        sqlite_cursor.execute("SELECT * FROM code")
        rows = sqlite_cursor.fetchall()

    code_data = {}

    # Process each row from the result set
    for row in rows:
        (code_id, task_id, code, created_date, modified_date) = row
        # Check if the task ID key exists in the dictionary, if not, create it
        if f"task_id_{task_id}" not in code_data:
            code_data[f"task_id_{task_id}"] = []

        # Append the code details to the corresponding task ID
        code_data[f"task_id_{task_id}"].append({
            "code_id": code_id,
            "code": code,
            "created_date": created_date,
            "modified_date": modified_date
        })

    return code_data


# Function to display code snippets by task ID
def display_code_table_by_taskid(task_id):
    # Connect to the SQLite database
    with connect_db(r"sqlite3_db/agent.db") as sqlite_conn:
        sqlite_cursor = sqlite_conn.cursor()
        # Execute SQL query to select all records from the code table where task ID matches
        sqlite_cursor.execute("SELECT * FROM code WHERE task_id=?", (task_id,))
        rows = sqlite_cursor.fetchall()

    code_data = {f"task_id_{task_id}": []}

    # Process each row from the result set
    for row in rows:
        (code_id, _, code, created_date, modified_date) = row

        # Append the code details to the corresponding task ID
        code_data[f"task_id_{task_id}"].append({
            "code_id": code_id,
            "code": code,
            "created_date": created_date,
            "modified_date": modified_date
        })

    return code_data


# Function to display all projects in the project table
def display_project_table():
    # Connect to the SQLite database
    with connect_db(r"sqlite3_db/agent.db") as sqlite_conn:
        sqlite_cursor = sqlite_conn.cursor()
        # Execute SQL query to select all records from the project table
        sqlite_cursor.execute("SELECT * FROM project")
        rows = sqlite_cursor.fetchall()

    project_data = {}

    # Process each row from the result set
    for row in rows:
        (project_id, brd, created_date) = row
        # Check if the project ID key exists in the dictionary, if not, create it
        if f"proj_id_{project_id}" not in project_data:
            project_data[f"proj_id_{project_id}"] = {}

        # Append the project details to the corresponding project ID
        project_data[f"proj_id_{project_id}"] = {
            "brd": brd,
            "created_date": created_date}

    return project_data


# Function to display project details by project ID
def display_project_table_by_id(proj_id):
    # Connect to the SQLite database
    with connect_db(r"sqlite3_db/agent.db") as sqlite_conn:
        sqlite_cursor = sqlite_conn.cursor()
        # Execute SQL query to select all records from the project table where project ID matches
        sqlite_cursor.execute("SELECT * FROM project WHERE project_id=?", (proj_id,))
        row = sqlite_cursor.fetchall()

    project_data = {}
    project_id, brd, created_date = row[0]
    # Append the project details to the corresponding project ID
    project_data[f"proj_id_{project_id}"] = {
        "brd": brd,
        "created_date": created_date
    }

    return project_data
