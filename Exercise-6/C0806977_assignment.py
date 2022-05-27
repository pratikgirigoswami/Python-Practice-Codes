# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:08:22 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Assignment-1

"""
# Part-1 The simplest encryption algorithm!

print("\n----------------PART-1----Caesar Cypher Algorithm----------------")

original_text=input("Enter text to encrpyt: ")
shift_var=int(input("Shift by: "))

def caesar_fun(original_text,shift_var): 
	encrypted_text = "" 

	# accessing each letter one by one
	for i in range(len(original_text)): 
		char = original_text[i] 

		# for uppercase letters
		if (char.isupper()): 
			encrypted_text += chr((ord(char) + shift_var-65) % 26 + 65) 

		# for lowercase letters
		else: 
			encrypted_text += chr((ord(char) + shift_var - 97) % 26 + 97) 

	return encrypted_text

print("Original Text was: ",original_text)
print("Encrypted Text is: ",caesar_fun(original_text,shift_var))

# Part-2 Binary Search Algorithm
print("\n----------------PART-2----Binary Search Algorithm----------------")

my_list=range(0,101)
target = int(input("Enter the value you want to search for: "))


def binary_search_algo(my_list, target):
	minv = 0
	maxv = len(my_list) - 1
	guess = 0

	while minv <= maxv:

		guess = (minv + maxv) // 2

		if my_list[guess] < target:
			minv = guess + 1

		elif my_list[guess] > target:
			maxv = guess - 1

		else:
			return 1

	return -1


result = binary_search_algo(my_list, target)

if result != -1:
	print("\nTRUE---Element is present in the list.")
else:
	print("\nFALSE---Element is not present in the list.")
    
# Part-3 Formula Implementation

print("\n----------------PART-3----Formula Implementation----------------")

import math

# Function to find factorial
def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
        
# Function to implement equation
def ramanuj_eq():
    
    k=0
    final=0
    pi=0
    while pi<1e-15:
        a=factorial(4*k)
        b=(1103+26390*k)
        c=factorial(k)
        d=c**4
        e=396**(4*k)
        f=2*math.sqrt(2)/9801
        final+=(a*b*f)/(d*e)
        k+=1
        pi=1/final
    return pi

print("\nEstimated value of Pi using formula:",ramanuj_eq())
print("\nActual value of Pi :",math.pi)