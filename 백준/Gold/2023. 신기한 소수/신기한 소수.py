import sys
input=sys.stdin.readline
print=sys.stdout.write

n=int(input().strip())
firstdigit=[2,3,5,7]
seconddigit=[1,3,5,7,9]
def checkprime(num):
    root=int(num**0.5)
    for i in range(2,root+1): #1로 절대 나누면 안됨.. 주의!! 항상 2 부터
        if not num%i :  #나머지가 0일때 참이 되어 소수가 아님을 증명
            return 0    
    return 1


def BFScheckprime(num,n): 
    if n==1:
        for digit in firstdigit:
            print(str(digit)+'\n')
        return
        
    if len(str(num))==n:
        print(str(num)+'\n')
        return 
    if num==0:
        for digit in firstdigit:
            newnum=10*num+digit
            if checkprime(newnum):
                BFScheckprime(newnum,n)
    else:
        for digit in seconddigit:
            newnum=10*num+digit
            if checkprime(newnum):
                BFScheckprime(newnum,n)
    

BFScheckprime(0,n)           

            
        