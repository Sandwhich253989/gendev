import json
import logging
from fastapi import APIRouter, File, UploadFile, Form
from agents.project_manager.main import run_pm_agent
from util.db_manager import connect_db

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/pm/get-plan/')
async def get_plan(proj_id, assigned_to, llmtype, model):
    try:
        sqlite_conn = connect_db(r"sqlite3_db/agent.db")
        result = run_pm_agent(proj_id, assigned_to, sqlite_conn, llmtype, model)
        return {"result": "Generated and stored the plan in database successfully", "plan": json.loads(result)["tasks"]}
    except Exception as e:
        logger.error(f"Error generating the plan : {e}\n\nError id : ETF-UID-168")
        return {"result": f"There was an error generating the plan ", "error_id": "ETF-UID-168"}
