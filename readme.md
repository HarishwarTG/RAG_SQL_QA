<h1 align="center" id="title">Walmart Inventory Q&amp;A Application</h1>

<h2>🚀 Streamlit Webpage</h2>

[https://ragprojectharishwar.streamlit.app/](https://ragprojectharishwar.streamlit.app/)

<h2>Project Idea</h2>

Efficient Query Processing: Retrieving information from a simulated Walmart inventory database using advanced technologies like GooglePalm LLM, Langchain, HuggingFace's Embedding model, and FAISS Vectorstore poses several challenges:


1.Natural Language Understanding: Translating user queries, expressed in natural language, into structured SQL queries that can efficiently retrieve data from the MySQL database.

2.Real-time Processing: Ensuring that user queries are processed in real-time, with minimal latency, to provide immediate answers to inventory-related questions.

3.Data Integration: Integrating multiple technologies seamlessly to handle various aspects of the question-answering pipeline—from text embedding to similarity search and database query execution.

4.Accuracy and Reliability: Ensuring that the retrieved answers are accurate and reliable, reflecting the current state of the simulated inventory database.

<h2>Database Information</h2>

<h3>T-Shirts:</h3>

 - We have a wide variety of t-shirts from brands like Van Huesen, Levi's, Nike, and Adidas. These t-shirts come in various sizes (XS, S, M, L, XL) and colors (Red, Blue, Black, White).
<h3>Shoes:</h3>

- Our shoe inventory includes different models such as Nike Air Force, Jordan, Adidas Ultraboost, Puma RS-X, Reebok Classic, Bata Power, and Nike Zoom. These shoes come in various sizes and colors.

<h3>Tables</h3>

- t_shirts: Contains information about t-shirts including brand, color, size, price per unit, and stock quantity.
- shoes: Contains information about shoes including model, color, size, price per unit, and stock quantity.
- discounts: Contains information about discounts on t-shirts and shoes.


<h2>Solution Approach</h2>

- Architecture: Implement a retrieval-augmented generation (RAG) architecture to handle the flow of data from user input to database query and response generation.

- Integration: Seamlessly integrate the different technologies to form a cohesive system that handles natural language processing and database querying.

![Arch Diagram](https://python.langchain.com/v0.1/assets/images/sql_usecase-d432701261f05ab69b38576093718cf3.png)

Here're some of the project's best features:

*   User Input: Users can enter natural language questions about the Walmart inventory. The interface is intuitive making it easy for usersto interact with the application.
*   Real-time Processing: The application processes user questions in real-time. It converts the question into an SQL query retrieves therelevant data and presents the answer back to the user.
*   Error Handling: The application includes robust error handling to manage unexpected issues gracefully. This ensures that users have asmooth experience even when something goes wrong.

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   Aws RDS-MySQL
*   Langchain
*   Huggingface

<h2>💖Like my work?</h2>

This project was created by Harishwar T G(https://www.linkedin.com/in/harishwartg/) as a personal learning endeavor. Note: This application does not include the original Walmart inventory database. It is a simulated environment for educational purposes.