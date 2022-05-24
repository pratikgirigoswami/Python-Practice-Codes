# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:34:52 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 4
@Exercise 3-11 Dictionaries

"""

mydict = {
  "Data Science and Machine Learning In Canada": "Vahid Hadavi",
  "Python Programming In Canada": "Manpreet Sodhi",
  "Careers In Artificial Intelligence and Machine": "Khyati Nagar",
  "Artificial Intelligence - A Canadian Perspective": "Farzad Amirjavid",
  "Big Data Fundamentals - Data Storage Networking": "Godwin Nyong",
  "Professional Communication": "Nikole Pascetta"
}
print('Original Dictionary:\n',mydict)
print('Number of subjects are:',len(mydict))
print('Instructor for the course of Python Programming in Canada is changed.')
mydict["Python Programming In Canada"] = "Sean Matthews"
print('Revised dictionary is:\n',mydict)