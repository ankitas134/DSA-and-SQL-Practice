# Write your MySQL query statement below
#first write the table on the left then leftjoin the table on the right the from table should be the one whose all data is needed
SELECT PRODUCT_NAME,YEAR,PRICE
FROM SALES S
LEFT JOIN PRODUCT P
ON P.PRODUCT_ID=S.PRODUCT_ID
