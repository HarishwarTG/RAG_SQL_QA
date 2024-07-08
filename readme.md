## Project Idea
    Efficient Query Processing: Retrieving information from a simulated Walmart inventory database using advanced technologies like GooglePalm LLM, Langchain, HuggingFace's Embedding model, and FAISS Vectorstore poses several challenges:

1.Natural Language Understanding: Translating user queries, expressed in natural language, into structured SQL queries that can efficiently retrieve data from the MySQL database.

2.Real-time Processing: Ensuring that user queries are processed in real-time, with minimal latency, to provide immediate answers to inventory-related questions.

3.Data Integration: Integrating multiple technologies seamlessly to handle various aspects of the question-answering pipeline—from text embedding to similarity search and database query execution.

4.Accuracy and Reliability: Ensuring that the retrieved answers are accurate and reliable, reflecting the current state of the simulated inventory database.

## Solution Approach
Architecture: Implement a retrieval-augmented generation (RAG) architecture to handle the flow of data from user input to database query and response generation.

Integration: Seamlessly integrate the different technologies to form a cohesive system that handles natural language processing and database querying.

![Arch Diagram](https://python.langchain.com/v0.1/assets/images/sql_usecase-d432701261f05ab69b38576093718cf3.png)

## Technologies Used
    - Langchain: A framework for developing applications powered by language models. Langchain is used to manage the workflow of converting user questions into SQL queries, retrieving data, and presenting answers.
    - GooglePalm LLM: Google’s language model is utilized for understanding and processing natural language questions. This model helps in parsing user queries and generating relevant SQL queries.
    - Langchain: A framework for developing applications powered by language models. Langchain is used to manage the workflow of converting user questions into SQL queries, retrieving data, and presenting answers.
    - HuggingFace's Embedding model: This model is used to convert textual data into embeddings, which are dense vector representations of text. These embeddings are crucial for comparing and finding the similarity between user queries and database entries.
    - FAISS Vectorstore: Facebook AI Similarity Search (FAISS) is a library for efficient similarity search and clustering of dense vectors. It is used to quickly find relevant data from the database based on the embeddings.
    - Streamlit: A fast and easy way to build and share data apps. Streamlit is used for building the web application interface, providing a user-friendly environment for entering questions and viewing answers.

## Features
    - User Input: Users can enter natural language questions about the Walmart inventory. The interface is intuitive, making it easy for users to interact with the application.
    - Real-time Processing: The application processes user questions in real-time. It converts the question into an SQL query, retrieves the relevant data, and presents the answer back to the user.
    - Error Handling: The application includes robust error handling to manage unexpected issues gracefully. This ensures that users have a smooth experience even when something goes wrong.

## Developer
        This project was created by [Harishwar T G](https://www.linkedin.com/in/harishwartg/) as a personal learning endeavor.

**Note:** This application does not include the original Walmart inventory database. It is a simulated environment for educational purposes.
        