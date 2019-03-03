# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 09:51:27 2019

@author: Subham Rout
"""

from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username,password):
    user =  UserModel.find_by_username(username = username)
    if user is not None and safe_str_cmp(user.password,password):
        return user
    
def identity(payload):
    user_id  = payload['identity']
    return UserModel.find_by_id(user_id)
    