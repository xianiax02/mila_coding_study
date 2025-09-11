# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:12:50 2025

@author: wuchi
"""

total=9*17 #18C2
hands=list(map(int,input().split(' ')))

cards=[]
for i in range(1,11):
	cards.append(i)
	cards.append(i)

answer=0
if (hands[0]==hands[1]):  #땡일때
	answer=(10-hands[0])/total
else:    #끗일때
	cards.remove(hands[0])
	cards.remove(hands[1])
	LSN=(hands[0]+hands[1])%10
	oppoddang=8  #상대가 땡으로 이기는 경우의 수
	oppoggeut=0  #상대가 끗으로 이기는 경우의 수
	for i in range(18):
		for j in range(i+1,18):
			if ((i!=j)&(cards[i]!=cards[j])):
				oppoLSN=(cards[i]+cards[j])%10
				if (oppoLSN>=LSN):
					oppoggeut+=1
	answer=(oppoddang+oppoggeut)/total #순서 무시
	



print('{:.3f}'.format(1-answer))