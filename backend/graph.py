from langgraph.graph import StateGraph, END

from backend.state import AgentState
from backend.nodes import router_node, tool_node

workflow = StateGraph(AgentState)

workflow.add_node("router", router_node)
workflow.add_node("tool", tool_node)

workflow.set_entry_point("router")

workflow.add_edge("router", "tool")
workflow.add_edge("tool", END)

graph = workflow.compile()


def run_agent(
    user_query,
    selected_document="All Documents"
):

    state = {

        "user_query": user_query,

        "selected_document": selected_document,

        "tool": "",

        "answer": "",

        "messages": []

    }

    result = graph.invoke(state)

    return result["answer"]


if __name__ == "__main__":

    while True:

        q = input("\nYou : ")

        if q.lower() == "exit":
            break

        print(
            run_agent(
                q,
                "All Documents"
            )
        )