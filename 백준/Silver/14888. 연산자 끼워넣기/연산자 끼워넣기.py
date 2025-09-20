def solve(index, current_value, add, sub, mul, div):
    if index == N:
        global max_val, min_val
        max_val = max(max_val, current_value)
        min_val = min(min_val, current_value)
        return


    if add > 0:
        solve(index + 1, current_value + numbers[index], add - 1, sub, mul, div)
    if sub > 0:
        solve(index + 1, current_value - numbers[index], add, sub - 1, mul, div)
    if mul > 0:
        solve(index + 1, current_value * numbers[index], add, sub, mul - 1, div)
    if div > 0:
        if current_value >= 0:
            new_value = current_value // numbers[index]
        else:
            new_value = -(-current_value // numbers[index])
        solve(index + 1, new_value, add, sub, mul, div - 1)


N = int(input())
numbers = list(map(int, input().split()))
ops_count = list(map(int, input().split()))

max_val = float('-inf')
min_val = float('inf')

    # 재귀 함수 호출 (초기값은 첫 번째 숫자, 인덱스는 1부터 시작)
solve(1, numbers[0], ops_count[0], ops_count[1], ops_count[2], ops_count[3])

print(max_val)
print(min_val)