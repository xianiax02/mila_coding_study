def solution(n, words):
    l=ord('z')
    s=ord('a')
    wordlist=[[] for _ in range(l-s+1)]
    for i in range(len(words)):
        if (words[i] in wordlist[ord(words[i][0])-s]) or (i>0 and words[i-1][-1]!=words[i][0]):
            p=(i%n)+1            
            q=(i//n)+1
            answer=[p,q]
            return answer
        wordlist[ord(words[i][0])-s].append(words[i])
    answer = [0,0]
    return answer