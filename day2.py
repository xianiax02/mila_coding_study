# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 14:41:17 2025

@author: wuchi
"""

heights=[]
for i in range(9):
	heights.append(int(input()))
answers=heights.copy()
S=sum(heights)
for alien in heights:
	anotheralien=S-alien-100
	if anotheralien in heights:
		answers.remove(alien)
		answers.remove(anotheralien)
		break
answers.sort()
for i in answers:
	print(i)


heights=[]
found=False
for i in range(9):
	heights.append(int(input()))
S=sum(heights)
answers=[]
for alienindex in range(9):
    for anotheralienindex in range(alienindex+1,9):
        if (S-heights[alienindex]-heights[anotheralienindex])==100:
            found=True
            for k in range(9):
                if (k!=alienindex)&(k!=anotheralienindex):
                    answers.append(heights[k])
                    
            break
    if found:
        break
answers.sort()
for i in answers:
	print(i)