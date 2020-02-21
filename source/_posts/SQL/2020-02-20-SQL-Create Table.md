---
layout: post
categories: SQL
tag: []
date: 2020-02-20
---



https://www.codecademy.com/courses/learn-sql/projects/learn_sql_create_table



```sql
CREATE TABLE friends(
  id INTEGER,
  name TEXT,
  birthday DATE
);

-- alter table friends
INSERT INTO friends (id, name, birthday)
VALUES (1, 'Jane Doe', '1990-05-30');

SELECT * FROM friends;

insert into friends (id, name, birthday)
values (2, 'Alex', '1986-06-06');

insert into friends (id, name, birthday)
values (3, 'Tina', '1984-12-12');
SELECT * FROM friends;

update friends
SET name = 'Jane Smith'
where id = 1;
SELECT * FROM friends;

ALTER TABLe friends
ADD COLUMN email TEXT;

update friends
set email = 'jane@codecademy.com'
where id = 1;
select * from friends;

DELETE FROM friends
where id  = 1;
select * from friends;
-- alter table friends (name)
-- values (1, )

```



<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gc2ud71ragj30oe0vwtbb.jpg" alt="image-20200220141807884" style="zoom:50%;" />