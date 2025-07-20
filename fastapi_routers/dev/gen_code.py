from fastapi import APIRouter
from agents.dev_agent.main import run_dev_agent_taskid, dev_agent_run
import logging

from util.db_manager import connect_db

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/dev/gen-code-by-task-id/")
async def gen_code_by_ids(task_id: int, llmtype: str, model: str):
    sqlite_conn = None
    try:
        sqlite_conn = connect_db(r"sqlite3_db/agent.db")
        result = run_dev_agent_taskid(task_id, sqlite_conn, llmtype, model)
        return {"result": "Generated and stored the code in database successfully", "code": result}
    except Exception as e:
        logger.error(f"Error generating the code: {e}\n\nError id : ETF-UID-442")
        return {"result": "There was an error generating the code", "error_id": "ETF-UID-442"}
    finally:
        sqlite_conn.close()


@router.get("/dev/gen-code-by-proj-id/")
async def gen_code_by_proj_id(proj_id: int, llmtype: str, model: str):
    sqlite_conn = None
    try:
        sqlite_conn = connect_db(r"sqlite3_db/agent.db")
        result = dev_agent_run(proj_id, sqlite_conn, llmtype, model)
        return {"result": "Generated and stored the code in database successfully", "code": result}
    except Exception as e:
        logger.error(f"Error generating the code: {e}\n\nError id : ETF-UID-542")
        return {"result": "There was an error generating the code", "error_id": "ETF-UID-542"}
    finally:
        sqlite_conn.close()
