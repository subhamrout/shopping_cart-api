# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:53:30 2019

@author: Subham Rout
"""
import sqlite3
import global_var

class BagModel:

    def find_by_name(self,data):
            connection = sqlite3.connect('data,db')
            cursor = connection.cursor()
            query = "SELECT * FROM bags WHERE name = ?"
            result = cursor.execute(query,(data['itemName'],))
            row = result.fetchone()
            connection.close()
            return row
        
    def save_to_db(self,data):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            query1 = "SELECT * FROM shoppings WHERE name = ?"
            result1 = cursor.execute(query1,(data['itemName'],))
            row = result1.fetchone()
            global_var.total += row[2]
            query2 = "INSERT INTO bags VALUES (NULL,?,?)"
            cursor.execute(query2,(row[1],row[2]))
            connection.commit()
            connection.close()
            return {"message":"Item added sucessfully"}
    def delete_from_db(self,itemName):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            query = "DELETE FROM bag WHERE name = ?"
            cursor.execute(query,(itemName,))
            connection.commit()
            connection.close()
    