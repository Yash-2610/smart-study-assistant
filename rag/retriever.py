from langchain_community.vectorstores import Chroma
import chromadb

from backend.config import embedding_model

VECTOR_DB = "vectorstore"


def get_retriever(selected_document=None):

    chromadb.api.client.SharedSystemClient.clear_system_cache()

    vectorstore = Chroma(

        persist_directory=VECTOR_DB,

        embedding_function=embedding_model

    )

    if selected_document in [None, "", "All Documents"]:

        return vectorstore.as_retriever(

            search_kwargs={"k": 4}

        )

    return vectorstore.as_retriever(

        search_kwargs={

            "k": 4,

            "filter": {

                "source": selected_document

            }

        }

    )