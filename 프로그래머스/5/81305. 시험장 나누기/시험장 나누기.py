import sys
sys.setrecursionlimit(10**6)
def solution(k, num, links):
    answer = 0
    cnt=0
    n=len(num)
    is_child=[False]*n
    for l,r in links:
        if l!=-1: is_child[l]=True
        if r!=-1: is_child[r]=True
    root=is_child.index(False)
    
    def is_ok(maxnum):
        cnt=0
        def postorder(node,maxnum):
            nonlocal cnt
            l,r=links[node][0],links[node][1]
            l_sum=postorder(l,maxnum) if l!=-1 else 0
            r_sum=postorder(r,maxnum) if r!=-1 else 0
            if l_sum+r_sum+num[node]<=maxnum:
                return l_sum+r_sum+num[node]
            elif l_sum>=r_sum and r_sum+num[node]<=maxnum: #오른쪽 자식을 자른다
                cnt+=1
                return r_sum+num[node]
            elif l_sum<r_sum and l_sum+num[node]<=maxnum:
                cnt+=1
                return l_sum+num[node]
            else:
                cnt+=2
                return num[node]
        
        postorder(root,maxnum)
        if cnt>=k:
            return False
        else: return True
    
    start,end=max(num),sum(num)
    while start<=end:
        mid=(start+end)//2
        if is_ok(mid):
            end=mid-1
        else:
            start=mid+1
    answer=start

    return answer