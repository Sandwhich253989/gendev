from fastapi import APIRouter
from pydantic import BaseModel

from langgraphh.main import run_req_graph
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

router = APIRouter()


class Requirements(BaseModel):
    query: str
    thread_id: str
    llmtype: str
    model: str


@router.post('/requirements/query/')
async def query_requirements(requirements: Requirements):
    try:
        result = run_req_graph(requirements.query, requirements.thread_id,requirements.llmtype,requirements.model)
        return {"user": requirements.query, "genai_response": result}
    except Exception as e:
        logger.error(f"Error getting response: {e}\n\nError id : ETF-UID-328")
        return {"result": f"There was an error getting response", "error_id": "ETF-UID-328"}
