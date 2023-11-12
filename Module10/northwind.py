import sqlite3

# Part 2 - The Northwind Database - Basic Queries

# Using sqlite3, connect to the given northwind_small.sqlite3 database
conn = sqlite3.connect("northwind_small.sqlite3")
curs = conn.cursor()


def execute_query(curs, query_list):
    for query in query_list:
        curs.execute(query)
    conn.commit()
    return curs.fetchall()


# Query 1: 10 most expensive items


expensive_items = '''
    SELECT *
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10
'''
# Query 2: Average hiring age


avg_hire_age = '''
    SELECT AVG(HireDate - BirthDate) AS avg_age
    FROM Employee
'''

# Part 3 Sailing the Northwind Seas

# Query 3: 10 most expensive items based on Products


ten_most_expensive = '''
    SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
    FROM Product
    JOIN Supplier ON Product.SupplierId = Supplier.Id
    ORDER BY Product.UnitPrice DESC
    LIMIT 10
'''
# Query 4: Largest catergory


largest_category = '''
    SELECT Category.CategoryName, COUNT(DISTINCT Product.ProductName) AS
    num_products
    FROM Category
    JOIN Product ON Category.Id = Product.CategoryId
    GROUP BY Category.CategoryName
    ORDER BY num_products DESC
    LIMIT 1
'''
query_list = (expensive_items, avg_hire_age,
              ten_most_expensive, largest_category)


if __name__ == '__main__':
    print(execute_query(curs, query_list))

"""
expensive_items: Query to find the ten most expensive items in the database.
expensive_items = <Query string for finding expensive items>

avg_hire_age: Query to find the average age of employee hiring.
avg_hire_age = <Query string for finding average hire age>

ten_most_expensive: Query to find the ten most expensive
items and their suppliers.
ten_most_expensive = <Query string for finding ten most expensive items>

largest_category: Query to find the largest
category (by number of unique products).
largest_category = <Query string for finding largest category>
"""
