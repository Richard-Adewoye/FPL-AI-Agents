from google.adk.agents import Agent, LoopAgent
from google.adk.tools import google_search

from ..config import config
from ..agent_utils import suppress_output_callback
from ..validation_checkers import OutlineValidationChecker

team_planner = Agent(
    model=config.worker_model,
    name="team_planner",
    description="Generates a Fantasy Premier League team strategy.",
    instruction="""
    You are a Fantasy Premier League strategist. Your job is to create a team lineup and transfer strategy.
    Consider the current team, player stats, upcoming fixtures, and budget constraints.
    Use online resources if needed to verify player performance trends or injury news.
    Your output should include the starting lineup, suggested transfers, and reasoning for each choice.
    """,
    tools=[google_search],
    output_key="team_strategy",
    after_agent_callback=suppress_output_callback,
)

robust_team_planner = LoopAgent(
    name="robust_team_planner",
    description="A robust FPL team planner that retries if it fails.",
    sub_agents=[
        team_planner,
        OutlineValidationChecker(name="strategy_validation_checker"),
    ],
    max_iterations=3,
    after_agent_callback=suppress_output_callback,
)
