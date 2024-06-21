import pyodbc

# Set up the SQL Server connection (replace with your actual connection details)
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=JASLEEN;'
    'DATABASE=Northwind;'
    'UID=JASLEEN\\ASUS;'
    'PWD=Jasleen@2002;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# Mapping of user-friendly table names to SQL table names
table_mapping = {
    "products": "Products",
    "categories": "Categories",
    "customers": "Customers",
    "employees": "Employees",
    "order details": "[Order Details]",
    "orders": "Orders",
    "shippers": "Shippers",
    "suppliers": "Suppliers",
    "territories": "Territories",
    "region": "Region",
    "customerdemographics": "CustomerDemographics",
    "employeeterritories": "EmployeeTerritories",
    "customercustomerdemo": "CustomerCustomerDemo"
}

predefined_queries = {
    "list all products": "SELECT * FROM Products",
    "list all categories": "SELECT * FROM Categories",
    "list all customers": "SELECT * FROM Customers",
    "list all employees": "SELECT * FROM Employees",
    "list all order details": "SELECT * FROM [Order Details]",
    "list all orders": "SELECT * FROM Orders",
    "list all shippers": "SELECT * FROM Shippers",
    "list all suppliers": "SELECT * FROM Suppliers",
    "list all territories": "SELECT * FROM Territories",
    "list all regions": "SELECT * FROM Region",
    "list all customer demographics": "SELECT * FROM CustomerDemographics",
    "list all employee territories": "SELECT * FROM EmployeeTerritories",
    "list all customer customer demo": "SELECT * FROM CustomerCustomerDemo",
    "count products": "SELECT COUNT(*) AS TotalCount FROM Products",
    "count categories": "SELECT COUNT(*) AS TotalCount FROM Categories",
    "count customers": "SELECT COUNT(*) AS TotalCount FROM Customers",
    "count employees": "SELECT COUNT(*) AS TotalCount FROM Employees",
    "count order details": "SELECT COUNT(*) AS TotalCount FROM [Order Details]",
    "count orders": "SELECT COUNT(*) AS TotalCount FROM Orders",
    "count shippers": "SELECT COUNT(*) AS TotalCount FROM Shippers",
    "count suppliers": "SELECT COUNT(*) AS TotalCount FROM Suppliers",
    "count territories": "SELECT COUNT(*) AS TotalCount FROM Territories",
    "count regions": "SELECT COUNT(*) AS TotalCount FROM Region",
    "count customer demographics": "SELECT COUNT(*) AS TotalCount FROM CustomerDemographics",
    "count employee territories": "SELECT COUNT(*) AS TotalCount FROM EmployeeTerritories",
    "count customer customer demo": "SELECT COUNT(*) AS TotalCount FROM CustomerCustomerDemo"
}

def query_database(sql_query):
    try:
        cursor.execute(sql_query)
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return results
    except Exception as e:
        return [{"Error": str(e)}]

def query_database(sql_query):
    try:
        cursor.execute(sql_query)
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return results
    except Exception as e:
        return [{"Error": str(e)}]

if __name__ == "__main__":
    while True:
        user_input = input("\nEnter your query (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        
        if user_input.lower() in predefined_queries:
            sql_query = predefined_queries[user_input.lower()]
            print(f"\nGenerated SQL Query: {sql_query}\n")
            
            results = query_database(sql_query)
            print("\nQuery Results:")
            if results and isinstance(results, list):
                for result in results:
                    if "TotalCount" in result:
                        print(f"Total count: {result['TotalCount']}")
                    else:
                        print(result)
            else:
                print(results)  # Print error message if query fails
        else:
            print("Query not found in predefined queries. Please try again.")

    # Close the database connection at the end
    conn.close()