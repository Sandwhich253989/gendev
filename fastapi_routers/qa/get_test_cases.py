import json
import logging
from fastapi import APIRouter
from agents.QA_agent.main import run_qa_agent
from util.db_manager import connect_db

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/qa/get-test-cases/')
async def get_plan(proj_id, assigned_to,llmtype,model):
    sqlite_conn = None
    try:
        sqlite_conn = connect_db(r"sqlite3_db/agent.db")
        result = run_qa_agent(proj_id, assigned_to, sqlite_conn,llmtype,model)
        return {"result": "Generated and stored the test cases in database successfully",
                "plan": json.loads(result)["tasks"]}
    except Exception as e:
        logger.error(f"Error generating the test cases : {e}\n\nError id : ETF-UID-168")
        return {"result": f"There was an error generating the test cases ", "error_id": "ETF-UID-168"}
    finally:
        sqlite_conn.close()

