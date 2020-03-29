---
layout: post
categories: SQL
tag: []
date: 2020-02-20

---



# Advanced Aggregate

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gcv26l5ilkj31bm0jcn1v.jpg" alt="image-20200316000428263" style="zoom:67%;" />



## Database Schema

| orders4999 rows |      |
| :-------------: | ---- |
|       id        | int  |
|   ordered_at    | text |
|  delivered_at   | text |
|  delivered_to   | int  |

| order_items20000 rows |      |
| :-------------------: | ---- |
|          id           | int  |
|       order_id        | int  |
|         name          | text |
|      amount_paid      | real |





## Percentage

```sql
select name, round(sum(amount_paid)/
(
  select sum(amount_paid) from order_items
) *100.0, 2) as pct
from order_items
group by name
order by 2 desc;
```

### Query Results

|      name       |   %   |
| :-------------: | :---: |
|  tikka-masala   | 31.7  |
| grilled-cheese  | 21.6  |
|  chicken-parm   | 19.95 |
|       blt       | 14.75 |
|      soda       | 5.48  |
|  orange-juice   | 2.94  |
|      cake       | 2.71  |
| banana-smoothie | 0.53  |
|  kale-smoothie  | 0.35  |



## Grouping with Case Statements

```sql

select
  /**/
  case name
    when 'kale-smoothie'    then 'smoothie'
    when 'banana-smoothie'  then 'smoothie'
    when 'orange-juice'     then 'drink'
    when 'soda'             then 'drink'
    when 'blt'              then 'sandwich'
    when 'grilled-cheese'   then 'sandwich'
    when 'tikka-masala'     then 'dinner'
    when 'chicken-parm'     then 'dinner'
     else 'other'
  end as category, 
  round(1.0 * sum(amount_paid) / 
          (
            select sum(amount_paid) from order_items
          ) * 100, 2
       ) as '%'
from order_items
group by 1
order by 2 desc; 
```

### Query Results

| category | round(1.0 * sum(amount_paid) / ( select sum(amount_paid) from order_items ) * 100, 2 ) |
| :------: | :----------------------------------------------------------: |
|  dinner  |                            51.64                             |
| sandwich |                            36.34                             |
|  drink   |                             8.42                             |
|  other   |                             2.71                             |
| smoothie |                             0.88                             |



## Reorder Rates

"While we do know that kale smoothies (and drinks overall) are not driving a lot of revenue, we don’t know why. A big part of data analysis is implementing your own metrics to get information out of the piles of data in your database.

In our case, the reason could be that no one likes kale, but it could be something else entirely. To find out, we’ll create a metric called *reorder rate* and see how that compares to the other products at SpeedySpoon.

We’ll define *reorder rate* as the ratio of the total number of orders to the number of people making those orders. A higher ratio means most of the orders are reorders. A lower ratio means more of the orders are first purchases."

![image-20200316112531249](https://tva1.sinaimg.cn/large/00831rSTgy1gcvlv4b5ldj327o0s4wkh.jpg)

![image-20200316113051990](https://tva1.sinaimg.cn/large/00831rSTgy1gcvm0mdyqsj324j0u0k30.jpg)



## Conclusion

## Conclusion

Wow! That’s unexpected. While smoothies aren’t making a lot of money for SpeedySpoon, they have a very high reorder rate. That means these smoothie customers are strong repeat customers.

Instead of recommending smoothies be taken off the menu, we should talk to the smoothie customers and see what they like so much about these smoothies. There could be an opportunity here to expand the product line, or get other customers as excited as these kale fanatics. Nice work!

Let’s generalize what we’ve learned so far:

- *Data aggregation* is the grouping of data in summary form.
- *Daily Count* is the count of orders in a day.
- *Daily Revenue Count* is the revenue on orders per day.
- *Product Sum* is the total revenue of a product.
- *Subqueries* can be used to perform complicated calculations and create filtered or aggregate tables on the fly.
- *Reorder Rate* is the ratio of the total number of orders to the number of people making orders.



# Count Metrics

### Query Results

|  id  | user_id | price |     refunded_at     |     created_at      |
| :--: | :-----: | :---: | :-----------------: | :-----------------: |
|  0   |   255   |  1.5  |                     | 2015-10-04 14:39:46 |
|  1   |   448   |  0.5  |                     | 2015-09-11 17:33:06 |
|  2   |   237   |  4.5  |                     | 2015-08-17 23:13:32 |
|  3   |   468   |  3.5  |                     | 2015-08-08 16:25:59 |
|  4   |   50    |  4.5  |                     | 2015-08-18 02:36:17 |
|  5   |   86    |  1.5  | 2015-11-19 10:02:31 | 2015-11-19 05:16:54 |
|  6   |   384   |  4.5  |                     | 2015-08-21 14:35:02 |
|  7   |   490   |  1.5  |                     | 2015-10-08 01:09:32 |
|  8   |   454   |  1.5  |                     | 2015-10-24 12:26:39 |
|  9   |   280   |  1.5  |                     | 2015-08-24 15:19:00 |

|  id  | user_id |     created_at      | platform |
| :--: | :-----: | :-----------------: | :------: |
|  0   |   225   | 2015-11-25 20:06:36 |   Web    |
|  1   |   175   | 2015-08-08 12:39:30 |   iOS    |
|  2   |   453   | 2015-11-11 05:44:58 |   Web    |
|  3   |   438   | 2015-10-27 07:26:07 | Android  |
|  4   |   413   | 2015-11-12 19:47:57 |   iOS    |
|  5   |   424   | 2015-11-10 23:23:49 | Android  |
|  6   |   55    | 2015-09-13 14:49:09 |   iOS    |
|  7   |   285   | 2015-08-31 18:32:49 |   Web    |
|  8   |   28    | 2015-08-16 00:34:09 |   iOS    |
|  9   |   22    | 2015-08-11 23:53:11 |   iOS    |

### Database Schema

| purchases2000 rows |      |
| :----------------: | ---- |
|         id         | int  |
|      user_id       | int  |
|       price        | real |
|    refunded_at     | text |
|     created_at     | text |

| gameplays14000 rows |      |
| :-----------------: | ---- |
|         id          | int  |
|       user_id       | int  |
|     created_at      | text |
|      platform       | text |

![image-20200316115322516](https://tva1.sinaimg.cn/large/00831rSTgy1gcvmo5pnolj32660lugq8.jpg)



## Daily Active Users

Mineblocks is a game, and one of the core metrics to any game is the number of people who play each day. That KPI is called *Daily Active Users*, or *DAU*.

*DAU* is defined as the number of unique players seen in-game each day. It’s important not to double count users who played multiple times, so we’ll use `distinct` in our `count` function.

Likewise, Weekly Active Users (WAU) and Monthly Active Users (MAU) are in the same family.

1. For Mineblocks, we’ll use the `gameplays` table to calculate DAU. Each time a user plays the game, their session is recorded in `gameplays`. Thus, a distinct count of users per day from gameplays will give us DAU.

   Calculate Daily Active Users for Mineblocks. Complete the query’s `count` function by passing in the `distinct` keyword and the `user_id` column name.

```sql
select
  date(created_at), 
  count(distinct user_id/**/) as dau
from gameplays
group by 1
order by 1;
```



## Daily Active Users 2

**1.**

Previously we calculated DAU only per day, so the output we wanted was `[date, dau_count]`. Now we want DAU per platform, making the desired output `[date, platform, dau_count]`.

Calculate DAU for Mineblocks per-platform. Complete the query below. You will need to select the `platform` column and add a `count` function by passing in the `distinct` keyword and the `user_id` column name.

```sql
select
  date(created_at), 
  platform,
  count(distinct user_id/**/) as dau
from gameplays
group by 1, 2
order by 1, 2;

P.S. IF NO 2nd group by , diff platforms collapse into the same day
```

| date(created_at) | platform | dau  |
| ---------------- | -------- | ---- |
| 2015-08-08       | Android  | 39   |
| 2015-08-08       | Web      | 43   |
| 2015-08-08       | iOS      | 25   |
| 2015-08-09       | Android  | 55   |
| 2015-08-09       | Web      | 44   |
| 2015-08-09       | iOS      | 37   |
| 2015-08-10       | Android  | 38   |



## Daily Average Revenue Per Purchasing User

We’ve looked at DAU and Daily Revenue in Mineblocks. Now we must understand the purchasing habits of our users.

Mineblocks, like every freemium game, has two types of users:

- purchasers: users who have bought things in the game
- players: users who play the game but have not yet purchased


The next KPI we'll look at *Daily ARPPU* - Average Revenue Per Purchasing User. This metric shows if the average amount of money spent by purchasers is going up over time.

*Daily ARPPU* is defined as the sum of revenue divided by the number of purchasers per day.

**1.**

To get Daily ARPPU, modify the daily revenue query from earlier to divide by the number of purchasers.

Complete the query by adding a numerator and a denominator. The numerator will display daily revenue, or `sum` the `price` columns. The denominator will display the number of purchasers by passing the `distinct` keyword and the `user_id` column name into the `count` function.

```sql
select
  date(created_at),
  round(/**/sum(price) / count(distinct user_id/**/), 2) as arppu
from purchases
where refunded_at is null
group by 1
order by 1;
```

| date(created_at) | arppu |
| :--------------: | :---: |
|    2015-08-04    | 3.46  |
|    2015-08-05    | 2.65  |
|    2015-08-06    | 1.44  |
|    2015-08-07    | 2.32  |
|    2015-08-08    | 2.53  |
|    2015-08-09    | 1.75  |
|    2015-08-10    |  3.0  |
|    2015-08-11    | 2.25  |
|    2015-08-12    | 2.78  |
|    2015-08-13    | 2.83  |
|    2015-08-14    |  2.7  |



## Daily Average Revenue Per User

The more popular (and difficult) cousin to Daily ARPPU is *Daily ARPU*, Average Revenue Per User. ARPU measures the average amount of money we’re getting across all players, ***whether or not they’ve purchased.***

ARPPU increases if purchasers are spending more money. ARPU increases if more players are choosing to purchase, even if the purchase size stays consistent.

***No one metric can tell the whole story.*** That’s why it’s so helpful to have many KPIs on the same dashboard.



## ARPU 2

Daily ARPU is defined as revenue divided by the number of players, per-day. To get that, we’ll need to calculate the daily revenue and daily active users separately, and then join them on their dates.

One way to easily create and organize temporary results in a query is with *CTEs*, *Common Table Expressions*, also known as `with` clauses. The `with` clauses make it easy to define and use results in a more organized way than subqueries.

These clauses usually look like this:

```sql
/**/with  daily_revenue as (
  select
    date(created_at) as dt,
    round(sum(price), 2) as rev
  from purchases
  where refunded_at is null
  group by 1
)
select * from daily_revenue order by dt;
```

**2.**

Now that we have the revenue and DAU, join them on their dates and calculate daily ARPU. Complete the query by adding the keyword `using` in the `join` clause.

```sql
/**/ with  daily_revenue as (
  select
    date(created_at) as dt,
    round(sum(price), 2) as rev
  from purchases
  where refunded_at is null
  group by 1
),
daily_players as (
  select
    /**/date(created_at) as dt,
    /**/count(distinct user_id) as players
  from gameplays
  group by 1
)
select
  daily_revenue.dt, 
  daily_revenue.rev / daily_players.players
from daily_revenue
  join daily_players using (dt);
```

In the final `select` statement, `daily_revenue.dt` represents the date, while `daily_revenue.rev / daily_players.players` is the daily revenue divided by the number of players that day. In full, it represents how much the company is making per player, per day.



When the columns to join have the same name in both tables you can use `using` instead of `on`. Our use of the `using` keyword is in this case equivalent to this clause:

```sql
from daily_revenue
  join daily_players on
    daily_revenue.dt = daily_players.dt;
```



## 1Day Retention

# 1 Day Retention

Now let’s find out what percent of Mineblock players are returning to play the next day. This KPI is called *1 Day Retention*.

*Retention* can be defined many different ways, but we’ll stick to the most basic definition. For all players on Day N, we’ll consider them retained if they came back to play again on Day N+1.

This will let us track whether or not Mineblocks is getting “stickier” over time. The stickier our game, the more days players will spend in-game.

And more time in-game means more opportunities to monetize and grow our business.



#### Cont.

Before we can calculate retention we need to get our data formatted in a way where we can determine if a user returned.

Currently the `gameplays` table is a list of when the user played, and it’s not easy to see if any user came back.

By using a `self-join`, we can make multiple gameplays available on the same row of results. This will enable us to calculate retention.

The power of `self-join` comes from joining every row to every other row. This makes it possible to compare values from two different rows in the new result set. In our case, we’ll compare rows that are one date apart from each user.

![SQL join types](https://tva1.sinaimg.cn/large/00831rSTgy1gcw6v3ohoqj30dj0a3q3j.jpg)

Now that we have our `gameplays` table joined to itself, we can start to calculate retention.

1 Day Retention is defined as the number of players who returned the next day divided by the number of original players, per day. Suppose 10 players played Mineblocks on Dec 10th. If 4 of them play on Dec 11th, the 1 day retention for Dec 10th is 40%.

Instructions

**1.**

The previous query joined all rows in gameplays against all other rows for each user, making a massive result set that we don’t need.

We’ll need to modify this query.

```sql
select
  date(g1.created_at) as dt,
  g1.user_id, 
  g2.user_id
from gameplays as g1
  /**/ left join 
    gameplays as g2 on
    g1.user_id = g2.user_id
    and date(g1.created_at) = date(datetime(g2.created_at, '-1 day'))
group by 1
order by 1
limit 100;
```



**2.**

The query above won’t return meaningful results because we’re using an `inner join`. This type of join requires that the condition be met for all rows, effectively limiting our selection to only the users that have returned.

Instead, we want to use a `left join`, this way all rows in `g1` are preserved, leaving nulls in the rows from `g2` where users did not return to play the next day.

Change the `join` clause to use `left join` and count the distinct number of users from `g1` and `g2` per date.

```sql
select
  date(g1.created_at) as dt,
  -- g1.user_id, 
  -- g2.user_id
  count(distinct g1.user_id) as total_users,
  count(distinct g2.user_id) as retained_users 
from gameplays as g1
  /**/ left join 
    gameplays as g2 on
    g1.user_id = g2.user_id
    and date(g1.created_at) = date(datetime(g2.created_at, '-1 day'))
group by 1
order by 1
limit 100;
```

| dt         | total_users | retained_users |
| ---------- | ----------- | -------------- |
| 2015-08-19 | 111         | 26             |
| 2015-08-20 | 117         | 31             |
| 2015-08-21 | 112         | 27             |
| 2015-08-22 | 117         | 24             |
| 2015-08-23 | 94          | 23             |
| 2015-08-24 | 108         | 23             |
| 2015-08-25 | 120         | 23             |





```sql
select
  date(g1.created_at) as dt,
  -- g1.user_id, 
  -- g2.user_id
  round(100 * count(distinct g1.user_id) as total_users /
  count(distinct g2.user_id)) as retention
from gameplays as g1
  /**/ left join 
    gameplays as g2 on
    g1.user_id = g2.user_id
    and date(g1.created_at) = date(datetime(g2.created_at, '-1 day'))
group by 1
order by 1
limit 100;
```



```sql
select
  date(g1.created_at) as dt,
  round(100 * count(distinct g2.user_id) /
    count(distinct g1.user_id)) as retention
from gameplays as g1
  left join gameplays as g2 on
    g1.user_id = g2.user_id
    and date(g1.created_at) = date(datetime(g2.created_at, '-1 day'))
group by 1
order by 1
limit 100;
```



## Common Metrics Conclusion

While every business has different metrics to track their success, most are based on revenue and usage.

The metrics in this lesson are merely a starting point, and from here you’ll be able to create and customize metrics to track whatever is most important to your company.

And remember, data science is exploratory! The current set of metrics can always be improved and there’s usually more to any spike or dip than what immediately meets the eye.

Let’s generalize what we’ve learned so far:

- *Key Performance Indicators* are high level health metrics for a business.
- *Daily Revenue* is the sum of money made per day.
- *Daily Active Users* are the number of unique users seen each day
- *Daily Average Revenue Per Purchasing User (ARPPU)* is the average amount of money spent by purchasers each day.
- *Daily Average Revenue Per User (ARPU)* is the average amount of money across all users.
- *1 Day Retention* is defined as the number of players from Day N who came back to play again on Day N+1.