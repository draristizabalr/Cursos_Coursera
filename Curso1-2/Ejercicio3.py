# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:40:58 2021

@author: zulac
"""

#%%
while True:
    fname = input('Enter name file: ')
    try:
        fhand = open(fname)
        break
    except:
        print('File name does not found it.')

lst = []; count = 0
for line in fhand:
    if line.startswith('From: '):
        lst.append(line)
for pos in range(len(lst)):
    print(lst[pos].split()[1])
    count += 1

print('There were',count,'lines in the file with From as the first word')

