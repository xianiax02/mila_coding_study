-- 코드를 작성해주세요
WITH GRADEBOARD AS (SELECT T.EMP_NO, CASE WHEN T.S>=192 THEN 'S'
                                WHEN T.S>=180 THEN 'A'
                                WHEN T.S>=160 THEN 'B'
                                ELSE 'C'
                                END AS GRADE
                    FROM (SELECT EMP_NO,SUM(SCORE) AS S
                          FROM HR_GRADE
                          GROUP BY EMP_NO
                          ) AS T
                   )
SELECT A.EMP_NO, A.EMP_NAME, B.GRADE, CASE WHEN B.GRADE='S' THEN 0.2*A.SAL
                                           WHEN B.GRADE='A' THEN 0.15*A.SAL
                                           WHEN B.GRADE='B' THEN 0.1*A.SAL
                                           ELSE 0 END AS BONUS
FROM HR_EMPLOYEES AS A
JOIN GRADEBOARD AS B ON A.EMP_NO=B.EMP_NO;