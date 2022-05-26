# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:27:22 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 6

"""
num_list = [x for x in range(1,10)]

for x in num_list:
    if x==1:
        print('1st')
    elif x==2:
        print('2nd')
    elif x==3:
        print('3rd')
    else:
        print(str(x)+'th')