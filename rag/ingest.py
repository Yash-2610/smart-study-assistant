import os
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

UPLOAD_FOLDER = "uploads"
VECTOR_DB = "vectorstore"


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def ingest_all_pdfs():

    # Remove previous database

    if os.path.exists(VECTOR_DB):

        shutil.rmtree(
            VECTOR_DB,
            ignore_errors=True
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    all_chunks = []

    pdf_files = [

        file

        for file in os.listdir(UPLOAD_FOLDER)

        if file.lower().endswith(".pdf")

    ]

    if len(pdf_files) == 0:

        print("No PDFs Found.")

        return False

    for pdf in pdf_files:

        print(f"Reading {pdf}")

        loader = PyPDFLoader(

            os.path.join(
                UPLOAD_FOLDER,
                pdf
            )

        )

        docs = loader.load()

        for doc in docs:

            doc.metadata["source"] = pdf

        chunks = splitter.split_documents(
            docs
        )

        all_chunks.extend(
            chunks
        )

    print(f"Chunks : {len(all_chunks)}")

    Chroma.from_documents(

        documents=all_chunks,

        embedding=embedding_model,

        persist_directory=VECTOR_DB

    )

    print("Vector Database Created.")

    return True


if __name__ == "__main__":

    success = ingest_all_pdfs()

    if success:

        print("SUCCESS")

    else:

        print("FAILED")