



<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gcg1afg4rdj30jg0hkdgt.jpg" alt="image-20200303001005931" style="zoom:50%;" />

```sql
WITH tmp
AS (
	SELECT *
	FROM Campaigns
	LEFT JOIN (
		SELECT Campaign_id
			,min(DATE) AS earliest_date
			,Spend_amount_USD
		FROM Spend
		GROUP BY Campaign_id
		) ss ON Campaigns.Campaign_id = ss.Campaign_id
	)
SELECT *
FROM tmp
```





```sql
SELECT *
FROM Campaigns
LEFT JOIN (
	SELECT s1.Campaign_id
		,s1.DATE
		,Spend_amount_USD
	FROM Spend AS s1
	INNER JOIN (
		SELECT Campaign_id
			,min(DATE) AS earliest_date
		FROM Spend
		GROUP BY Campaign_id
		) tmp ON s1.Campaign_id = tmp.Campaign_id
		AND s1.DATE = tmp.earliest_date
	) ss ON Campaigns.Campaign_id = ss.Campaign_id
```

left join 因為，可能 Spend裡找不到235這活動，但是他的確是Account_id２辦過的



```sql
WITH cs
AS (
	SELECT *
	FROM Campaigns
	LEFT JOIN (
		SELECT Campaign_id
			,min(DATE) AS earliest_date
			,Spend_amount_USD
		FROM Spend
		GROUP BY Campaign_id
		) ss ON Campaigns.Campaign_id = ss.Campaign_id
	)
	
SELECT *
FROM cs AS c1
WHERE c1.earliest_date = (
		SELECT min(c2.earliest_date)
		FROM cs AS c2
		WHERE c2.Account_id = c2.Account_id
		)
	OR c1.earliest_date IS NULL
ORDER BY account_id
```





| ID   | Account_id | Campaign_id | Campaign_type    | Campaign_id:1 | earliest_date | Spend_amount_USD |
| ---- | ---------- | ----------- | ---------------- | ------------- | ------------- | ---------------- |
| 1    | 1          | 123         | Promoted Trend   | 123           | 2017-08-01    | 200.0            |
| 2    | 1          | 234         | Promoted Account | 234           | 2017-08-01    | 500.0            |
| 3    | 2          | 235         | Promoted Tweet   |               |               |                  |
| 4    | 1          | 456         | Promoted Trend   | 456           | 2017-08-01    | 200.0            |
| 5    | 1          | 999         | NONO             | 999           | 2017-08-11    | 1000.0           |

| ID   | Account_id | Campaign_id | Campaign_type    | Campaign_id:1 | earliest_date | Spend_amount_USD |
| ---- | ---------- | ----------- | ---------------- | ------------- | ------------- | ---------------- |
| 1    | 1          | 123         | Promoted Trend   | 123           | 2017-08-01    | 200.0            |
| 2    | 1          | 234         | Promoted Account | 234           | 2017-08-01    | 500.0            |
| 4    | 1          | 456         | Promoted Trend   | 456           | 2017-08-01    | 200.0            |
| 3    | 2          | 235         | Promoted Tweet   |               |               |                  |



```sql
WITH cs
AS (
	SELECT *
	FROM Campaigns
	LEFT JOIN (
		SELECT Campaign_id
			,min(DATE) AS earliest_date
			,SUM(Spend_amount_USD)
		FROM Spend
		GROUP BY Campaign_id
		) ss ON Campaigns.Campaign_id = ss.Campaign_id
	)
	
SELECT *
FROM cs AS c1
WHERE c1.earliest_date = (
		SELECT min(c2.earliest_date)
		FROM cs AS c2
		WHERE c1.Account_id = c2.Account_id
		)
	OR c1.earliest_date IS NULL
ORDER BY account_id
```

