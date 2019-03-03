# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 07:19:54 2019

@author: Subham Rout
"""

import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS shoppings (id INTEGER PRIMARY KEY, name text, price real)"

cursor.execute(create_table)

query = [['bata shoe',39.45],['classmate copy',12.45],['dettole handwash',10.43],['one plus 5t',100.67],['hp laptop',250.56],
         ['cracking the coding interview book',33.45],['watter bottle',26.78],['blackberry shirt',45.67],['rolex watch',450.00],['school bag',60.67],
         ['5 star chocolate',5.67]]

insert_query = "INSERT INTO shoppings VALUES (NULL,?,?)"

for q in query:
    cursor.execute(insert_query,(q[0],q[1]))

create_table = "CREATE TABLE IF NOT EXISTS bags (id INTEGER PRIMARY KEY, name text, price real)" 
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" 
cursor.execute(create_table)
connection.commit()
connection.close()    