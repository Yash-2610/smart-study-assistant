from typing import TypedDict, List


class AgentState(TypedDict):

    user_query: str

    selected_document: str

    tool: str

    answer: str

    messages: List[str]