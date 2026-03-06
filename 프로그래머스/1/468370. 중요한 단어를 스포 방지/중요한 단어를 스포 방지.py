def solution(message, spoiler_ranges):
    important=set() # if not in nonspoiler and contain spoiler_range
    nonspoiler=set()
    message+=' ' # 마지막 단어를 점검하기 위해 하나 넣어줌
    pos=0
    wordstart,wordend=0,0
    n_spoilers=len(spoiler_ranges)
    while wordstart<len(message) and message[wordstart]==' ':
        wordstart+=1
    for i,char in enumerate(message):
        if char==' ':
            wordend=i
            word=message[wordstart:wordend] #지금 막 검사를 끝낸 단어는 인덱스가 [wordstart:wordend]
            if word: # 빈 단어가 아닐 때만 로직 가동
                while pos < n_spoilers and spoiler_ranges[pos][1] < wordstart:
                    pos += 1
                
                is_spoiler = False
                # [수정 2] 현재 유효한 pos가 단어 범위 [wordstart, i-1]과 겹치는지 확인
                if pos < n_spoilers:
                    ss, se = spoiler_ranges[pos]
                    # 구간 겹침 공식: max(S1, S2) <= min(E1, E2)
                    if max(wordstart, ss) <= min(i - 1, se):
                        is_spoiler = True
                
                if is_spoiler and (word not in nonspoiler):
                    important.add(word)
                else:
                    important.discard(word)
                    nonspoiler.add(word)
                
                # [수정 3] 단어 검사 후: 현재 단어 끝(i-1)에서 이미 끝난 스포일러는 다음을 위해 제거
                while pos < n_spoilers and spoiler_ranges[pos][1] <= i - 1:
                    pos += 1
            wordstart=i+1 #다음 단어로 넘어감. 
    answer = len(important)
    return answer