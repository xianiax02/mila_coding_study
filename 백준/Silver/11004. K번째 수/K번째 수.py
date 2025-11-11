import sys, random
sys.setrecursionlimit(10**6)

n, k = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))

def partition(s, e):
    # pivot을 중간값으로 설정
    m = (s + e) // 2
    numbers[s], numbers[m] = numbers[m], numbers[s]
    pivot = numbers[s]
    i = s + 1
    j = e
    while i <= j:
        while i <= j and numbers[i] < pivot:
            i += 1
        while i <= j and numbers[j] > pivot:
            j -= 1
        if i <= j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
            j -= 1
    numbers[s], numbers[j] = numbers[j], numbers[s]
    return j

def quickselect(s, e, k):
    if s < e:
        pivot = partition(s, e)
        if pivot == k:
            return
        elif k < pivot:
            quickselect(s, pivot - 1, k)
        else:
            quickselect(pivot + 1, e, k)

quickselect(0, n - 1, k - 1)
print(numbers[k - 1])
