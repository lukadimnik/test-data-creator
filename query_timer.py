# script to test execution times of queries
import sqlite3
import random
import time

# open database
conn = sqlite3.connect('Movies.sqlite')
cur = conn.cursor()

count = 0
start_time = time.time()
while count < 100:
    count = count + 1
    random_year = random.randint(1900, 2000)
    # result = cur.execute(
    #     f'SELECT COUNT(*) FROM Movie WHERE year = ${random_year}')
    query = cur.execute(
        'SELECT COUNT(*) FROM Movie WHERE year = ?', (random_year,))
    fetch_query = query.fetchall()
    result = fetch_query[0][0]
    # print(f"There was {result} movies in year {random_year}")

end_time = time.time()
print("Elapsed time: ", end_time - start_time)
