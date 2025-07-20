import logging
import sqlite3

# Set up logging
logger = logging.getLogger(__name__)


# Function to connect to the SQLite database
def connect_db(path):
    # Connect to the SQLite database at the given path
    sqlite_conn = sqlite3.connect(path)
    # Commit any initial transactions
    sqlite_conn.commit()
    # Return the connection object
    return sqlite_conn

# !!!! USE THIS ONLY IF YOU WANT TO CREATE NEW TABLE !!!!
# # Function to create the 'test_case' table in the SQLite database
# def create_agent_db(sqlite_conn):
#     # Create a cursor object to interact with the database
#     sqlite_cursor = sqlite_conn.cursor()
#     # Execute the SQL command to create the 'test_case' table
#     sqlite_cursor.execute(
#         """
#         CREATE TABLE test_case (
#             test_case_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#             task_id INT NULL,
#             test_case_description TEXT NULL,
#             assigned_to VARCHAR NULL,
#             created_date TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
#             modified_date TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
#             FOREIGN KEY (task_id) REFERENCES task(task_id)
#         );
#         """
#     )
#     # Commit the transaction to the database
#     sqlite_conn.commit()
