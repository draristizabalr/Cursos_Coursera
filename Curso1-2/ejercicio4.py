# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:05:16 2021

@author: zulac
"""

#%%
while True:
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
        break
    except:
        print('File does not exist')

counts = {}; mails = []
for line in fhand:
    if line.startswith('From: '):
        words = line.split()
        mails.append(words[1])

for mail in mails:
    counts[mail] = counts.get(mail,0) + 1

maxi = None; mmaxi = None
for key in counts:
    if mmaxi == None or maxi < counts[key]:
        maxi = counts[key]
        mmaxi = key
        
print(mmaxi,maxi)