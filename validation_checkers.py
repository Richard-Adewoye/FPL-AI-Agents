from typing import AsyncGenerator

from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event, EventActions

class TeamStrategyValidationChecker(BaseAgent):
    """Checks if the FPL team strategy is valid."""

    async def _run_async_impl(
        self, context: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        if context.session.state.get("team_strategy"):
            yield Event(
                author=self.name,
                actions=EventActions(escalate=True),
            )
        else:
            yield Event(author=self.name)


class TeamReportValidationChecker(BaseAgent):
    """Checks if the FPL team report is valid."""

    async def _run_async_impl(
        self, context: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        if context.session.state.get("team_report"):
            yield Event(author=self.name, actions=EventActions(escalate=True))
        else:
            yield Event(author=self.name)
