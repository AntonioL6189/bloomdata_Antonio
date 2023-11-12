import sqlite3

# Open a connection to a new (blank) database file called demo_data.sqlite3
conn = sqlite3.connect("demo_data.sqlite3")
curs = conn.cursor()


def execute_query(curs, query_list):
    for query in query_list:
        curs.execute(query)
    conn.commit()
    return curs.fetchall()

# Execute CREATE TABLE statement to create the 'demo' table


table = '''
    CREATE TABLE IF NOT EXISTS demo (
        s TEXT NOT NULL,
        x INTEGER NOT NULL,
        y INTEGER NOT NULL
    )
'''

row_1 = '''INSERT INTO demo ('s', 'x', 'y') VALUES ('g', 3, 9)'''
row_2 = '''INSERT INTO demo ('s', 'x', 'y') VALUES ('v', 5, 7)'''
row_3 = '''INSERT INTO demo ('s', 'x', 'y') VALUES ('f', 8, 7)'''

query_list = (table, row_1, row_2, row_3)

if __name__ == '__main__':
    print(execute_query(curs, query_list))

# Query 1: How many rows are in the table?
row_count = "SELECT COUNT(*) FROM demo"


# Query 2: How many rows are there where both x and y are at least 5?
xy_at_least_5 = "SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5"


# Query 3: How many unique values of y are there?
unique_y = "SELECT COUNT(DISTINCT y) FROM demo"


"""
row_count: The result of the query to count the number of rows in the
table.
row_count_ = <Result from the database query for row count>

xy_at_least_5: The result of the query to count the number of rows
where x and y are at least 5.
xy_at_least_5 = <Result from the database query for xy_at_least_5>

unique_y: The result of the query to count the number of unique values
of y.
unique_y = <Result from the database query for unique_y>
"""
