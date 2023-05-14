# Import relevant modules

# import os

from langchain import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

# import requests
# from langchain.indexes import VectorstoreIndexCreator
# from langchain.chains.question_answering import load_qa_chain

# from getpass import getpass


# def ask_user_for_key():
#     """
#     Asks user for HuggingFace API token
#     """
#     HUGGINGFACEHUB_API_TOKEN = getpass()
#     os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN


def load_document(document_path):
    """
    Fetches path to PDF from user and loads it using PyPDF
    """
    return PyPDFLoader(document_path).load()


def split_document(document):
    """
    Provided document is split using CharacterTextSplitter
    """
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    return texts


# This code loads a model from the HuggingFace repository.

def load_embeddings():
    """
    HuggingFaceEmbeddings is loaded here.
    """
    return HuggingFaceEmbeddings()


def create_vectors(texts, embeddings):
    """
    Chroma vectorstore is created here.
    Chroma is a database for building AI applications with embeddings.
    """
    return Chroma.from_documents(texts, embeddings)


def create_retriever(vector):
    """
    Retrievers are used to find the most similar documents to a query.
    """
    retriever = vector.as_retriever(
        search_type="similarity", search_kwargs={"k": 1})
    return retriever


def ask_question(retriever):
    """
    RetrievalQA is used to find the most similar documents to a query.
    User asks query and the chain is utilized to retrieve answer
    from the document provided.
    """
    qa = RetrievalQA.from_chain_type(
        llm=HuggingFaceHub(
            repo_id="google/flan-t5-large",
            model_kwargs={"temperature": 0, "max_length": 512}),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa


def qa_model(document_path):
    """
    This function is the main function that runs the entire script.
    """
    document = load_document(document_path)
    texts = split_document(document)
    embeddings = load_embeddings()
    vector = create_vectors(texts, embeddings)
    retriever = create_retriever(vector)
    qa = ask_question(retriever)

    return qa
