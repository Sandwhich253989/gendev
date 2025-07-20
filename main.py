from fastapi import FastAPI
from fastapi_routers.brd.upload_file import router as brd
from fastapi_routers.display.tables import router as dis
from fastapi_routers.pm.get_plan import router as pm
from fastapi_routers.qa.get_test_cases import router as qa
from fastapi_routers.dev.gen_code import router as dev
from fastapi_routers.requirements.req import router as req

app = FastAPI()


@app.get("/")
async def root():
    return {"result": "Nothing to see here"}


routers = [req, brd, pm, qa, dev, dis]
for route in routers:
    app.include_router(route)
