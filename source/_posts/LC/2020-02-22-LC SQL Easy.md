---
layout: post
categories: LC
tag: []
date: 2020-02-21
---



#### 175. Combine Two Tables

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
```

Table: `Address`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
```

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

```SQL
SELECT FirstName, LastName, City, State
FROM Person 
LEFT JOIN Address
ON Person.PersonId = Address.PersonId
```



#### 176. Second Highest Salary

For example, given the above Employee table, the query should return `200` as the second highest salary. If there is no second highest salary, then the query should return `null`.

Write a SQL query to get the second highest salary from the `Employee` table.

```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

For example, given the above Employee table, the query should return `200` as the second highest salary. If there is no second highest salary, then the query should return `null`.

```
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

```SQL
SELECT MAX(a.Salary) AS SecondHighestSalary
FROM Employee AS a
INNER JOIN Employee as b
ON a.Salary < b.Salary
```



#### 181. Employees Earning More Than Their Managers

The `Employee` table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

```
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
```

Given the `Employee` table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

```
+----------+
| Employee |
+----------+
| Joe      |
+----------+
```

```sql
select tb1.Name AS Employee
FROM Employee as tb1
inner join Employee as tb2
on tb1.ManagerId = tb2.Id
where tb1.Salary > tb2.Salary
```



#### 182. Duplicate Emails

Write a SQL query to find all duplicate emails in a table named `Person`.

For example, your query should return the following for the above table:

```
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
```

```SQL
SELECT Email #, COUNT(Email)
FROM Person
GROUP BY Email
# ORDER BY COUNT(Email)
HAVING COUNT(Email) > 1
```



#### 183. Customers Who Never Order

Suppose that a website contains two tables, the `Customers` table and the `Orders` table. Write a SQL query to find all customers who never order anything.

Table: `Customers`.

```
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
```

Table: `Orders`.

```
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
```

Using the above tables as example, return the following:

```
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

```SQL
select tb1.Name AS Customers
from Customers as tb1
LEFT JOIN Orders 
ON tb1.Id = Orders.CustomerId
WHERE Orders.CustomerId is NULL
```



#### 196. Delete Duplicate Emails

```sql
DELETE p1
FROM Person p1
CROSS JOIN Person p2
WHERE p1.Email = p2.Email
	AND p1.Id > p2.Id;
```



#### 197.



#### 511.



#### 512.