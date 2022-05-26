# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:52:58 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 6

"""
age = int(input('Enter age of person:'))

if age <2:
    print('The person is baby.')
elif age>=2 and age<4:
    print('The person is a toddler.')    
elif age>=4 and age<13:
    print('The person is a kid.')
elif age>=13 and age<20:
    print('The person is a teenager.')
elif age>=20 and age<65:
    print('The person is an adult.')
else:
    print('The person is an elder.')