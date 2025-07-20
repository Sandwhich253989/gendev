from business_analytics_agent import main as ba
from project_manager import main as pm
from QA_agent import main as qa
from dev_agent import main as dev
from util.db_manager import connect_db


def main(proj_id, assigned_to):
    # ba.run_brd_agent(proj_id)
    pm.run_pm_agent(proj_id, assigned_to)
    qa.run_qa_agent(proj_id, assigned_to)
    dev.dev_agent_run(proj_id)


# main(4, "me")
