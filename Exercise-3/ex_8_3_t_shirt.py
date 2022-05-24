# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:34:33 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 5
"""
# Defining function
def make_shirt(sz,ms):
    print('The size of the shirt is:',sz)
    print('The message is:',ms)
    
# Calling by positional arguments
make_shirt('medium', 'The shirt is made of cotton.')

# Calling by keyword arguments
make_shirt(sz='large', ms='The shirt is made of cotton.')