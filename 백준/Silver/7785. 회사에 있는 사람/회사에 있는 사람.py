import sys
inp=sys.stdin.readline().strip()
n=int(inp)
incompany=set([])
for _ in range(n):
    name,status=sys.stdin.readline().strip().split(' ')
    if status=='enter':
       incompany.add(name)
    elif status=='leave':
        incompany.remove(name)

printcompany=sorted(incompany,reverse=True)
for i in range(len(printcompany)):
    sys.stdout.write(str(printcompany[i])+'\n')