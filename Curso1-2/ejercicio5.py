# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 23:36:20 2021

@author: zulac
"""

#%%
while True:
    try:
        fname = input('Enter file name: ')
        fhand = open(fname)
        break
    except:
        print('File does not exist')

hms = []; hour = []
for line in fhand:
    if line.startswith('From '):
        hms.append(line.split()[5])

for i in hms:
    hour.append(i.split(':')[0])

count = {}
for key in hour:
    count[key] = count.get(key, 0) + 1

for k,v in sorted(count.items()):
    print(k,v)