def solution(expressions):
    answer = []
    def to_base_n(num,base):
        if num==0:
            return '0'
        result=''
        while num:
            result=str(num%base)+result
            num=num//base
        return result 
        
    conditions=[]
    problems=[]
    lowestbase=1
    del_cands=set()
    #전체 조건에서 각 숫자를 뽑아내서 가장 큰 자릿수 뽑아내서 범위 좁히기, 하는 김에 문제와 조건 분리
    for expression in expressions:
        for letter in expression:
            if letter.isdigit():
                lowestbase=max(lowestbase,int(letter))
        if expression[-1]=='X':
            problems.append(expression)
        else:
            conditions.append(expression)
    cands = set(range(max(2, lowestbase + 1), 10))
    for i in range(len(conditions)):
        a,op,b,_,r=conditions[i].split()
        for base in cands:
            an,bn,rn=int(a,base),int(b,base),int(r,base)
            if op=='+':
                if an+bn==rn: continue
                else: del_cands.add(base)
            elif op=='-':
                if an-bn==rn: continue
                else: del_cands.add(base)
    for delcand in del_cands:
        cands.remove(delcand)
    for problem in problems:
        a, op, b, _, _ = problem.split()
        results_set = set()  # 중복을 허용하지 않는 바구니 생성

        for base in cands:
            # 1. 현재 진법(base)에서 10진수로 계산
            an, bn = int(a, base), int(b, base)
            res_10 = an + bn if op == '+' else an - bn

            # 2. 계산 결과를 다시 n진법 '문자열'로 변환해서 바구니에 넣기
            # (집합이라서 같은 문자열이 들어오면 하나만 남아요!)
            results_set.add(to_base_n(res_10, base))

        # 3. 바구니에 담긴 결과의 종류가 몇 개인지만 확인!
        if len(results_set) == 1:
            # 결과가 하나뿐이면 모든 진법에서 답이 같다는 뜻
            final_val = list(results_set)[0]
            answer.append(f"{a} {op} {b} = {final_val}")
        else:
            # 결과가 2개 이상이면 진법에 따라 답이 달라진다는 뜻
            answer.append(f"{a} {op} {b} = ?")    
    
    return answer