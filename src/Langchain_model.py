from langchain.llms import GooglePalm
import streamlit as st
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate

from src.few_shots_helper import few_shots, mysql_prompt ,final_prompt


import os
from dotenv import load_dotenv
load_dotenv()

LANGCHAIN_TRACING_V2 = st.secrets.LANGCHAIN_TRACING_V2
LANGCHAIN_API_KEY = st.secrets.LANGCHAIN_API_KEY


def create_sql_database(db_user, db_password, db_host, db_name):
    """
    Create an SQLDatabase instance from the provided connection details.
    """
    return SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                                sample_rows_in_table_info=3)

def create_llm(google_api_key, temperature=0.1):
    """
    Create a GooglePalm LLM instance with the provided API key and temperature.
    """
    return GooglePalm(google_api_key=google_api_key, temperature=temperature)

def create_embeddings():
    """
    Create a HuggingFaceEmbeddings instance.
    """
    return HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

def create_vectorstore(embeddings, few_shots):
    """
    Create a FAISS vectorstore from the provided few-shot examples.
    """
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    return FAISS.from_texts(to_vectorize, embeddings, metadatas=few_shots)

def create_example_selector(vectorstore):
    """
    Create a SemanticSimilarityExampleSelector instance with the provided vectorstore.
    """
    return SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,
    )

def create_example_prompt():
    """
    Create an example prompt for the FewShotPromptTemplate.
    """
    return PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

def create_few_shot_prompt(example_selector, example_prompt):
    """
    Create a FewShotPromptTemplate with the provided example selector and example prompt.
    """
    return FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],
    )

def get_few_shot_db_chain(db_user, db_password, db_host, db_name, google_api_key):
    """
    Create a SQLDatabaseChain with a FewShotPromptTemplate.
    """
    db = create_sql_database(db_user, db_password, db_host, db_name)
    google_llm = create_llm(google_api_key)
    embeddings = create_embeddings()
    vectorstore = create_vectorstore(embeddings, few_shots)
    example_selector = create_example_selector(vectorstore)
    example_prompt = create_example_prompt()
    few_shot_prompt = create_few_shot_prompt(example_selector, example_prompt)
    chain = SQLDatabaseChain.from_llm(google_llm, db, verbose=True, prompt=few_shot_prompt)
    return chain

def generate_final_output(chain,google_llm, question):
    """
    Generate the final output by sending the result to the LLM again with the question and answer.
    """
    result = chain.run(question)
    final_output = google_llm(f"Question: {question} Answer: {result} prompt:{final_prompt}")
    return final_output

def get_answer_to_question(question):
    db_user = st.secrets.db_user
    db_password = st.secrets.db_password
    db_host = st.secrets.db_host
    db_name = st.secrets.db_name
    google_api_key = st.secrets.GOOGLE_API_KEY

    chain = get_few_shot_db_chain(db_user, db_password, db_host, db_name, google_api_key)
    google_llm = create_llm(google_api_key)
    final_output = generate_final_output(chain,google_llm, question)
    return final_output

if __name__ == "__main__":
    question = "What is the price of puma white shoe size 10 and black van heusen tshirt?"
    answer = get_answer_to_question(question)
    print(answer)
