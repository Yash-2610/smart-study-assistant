from langchain_core.messages import HumanMessage, AIMessage

from tools.summary_tool import summarize_notes
from tools.quiz_tool import generate_quiz
from tools.flashcard_tool import generate_flashcards
from rag.qa import ask_pdf
from backend.config import llm

chat_history = []


def choose_tool(user_query: str):

    prompt = f"""
You are an intelligent routing agent.

Only choose SUMMARY if the user explicitly asks to summarize.

Only choose QUIZ if the user explicitly asks for quiz, MCQs, test or questions.

Only choose FLASHCARD if the user explicitly asks for flashcards.

For every other request including:
- What is...
- Explain...
- Advantages...
- Define...
- Difference...
- Why...
- How...
- List...
- Compare...

ALWAYS choose RAG.

Return ONLY one word.

SUMMARY
QUIZ
FLASHCARD
RAG

User:
{user_query}
"""

    response = llm.invoke(prompt)

    return response.content.strip().upper()


def study_agent(user_query: str):

    tool = choose_tool(user_query)

    print(f"\nUsing Tool : {tool}\n")

    chat_history.append(
        HumanMessage(content=user_query)
    )

    if tool == "SUMMARY":

        answer = summarize_notes(user_query)

    elif tool == "QUIZ":

        answer = generate_quiz(user_query)

    elif tool == "FLASHCARD":

        answer = generate_flashcards(user_query)

    else:

        answer = ask_pdf(user_query)

    chat_history.append(
        AIMessage(content=answer)
    )

    return answer


if __name__ == "__main__":

    while True:

        query = input("\nYou : ")

        if query.lower() == "exit":
            break

        response = study_agent(query)

        print("\nAssistant:\n")

        print(response)