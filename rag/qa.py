from backend.config import llm
from rag.retriever import get_retriever


def ask_pdf(question, selected_document=None):

    retriever = get_retriever(selected_document)

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    sources = []

    for doc in docs:

        src = doc.metadata.get("source", "Unknown")

        page = doc.metadata.get("page", "?") + 1

        sources.append(f"{src} (Page {page})")

    prompt = f"""
You are a Smart Study Assistant.

Answer ONLY using the context.

If the answer does not exist in the context,
say

"I couldn't find that information in the uploaded study material."

Context:

{context}

Question:

{question}
"""

    response = llm.invoke(prompt)

    answer = response.content

    unique_sources = list(dict.fromkeys(sources))

    answer += "\n\n---\n📚 Sources Used:\n"

    for s in unique_sources:

        answer += f"\n• {s}"

    return answer


if __name__ == "__main__":

    while True:

        q = input("\nQuestion : ")

        if q.lower() == "exit":
            break

        print(ask_pdf(q))