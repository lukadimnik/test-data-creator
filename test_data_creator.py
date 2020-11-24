import sqlite3
import random
import string
import time

# open database
conn = sqlite3.connect('Movies.sqlite')
cur = conn.cursor()

# Setup a table
cur.executescript('''

DROP TABLE IF EXISTS Movie;

CREATE TABLE Movie (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT,
    year   INTEGER
);

''')


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


count = 0
start_time = time.time()
# create 1 million rows of random test data
while count < 1000000:
    count = count + 1
    random_name = get_random_string(5)
    random_year = random.randint(1900, 2000)
    cur.execute('''INSERT OR IGNORE INTO Movie (name, year)
                VALUES ( ?, ? )''', (random_name, random_year))
    #print(f"Inserting: Name:{random_name} Year:{random_year}. Count: {count}")
conn.commit()
end_time = time.time()
print("Elapsed time: ", end_time - start_time)
