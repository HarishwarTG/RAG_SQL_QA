few_shots = [
    {
        'Question': "How many t-shirts do we have left for Nike in XS size and white color?",
        'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
        'SQLResult': "Result of the SQL query",
        'Answer': "91"
    },
    {
        'Question': "What is the total price of the inventory for all S-size t-shirts?",
        'SQLQuery': "SELECT SUM(price_per_unit * stock_quantity) FROM t_shirts WHERE size = 'S'",
        'SQLResult': "Result of the SQL query",
        'Answer': "22292"
    },
    {
        'Question': "If we sell all the Levi’s T-shirts today with discounts applied, how much revenue will our store generate (post discounts)?",
        'SQLQuery': """
            SELECT SUM(a.total_amount * ((100 - COALESCE(discounts.pct_discount, 0)) / 100)) AS total_revenue 
            FROM (
                SELECT SUM(price_per_unit * stock_quantity) AS total_amount, t_shirt_id 
                FROM t_shirts 
                WHERE brand = 'Levi'
                GROUP BY t_shirt_id
            ) a 
            LEFT JOIN discounts ON a.t_shirt_id = discounts.t_shirt_id
        """,
        'SQLResult': "Result of the SQL query",
        'Answer': "16725.4"
    },
    {
        'Question': "If we sell all the Levi’s T-shirts today, how much revenue will our store generate without discount?",
        'SQLQuery': "SELECT SUM(price_per_unit * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
        'SQLResult': "Result of the SQL query",
        'Answer': "17462"
    },
    {
        'Question': "Availability stock of LEvi tshirts ",
        'SQLQuery': "SELECT brand, color, size, stock_quantity FROM t_shirts where brand ='Levi'",
        'SQLResult': "Result of the SQL query",
        'Answer': '''Levi	Red	M	20
                Levi	Blue	L	30
                Levi	Black	M	35
                Levi	White	XS	70"'''
    },
    {
        'Question': "list stoke of nike white shoe size available?",
        'SQLQuery': """
            SELECT model,size, stock_quantity 
FROM shoes WHERE model IN ('Nike Air Force', 'Nike Zoom') AND color = 'White';
        """,
        'SQLResult': "Result of the SQL query",
        'Answer': "Nike Air Force	7	22"
    },
    {
        'Question': "What is the total revenue of all products in the inventory?",
        'SQLQuery': """
            SELECT SUM(price_per_unit * stock_quantity) AS total_revenue 
            FROM (
                SELECT price_per_unit, stock_quantity FROM t_shirts
                UNION ALL
                SELECT price_per_unit, stock_quantity FROM shoes
            ) AS all_products
        """,
        'SQLResult': "Result of the SQL query",
        'Answer': "Result of the SQL query"
    }
]


    
    



mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".
    
    Use the following format:
    
    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here
    
    No pre-amble.
    """
    

final_prompt = """You're the inventory manager at a Walmart store. An employee asks you various questions about stock levels, pricing, and discounts. Respond in a casual and informative way, providing the answer in rupees (₹). 
Answer only in 1 line relavent to the above Question and given answer.if multiple answers return in list table format.
**Here's a quick rundown to help you out:**

* We have a wide variety of t-shirts (Van Huesen, Levi's, Nike, Adidas) in various sizes (XS, S, M, L, XL) and colors (Red, Blue, Black, White).
* Shoes come in different brands model(Nike Air Force,Jordan,Adidas Ultraboost,Puma RS-X,Reebok Classic,Bata Power,Nike Zoom) with various sizes and colors."""