import csv
import sqlite3


def read_csv_in_chunks(file_path, chunk_size=1):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk


for chunk in read_csv_in_chunks('../AAPL.csv', chunk_size=2):
    print(chunk)


def read_sql_in_chunks(db_path, query, chunk_size=10):
    offset = 0
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        while True:
            limited_query = f"{query} LIMIT {chunk_size} OFFSET {offset}"
            cursor.execute(limited_query)
            results = cursor.fetchall()
            if not results:
                break
            yield results
            offset += chunk_size


db_path = 'example.db'
query = 'SELECT * FROM some_table'

for chunk in read_sql_in_chunks(db_path, query, chunk_size=10):
    print(chunk)
