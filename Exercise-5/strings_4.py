# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:57:02 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 7

"""

def FtoC(far):
    cel=(far-32)*(5/9)
    return cel
far=float(input('Enter temperature in Fahrenheit:'))
print('Equivalent temperature in Celsius is:',FtoC(far))