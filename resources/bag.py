# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:57:32 2019

@author: Subham Rout
"""
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.bag import BagModel
import sqlite3
import global_var

class Bag(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('itemName',type = str,required = True,
                        help = "This field cannot left blank")
    @jwt_required()
    def get(self,itemName):
        data = Bag.parser.parse_args()
        row = BagModel.find_by_name(data)
        if row:    
            return {"item": row}
        return {"message":"Item not present in the bag"}
    
        
    @jwt_required()
    def post(self,itemName):
        data = Bag.parser.parse_args()
        try:
            BagModel.save_to_db(self,data)
        except:
           return {"Message":"An error occured while saving data in db"}
        return {"message":"Item added sucessfully"}
    
    @jwt_required()
    def delete(self,itemName):
        data = Bag.parser.parse_args()
        row = BagModel.find_by_name(data)
        if row is None:
            return {"message":"Item is not present in the bag"}
        
        global_var.total -= row[2]
        try:
            BagModel.delete_from_db(itemName)
        except:
            return {"Message":"An error cooured while deleting the item"}
        return {"Message":"Item is deleted"}
    
        
class Print_bill(Resource):
    
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM bags"
        result = cursor.execute(query)
        res =[]
        for r in result:
            res.append({'itemName':r[1],'price':r[2]})
        query = "DELETE FROM bags"
        cursor.execute(query)
        tot = global_var.total
        global_var.total =0
        connection.commit()
        connection.close()
        return {'items':res,'TOTAL AMOUNT':tot}    
    
        
class Present_Bag_item(Resource):
    
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM bags"
        result = cursor.execute(query)
        res = []
        for r in result:
            res.append({"itemName":r[1],"price":r[2]})
        connection.close()    
        return {"items in bag": res,"total amount till now": global_var.total}
    


class Shopping_List(Resource):
    
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM shoppings"
        result = cursor.execute(query)
        res_tmp = []
        for res in result:
            res_tmp.append({"id":res[0],"itemName":res[1],"price":res[2]})
        connection.close()    
        return {"Shopping DataBase": res_tmp}