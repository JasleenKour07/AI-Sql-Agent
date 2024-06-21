# AI-Sql-Agent
# Northwind Database Query Bot

This Python script allows you to query the Northwind database using predefined SQL queries and aggregate functions. It supports listing all records, counting records, and performing aggregate operations such as SUM, AVG, MIN, and MAX.

## Features

- List all records from various tables in the Northwind database.
- Count the total number of records in various tables.
- Perform aggregate operations such as SUM, AVG, MIN, and MAX on different fields.
- Predefined SQL queries for common tasks.

## Prerequisites

- Python 3.x
- `pyodbc` library
- SQL Server Management Studio (SSMS)
- SQL Server with Northwind database installed

## Installation

1. **Install SQL Server and SSMS:**
   - Download and install SQL Server from the [Microsoft website](https://www.microsoft.com/en-us/sql-server/sql-server-downloads).
   - Download and install SQL Server Management Studio (SSMS) from the [Microsoft website](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms).

2. **Install the Northwind Database:**
   - Open SSMS and connect to your SQL Server instance.
   - Download the Northwind database script from [Microsoft's sample database GitHub repository](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/northwind-pubs).
   - Execute the script in SSMS to create and populate the Northwind database.

3. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/northwind-query-bot.git
    cd northwind-query-bot
    ```

4. **Install the required Python packages:**

    ```sh
    pip install pyodbc
    ```

5. **Update the database connection details in the script:**

    ```python
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=YOUR_SERVER_NAME;'
        'DATABASE=Northwind;'
        'UID=YOUR_USERNAME;'
        'PWD=YOUR_PASSWORD;'
        'Trusted_Connection=yes;'
    )
    ```

## Usage

1. **Run the script:**

    ```sh
    python query_bot.py
    ```

2. **Enter your query when prompted.** You can use any of the predefined queries listed below.

### Predefined Queries

- **Listing all records:**
  - `list all products`
  - `list all categories`
  - `list all customers`
  - `list all employees`
  - `list all order details`
  - `list all orders`
  - `list all shippers`
  - `list all suppliers`
  - `list all territories`
  - `list all regions`
  - `list all customer demographics`
  - `list all employee territories`
  - `list all customer customer demo`

- **Counting records:**
  - `count products`
  - `count categories`
  - `count customers`
  - `count employees`
  - `count order details`
  - `count orders`
  - `count shippers`
  - `count suppliers`
  - `count territories`
  - `count regions`
  - `count customer demographics`
  - `count employee territories`
  - `count customer customer demo`

- **Aggregate functions:**
  - `average unit price by category`
  - `max unit price by category`
  - `min unit price by category`
  - `total quantity by product`
  - `average discount by product`
  - `max discount by product`
  - `min discount by product`
  - `total sales by employee`
  - `total sales by customer`

- **Other queries:**
  - `ten most expensive products`
  - `orders by customer`
  - `products in category`
  - `sales by employee`
  - `orders in date range`
  - `employees in region`
  - `products by supplier`

## Example

```sh
Enter your query (or 'exit' to quit): list all products

Generated SQL Query: 
SELECT * FROM Products;

Query Results:
{'ProductID': 1, 'ProductName': 'Chai', 'SupplierID': 1, 'CategoryID': 1, ...}
{'ProductID': 2, 'ProductName': 'Chang', 'SupplierID': 1, 'CategoryID': 1, ...}
...
# Northwind Database Query Bot

This Python script allows you to query the Northwind database using predefined SQL queries and aggregate functions. It supports listing all records, counting records, and performing aggregate operations such as SUM, AVG, MIN, and MAX.

## Libraries and Tools Used

- **Python 3.x:** The programming language used to write the script.
- **pyodbc:** A Python library for connecting to ODBC databases. Install using `pip install pyodbc`.
- **SQL Server:** The database server where the Northwind database is hosted.
- **SQL Server Management Studio (SSMS):** A tool for managing SQL Server databases.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
 
This README now includes information about the libraries (`pyodbc`), tools (SQL Server and SSMS), installation steps, usage instructions, predefined queries, example usage, and details about contributing and the project's license. Adjust the placeholders (`YOUR_SERVER_NAME`, `YOUR_USERNAME`, `YOUR_PASSWORD`) in the database connection section with your actual credentials.
