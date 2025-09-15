# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 10:32:26 2025

@author: wuchi
"""

def BNP(cash, pricelist):
    cash=cash
    stocks=0
    for i in range(len(pricelist)):
        buyable=cash//pricelist[i]
        if buyable:
            cash-=buyable*pricelist[i]
            stocks+=buyable
    totalasset=cash+stocks*pricelist[-1]
    return totalasset

def TIMING(cash,pricelist):
    cash=cash
    track=[0,0,0]
    stocks=0
    for i in range(len(pricelist)):
        index=i%3
        if (i>0):
            if pricelist[i-1]>pricelist[i]: #가격 하락
                track[index]=-1
            elif pricelist[i-1]<pricelist[i]: #가격 상승
                track[index]=1
            else:
                track[index]=0
        if sum(track)==3:#3일연속 오름-> 전량 매도
            cash+=stocks*pricelist[i]
            stocks-=stocks
        elif sum(track)==-3: #3일연속 떨어짐-> 전량매수
            buyable=cash//pricelist[i]
            cash-=buyable*pricelist[i]
            stocks+=buyable
    totalasset=cash+stocks*pricelist[-1]
    return totalasset

cash=int(input())
pricelist=list(map(int,input().split(' ')))
bnpresult=BNP(cash, pricelist)
timingresult=TIMING(cash,pricelist)
if bnpresult>timingresult:
    print('BNP')
elif bnpresult<timingresult:
    print('TIMING')
else:
    print('SAMESAME')