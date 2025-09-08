# -*- coding: utf-8 -*-

num=input()
num=int(num)
answer=0
def decomposesum(n):
	sum=n
	for i in str(n):
		sum+=int(i)
	return sum

digits=len(str(num))
for i in range(num-9*digits,num):
	if decomposesum(i)==num:
		answer=i
