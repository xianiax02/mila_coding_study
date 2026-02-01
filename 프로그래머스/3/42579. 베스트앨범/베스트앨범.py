def solution(genres, plays):
    genreplay=dict()
    album=[]
    answer = []
    n=len(genres)
    inf=float("inf")
    genres.append(inf)
    for num in range(n):
        genreplay[genres[num]]=[genreplay.get(genres[num],[0,0,0])[0]+plays[num],genreplay.get(genres[num],[0,n])[1],genreplay.get(genres[num],[0,0,n])[2]]
        if genreplay[genres[num]][1]!=n and genreplay[genres[num]][2]==n:
            genreplay[genres[num]][2]=num
        if genreplay[genres[num]][1]==n:
            genreplay[genres[num]][1]=num
        else:
            if plays[genreplay[genres[num]][1]]<plays[num]:
                genreplay[genres[num]][2]=genreplay[genres[num]][1] #한칸 뒤로 이동
                genreplay[genres[num]][1]=num #최고 노래 갱신
            elif plays[genreplay[genres[num]][2]]<plays[num]:
                genreplay[genres[num]][2]=num
    for genre,info in genreplay.items():
        album.append(info)
    album.sort(reverse=True)
    for objects in album:
        if objects[1]!=n:
            answer.append(objects[1])
        if objects[2]!=n:
            answer.append(objects[2])
    return answer