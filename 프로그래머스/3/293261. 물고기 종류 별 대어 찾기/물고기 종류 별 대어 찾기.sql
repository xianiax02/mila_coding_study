SELECT I.ID,N.FISH_NAME,I.LENGTH
FROM FISH_INFO I
JOIN FISH_NAME_INFO N ON I.FISH_TYPE=N.FISH_TYPE
WHERE (N.FISH_NAME,I.LENGTH) IN (SELECT FISH_NAME,MAX(LENGTH)
                                 FROM FISH_INFO A
                                 JOIN FISH_NAME_INFO B 
                                 ON A.FISH_TYPE=B.FISH_TYPE
                                 GROUP BY B.FISH_NAME)

ORDER BY I.ID;