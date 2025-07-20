import logging
import shutil
from typing import Annotated
from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel
from util.db_manager import connect_db

from agents.business_analytics_agent.main import run_brd_agent

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

router = APIRouter()


class Data(BaseModel):
    text: str


def gen_brd(text):
    sqlite_conn = None
    try:
        sqlite_conn = connect_db(r"sqlite3_db/agent.db")
        result = run_brd_agent(text, sqlite_conn)  # Store the file in the database
        return {"result": "Successfully generated and stored the BRD doc in database", "text": result}
    except Exception as e:
        logger.error(f"Error uploading file: {e}\n\nError id : ETF-UID-12")
        return {"result": "There was an error uploading the file", "error_id": "ETF-UID-12"}
    finally:
        sqlite_conn.close()


@router.post('/upload/document/')
async def upload_doc(file: UploadFile = File(...)):
    try:
        with open(r"../../temp/tmp.txt", "wb") as f:
            shutil.copyfileobj(file.file, f)
        file = open(r"../../temp/tmp.txt", "rb")
        content = file.read()
        file.close()
        return gen_brd(content)
    except Exception as e:
        logger.error(f"Error uploading file: {e}\n\nError id : ETF-UID-12")
        return {"result": "There was an error uploading the file", "error_id": "ETF-UID-12"}


@router.post('/upload/text/')
async def upload_text(data: Data):
    return gen_brd(data.text)
