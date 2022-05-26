# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:14:48 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 6

"""
users = []
if users:
    for x in users:
        if x=='admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello '+ x +', thank you for logging in again.')
else:
    print('We need to find some users!')