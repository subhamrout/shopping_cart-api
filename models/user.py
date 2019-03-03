# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:51:05 2019

@author: Subham Rout
"""
import sqlite3

class UserModel:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password
        
    
    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()
        connection.close()
        if row:
            return cls(*row)
        
    @classmethod
    def find_by_id(cls,_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query,(_id,))
        row = result.fetchone()
        connection.close()
        if row:
            return cls(*row)