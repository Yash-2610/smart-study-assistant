import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import streamlit as st

from backend.graph import run_agent

from frontend.upload_handler import (
    process_uploaded_documents,
    get_uploaded_documents
)


st.set_page_config(

    page_title="Smart Study Assistant",

    page_icon="📚",

    layout="wide"

)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.main{
    background:#0E1117;
}

.stButton>button{
    width:100%;
    height:45px;
    border-radius:10px;
}

[data-testid="stSidebar"]{
    background:#1E293B;
}

[data-testid="stSidebar"] *{
    color:white !important;
}

div[data-testid="metric-container"]{
    background:#1E293B;
    padding:15px;
    border-radius:12px;
    border:1px solid #334155;
}

</style>
""", unsafe_allow_html=True)

# ===================================================
# SIDEBAR
# ===================================================

with st.sidebar:

    st.title("📚 Smart Study Assistant")

    st.markdown("---")

    uploaded_files = st.file_uploader(

        "Upload Study Material",

        type=["pdf"],

        accept_multiple_files=True

    )

    if uploaded_files:

        st.success(
            f"{len(uploaded_files)} file(s) selected."
        )

        if st.button(
            "🚀 Process Documents",
            use_container_width=True
        ):

            process_uploaded_documents(
                uploaded_files
            )

            st.rerun()

    st.markdown("---")

    st.subheader("📂 Uploaded Documents")

    documents = get_uploaded_documents()

    if documents:

        selected_document = st.radio(

            "Search Scope",

            ["All Documents"] + documents,

            index=0

        )

    else:

        selected_document = "All Documents"

        st.info(
            "Upload PDFs to begin."
        )

    st.markdown("---")

    st.subheader("⚡ Quick Actions")

    if st.button(
        "📑 Summary",
        use_container_width=True
    ):

        st.session_state["prompt"] = (
            "Summarize selected document"
        )

    if st.button(
        "❓ Quiz",
        use_container_width=True
    ):

        st.session_state["prompt"] = (
            "Generate quiz"
        )

    if st.button(
        "🧠 Flashcards",
        use_container_width=True
    ):

        st.session_state["prompt"] = (
            "Generate flashcards"
        )

    if st.button(
        "💬 Ask Question",
        use_container_width=True
    ):

        st.session_state["prompt"] = ""

    st.markdown("---")

    st.caption("⚙ Powered By")

    st.caption("• Groq")

    st.caption("• LangChain")

    st.caption("• LangGraph")

    st.caption("• ChromaDB")

    st.caption("• Streamlit")


# ===================================================
# HEADER
# ===================================================

st.title("📚 Smart Study Assistant")

st.markdown(
    "### Learn Smarter with AI"
)

st.caption(
    "Upload multiple PDFs • Ask Questions • Summary • Quiz • Flashcards"
)

st.markdown("---")

# ===================================================
# METRICS
# ===================================================

documents = get_uploaded_documents()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "📄 Documents",
        len(documents)
    )

with c2:

    if documents:
        st.metric(
            "📚 Vector DB",
            "Ready"
        )
    else:
        st.metric(
            "📚 Vector DB",
            "Empty"
        )

with c3:
    st.metric(
        "🤖 AI",
        "Online"
    )

with c4:
    st.metric(
        "⚡ Status",
        "Active"
    )

st.markdown("---")

# ===================================================
# CHAT HISTORY
# ===================================================

if "messages" not in st.session_state:

    st.session_state.messages = [

        {
            "role": "assistant",

            "content":
            "👋 Hello!\n\n"
            "Upload one or more PDFs.\n\n"
            "Click **Process Documents**.\n\n"
            "Choose a document (or All Documents) from the sidebar.\n\n"
            "Then ask me anything!"
        }

    ]

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

default_prompt = st.session_state.get(
    "prompt",
    ""
)

prompt = st.chat_input(
    "Ask anything..."
)

if prompt is None and default_prompt != "":

    prompt = default_prompt

    st.session_state["prompt"] = ""

# ===================================================
# CHAT
# ===================================================

if prompt:

    st.session_state.messages.append(

        {

            "role": "user",

            "content": prompt

        }

    )

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner(
            "Thinking..."
        ):

            answer = run_agent(

                prompt,

                selected_document

            )

            st.markdown(answer)

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": answer

        }

    )