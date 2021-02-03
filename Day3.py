# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:24:24 2021

@author: TQC
"""

f=open('file1.txt','r')
for line in f:
    print(line)
f.close()

with open ('file1.txt','r')as f:
    for line in f:
        print(line)
f=open('file1.txt','r')
s=f.read(12)
print(s)
f.close(12)