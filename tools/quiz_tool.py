from backend.config import llm
from rag.retriever import get_retriever


def generate_quiz(topic, selected_document=None):

    retriever = get_retriever(selected_document)

    docs = retriever.invoke(topic)

    context = "\n\n".join(
        d.page_content for d in docs
    )

    prompt = f"""
Generate 5 MCQs.

Only use:

{context}
"""

    return llm.invoke(prompt).content