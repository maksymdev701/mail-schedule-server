from langchain.tools import BaseTool


class ConflictTool(BaseTool):
    name = "Conflict"
    description = "Only use for when email is about schedule in case of conflicting availabilites"

    def _run(self, tool_input: str) -> str:
        """Use the tool."""
        return "Conflicting availabilities"

    async def _arun(self, tool_input: str) -> str:
        """Use the tool asynchronously."""
        return "Conflicting availabilities"


class TimezoneTool(BaseTool):
    name = "Timezone"
    description = "Only use for when email is about schedule in case of timezone differences that may not be clearly communicated"

    def _run(self, tool_input: str) -> str:
        """Use the tool."""
        return "Time zone differences that may not be clearly communicated"

    async def _arun(self, tool_input: str) -> str:
        """Use the tool asynchronously."""
        return "Time zone differences that may not be clearly communicated"


class LastMinuteTool(BaseTool):
    name = "LastMinute"
    description = "Only use for when email is about schedule in case of last minute changes"

    def _run(self, tool_input: str) -> str:
        """Use the tool."""
        return "Last minute changes"

    async def _arun(self, tool_input: str) -> str:
        """Use the tool asynchronously."""
        return "Last minute changes"


class HighAttendeesTool(BaseTool):
    name = "HighAttendees"
    description = "Only use for when email is about schedule in case of high profile attendees with limited availability"

    def _run(self, tool_input: str) -> str:
        """Use the tool."""
        return "High profile attendees with limited availability"

    async def _arun(self, tool_input: str) -> str:
        """Use the tool asynchronously."""
        return "High profile attendees with limited availability"


class LargeScaleTool(BaseTool):
    name = "LargeScale"
    description = "Only use for when email is about schedule in case of large scale event complexity"

    def _run(self, tool_input: str) -> str:
        """Use the tool."""
        return "Large scale event complexity"

    async def _arun(self, tool_input: str) -> str:
        """Use the tool asynchronously"""
        return "Large scale event compelxity"


class RecurringTool(BaseTool):
    name = "Recurring"
    description = "Only use for when email is about schedule in case of recurring meeting"

    def _run(self, tool_input: str) -> str:
        """Use the tool."""
        return "Recurring meeting"

    async def _arun(self, tool_input: str) -> str:
        """Use the tool asynchronously"""
        return "Recurring meeting"

class UnexpectedTool(BaseTool):
    name = "Unexpected"
    description = "Only use for when email is about schedule in case of unexpected interruptions"

    def _run(self, tool_input: str) -> str:
        """Use the tool."""
        return "Unexpected interruptions"

    async def _arun(self, tool_input: str) -> str:
        """Use the tool asynchronously"""
        return "Unexpected interruptions"


class GeneralLackTool(BaseTool):
    name = "GeneralLack"
    description = "Only use for when email is about schedule in case of general lack of clarity in communication"

    def _run(self, tool_input: str) -> str:
        """Use the tool."""
        return "General lack of clarity in communication"

    async def _arun(self, tool_input: str) -> str:
        """Use the tool asynchronously."""
        return "General lack of clarity in communication"

class InviteDelayTool(BaseTool):
    name = "InviteDelay"
    description = "Only use for when email is about schedule in case of invite from other party was promised but not sent"

    def _run(self, tool_input: str) -> str:
        """Use the tool."""
        return "Inivte from other party was promiesd but not sent"

    async def _arun(self, tool_input: str) -> str:
        """Use the tool asynchronously."""
        return "Inivite from other party was promised but not sent"