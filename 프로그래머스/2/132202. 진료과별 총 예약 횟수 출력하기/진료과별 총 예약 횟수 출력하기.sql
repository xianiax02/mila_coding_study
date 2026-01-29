SELECT 
    MCDP_CD AS "진료과 코드", 
    COUNT(APNT_NO) AS "5월예약건수"
FROM APPOINTMENT
-- LIKE 대신 함수를 써서 날짜를 더 정확하게 뽑아냅니다.
WHERE YEAR(APNT_YMD) = 2022 AND MONTH(APNT_YMD) = 5
GROUP BY MCDP_CD
-- 별칭 대신 원본 컬럼명과 집계 함수를 직접 써서 정렬 (가장 에러 없는 방식)
ORDER BY COUNT(APNT_NO) ASC, MCDP_CD ASC;