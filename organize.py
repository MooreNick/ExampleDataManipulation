import pandas as pd
import sqlite3

# I want to demonstrate proficiency with SQL.
# To accomplish this I will be using the sqlite3 library
# and the data we have previously generated and manipulated.
# Sqlite3 allows me to create a database in memory and run queries on it.

def main():
    # :memory: is a special name that creates a database in memory
    conn = sqlite3.connect(':memory:')
    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Create Pandas DataFrame Objects to store our data
    data = pd.read_csv('fixedData.csv')
    print(data)

    # Use that object to create our new in-memory database
    data.to_sql('data', conn, if_exists='replace', index=False)

    # Example basic query using our cursor (cur) object
    cursorQuery = cur.execute('SELECT * FROM data LIMIT 10')
    print("Basic query utilizing in-memory database:", "\n", cursorQuery.fetchall())

    # More complex query using Pandas to store the data as a Pandas DataFrame Object
    query = "SELECT GENDER, COUNT(*) AS Number FROM data d WHERE d.Age > 50 GROUP BY d.Gender"
    queryDF = pd.read_sql(query, conn)
    conn.close()

    # Let's look at some simpler ways to achieve the same results, using Pandas, without an in-memory database
    # Refer to line 15 where we read in the .csv file
    womenOver50 = data[(data['Age'] > 50) & (data['Gender'] == 'F')]
    menOver50 = data[(data['Age'] > 50) & (data['Gender'] == 'M')]

    print("Query using Pandas.read_sql() method:", "\n", queryDF)
    print("Count of women over 50 using simpler method:", len(womenOver50))
    print("Count of men over 50 using simpler method:", len(menOver50))


if __name__ == '__main__':
    main()