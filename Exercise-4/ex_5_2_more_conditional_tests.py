# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 20:08:49 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 6

"""
# Part-1
string_1=input('Enter first string:')
string_2=input('Enter second string:')

if string_1==string_2:
    print('Entered strings were same.')
else:
    print('Entered strings were not same.')

# Part-2
word_1=input('Enter first word:')
word_2=input('Enter second word:')

if word_1.lower()==word_2.lower():
    print('Entered words were same.')
else:
    print('Entered words were not same.')

# Part-3
num_1=float(input('Enter first number:'))
num_2=float(input('Enter second number:'))

if num_1==num_2:
    print('Numbers are equal.')
elif num_1>num_2:
    print('First number is greater than the second.')
else:
    print('First number is less than the second.')
    
# Part-4
num_1=float(input('Enter first number:'))
num_2=float(input('Enter second number:'))

if num_1>=num_2:
    print('First number is greater than or equal to the second number.')
else:
    print('First number is less than the second.')

num_1=float(input('Enter first number:'))
num_2=float(input('Enter second number:'))

if num_1<=num_2:
    print('First number is less than or equal to the second number.')
else:
    print('First number is greater than the second.')

# Part-5
# Check if the number is between 5 and 10
num = float(input('Enter a number:'))
if num>=5 and num<=10:
    print('The number is more than or equal to 5 but less than or equal to 10.')
else:
    print('The number is not between 5 and 10.')

# Check if the number is either less than 5 or more than 10
log_1 = input('Enter True or False:')
log_2 = input('Enter True or False:')
if log_1 or log_2:
    print('At least one logic is True.')
else:
    print('Either both are True or both are False.')

# Part-6
my_list = [2,4,6,8,10]
x=int(input('Enter a number to check:'))
if x in my_list:
    print('in the list')
else:
    print('not in the list')