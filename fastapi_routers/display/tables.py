import logging
import shutil
from typing import Annotated
from fastapi import APIRouter, File, UploadFile, Form
from pydantic import BaseModel

from util.display_tables import display_project_table, display_project_table_by_id, display_task_table, \
    display_task_table_by_id, display_test_case_table, display_test_case_table_by_id, display_code_table, \
    display_code_table_by_taskid

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/display/table/{table_name}')
async def task_table(table_name: str):
    try:
        result = {}
        if table_name == "project":
            result = display_project_table()
        elif table_name == "task":
            result = display_task_table()
        elif table_name == "test_case":
            result = display_test_case_table()
        elif table_name == "code":
            result = display_code_table()
        else:
            raise Exception
        return result
    except Exception as e:
        logger.error(f"Error displaying the table {table_name}: {e}\n\nError id : ETF-UID-142")
        return {"result": f"There was an error displaying the table {table_name}", "error_id": "ETF-UID-142"}


@router.get('/display/table-by-id/')
async def task_table(table_name: str, index: int):
    try:
        result = {}
        if table_name == "project":
            result = display_project_table_by_id(index)
        elif table_name == "task":
            result = display_task_table_by_id(index)
        elif table_name == "test_case":
            result = display_test_case_table_by_id(index)
        elif table_name == "code":
            result = display_code_table_by_taskid(index)
        else:
            raise Exception
        return result

    except Exception as e:
        logger.error(f"Error displaying the table {table_name}: {e}\n\nError id : ETF-UID-152")
        return {"result": f"There was an error displaying the table {table_name}", "error_id": "ETF-UID-152"}
