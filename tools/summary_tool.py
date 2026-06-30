from backend.config import llm
from rag.retriever import get_retriever


def summarize_notes(topic, selected_document=None):

    retriever = get_retriever(selected_document)

    docs = retriever.invoke(topic)

    context = "\n\n".join(
        d.page_content for d in docs
    )

    prompt = f"""
Summarize ONLY using the context.

Context:

{context}

Topic:

{topic}
"""

    return llm.invoke(prompt).content