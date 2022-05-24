"""
Created on Fri Feb 12 13:34:52 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 4
@Exercise 3-6
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


for x in guest_list:
    print('\nDear',x,',you are invited for the dinner!')
    
print('\nNow we have a bigger table! So I am inviting Guest0,GuestMiddle,GuestEnd')
guest_list.insert(0,'Guest0')
guest_list.insert((round(len(guest_list)/2))+1,'GuestMiddle')
guest_list.append('GuestEnd')
print(guest_list)

for x in guest_list:
    print('\nDear',x,',you are invited for the dinner!')