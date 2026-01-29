WITH SKILLTABLE AS (SELECT D.ID,D.EMAIL, D.SKILL_CODE, S.NAME, S.CATEGORY, S.CODE
FROM DEVELOPERS D
JOIN SKILLCODES S ON D.SKILL_CODE & S.CODE > 0)
SELECT CASE WHEN EXISTS(SELECT 1 
                      FROM SKILLTABLE A
                      WHERE (A.ID=B.ID) AND (A.NAME LIKE 'Python') )
                      AND EXISTS(SELECT 1
                                 FROM SKILLTABLE A
                                 WHERE (A.ID=B.ID) AND A.CATEGORY='Front End')
                      THEN 'A'
            WHEN EXISTS(SELECT 1
                      FROM SKILLTABLE A
                      WHERE (A.ID=B.ID) AND A.NAME LIKE 'C#')
                      THEN 'B'
            WHEN EXISTS(SELECT 1
                       FROM SKILLTABLE A
                       WHERE A.ID=B.ID AND A.CATEGORY='Front End') THEN 'C'  END AS GRADE,B.ID,B.EMAIL
FROM DEVELOPERS B
HAVING GRADE IS NOT NULL
ORDER BY GRADE, B.ID