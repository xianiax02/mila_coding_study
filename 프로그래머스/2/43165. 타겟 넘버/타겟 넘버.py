def solution(numbers, target):
    n = len(numbers)
    dp = [0] * (1 << n)
    
    # 첫 번째 숫자는 미리 세팅 (0번 숫자를 처리한 상태로 시작)
    dp[0] = -numbers[0]
    dp[1] = numbers[0]
    
    # 1번째 숫자부터 n-1번째 숫자까지 처리
    for i in range(1, n):
        num = numbers[i]
        # 현재 층의 마지막 노드 인덱스부터 0까지 거꾸로 진행
        # i=1일 때 j는 1, 0 순서 / i=2일 때 j는 3, 2, 1, 0 순서
        for j in range((1 << i) - 1, -1, -1):
            value = dp[j] # 아직 업데이트되지 않은 부모의 값
            
            # 자식 인덱스는 부모 인덱스보다 크거나 같으므로 안전함
            dp[j * 2] = value - num
            dp[j * 2 + 1] = value + num
            
    return dp.count(target)