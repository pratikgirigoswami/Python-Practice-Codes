# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:19:50 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 6

"""
current_users = ['admin','Pratik','John','Jack','Don']
new_users = ['Amandeep','John','Rabjot','Nihar','admin']

current_users_low = [x.lower() for x in current_users]
for x in new_users:
    if x.lower() in current_users_low:
        print('Username not available. Enter a different user name.')
    else:
        print('Username is available.')