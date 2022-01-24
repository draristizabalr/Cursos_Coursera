# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 11:50:50 2021

Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end


@author: zulac
"""



#%%
import re

file = open('regex_sum_1418695.txt')
nums = []
suma = None

for line in file:
    if re.findall('[0-9]+',line) != []:
        if len(re.findall('[0-9]+',line)) > 1:
            lines = []            
            lines.append(re.findall('[0-9]+',line))
            for l in lines[0]:
                nums.append(l)
        else:
            nums.append(re.findall('[0-9]+',line)[0])
for pos in range(len(nums)):
    nums[pos] = int(nums[pos])

suma = sum(nums)
print(suma)

