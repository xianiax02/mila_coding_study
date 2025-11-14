import sys
input=sys.stdin.readline
print=sys.stdout.write
n=int(input().strip())
numbers=[]
for _ in range(n):
    numbers.append(int(input().strip()))
sortedarray=[0]*n
# 구간 나누고-> 인접 구간끼리 병합( 순서 나눠서)  반복
#투포인터 활용 
def mergesort_iterative(numbers):
    n=len(numbers)
    size=1
    while size<n:
        for i in range(0,n,size*2): #2개 인접 구역을 병합할 것이므로 size*2만큼 건너뜀
            index1=i
            index2=i+size
            end1=min(i+size,n)
            end2=min(n,end1+size)
            targetindex=i
            while index1<end1 and index2<end2:
                if numbers[index1]<numbers[index2]:
                    sortedarray[targetindex]=numbers[index1]
                    index1+=1
                else:
                    sortedarray[targetindex]=numbers[index2]
                    index2+=1
                targetindex+=1
            while index1<end1: #끝까지 배분되지 않고 한쪽이 먼저 배분이 끝났을때
                sortedarray[targetindex]=numbers[index1]
                index1+=1
                targetindex+=1
            while index2<end2:
                sortedarray[targetindex]=numbers[index2]
                index2+=1
                targetindex+=1
        for i in range(len(numbers)):
            numbers[i]=sortedarray[i]
        size*=2 #다음 사이즈로 넘어감

mergesort_iterative(numbers)
for i in range(n):
    print(str(numbers[i])+'\n')
    