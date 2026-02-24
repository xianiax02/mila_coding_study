def solution(files):
    answer = []
    temp=[]
    def convert(file):
        p=0
        while file[p] not in '0123456789':
            p+=1
        p1=p
        while p<len(file) and file[p] in '0123456789':
            p+=1
        p2=p
        if p2==len(file)-1:
            head,number=file[:p1],int(file[p1:])
        else:
            head,number=file[:p1],int(file[p1:p2])
        return (head.upper(),number)
    files.sort(key=lambda x:(convert(x)[0],convert(x)[1]))
    answer=files
    return answer