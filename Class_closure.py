# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:55:14 2021

@author: sattw
"""

def outer(msg):
    message = msg
    
    def inner():
        print(msg)
    
    return inner()

func=outer('Hello')
#print(func())