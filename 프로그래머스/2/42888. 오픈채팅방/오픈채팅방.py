def solution(record):
    d={}
    msguid=[]
    msg=[]
    inmsg="님이 들어왔습니다."
    outmsg="님이 나갔습니다."
    messages=[inmsg,outmsg]
    answer = []
    for command in record:
        if command[0]=='L':
            act,id=command.split()
            msg.append(1)
            msguid.append(id)
        else:
            act,id,nick=command.split()
            if act=='Enter':
                d[id]=nick
                msg.append(0)
                msguid.append(id)
            elif act=='Change':
                d[id]=nick
    for i in range(len(msg)):
        answer.append(d[msguid[i]]+messages[msg[i]])
    return answer