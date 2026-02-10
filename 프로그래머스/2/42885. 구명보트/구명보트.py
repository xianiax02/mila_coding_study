from bisect import bisect_left
def solution(people, limit):
    n=len(people)
    answer = 0
    people.sort()
    p1,p2=0,n-1
    while p1<=p2:
        if people[p1]+people[p2]<=limit:
            p1+=1
        p2-=1
        answer+=1
    return answer