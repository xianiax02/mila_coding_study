import heapq
def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    t=0
    foods=[]
    for i,food in enumerate(food_times):
        heapq.heappush(foods,(food,i+1))
    previoustime=0
    while foods and t+(foods[0][0]-previoustime)*len(foods)<k+1:
        t+=(foods[0][0]-previoustime)*len(foods)
        food,idx=heapq.heappop(foods)
        previoustime=food
    if len(foods)>=(k-t)%len(foods):
        foods.sort(key=lambda x:x[1])
        answer = foods[(k-t)%len(foods)][1]
    return answer