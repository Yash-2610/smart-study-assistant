import os
import subprocess
import sys

import streamlit as st

UPLOAD_FOLDER = "uploads"


def save_uploaded_files(uploaded_files):

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Remove old PDFs

    for file in os.listdir(UPLOAD_FOLDER):

        if file.lower().endswith(".pdf"):

            os.remove(
                os.path.join(
                    UPLOAD_FOLDER,
                    file
                )
            )

    # Save new PDFs

    for uploaded_file in uploaded_files:

        with open(
            os.path.join(
                UPLOAD_FOLDER,
                uploaded_file.name
            ),
            "wb"
        ) as f:

            f.write(uploaded_file.getbuffer())


def process_uploaded_documents(uploaded_files):

    if not uploaded_files:

        st.warning("Please upload at least one PDF.")

        return False

    save_uploaded_files(uploaded_files)

    with st.spinner("Creating Vector Database..."):

        result = subprocess.run(

            [sys.executable, "-m", "rag.ingest"],

            capture_output=True,

            text=True

        )

    if result.returncode == 0:

        st.success("✅ Documents Processed Successfully")

        st.rerun()

        return True

    else:

        st.error("❌ Failed to process documents.")

        st.code(result.stderr)

        return False


def get_uploaded_documents():

    if not os.path.exists(UPLOAD_FOLDER):

        return []

    return sorted(

        [

            file

            for file in os.listdir(UPLOAD_FOLDER)

            if file.lower().endswith(".pdf")

        ]

    )