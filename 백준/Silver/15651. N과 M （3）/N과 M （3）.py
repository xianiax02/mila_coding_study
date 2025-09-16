N,M=list(map(int,input().split(' ')))



def permutation(n,m,sequence):
    if (len(sequence)==m):
        print(' '.join(map(str,sequence)))
        return
    for num in range(1,n+1):
        sequence.append(num)
        permutation(n,m,sequence)
        sequence.pop()
       

sequence=[]
permutation(N,M,sequence)