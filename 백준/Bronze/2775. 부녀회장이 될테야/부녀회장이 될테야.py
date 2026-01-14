#아파트가 최대 0~14층이니 그냥 미리 만들어놓고 짜도 될 것 같다. 
N=15
A=[[0]*(N) for _ in range(N)] #column 0-padding
for i in range(1,N):
    A[0][i]=i

for floor in range(1,N):
    for room in range(1,N):
        A[floor][room]=A[floor-1][room]+A[floor][room-1]

t=int(input())
for _ in range(t):
    floor=int(input())
    room=int(input())
    print(A[floor][room])
        