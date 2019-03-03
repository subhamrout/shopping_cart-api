# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 07:39:32 2019

@author: Subham Rout
"""
from flask import Flask
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
from resources.user import UserRegister
from resources.bag import Bag,Print_bill,Shopping_List,Present_Bag_item
import global_var

global_var.init()

app = Flask(__name__)
app.secret_key = "SubhamRoUtRoCkS"
api = Api(app)
jwt = JWT(app,authenticate,identity)

total = 0

'''
@app.before_first_request
def create_all():
    db.create_all()
'''

api.add_resource(Bag,'/<string:itemName>')        
api.add_resource(Print_bill,"/printBill")
api.add_resource(Shopping_List,"/shoppings")
api.add_resource(UserRegister,"/register")
api.add_resource(Present_Bag_item,'/present_bag')

app.run(port = 5000,debug = True)        
        
        
        
        
        
        
    

