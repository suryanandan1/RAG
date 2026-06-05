from chatbot.loaders import load_pdfs
from chatbot.splitter import split_documents
from chatbot.embeddings_store import create_vectorstore
from chatbot.qa_chain import build_qa_chain


def load_rag():

    domestic_docs = load_pdfs(
        ["data/domestic_travel.pdf"]
    )

    foreign_docs = load_pdfs(
        ["data/foreign_travel.pdf"]
    )

    all_docs = domestic_docs + foreign_docs

    splits = split_documents(
        all_docs
    )

    vectorstore = create_vectorstore(
        splits
    )

    qa_chain = build_qa_chain(
        vectorstore
    )

    return qa_chain