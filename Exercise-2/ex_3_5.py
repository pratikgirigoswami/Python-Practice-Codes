"""
Created on Fri Feb 12 13:34:52 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 4
@Exercise 3-5
"""

guest_list=['Guest1','Guest2','Guest3','Guest4']
i=0
for x in guest_list:
    print('\nDear',x)
    conf=input('Are you coming? Say y for Yes and n for No :')       
    if conf=='n':
        print(x,'is not coming!')
        guest_list[i]=input('Who wants to come instead? :')
    i=i+1

# print('\nSo now',guest_list,'are coming for the dinner.')
print('\n')
for x in guest_list:
    print('\nDear',x,',you are invited for the dinner!')