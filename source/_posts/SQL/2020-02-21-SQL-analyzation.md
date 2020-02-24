---
layout: post
categories: SQL
tag: []
date: 2020-02-20

---



# Analyze Data with SQL

### 1. 

The UX Research team wants to see a distribution of watch durations. They want the result to contain:

- `duration`, which is the watch event duration, rounded to the closest minute
- `count`, the number of watch events falling into this “bucket”

Your result should look like:

| duration | count |
| -------- | ----- |
| 1.0      | 9     |
| 2.0      | 21    |
| 3.0      | 19    |
| …        | …     |
|          |       |



Use `COUNT()`, `GROUP BY`, and `ORDER BY` to create this result and order this data by increasing `duration`.

```sql
select round(watch_duration_in_minutes, 0) 
from watch_history 
limit 10;

SELECT
  ROUND(watch_duration_in_minutes, 0) as duration,
  COUNT(*) as count
FROM watch_history
GROUP BY duration
ORDER BY duration ASC limit 20;

select round(watch_duration_in_minutes, 0) as duration, 
count(*) as count
from watch_history
group by duration
order by duration asc limit 20;
-- order by count(*) asc limit 20;
```



### 2.

Find all the users that have successfully made a payment to Codeflix and find their total amount paid.

Sort them by their total payments (from high to low).

Use `SUM()`, `WHERE`, `GROUP BY`, and `ORDER BY`



```sql
SELECT user_id, SUM(amount)
FROM payments
WHERE status = 'paid'
GROUP BY user_id
ORDER BY SUM(amount) DESC;
```

```sql
SELECT user_id, SUM(amount) AS 'total'
FROM payments
WHERE status = 'paid'
GROUP BY 1
ORDER BY 2 DESC;
```



The `watch_history` table has the following columns:

- `id`
- `user_id`
- `watch_date`
- `watch_duration_in_minutes`

Click [here](https://s3.amazonaws.com/codecademy-content/courses/learn-sql-aggregates-code-challenge/user-payments-history.png) for the table diagram.

Instructions

Generate a table of user ids and total watch duration for users who watched more than 400 minutes of content.

Use `SUM()`, `GROUP BY`, and `HAVING` to achieve this.

```sql
Select user_id, SUM(watch_duration_in_minutes) 
from watch_history 
group by user_id
having SUM(watch_duration_in_minutes) > 400;
```



### 3. 

Which days in this period did Codeflix collect the most money?

Your result should have two columns, `pay_date` and total `amount`, sorted by the latter descending.

This should only include successful payments (`status = 'paid'`).

Use `SUM()`, `GROUP BY`, and `ORDER BY`.

```sql
select pay_date, sum(amount)
from payments
where status = 'paid'
group by pay_date
order by sum(amount) desc;
```





# The Metropolitan Museum of Art

First, let’s find the “lowest” year:

```
SELECT MIN(date)
FROM met;
```

The result is 1600-1700.

Now, let’s try this:

```
SELECT date, title, medium
FROM met
WHERE date LIKE '%1600%';
```

Woah! [Betty Lamp](https://www.metmuseum.org/art/collection/search/507), [Candlestick](https://www.metmuseum.org/art/collection/search/1194), and [Casement Window](https://www.metmuseum.org/art/collection/search/1458) are among the oldest pieces in the collection.



**7.**

Lastly, let’s look at some bling!

Count the number of pieces where the `medium` contains ‘gold’ or ‘silver’.

And sort in descending order.

Hint

```SQL
-- ★★★ 7 
select medium, count(*)
from met
where medium like '%gold%' or '%silver%'
group by medium
order by count(*) desc;
-- 可以做得再更往大分類去，要用到 CASE!如這裡
select CASE
    WHEN medium like '%gold%' THEN 'GOLD'
    WHEN medium like '%silver%' THEN 'SILVER'
    ELSE NULL
  END AS 'Bling', 
  count(*)
from met
-- where medium like '%gold%' or '%silver%'
-- group by medium
where Bling is not null
group by Bling
order by count(*) desc;
```



# Hacker News



### Which sites feed Hacker News?

**6.**

Hacker News stories are essentially links that take users to other websites.

*Which of these sites feed Hacker News the most*:

*[GitHub](https://www.github.com/), [Medium](https://www.medium.com/), or [New York Times](https://www.nytimes.com/)?*

First, we want to categorize each story based on their source.

We can do this using a `CASE` statement:

```
SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   -- WHEN statement here
   -- WHEN statement here
   -- ELSE statement here
  END AS 'Source'
FROM hacker_news;
```

Fill in the other `WHEN` statements and the `ELSE` statement.

Stuck? Get a hint

**7.**

Next, build on the previous query:

Add a column for the number of stories from each URL using `COUNT()`.

Also, `GROUP BY` the `CASE` statement.

Remember that you can refer to a column in `GROUP BY` using a number.



```sql
-- 6, 7
SELECT CASE
  WHEN url LIKE '%github%' THEN 'GitHub'
  WHEN url LIKE '%medium.com%' THEN 'Medium'
  WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
  ELSE 'Other'
END AS three_urls, count(*)
from hacker_news 
group by three_urls
order by count(*);
```



### What's the best time to post a story?

**8.**

Every submitter wants their story to get a high score so that the story makes it to the front page, but…

*What’s the best time of the day to post a story on Hacker News?*

Before we get started, let’s run this query and take a look at the `timestamp` column:

```
SELECT timestamp
FROM hacker_news
LIMIT 10;
```

Notice that the values are formatted like:

```
2018-05-08T12:30:00Z
```

If you ignore the `T` and `Z`, the format is:

```
YYYY-MM-DD HH:MM:SS
```

Stuck? Get a hint

**9.**

SQLite comes with a `strftime()` function - a very powerful function that allows you to return a formatted date.

It takes two arguments:

```
strftime(format, column)
```

Let’s test this function out:

```
SELECT timestamp,
   strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;
```

What do you think this does? Open the hint if you’d like to learn more.

Stuck? Get a hint

```sql
-- 8, 9
select timestamp
from hacker_news
limit 15;

select timestamp,
  strftime('%H', timestamp)
from hacker_news
group by 1
-- order by 
limit 15;
-- This returns the hour, HH, of the timestamp column!

-- For strftime(__, timestamp):

-- %Y returns the year (YYYY)
-- %m returns the month (01-12)
-- %d returns the day of the month (1-31)
-- %H returns 24-hour clock (00-23)
-- %M returns the minute (00-59)
-- %S returns the seconds (00-59)
-- if timestamp format is YYYY-MM-DD HH:MM:SS.

```



**10.**

Okay, now we understand how `strftime()` works. Let’s write a query that returns three columns:

1. The hours of the `timestamp`
2. The *average* `score` for each hour
3. The *count* of stories for each hour

Stuck? Get a hint

**11.**

Let’s edit a few things in the previous query:

- Round the average `score`s (`ROUND()`).
- Rename the columns to make it more readable (`AS`).
- Add a `WHERE` clause to filter out the `NULL` values in `timestamp`.

Take a look at the result again:

What are the best hours to post a story on Hacker News?

```sql
-- 10 ●○●○● 
select strftime('%H', timestamp), avg(score) ,count(*)
from hacker_news
group by 1 
order by 1;
-- limit 15;
-- having sum(score)

-- 11
select strftime('%H', timestamp) AS Hour, round(avg(score), 2) AS 'Average Score',count(*) AS '# of Stories'
from hacker_news
where timestamp is not null  -- 注意！！　這裡不能寫１，而要用本來的column名
group by 1 
order by 1;
```



<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc5jrvpb7ij30fi0bq3yv.jpg" alt="image-20200222222825218" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc5k2mxbs4j31520hitmq.jpg" alt="image-20200222223832094" style="zoom:67%;" />



<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc5ka80insj31b00caqf3.jpg" alt="image-20200222224606164" style="zoom:67%;" />