from backend.state import AgentState

from backend.agent import choose_tool

from rag.qa import ask_pdf
from tools.summary_tool import summarize_notes
from tools.quiz_tool import generate_quiz
from tools.flashcard_tool import generate_flashcards


def router_node(state: AgentState):

    state["tool"] = choose_tool(
        state["user_query"]
    )

    return state


def tool_node(state: AgentState):

    query = state["user_query"]

    selected_document = state["selected_document"]

    if state["tool"] == "SUMMARY":

        answer = summarize_notes(
            query,
            selected_document
        )

    elif state["tool"] == "QUIZ":

        answer = generate_quiz(
            query,
            selected_document
        )

    elif state["tool"] == "FLASHCARD":

        answer = generate_flashcards(
            query,
            selected_document
        )

    else:

        answer = ask_pdf(
            query,
            selected_document
        )

    state["answer"] = answer

    state["messages"].append(answer)

    return state