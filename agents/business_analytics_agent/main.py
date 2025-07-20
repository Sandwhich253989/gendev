import uuid
from sqlalchemy import null
from agents.business_analytics_agent.graph_router import construct_graph
from util.db_manager import connect_db
from datetime import datetime
from configs import config


# Function to store a BRD (Business Requirements Document) in the project table
def store_brd(brd, sqlite_conn):
    # Connect to the SQLite database
    sqlite_cursor = sqlite_conn.cursor()
    try:

        # Open a file to write the resulting BRD
        file = open("agents/business_analytics_agent/brd.md", "w")
        file.write(brd)  # Write the content of the last message to the file
        file.close()  # Close the file

        # Insert the BRD into the project table with a null project_id
        sqlite_cursor.execute("INSERT INTO project (project_id, brd) VALUES (?, ?)", (None, brd))
        sqlite_conn.commit()  # Commit the transaction
    except Exception as e:
        # Raise an exception if any error occurs
        raise e
    finally:
        # Close the database connection
        sqlite_conn.close()


# Function to run the graph-based analysis on the summary and store the resulting BRD
def run_brd_agent(summary, sqlite_conn):
    # Construct the graph for analysis
    graph = construct_graph()

    # Stream the summary through the graph and capture the events
    events = graph.stream({"messages": [("user", summary)]}, stream_mode="values")

    # DEBUG
    # Process each event and pretty print the last message in the event
    for event in events:
        event["messages"][-1].pretty_print()

    # Store the resulting BRD in the database
    store_brd(event["messages"][-1].content, sqlite_conn)

    return event["messages"][-1].content  # Return the content of the last message
