# Write your MySQL query statement below
SELECT p.firstName,p.lastname,a.city,a.state
FROM PERSON p
LEFT JOIN Address a
ON p.personid=a.personid;