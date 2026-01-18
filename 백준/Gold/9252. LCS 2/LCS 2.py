import sys
input=sys.stdin.readline
string1=input().strip()
string2=input().strip()
n1=len(string1) #row
n2=len(string2) #column
DP=[[0]*n2 for _ in range(n1)]
for row in range(n1):
    if string1[row]==string2[0]:
        DP[row][0]=1
    elif row==0:
        DP[row][0]=0
    else:
        DP[row][0]=DP[row-1][0]

for col in range(n2):
    if string2[col]==string1[0]:
        DP[0][col]=1
    elif col==0:
        DP[0][col]=0
    else:
        DP[0][col]=DP[0][col-1]

for row in range(1,n1):
    for col in range(1,n2):
        if string1[row]==string2[col]:
            DP[row][col]=DP[row-1][col-1]+1
        else:
            DP[row][col]=max(DP[row-1][col],DP[row][col-1])

result=[]
startrow=n1-1
startcol=n2-1
row=startrow
col=startcol
while row>0 and col>0:
    if DP[row-1][col]==DP[row][col]:
        row-=1
    elif DP[row][col-1]==DP[row][col]:
        col-=1
    elif DP[row-1][col-1]==DP[row][col]-1:
            result.append(string1[row])
            row-=1
            col-=1
if DP[row][col]:
    if row:
        result.append(string2[0])
    else:
        result.append(string1[0])
result.reverse()

print(DP[n1-1][n2-1])
print(''.join(result))
            