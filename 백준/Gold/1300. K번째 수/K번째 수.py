n=int(input())
searchindex=int(input())
def check(index,number):
    global n
    cnt=0
    for i in range(1,n+1):
        cnt+=min(number//i,n)
    if cnt<index:
        return True
    else:
        return False

start=1
end=n**2
while start<=end:
    center=(start+end)//2
    if check(searchindex,center):
        start=center+1
    else:
        end=center-1


print(start)