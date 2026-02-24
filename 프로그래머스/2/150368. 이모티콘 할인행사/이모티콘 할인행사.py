from itertools import product
def solution(users, emoticons):
    emon=len(emoticons)
    cases=list(product([10,20,30,40],repeat=emon))
    def getresult(case):
        totalsales=0
        totalmembers=0
        prices=[int((100-rate)*(price//100)) for rate,price in zip(case,emoticons)]
        for userrate,useramount in users:
            usersales=0
            for i in range(emon):
                if case[i]>=userrate:
                    usersales+=prices[i]
                if usersales>=useramount:
                    break
            if usersales>=useramount:
                totalmembers+=1
            else:
                totalsales+=usersales
        return (totalmembers,totalsales)
    maxsales,maxmembers=0,0
    for case in cases:
        casemembers,casesales=getresult(case)
        if casemembers>maxmembers:
            maxsales,maxmembers=casesales,casemembers
        elif casemembers==maxmembers and casesales>maxsales:
            maxsales,maxmembers=casesales,casemembers
        else:
            continue      
    answer = [maxmembers,maxsales]
    return answer