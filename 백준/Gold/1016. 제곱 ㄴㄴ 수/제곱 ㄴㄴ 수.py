Min, Max = map(int, input().split())
N = int(Max**0.5)

numbers = [1] * (N + 1)
primes = []
numbers[0] = numbers[1] = 0
for i in range(2, N + 1):
    if numbers[i]:
        for mul in range(i + i, N + 1, i):
            numbers[mul] = 0
        primes.append(i)

# 2. candidates를 True(1)로 초기화 (제곱ㄴㄴ수라고 가정)
candidates = [1] * (Max - Min + 1)

for prime in primes:
    square = prime**2
    # Min보다 크거나 같은 square의 첫 번째 배수 찾기 (핵심 수정)
    start_val = (Min // square) * square
    if start_val < Min:
        start_val += square
    
    # 3. 배수들을 0으로 지우기 (루프 변수 mul 사용)
    for mul in range(start_val, Max + 1, square):
        candidates[mul - Min] = 0 # 인덱스는 항상 '값 - Min'

# 4. 1로 남은 것들이 제곱ㄴㄴ수
print(candidates.count(1))