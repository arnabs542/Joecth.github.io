#### layout: post
categories: Pandas
tag: []
date: 2015-02-21






```python
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name':['t-shirt', 't-shirt', 'skirt', 'skirt'], 
  'Color':['blue', 'green', 'red', 'black']
})

print(df1)
```

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc4f7b94uej30py09qdg6.jpg" alt="image-20200221230441471" style="zoom:50%;" />

```python
import pandas as pd

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  # Fill in rows 3 and 4
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115],
],
  columns=[
    #add column names here
    'Store ID', 'Location', 'Number of Employees'
  ])

print(df2)
```

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc4f7o819gj30pw0a8q3d.jpg" alt="image-20200221230502087" style="zoom: 50%;" />





<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc4fgr9zz2j30xj0u0n2t.jpg" alt="image-20200221231348325" style="zoom:67%;" />



<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc4flj5cvgj319q0ru44j.jpg" alt="image-20200221231823180" style="zoom:67%;" />

```python
march = df.iloc[2]	# single row
april_may_june = df.iloc[3:6]	# multi row
january = df[df.month == 'January'] # condition, single row
```

|      | month   | clinic_east | clinic_north | clinic_south | clinic_west |
| :--- | :------ | :---------- | :----------- | :----------- | ----------- |
| 0    | January | 100         | 100          | 23           | 100         |



```python
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

march_april = df[(df.month == 'March') | (df.month == 'April')]
```

|      | month | clinic_east | clinic_north | clinic_south | clinic_west |
| :--- | :---- | :---------- | :----------- | :----------- | :---------- |
| 2    | March | 81          | 96           | 65           | 96          |
| 3    | April | 80          | 80           | 54           | 180         |



```python
january_february_march = df[df.month.isin(['January', 'February', 'March'])]
print(january_february_march)
```

|      | month    | clinic_east | clinic_north | clinic_south | clinic_west |
| :--- | :------- | :---------- | :----------- | :----------- | ----------- |
| 0    | January  | 100         | 100          | 23           | 100         |
| 1    | February | 51          | 45           | 145          | 45          |
| 2    | March    | 81          | 96           | 65           | 96          |



### setting indices

|      | month    | clinic_east | clinic_north | clinic_south | clinic_west |
| :--- | :------- | :---------- | :----------- | :----------- | ----------- |
| 1    | February | 51          | 45           | 145          | 45          |
| 3    | April    | 80          | 80           | 54           | 180         |
| 5    | June     | 112         | 109          | 79           | 129         |



```python
df2 = df.loc[[1, 3, 5]]

# print(df2)

df3 = df2.reset_index()

print(df3)

df2.reset_index(inplace = True, drop = True)

print(df2)
```

|      | index | month    | clinic_east | clinic_north | clinic_south | clinic_west |
| :--- | :---- | :------- | :---------- | :----------- | :----------- | :---------- |
| 0    | 1     | February | 51          | 45           | 145          | 45          |
| 1    | 3     | April    | 80          | 80           | 54           | 180         |
| 2    | 5     | June     | 112         | 109          | 79           | 129         |

|      | month    | clinic_east | clinic_north | clinic_south | clinic_west |
| :--- | :------- | :---------- | :----------- | :----------- | :---------- |
| 0    | February | 51          | 45           | 145          | 45          |
| 1    | April    | 80          | 80           | 54           | 180         |
| 2    | June     | 112         | 109          | 79           | 129         |





## Case : ShoeFly.com

```python
orders = pd.read_csv('shoefly.csv')
print(orders.iloc([:5]))  # check first 5 lines

```

| id   | first_name | last_name | email    | shoe_type                    | shoe_material | shoe_color   |       |
| :--- | :--------- | :-------- | :------- | :--------------------------- | :------------ | :----------- | ----- |
| 0    | 54791      | Rebecca   | Lindsay  | RebeccaLindsay57@hotmail.com | clogs         | faux-leather | black |
| 1    | 53450      | Emily     | Joyce    | EmilyJoyce25@gmail.com       | ballet flats  | faux-leather | navy  |
| 2    | 91987      | Joyce     | Waller   | Joyce.Waller@gmail.com       | sandals       | fabric       | black |
| 3    | 14437      | Justin    | Erickson | Justin.Erickson@outlook.com  | clogs         | faux-leather | red   |
| 4    | 79357      | Andrew    | Banks    | AB4318@gmail.com             | boots         | leather      | brown |



### Review

You’ve completed the lesson! You’ve just learned the basics of working with a single table in Pandas, including:

- Create a table from scratch
- Loading data from another file
- Selecting certain rows or columns of a table

Let’s practice what you’ve learned.

Instructions

**1.**

In this example, you’ll be the data analyst for ShoeFly.com, a fictional online shoe store. You’ve seen this data; now it’s your turn to work with it!

Load the data from `shoefly.csv` into the variable `orders`.

Hint

You’ll need to use `pd.read_csv`.

**2.**

Inspect the first 5 lines of the data.

Stuck? Get a hint

**3.**

Your marketing department wants to send out an email blast to everyone who ordered shoes!

Select all of the email addresses from the column `email` and save them to a variable called `emails`.

Stuck? Get a hint

**4.**

Frances Palmer claims that her order was wrong. What did Frances Palmer order?

Use logic to select that row of `orders` and save it to the variable `frances_palmer`.

Stuck? Get a hint

**5.**

We need some customer reviews for our comfortable shoes. Select all orders for `shoe_type`: `clogs`, `boots`, and `ballet flats` and save them to the variable `comfy_shoes`.

![image-20200221235121135](https://tva1.sinaimg.cn/large/0082zybpgy1gc4gjxbp5vj32380sin7i.jpg)





## Case 2:

Use the lambda function `get_last_name` to create a new column `last_name` with only the employees’ last name.

```python
# Add columns here
get_last_name = lambda s: s.split()[-1]
df['last_name'] = df.name.apply(get_last_name)
print(df)
```

|      | id    | name              | hourly_wage | hours_worked | last_name |
| :--- | :---- | :---------------- | :---------- | :----------- | --------- |
| 0    | 10310 | Lauren Durham     | 19          | 43           | Durham    |
| 1    | 18656 | Grace Sellers     | 17          | 40           | Sellers   |
| 2    | 61254 | Shirley Rasmussen | 16          | 30           | Rasmussen |
| 3    | 16886 | Brian Rojas       | 18          | 47           | Rojas     |
| 4    | 89010 | Samantha Mosley   | 11          | 38           | Mosley    |
| 5    | 87246 | Louis Guzman      | 14          | 39           | Guzman    |



花俏。。，但就熟悉下

```python
total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
	if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked
  
df['total_earned'] = df.apply(total_earned, axis = 1)

print(df)

```

|      | id    | name              | hourly_wage | hours_worked | total_earned |
| :--- | :---- | :---------------- | :---------- | :----------- | :----------- |
| 0    | 10310 | Lauren Durham     | 19          | 43           | 845.5        |
| 1    | 18656 | Grace Sellers     | 17          | 40           | 680.0        |
| 2    | 61254 | Shirley Rasmussen | 16          | 30           | 480.0        |
| 3    | 16886 | Brian Rojas       | 18          | 47           | 909.0        |
| 4    | 89010 | Samantha Mosley   | 11          | 38           | 418.0        |

### rename column

```python
df.rename(columns={
  'name': 'movie_title'
  }, 
  inplace=True)
print(df)
```



## Case ShoeFly.com

#### Add Columns

```python
orders['shoe_source'] = orders.shoe_material.apply(lambda x: \
                        	'animal' if x == 'leather'else 'vegan')

orders['salutation'] = orders.apply(lambda row: \
                                    'Dear Mr. ' + row['last_name']
                                    if row['gender'] == 'male'
                                    else 'Dear Ms. ' + row['last_name'],
                                    axis=1)
```

