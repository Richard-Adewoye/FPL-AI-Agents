from google.adk.agents import Agent, LoopAgent
from google.adk.tools import google_search

from ..config import config
from ..agent_utils import suppress_output_callback
from ..validation_checkers import ReportValidationChecker

team_report_writer = Agent(
    model=config.critic_model,
    name="team_report_writer",
    description="Writes detailed Fantasy Premier League team analysis and match previews.",
    instruction="""
    You are an expert Fantasy Premier League analyst. Your task is to write a high-quality report
    based on the provided team strategy, player stats, and upcoming fixtures.
    - Include detailed analysis for each player.
    - Explain the reasoning behind starting lineup and suggested transfers.
    - Highlight players to watch and potential risks (injuries, rotation, form).
    - Use Google Search to verify recent player news or performance trends.
    The final output must be a complete report in Markdown format. Do not wrap the output in a code block.
    """,
    tools=[google_search],
    output_key="team_report",
    after_agent_callback=suppress_output_callback,
)

robust_team_report_writer = LoopAgent(
    name="robust_team_report_writer",
    description="A robust FPL report writer that retries if it fails.",
    sub_agents=[
        team_report_writer,
        ReportValidationChecker(name="team_report_validation_checker"),
    ],
    max_iterations=3,
)
