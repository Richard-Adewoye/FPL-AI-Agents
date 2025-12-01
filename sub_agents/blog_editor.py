from google.adk.agents import Agent
from ..config import config
from ..agent_utils import suppress_output_callback

transfer_advisor = Agent(
    model=config.critic_model,
    name="transfer_advisor",
    description="Suggests optimal player transfers for a Fantasy Premier League team based on team performance and upcoming fixtures.",
    instruction="""
    You are a Fantasy Premier League advisor. You will be given a user's current team, player stats, and upcoming fixtures.
    Your task is to recommend transfers that maximize expected points while staying within the budget.
    The final output should be a list of recommended transfers with justification for each.
    """,
    output_key="transfer_suggestions",
    after_agent_callback=suppress_output_callback,
)
