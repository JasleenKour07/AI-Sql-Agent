import pyodbc

# Set up the SQL Server connection (replace with your actual connection details)
# use it while using SSMS
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=your_server_name;'
    'DATABASE=database_name;'
    'UID=your_username;'
    'PWD=your_password;'
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
    "count customer customer demo": "SELECT COUNT(*) AS TotalCount FROM CustomerCustomerDemo",
    "ten most expensive products": "SELECT TOP 10 ProductName, UnitPrice FROM Products ORDER BY UnitPrice DESC",
    "orders by customer": "SELECT * FROM Orders WHERE CustomerID = 'ALFKI'",  # Example CustomerID
    "products in category": "SELECT * FROM Products WHERE CategoryID = 1",  # Example CategoryID
    "sales by employee": "SELECT Employees.LastName, Employees.FirstName, Orders.OrderID, Orders.OrderDate, [Order Details].UnitPrice * [Order Details].Quantity AS SaleAmount FROM Orders INNER JOIN [Order Details] ON Orders.OrderID = [Order Details].OrderID INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID ORDER BY Employees.LastName, Employees.FirstName",
    "total sales by employee": "SELECT Employees.LastName, Employees.FirstName, SUM([Order Details].UnitPrice * [Order Details].Quantity) AS TotalSales FROM Orders INNER JOIN [Order Details] ON Orders.OrderID = [Order Details].OrderID INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID GROUP BY Employees.LastName, Employees.FirstName ORDER BY TotalSales DESC",
    "total sales by customer": "SELECT Customers.CompanyName, SUM([Order Details].UnitPrice * [Order Details].Quantity) AS TotalSales FROM Orders INNER JOIN [Order Details] ON Orders.OrderID = [Order Details].OrderID INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID GROUP BY Customers.CompanyName ORDER BY TotalSales DESC",
    "products by supplier": "SELECT Suppliers.CompanyName, Products.ProductName FROM Products INNER JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID ORDER BY Suppliers.CompanyName",
    "orders in date range": "SELECT * FROM Orders WHERE OrderDate BETWEEN '1997-01-01' AND '1997-12-31'",  # Example date range
    "employees in region": "SELECT * FROM Employees WHERE Region = 'WA'",  # Example region
    "average unit price by category": "SELECT Categories.CategoryName, AVG(Products.UnitPrice) AS AvgUnitPrice FROM Products INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID GROUP BY Categories.CategoryName",
    "max unit price by category": "SELECT Categories.CategoryName, MAX(Products.UnitPrice) AS MaxUnitPrice FROM Products INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID GROUP BY Categories.CategoryName",
    "min unit price by category": "SELECT Categories.CategoryName, MIN(Products.UnitPrice) AS MinUnitPrice FROM Products INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID GROUP BY Categories.CategoryName",
    "total quantity by product": "SELECT Products.ProductName, SUM([Order Details].Quantity) AS TotalQuantity FROM [Order Details] INNER JOIN Products ON [Order Details].ProductID = Products.ProductID GROUP BY Products.ProductName",
    "average discount by product": "SELECT Products.ProductName, AVG([Order Details].Discount) AS AvgDiscount FROM [Order Details] INNER JOIN Products ON [Order Details].ProductID = Products.ProductID GROUP BY Products.ProductName",
    "max discount by product": "SELECT Products.ProductName, MAX([Order Details].Discount) AS MaxDiscount FROM [Order Details] INNER JOIN Products ON [Order Details].ProductID = Products.ProductID GROUP BY Products.ProductName",
    "min discount by product": "SELECT Products.ProductName, MIN([Order Details].Discount) AS MinDiscount FROM [Order Details] INNER JOIN Products ON [Order Details].ProductID = Products.ProductID GROUP BY Products.ProductName"
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
