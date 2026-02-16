def solution(expressions):
    answer = []
    problems=[]
    numeral=set()
    maxnum='0'
    def tobase(res,num):
        if res==0:
            return '0'
        ans=''
        while res>0:
            ans+=str(res%num)
            res=res//num#res를 num진법형태로 변환
        return ans[::-1]
    def calculate(expression,base):
        n1,op,n2,_,res=expression.split()
        if op=='-':
            res=int(n1,base)-int(n2,base)
        elif op=='+':
            res=int(n1,base)+int(n2,base)
        return res
    
    for i,exp in enumerate(expressions):
        n1,op,n2,_,res=exp.split()
        for d in n1+n2+(res if res!='X' else ''):
            if maxnum<d: maxnum=d
    numeral=set([i for i in range(int(maxnum)+1,10)])
    for i,exp in enumerate(expressions):
        n1,op,n2,_,res=exp.split()
        if res=='X':
            problems.append(exp)
            continue
        reduceset=set()
        for num in list(numeral):
            if calculate(exp,num)!=int(res,num):
                reduceset.add(num)
        numeral-=reduceset
    ansset=dict()
    #각 문제에서 해답이 될 수 있는 숫자를 집어넣음
    for i,problem in enumerate(problems):
        ansset[i]=set()
        for num in numeral:
            res=calculate(problem,num)
            ansset[i].add(tobase(res,num))
    for problemnum,answers in ansset.items():
        if len(answers)>1:
            answer.append(problems[problemnum].replace('X','?'))
        else:
            ans=answers.pop()
            answer.append(problems[problemnum].replace('X',ans))
    return answer