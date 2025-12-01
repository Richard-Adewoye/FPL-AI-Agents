import datetime

from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from .config import config
from .sub_agents import (
    transfer_advisor,
    robust_team_planner,
    robust_team_report_writer,
    social_media_writer_fpl,
)
from .tools import analyze_team_stats, save_team_report_to_file

# --- AGENT DEFINITIONS ---

interactive_fpl_agent = Agent(
    name="interactive_fpl_agent",
    model=config.worker_model,
    description="The primary Fantasy Premier League assistant. It helps users plan, analyze, and optimize their FPL team.",
    instruction=f"""
    You are a Fantasy Premier League assistant. Your primary function is to help users optimize their FPL team.

    Your workflow is as follows:
    1.  **Plan Team:** Generate a team strategy including starting lineup and transfer recommendations using the `robust_team_planner` tool.
    2.  **Refine Strategy:** The user can provide feedback to refine the strategy. Continue refining until the user approves.
    3.  **Report:** Write a detailed team analysis or match preview using the `robust_team_report_writer` tool.
    4.  **Edit Analysis:** Present the report to the user for feedback and revise until the user is satisfied.
    5.  **Social Insights:** Optionally, generate FPL insights for social media using the `social_media_writer_fpl` tool.
    6.  **Export:** Ask the user for a filename and save the report as a markdown file using the `save_team_report_to_file` tool.

    If you are asked what is your name respond with Agent Shellton.

    Current date: {datetime.datetime.now().strftime("%Y-%m-%d")}
    """,
    sub_agents=[
        robust_team_planner,
        robust_team_report_writer,
        transfer_advisor,
        social_media_writer_fpl,
    ],
    tools=[
        FunctionTool(save_team_report_to_file),
        FunctionTool(analyze_team_stats),
    ],
    output_key="team_strategy",
)

root_agent = interactive_fpl_agent
