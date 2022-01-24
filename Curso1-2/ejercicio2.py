# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:27:55 2021

@author: zulac
"""

#%%
fname = input('Enter name file: ')
while True:
    try:
        fhand = open(fname)
        break
    except:
        print('Name file does not exist')

lst = []; lst1 = []; pos = 0
for line in fhand:
    lst.append(line.split())

for line in lst:
    for word in line:
        if word not in lst1[:pos]:
            lst1.append(word)
            pos += 1
lst1.sort()
print(lst1)
    