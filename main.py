# from datetime import date

# d = date(2023, 9, 22)

# print(d)


import sqlite3

DB_NAME = "sqlite3_db.db"

abc = [
    (322, 'asad', 21, 12),
    (121, 'afafa', 424, 35),
    (131, 'zcvxc', 5454, 131)
]


with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty >= 50"
    sql_cirsir = sqlite_conn.execute(sql_request)
    for record in sql_cirsir:
        print(record)


# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sqlite_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     for abc in abc:
#         sqlite_conn.execute(sqlite_request, abc)
#     sqlite_conn.commit()
# with sqlite3.connect(DB_NAME) as sql_conn:
#     print(sql_conn)
#     print(sqlite3.version)


# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """ CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer);"""
#     sqlite_conn.execute(sql_request)
