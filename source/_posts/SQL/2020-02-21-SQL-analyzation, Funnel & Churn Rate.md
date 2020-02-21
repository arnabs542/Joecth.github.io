---
layout: post
categories: SQL
tag: []
date: 2020-02-20
---

https://s3.amazonaws.com/codecademy-content/courses/sql-intensive/SQL_diagram_v6.pdf



```sql
SELECT premium_users.user_id,
  months.months,
  CASE
    WHEN (
      premium_users.purchase_date <= months.months
      )
      AND
      (
        premium_users.cancel_date >= months.months
        OR
        premium_users.cancel_date IS NULL
      )
    THEN 'active'
    ELSE 'not_active'
  END AS 'status'
FROM premium_users
CROSS JOIN months;
```



## Build a Funnel From a Single Table



```sql
select * from survey_responses limit 15;
-- with count_of_users as(
--   select user_id, count(*) as nums
--   from survey_responses
--   group by user_id
--   order by count(*) desc
-- )  

-- select user_id, count(*)
-- from count_of_users
-- where nums = 5;  # SINCE 5 Questions

select question_text, 
   count(distinct user_id)
from survey_responses
group by question_text;
```



---

*If we divide the number of people completing each step by the number of people completing the previous step:*

| Question | Percent Completed this Question |
| -------- | ------------------------------- |
| 1        | 100%                            |
| 2        | 95%                             |
| 3        | 82%                             |
| 4        | 95%                             |
| 5        | 74%                             |
|          |                                 |

We see that Questio*ns 2 and 4 have high completion rates, but Questions 3 and 5 have lower rates.*

*This suggests that age and household income are more sensitive questions that people might be reluctant to answer!*

---



## Compare Funnels for A/B Tests

They’ve set up an A/B test where:

- 50% of users view the original `control` version of the pop-ups
- 50% of users view the new `variant` version of the pop-ups

Eventually, we’ll want to answer the question:

*How is the funnel different between the two groups?*

We will be using a table called `onboarding_modals` with the following columns:

- `user_id` - the user identifier
- `modal_text` - the modal step
- `user_action` - the user response (Close Modal or Continue)
- `ab_group` - the version (control or variant)

**2.**

```sql
-- 2
-- select modal_text, 
--   count(distinct user_id)
-- from onboarding_modals 
-- group by modal_text
-- order by modal_text asc;

```



**3.**

Delete your previous code.

The previous query combined both the control and variant groups.

We can use a `CASE` statement within our `COUNT()` aggregate so that we only count `user_id`s whose `ab_group` is equal to ‘control’:

```sql
SELECT modal_text,
  COUNT(DISTINCT CASE
    WHEN ab_group = 'control' THEN user_id
    END) AS 'control_clicks'
FROM onboarding_modals
GROUP BY 1
ORDER BY 1;
```

Paste this code into the code editor and see what happens.



**4.**

Add an additional column to your previous query that counts the number of clicks from the variant group and alias it as ‘variant_clicks’.

Hint

Your third column should be:

```sql
COUNT(DISTINCT CASE
  WHEN ab_group = 'variant' THEN user_id
  END) AS 'variant_clicks'
```

Don’t forget that columns need to be separated by a comma!

```sql
SELECT modal_text,
  COUNT(DISTINCT CASE
    WHEN ab_group = 'control' THEN user_id
    END) AS 'control_clicks',
  COUNT(DISTINCT CASE
    WHEN ab_group = 'variant' THEN user_id
    END) AS 'variant_clicks'
FROM onboarding_modals
GROUP BY 1
ORDER BY 1;
```

The result should have three columns:

- `modal_text`
- `control_clicks`
- `variant_clicks`

Now you can see the differences between the control and variant side by side!

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc3vrr5bsrj30pk07ijsa.jpg" alt="image-20200221115221429" style="zoom:50%;" />



![image-20200221115615095](https://tva1.sinaimg.cn/large/0082zybpgy1gc3vvqh9g9j30fs0nkaba.jpg)



## Build a Funnel from Multiple Tables

```sql
-- with bc as (
--   select *
--   from browse as b
--   left join checkout as c
--   on b.user_id = c.user_id
--   where c.user_id is not null
--   -- limit 50
-- )

-- -- select * from bc limit 15;
-- select * 
-- from bc
-- left join purchase as p
-- on bc.user_id = p.user_id
-- limit 50;

-- BETTER SOLUTION ●○●○●
select distinct b.browse_date, b.user_id, 
  c.user_id IS NOT NULL AS 'is_checkout',
  p.user_id IS NOT NULL AS 'is_purchase'
from browse as b
left join checkout as c
  on b.user_id = c.user_id
left join purchase as p
  on p.user_id = b.user_id
limit 50;
```



```sql
WITH funnels AS (
  SELECT DISTINCT b.browse_date,
     b.user_id,
     c.user_id IS NOT NULL AS 'is_checkout',
     p.user_id IS NOT NULL AS 'is_purchase'
  FROM browse AS 'b'
  LEFT JOIN checkout AS 'c'
    ON c.user_id = b.user_id
  LEFT JOIN purchase AS 'p'
    ON p.user_id = c.user_id)
-- SELECT ______
-- _____________;

-- select * from funnels limit 15;

select count(*) as 'num_browse', sum(is_checkout) as 'num_checkout', sum(is_purchase) as 'num_purchase',
1.0 * SUM(is_checkout) / COUNT(user_id) as 'checkout %', 
1.0 * SUM(is_purchase) / SUM(is_checkout) as 'purchase %'
from funnels;
```

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc41t7u4ngj30ug038dg7.jpg" alt="image-20200221152122704" style="zoom:50%;" />





```sql
WITH funnels AS (
  SELECT DISTINCT b.browse_date,
     b.user_id,
     c.user_id IS NOT NULL AS 'is_checkout',
     p.user_id IS NOT NULL AS 'is_purchase'
  FROM browse AS 'b'
  LEFT JOIN checkout AS 'c'
    ON c.user_id = b.user_id
  LEFT JOIN purchase AS 'p'
    ON p.user_id = c.user_id)
    
SELECT browse_date, COUNT(*) AS 'num_browse',
   SUM(is_checkout) AS 'num_checkout',
   SUM(is_purchase) AS 'num_purchase',
   1.0 * SUM(is_checkout) / COUNT(user_id) AS 'browse_to_checkout',
   1.0 * SUM(is_purchase) / SUM(is_checkout) AS 'checkout_to_purchase'
FROM funnels
group by browse_date;
```

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc45hn77ibj312006i3zs.jpg" alt="image-20200221172848148" style="zoom:50%;" />



<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc45jto9t8j30gq0p0gml.jpg" alt="image-20200221173038606" style="zoom: 50%;" />





## Usage Funnels with Warby Parker

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc4715qtfhj31qw0caq6d.jpg" alt="image-20200221182158177" style="zoom:67%;" />

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc4724wgkoj31rc09c0uz.jpg" alt="image-20200221182256478" style="zoom:67%;" />![image-20200221182442175](https://tva1.sinaimg.cn/large/0082zybpgy1gc473tav67j31qq0ayaeb.jpg)

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc473xoshtj31rc09c0uz.jpg" alt="image-20200221182256478" style="zoom:67%;" />![image-20200221182442175](https://tva1.sinaimg.cn/large/0082zybpgy1gc473tav67j31qq0ayaeb.jpg)



## Churn Rate

### Single Month I

Remember from the previous exercise that churn rate is:

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc48q5lr2bj307d03ajra.jpg" alt="Churn" style="zoom: 67%;" />

For the numerator, we only want the portion of the customers who cancelled during December:

```sql
SELECT 1.0 * 
(
  SELECT COUNT(*)
  FROM subscriptions
  WHERE subscription_start < '2017-01-01'
  AND (
    subscription_end
    BETWEEN '2017-01-01'
    AND '2017-01-31'
  )
) / (
  SELECT COUNT(*) 
  FROM subscriptions 
  WHERE subscription_start < '2017-01-01'
  AND (
    (subscription_end >= '2017-01-01')
    OR (subscription_end IS NULL)
  )
) 
AS result;
```





### Single Month II

The previous method worked, but you may have noticed we selected the same group of customers twice for the same month and repeated a number of conditional statements.

Companies typically look at churn data over a period of many months. We need to modify the calculation a bit to make it easier to mold into a multi-month result. This is done by making use of `WITH` and `CASE`.

To start, use `WITH` to create the group of customers that are active going into December:

```sql

WITH enrollments AS
(SELECT *
FROM subscriptions
WHERE subscription_start < '2017-01-01'
AND (
  (subscription_end >= '2017-01-01')
  OR (subscription_end IS NULL)
)),
status AS 
(SELECT
  CASE
    WHEN (subscription_end > '2017-01-31')
      OR (subscription_end IS NULL) THEN 0
      ELSE 1
    END as is_canceled,
   CASE
    WHEN subscription_start < '2017-01-01'
      AND (
        (subscription_end >= '2017-01-01')
        OR (subscription_end IS NULL)
      ) THEN 1
    ELSE 0
  END as is_active
  FROM enrollments
)

SELECT 1.0 * SUM(is_canceled) / SUM(is_active)
FROM status;
```

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc49fnhr1dj30py0kkjt3.jpg" alt="image-20200221194509437" style="zoom:50%;" />



### Multiple Month: Create Months Temporary Table

Our single month calculation is now in a form that we can extend to a multiple month result. But first, we need months!

Some SQL table schemes will contain a prebuilt table of months. Ours doesn’t, so we’ll need to build it using `UNION`. We’ll need the first and last day of each month.

Our churn calculation uses the first day as a cutoff for subscribers and the last day as a cutoff for cancellations.

This table can be created like:



**1.**

We will be using the months as a temporary table (using `WITH`) in the churn calculation.

Create the `months` temporary table using `WITH` and `SELECT` everything from it so that you can see the structure.

We need a table for January, February, and March of 2017.

```sql
WITH months AS
  (
    SELECT
    '2017-01-01' AS first_day,
    '2017-01-31' AS last_day
    UNION
    SELECT
    '2017-02-01' AS first_day,
    '2017-02-28' AS last_day
    UNION
    SELECT
    '2017-03-01' AS first_day,
    '2017-03-31' AS last_day
  )
  
select *
from months;
```



### Multiple Month: Cross Join Months and Users

Now that we have a table of months, we will join it to the subscriptions table. This will result in a table containing every combination of month and subscription.

Ultimately, this table will be used to determine the status of each subscription in each month.

Instructions

**1.**

The workspace contains the `months` temporary table from the previous exercise.

Create a `cross_join` temporary table that is a `CROSS JOIN` of `subscriptions` and `months`.

We’ve added:

```sql
SELECT *
FROM cross_join
LIMIT 100;
```

at the bottom of this exercise so you can visualize the temporary table you create.

It should `SELECT` all the columns from the temporary table.



```sql
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
-- Add temporary cross_join definition here
cross_join AS
(
  select *
  from subscriptions 
  cross join months
)

SELECT *
FROM cross_join
LIMIT 100;
```



#### Query Results - cross_join

|  id  | subscription_start | subscription_end | first_day  |  last_day  |
| :--: | :----------------: | :--------------: | :--------: | :--------: |
|  1   |     2017-03-18     |                  | 2017-01-01 | 2017-01-31 |
|  1   |     2017-03-18     |                  | 2017-02-01 | 2017-02-28 |
|  1   |     2017-03-18     |                  | 2017-03-01 | 2017-03-31 |
|  2   |     2017-03-05     |                  | 2017-01-01 | 2017-01-31 |
|  2   |     2017-03-05     |                  | 2017-02-01 | 2017-02-28 |
|  2   |     2017-03-05     |                  | 2017-03-01 | 2017-03-31 |
|  3   |     2016-12-21     |                  | 2017-01-01 | 2017-01-31 |
|  3   |     2016-12-21     |                  | 2017-02-01 | 2017-02-28 |
|  3   |     2016-12-21     |                  | 2017-03-01 | 2017-03-31 |
|  4   |     2017-03-26     |                  | 2017-01-01 | 2017-01-31 |
|  4   |     2017-03-26     |                  | 2017-02-01 | 2017-02-28 |
|  4   |     2017-03-26     |                  | 2017-03-01 | 2017-03-31 |
|  5   |     2017-03-14     |                  | 2017-01-01 | 2017-01-31 |
|  5   |     2017-03-14     |                  | 2017-02-01 | 2017-02-28 |
|  5   |     2017-03-14     |                  | 2017-03-01 | 2017-03-31 |
|  6   |     2016-12-02     |                  | 2017-01-01 | 2017-01-31 |
|  6   |     2016-12-02     |                  | 2017-02-01 | 2017-02-28 |
|  6   |     2016-12-02     |                  | 2017-03-01 | 2017-03-31 |
|  7   |     2017-03-22     |                  | 2017-01-01 | 2017-01-31 |
|  7   |     2017-03-22     |                  | 2017-02-01 | 2017-02-28 |
|  7   |     2017-03-22     |                  | 2017-03-01 | 2017-03-31 |
|  8   |     2017-03-06     |                  | 2017-01-01 | 2017-01-31 |
|  8   |     2017-03-06     |                  | 2017-02-01 | 2017-02-28 |
|  8   |     2017-03-06     |                  | 2017-03-01 | 2017-03-31 |
|  9   |     2016-12-22     |    2017-03-31    | 2017-01-01 | 2017-01-31 |
|  9   |     2016-12-22     |    2017-03-31    | 2017-02-01 | 2017-02-28 |
|  9   |     2016-12-22     |    2017-03-31    | 2017-03-01 | 2017-03-31 |
|  10  |     2017-02-22     |                  | 2017-01-01 | 2017-01-31 |
|  10  |     2017-02-22     |                  | 2017-02-01 | 2017-02-28 |
|  10  |     2017-02-22     |                  | 2017-03-01 | 2017-03-31 |
|  11  |     2017-03-02     |                  | 2017-01-01 | 2017-01-31 |
|  11  |     2017-03-02     |                  | 2017-02-01 | 2017-02-28 |
|  11  |     2017-03-02     |                  | 2017-03-01 | 2017-03-31 |
|  12  |     2016-12-14     |    2017-03-29    | 2017-01-01 | 2017-01-31 |
|  12  |     2016-12-14     |    2017-03-29    | 2017-02-01 | 2017-02-28 |
|  12  |     2016-12-14     |    2017-03-29    | 2017-03-01 | 2017-03-31 |
|  13  |     2016-12-16     |                  | 2017-01-01 | 2017-01-31 |
|  13  |     2016-12-16     |                  | 2017-02-01 | 2017-02-28 |
|  13  |     2016-12-16     |                  | 2017-03-01 | 2017-03-31 |
|  14  |     2017-03-03     |                  | 2017-01-01 | 2017-01-31 |
|  14  |     2017-03-03     |                  | 2017-02-01 | 2017-02-28 |
|  14  |     2017-03-03     |                  | 2017-03-01 | 2017-03-31 |
|  15  |     2016-12-10     |    2017-01-16    | 2017-01-01 | 2017-01-31 |
|  15  |     2016-12-10     |    2017-01-16    | 2017-02-01 | 2017-02-28 |
|  15  |     2016-12-10     |    2017-01-16    | 2017-03-01 | 2017-03-31 |
|  16  |     2016-12-12     |                  | 2017-01-01 | 2017-01-31 |
|  16  |     2016-12-12     |                  | 2017-02-01 | 2017-02-28 |
|  16  |     2016-12-12     |                  | 2017-03-01 | 2017-03-31 |
|  17  |     2017-01-05     |    2017-02-07    | 2017-01-01 | 2017-01-31 |
|  17  |     2017-01-05     |    2017-02-07    | 2017-02-01 | 2017-02-28 |
|  17  |     2017-01-05     |    2017-02-07    | 2017-03-01 | 2017-03-31 |
|  18  |     2017-02-14     |                  | 2017-01-01 | 2017-01-31 |
|  18  |     2017-02-14     |                  | 2017-02-01 | 2017-02-28 |
|  18  |     2017-02-14     |                  | 2017-03-01 | 2017-03-31 |
|  19  |     2016-12-17     |                  | 2017-01-01 | 2017-01-31 |
|  19  |     2016-12-17     |                  | 2017-02-01 | 2017-02-28 |
|  19  |     2016-12-17     |                  | 2017-03-01 | 2017-03-31 |
|  20  |     2017-01-20     |                  | 2017-01-01 | 2017-01-31 |
|  20  |     2017-01-20     |                  | 2017-02-01 | 2017-02-28 |
|  20  |     2017-01-20     |                  | 2017-03-01 | 2017-03-31 |
|  21  |     2017-03-01     |                  | 2017-01-01 | 2017-01-31 |
|  21  |     2017-03-01     |                  | 2017-02-01 | 2017-02-28 |
|  21  |     2017-03-01     |                  | 2017-03-01 | 2017-03-31 |
|  22  |     2017-01-26     |                  | 2017-01-01 | 2017-01-31 |
|  22  |     2017-01-26     |                  | 2017-02-01 | 2017-02-28 |
|  22  |     2017-01-26     |                  | 2017-03-01 | 2017-03-31 |
|  23  |     2016-12-19     |    2017-01-25    | 2017-01-01 | 2017-01-31 |
|  23  |     2016-12-19     |    2017-01-25    | 2017-02-01 | 2017-02-28 |
|  23  |     2016-12-19     |    2017-01-25    | 2017-03-01 | 2017-03-31 |
|  24  |     2017-01-31     |    2017-03-26    | 2017-01-01 | 2017-01-31 |
|  24  |     2017-01-31     |    2017-03-26    | 2017-02-01 | 2017-02-28 |
|  24  |     2017-01-31     |    2017-03-26    | 2017-03-01 | 2017-03-31 |
|  25  |     2016-12-18     |                  | 2017-01-01 | 2017-01-31 |
|  25  |     2016-12-18     |                  | 2017-02-01 | 2017-02-28 |
|  25  |     2016-12-18     |                  | 2017-03-01 | 2017-03-31 |
|  26  |     2017-02-25     |                  | 2017-01-01 | 2017-01-31 |
|  26  |     2017-02-25     |                  | 2017-02-01 | 2017-02-28 |
|  26  |     2017-02-25     |                  | 2017-03-01 | 2017-03-31 |
|  27  |     2017-01-15     |    2017-03-31    | 2017-01-01 | 2017-01-31 |
|  27  |     2017-01-15     |    2017-03-31    | 2017-02-01 | 2017-02-28 |
|  27  |     2017-01-15     |    2017-03-31    | 2017-03-01 | 2017-03-31 |
|  28  |     2016-12-20     |    2017-01-28    | 2017-01-01 | 2017-01-31 |
|  28  |     2016-12-20     |    2017-01-28    | 2017-02-01 | 2017-02-28 |
|  28  |     2016-12-20     |    2017-01-28    | 2017-03-01 | 2017-03-31 |
|  29  |     2017-01-25     |    2017-02-25    | 2017-01-01 | 2017-01-31 |
|  29  |     2017-01-25     |    2017-02-25    | 2017-02-01 | 2017-02-28 |
|  29  |     2017-01-25     |    2017-02-25    | 2017-03-01 | 2017-03-31 |
|  30  |     2017-01-11     |                  | 2017-01-01 | 2017-01-31 |
|  30  |     2017-01-11     |                  | 2017-02-01 | 2017-02-28 |
|  30  |     2017-01-11     |                  | 2017-03-01 | 2017-03-31 |
|  31  |     2016-12-13     |    2017-01-16    | 2017-01-01 | 2017-01-31 |
|  31  |     2016-12-13     |    2017-01-16    | 2017-02-01 | 2017-02-28 |
|  31  |     2016-12-13     |    2017-01-16    | 2017-03-01 | 2017-03-31 |
|  32  |     2016-12-11     |                  | 2017-01-01 | 2017-01-31 |
|  32  |     2016-12-11     |                  | 2017-02-01 | 2017-02-28 |
|  32  |     2016-12-11     |                  | 2017-03-01 | 2017-03-31 |
|  33  |     2016-12-21     |    2017-02-12    | 2017-01-01 | 2017-01-31 |
|  33  |     2016-12-21     |    2017-02-12    | 2017-02-01 | 2017-02-28 |
|  33  |     2016-12-21     |    2017-02-12    | 2017-03-01 | 2017-03-31 |
|  34  |     2017-03-19     |                  | 2017-01-01 | 2017-01-31 |



### Multiple Month: Determine Active/Cancellation Status

```sql
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
(SELECT *
FROM subscriptions
CROSS JOIN months),
status AS
(SELECT id, first_day as month,
CASE
  WHEN (subscription_start < first_day)
    AND (
      subscription_end > first_day
      OR subscription_end IS NULL
    ) THEN 1
  ELSE 0
END as is_active,
-- add is_canceled here
CASE 
  WHEN (subscription_end BETWEEN first_day AND last_day) THEN 1
  ELSE 0
 END AS is_canceled
FROM cross_join)


SELECT *
FROM status
LIMIT 100;
```

#### 

#### Query Results - status

|  id  |   month    | is_active | is_canceled |
| :--: | :--------: | :-------: | :---------: |
|  1   | 2017-01-01 |     0     |      0      |
|  1   | 2017-02-01 |     0     |      0      |
|  1   | 2017-03-01 |     0     |      0      |
|  2   | 2017-01-01 |     0     |      0      |
|  2   | 2017-02-01 |     0     |      0      |
|  2   | 2017-03-01 |     0     |      0      |
|  3   | 2017-01-01 |     1     |      0      |
|  3   | 2017-02-01 |     1     |      0      |
|  3   | 2017-03-01 |     1     |      0      |
|  4   | 2017-01-01 |     0     |      0      |
|  4   | 2017-02-01 |     0     |      0      |
|  4   | 2017-03-01 |     0     |      0      |
|  5   | 2017-01-01 |     0     |      0      |
|  5   | 2017-02-01 |     0     |      0      |
|  5   | 2017-03-01 |     0     |      0      |
|  6   | 2017-01-01 |     1     |      0      |
|  6   | 2017-02-01 |     1     |      0      |
|  6   | 2017-03-01 |     1     |      0      |
|  7   | 2017-01-01 |     0     |      0      |
|  7   | 2017-02-01 |     0     |      0      |
|  7   | 2017-03-01 |     0     |      0      |
|  8   | 2017-01-01 |     0     |      0      |
|  8   | 2017-02-01 |     0     |      0      |
|  8   | 2017-03-01 |     0     |      0      |
|  9   | 2017-01-01 |     1     |      0      |
|  9   | 2017-02-01 |     1     |      0      |
|  9   | 2017-03-01 |     1     |      1      |
|  10  | 2017-01-01 |     0     |      0      |
|  10  | 2017-02-01 |     0     |      0      |
|  10  | 2017-03-01 |     1     |      0      |
|  11  | 2017-01-01 |     0     |      0      |





### Multiple Month: Sum Active and Canceled Users

```sql
-- add status_aggregate here
status_aggregate AS
(
  SELECT month, sum(is_active), sum(is_canceled)
  FROM status
  Group by month
)

SELECT *
FROM status_aggregate;
```

#### Query Results - status_aggregate

|   month    | sum(is_active) | sum(is_canceled) |
| :--------: | :------------: | :--------------: |
| 2017-01-01 |      276       |        35        |
| 2017-02-01 |      506       |        63        |
| 2017-03-01 |      667       |       158        |



### Multiple Month: Churn Rate Calculation

```sql
select month, 1.0 * a.canceled / a.active as churn_rate
from status_aggregate as a;
```

#### Query Results - churn_rate

|   month    |    churn_rate     |
| :--------: | :---------------: |
| 2017-01-01 | 0.126811594202899 |
| 2017-02-01 | 0.124505928853755 |
| 2017-03-01 | 0.23688155922039  |





*In this lesson you learned:*

- *The churn rate is a percent of subscribers at the beginning of a period that cancel within that period. “Monthly churn” is a typical metric and what was used in the examples.*
- *How to calculate this metric using SQL for a single month. This used `COUNT()` and conditions to determine the number of subscribers that were active and how many canceled.*
- *A more complex method to track the subscriber churn rate over many months.*

*Instructions*

*The complete churn calculation is provided here for you to experiment with.*