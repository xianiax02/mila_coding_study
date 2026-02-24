from bisect import bisect_left,bisect_right
from collections import defaultdict
def solution(info, query):
    max_score=100001
    alldict=defaultdict(list)
    for pinfo in info:
        stack,pos,level,food,score=pinfo.split()
        score=int(score)
        alldict[(stack,pos,level,food)].append(score)
        alldict[('-',pos,level,food)].append(score)
        alldict[(stack,'-',level,food)].append(score)
        alldict[(stack,pos,'-',food)].append(score)
        alldict[(stack,pos,level,'-')].append(score)
        alldict[('-','-',level,food)].append(score)
        alldict[('-',pos,'-',food)].append(score)
        alldict[('-',pos,level,'-')].append(score)
        alldict[(stack,'-','-',food)].append(score)
        alldict[(stack,'-',level,'-')].append(score)
        alldict[(stack,pos,'-','-')].append(score)
        alldict[('-','-','-',food)].append(score)
        alldict[('-','-',level,'-')].append(score)
        alldict[('-',pos,'-','-')].append(score)
        alldict[(stack,'-','-','-')].append(score)
        alldict[('-','-','-','-')].append(score)
    for lst in alldict.values():
        lst.sort()
    def ask(command):
        stack,pos,level,food,score=command
        score=int(score)
        length=bisect_right(alldict[(stack,pos,level,food)],max_score)
        return length-bisect_left(alldict[(stack,pos,level,food)],score)
    answer = []
    for q in query:
        a,b,c,d=q.split('and')
        a,b,c=a.split()[0],b.split()[0],c.split()[0]
        d,e=d.split()
        command=(a,b,c,d,e)
        answer.append(ask(command))
        
    
    return answer