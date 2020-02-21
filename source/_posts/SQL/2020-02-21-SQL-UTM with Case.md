---
layout: post
categories: SQL
tag: []
date: 2020-02-21
---



## The Attribution Query II

To get the UTM parameters, we’ll need to `JOIN` these results back with the original table.

We’ll join tables `first_touch`, aka`ft`, and `page_visits`, aka `pv`, on `user_id` and `timestamp`.

```
ft.user_id = pv.user_id
AND ft.first_touch_at = pv.timestamp
```

Remember that `first_touch_at` is the earliest timestamp for each user. Here’s the simplified query:

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc4dkxtc5wj31640tgdjo.jpg" alt="image-20200221220840486" style="zoom:67%;" />

```sql
WITH first_touch AS (
   SELECT user_id,
      MIN(timestamp) AS 'first_touch_at'
   FROM page_visits
   GROUP BY user_id)
SELECT ft.user_id,
  ft.first_touch_at,
  pv.utm_source
FROM first_touch AS 'ft'
JOIN page_visits AS 'pv'
  ON ft.user_id = pv.user_id
  AND ft.first_touch_at = pv.timestamp;
```



## The Attribution Query III

```sql

WITH last_touch AS
(
  SELECT user_id,
     MAX(timestamp) AS 'last_touch_at'
  FROM page_visits
  -- WHERE user_id = 10069
  GROUP BY user_id
)

-- select * from last_touch limit 10;
SELECT lt.user_id, lt.last_touch_at, pv.utm_source
FROM last_touch as 'lt'
INNER JOIN page_visits as 'pv'
  ON lt.user_id = pv.user_id 
  AND lt.last_touch_at = pv.timestamp
WHERE lt.user_id = 10069;
```





<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc4dypt1xnj30ps03aaa8.jpg" alt="image-20200221222149765" style="zoom:67%;" />

# Review

You can now wield SQL to find where, when, and how users are visiting a website. Well done! Here’s a summary of what you learned:

- *UTM parameters* are a way of tracking visits to a website. Developers, marketers, and analysts use them to capture information like the time, attribution source, and attribution medium for each user visit.
- *First-touch attribution* only considers the first source for each customer. This is a good way of knowing how visitors initially discover a website.
- *Last-touch attribution* only considers the last source for each customer. This is a good way of knowing how visitors are drawn back to a website, especially for making a final purchase.
- Find first and last touches by grouping `page_visits` by `user_id` and finding the `MIN` and `MAX` of `timestamp`.
- To find first- and last-touch attribution, join that table back with the original `page_visits` table on `user_id` and `timestamp`.