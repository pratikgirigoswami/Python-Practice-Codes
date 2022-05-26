# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:06:19 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 6

"""
users = ['admin','Pratik','John','Jack','Don']

for x in users:
    if x=='admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello '+ x +', thank you for logging in again.')