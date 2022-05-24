# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:43:13 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 5
"""
animals=['cats','dogs', 'seals']

print('\n---Animals in the list.---')
for x in animals:
    print(x)

print('\n---Animals with statement.---')
for x in animals:
    if x=='cats':
        print('The oldest known pet,',x,',existed 9,500 years ago')
    elif x=='dogs':
        print('Three',x,'survived the Titanic sinking.')
    else:
        print(x.title(),'can live for up to 30 years.')

print('\n---Animals with sentence & a sentence at last.---')

for x in animals:
    if x=='cats':
        print('The oldest known pet,',x,'existed 9,500 years ago')
    elif x=='dogs':
        print('Three',x,'survived the Titanic sinking.')
    else:
        print(x.title(),'can live for up to 30 years.')
print('All of them are mammals.')