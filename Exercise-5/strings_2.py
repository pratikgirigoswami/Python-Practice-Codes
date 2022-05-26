# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:43:33 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 7

"""
my_string = 'www.pratikgoswami.weebly.com'

def charfreq(my_string):
    dict = {}
    for x in my_string:
        keys = dict.keys()
        if x in keys:
            dict[x] += 1
        else:
            dict[x] = 1
    return dict
print(charfreq(my_string))