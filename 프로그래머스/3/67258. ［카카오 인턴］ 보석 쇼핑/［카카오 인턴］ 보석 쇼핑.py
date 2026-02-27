def solution(gems):
    cart=dict()
    totalgem=len(set(gems))
    p1,p2=0,0
    cart[gems[p1]]=1
    maxlength=float('inf')
    answer = [0,0]
    n=len(gems)
    def allincluded(cart):
        if len(cart)==totalgem:
            return True
        else:
            return False
    while p2<n and p1<=p2:
        if allincluded(cart):
            if p2-p1+1<maxlength:
                maxlength=p2-p1+1
                answer=[p1,p2]
            cart[gems[p1]]-=1
            if cart[gems[p1]]==0:
                del cart[gems[p1]]
            p1+=1
        else:
            p2+=1
            if p2<n:
                cart[gems[p2]]=cart.get(gems[p2],0)+1
        
    answer=[i+1 for i in answer]
    return answer