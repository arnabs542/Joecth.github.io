---
layout: post
categories: Python
tag: []
date: 2018-12-25
---



```bash 
(joe_py36) ~ » redis-server /usr/local/etc/redis.conf                                                                    
```



### Select collection

```bash
redis-cli
127.0.0.1:6379> select 0
OK
```



### prevent Chinese error codes

```shell
redis-cli --raw
```



### Dict

```shell
redis 127.0.0.1:6379> SET runoobkey redis
OK
redis 127.0.0.1:6379> DEL runoobkey
(integer) 1
```



### 