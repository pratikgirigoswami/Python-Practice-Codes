# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:16:37 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 6
"""

car='volvo'
test_list=['volvo','BMW','Mercedes','volvo','maruti','volvo','Hyundai','volvo','Tata','volvo']

for x in test_list:
    guessed_car=x
    if guessed_car==car:
        print('True')
    else:
        print('False')