# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:44:21 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 5
"""

# Defining function
def make_shirt(sz='large',ms='I love Python.'):
    print('The size of the shirt is:',sz)
    print('The message is:',ms)

print('---With default arguments---')    
make_shirt()
print('---With default arguments---')    
make_shirt(sz='medium')
print('---With different size---')    
make_shirt('small','I enjoy coding with Python.')