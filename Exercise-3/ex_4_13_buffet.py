# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:23:10 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 5
"""
print('---Original Menu---')
menu=('Tandoori Chicken','Vegetable Samosas','Curry','Naan','Aloo Gobi')
for x in menu:
    print(x)
    
# Trying to change item
#menu[2]='Khichdi' # Comment this line later

# Revised menu
menu=('Tandoori Chicken','Vegetable Samosas','Curry','Naan','Khichdi')
print('---Revised Menu---')
for x in menu:
    print(x)