select t1.contest_id as contest_id,
ROUND(100*count(t1.user_id)/(select count(*) from Users),2) as percentage from Register t1
group by t1.contest_id
order by percentage desc,contest_id ;