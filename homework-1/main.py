"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

with psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="1706"
) as conn:
    with conn.cursor() as cur:
        with open("../homework-1/north_data/customers_data.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            for ow in file_reader:
                if count > 0:
                    cur.execute('INSERT INTO customers VALUES (%s,%s,%s)', (ow[0], ow[1], ow[2]))
                count += 1

    with conn.cursor() as cur:
        with open("../homework-1/north_data/employees_data.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            for ow in file_reader:
                if count > 0:
                    cur.execute('INSERT INTO employees VALUES (%s,%s,%s,%s,%s)', (ow[0], ow[1], ow[2], ow[3], ow[4]))
                count += 1

    with conn.cursor() as cur:
        with open("../homework-1/north_data/orders_data.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            for ow in file_reader:
                if count > 0:
                    cur.execute('INSERT INTO orders VALUES (%s,%s,%s,%s,%s)', (ow[0], ow[1], ow[2], ow[3], ow[4]))
                count += 1

conn.close()
