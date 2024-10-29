# Write your MySQL query statement below
select c.name as Employee from employee c
 inner join employee m
 on m.id = c.managerid
 where c.salary > m.salary;
 