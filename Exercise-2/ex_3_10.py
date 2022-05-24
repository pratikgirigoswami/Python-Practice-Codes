# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:34:52 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 4
@Exercise 3-10
"""
print('Following is the list of flights from Mumbai,India')
flight_list=['AI131-01:00 am','BA138-02:00 am','UK11-03:00 am','EY205-04:00 am','EK505-05:00 am']
print(flight_list)
print('Number of flights:',len(flight_list))

print('\nThe last flight',flight_list.pop(),'is cancelled now.')
print('Revised flight list is',flight_list)

flight_list.append('UK123--5:00 am')
print('\nNew flight UK123 is accomodated now at that time so new flight list is',flight_list)
print('Number of flights now:',len(flight_list))

print('\nOne more flight BA138 is cancelled now.')
ind=flight_list.index('BA138-02:00 am')
print('Its position in the list was',ind)

flight_list.remove('BA138-02:00 am')
flight_list.insert(ind, 'BA149-02:00 am')
print('\nCancelled flight is replaced by another flight and the new list is:',flight_list)

flight_list.sort()
print('\nList in alphabetical order:',flight_list)

flight_list.reverse()
print('\nReversed list is:',flight_list)

print('\nDue to extreme weather conditions, all the flights are cancelled.')
flight_list.clear()
print('Revised flight list:',flight_list)

