# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:12:23 2021

@author: zulac
"""

#%%
import urllib as url

fhand = url.request.urlopen('https://es.wowhead.com/news/tips-and-tricks-for-\
shadowlands-mythic-dungeons-on-sanguine-necrotic-fortified-325123')

lines = []

for line in fhand:
    print(line)

