# Write your MySQL query statement below
#in this count is new,group by customer id because we want the count of customer id
SELECT V.CUSTOMER_ID,COUNT(CUSTOMER_ID) AS COUNT_NO_TRANS
FROM VISITS V
LEFT JOIN TRANSACTIONS T
ON V.VISIT_ID=T.VISIT_ID
WHERE TRANSACTION_ID IS NULL
GROUP BY CUSTOMER_ID