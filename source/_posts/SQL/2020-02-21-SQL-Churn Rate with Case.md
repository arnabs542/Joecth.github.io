---
layout: post
categories: SQL
tag: []
date: 2020-02-21
---



> Codeflix, a streaming video startup, is interested in measuring their user churn rate. In this project, you’ll be helping them answer these questions about their churn:
>
> \1. Get familiar with the company.
>
> - How many months has the company been operating? Which months do you have enough information to calculate a churn rate?
> - What segments of users exist?
>
> \2. What is the overall churn trend since the company started?
>
> \3. Compare the churn rates between user segments.
>
> - Which segment of users should the company focus on expanding?
>
> ------
>
> Start the following project, which will guide you through the queries you need to answer the above questions. Make sure to save your queries and results — you’ll be using them as well.
>
> Then, create a set of slides using [Google Slides](https://www.google.com/slides/about/), Microsoft Powerpoint, or some other presentation software. Your presentation should answer all of the questions listed above. Each answer should include a text explanation and data to support your claim. The queries used to find that data should be included in a separate **.sql** file.
>
> - **[Template:](https://s3.amazonaws.com/codecademy-content/programs/learn-sql-from-scratch/SQL+Templates+ADwSQL.pptx)** We recommend that you use the template linked here. This template contains examples of the types of slides you’ll want to use.
> - **[Rubric:](https://s3.amazonaws.com/codecademy-content/programs/learn-sql-from-scratch/calc-churn-proj/churn-rubric-for-learners-ADwSQL.pdf)** You can share your work with your peers on Codecademy, who can give you feedback based on this rubric. Make sure to check your work before submitting!





```sql
-- select * from subscriptions limit 20;

-- select min(subscription_start), max(subscription_start)
-- from subscriptions;

WITH months AS
(SELECT
   '2017-01-01' as first_day,
   '2017-01-31' as last_day
 UNION
 SELECT
   '2017-02-01' as first_day,
   '2017-02-28' as last_day
 UNION
 SELECT
   '2017-03-01' as first_day,
   '2017-03-31' as last_day
),
cross_join AS
(SELECT * FROM subscriptions CROSS JOIN months
),
status AS
(SELECT id, first_day as month, 
  CASE
   WHEN segment = 87 AND 
     (subscription_start < first_day
        AND
        (
          subscription_end > first_day
          OR
          subscription_end is null
        )
     ) THEN 1
   ELSE 0
 END AS is_active_87
 ,
 CASE
   WHEN segment = 30 AND 
     (subscription_start < first_day
        AND
        (
          subscription_end > first_day
          OR
          subscription_end is null
        )
     ) THEN 1
   ELSE 0
 END AS is_active_30
 ,
 CASE 
   WHEN segment = 87 AND
     (
       subscription_end BETWEEN first_day AND last_day
     ) THEN 1
   ELSE 0
 END AS is_canceled_87
 ,
 CASE 
   WHEN segment = 30 AND
     (
       subscription_end BETWEEN first_day AND last_day
     ) THEN 1
   ELSE 0
 END AS is_canceled_30
 FROM cross_join 
),
status_aggregate AS
(
  SELECT  month, 
          SUM(is_active_87) AS sum_active_87,
          SUM(is_active_30) AS sum_active_30,       
          SUM(is_canceled_87) AS sum_canceled_87, 
          SUM(is_canceled_30) AS sum_canceled_30
  FROM status
  GROUP BY month
)



select * from status_aggregate limit 10;
 
```

### Query Results - status_aggregate

|   month    | sum_active_87 | sum_active_30 | sum_canceled_87 | sum_canceled_30 |
| :--------: | :-----------: | :-----------: | :-------------: | :-------------: |
| 2017-01-01 |      278      |      291      |       70        |       22        |
| 2017-02-01 |      462      |      518      |       148       |       38        |
| 2017-03-01 |      531      |      716      |       258       |       84        |



**8.**

Calculate the churn rates for the two segments over the three month period. Which segment has a lower churn rate?

```sql

-- select * from status_aggregate limit 10;

SELECT  a.month, 
        1.0 * a.sum_canceled_87 / a.sum_active_87 AS churn_87, 
        1.0 * a.sum_canceled_30 / a.sum_active_30 AS churn_30
FROM status_aggregate as a;
```

