---
layout: post
categories: Python
tag: []
date: 2018-05-06
---



ref: http://www.grantjenks.com/docs/sortedcontainers/



For Map/TreeMap data structure, we may use [sortedcontainers](http://www.grantjenks.com/docs/sortedcontainers/) library.

```python
>>> from sortedcontainers import SortedList
>>> sl = SortedList(['e', 'a', 'c', 'd', 'b'])
>>> sl
SortedList(['a', 'b', 'c', 'd', 'e'])
>>> sl *= 10_000_000
>>> sl.count('c')
10000000
>>> sl[-3:]
['e', 'e', 'e']
>>> from sortedcontainers import SortedDict
>>> sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
>>> sd
SortedDict({'a': 1, 'b': 2, 'c': 3})
>>> sd.popitem(index=-1)
('c', 3)
>>> from sortedcontainers import SortedSet
>>> ss = SortedSet('abracadabra')
>>> ss
SortedSet(['a', 'b', 'c', 'd', 'r'])
>>> ss.bisect_left('c')
2
```

All of the operations shown above run in faster than linear time.





Ref: https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages-

> # What are the environments for the programming languages?
>
> - 1 month ago
> -  
>
> - Updated
>
> [Follow](https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages-/subscription.html)
>
> | Language   | Version             | Notes                                                        |
> | ---------- | ------------------- | ------------------------------------------------------------ |
> | C++        | clang 9             | Uses the C++17 standard.                                     |
> | Java       | java 13.0.1         | Includes `Pair` class, with documentation at https://docs.oracle.com/javase/8/javafx/api/javafx/util/Pair.html |
> | Python     | python 2.7.12       | For Map/TreeMap data structure, you may use [sortedcontainers](http://www.grantjenks.com/docs/sortedcontainers/) library. |
> | Python3    | Python 3.8          | For Map/TreeMap data structure, you may use [sortedcontainers](http://www.grantjenks.com/docs/sortedcontainers/) library. |
> | MySQL      | mysql-server 5.7.21 |                                                              |
> | MS SQL     | mssql 14.0.3        |                                                              |
> | Oracle     | Oracle SQL 11.2     |                                                              |
> | C          | gcc 8.2             | For hash table operations, you may use [uthash](https://troydhanson.github.io/uthash/). `"uthash.h"` is included by default. |
> | C#         | mono 5.18.0         | Run with `/debug` flag, with [full support for C# 7](https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-7). |
> | JavaScript | nodejs 10.15.0      | Run with `--harmony` flag, enabling [new ES6 features](http://node.green/). [lodash.js](https://lodash.com/) library is included by default. |
> | Ruby       | ruby 2.4.5          |                                                              |
> | Bash       | bash 4.3.30         |                                                              |
> | Swift      | swift 5.0.1         |                                                              |
> | Go         | go 1.13             |                                                              |
> | Scala      | Scala 2.13          |                                                              |
> | Kotlin     | Kotlin 1.3.10       |                                                              |
> | Rust       | 1.40.0              | edition = 2018, supports [rand](https://crates.io/crates/rand) from crates.io |
> | PHP        | PHP 7.2             |                                                              |
>
> 



ref: https://leetcode.com/discuss/general-discussion/452863/how-do-you-deal-with-no-treeset-or-treemap-in-python

> There are quite a few problems that can use TreeSet or TreeMap, but it seems python does not have anything? Any tips on how to deal with this. Recently switched over from java to pyhton
>
> 
>
> https://leetcode.com/problems/the-skyline-problem/ -> Needs removal O log(n)
> https://leetcode.com/problems/k-empty-slots/ -> TreeMap is a accepted solution
>
> 
>
> Thanks,
> Uv
>
> Comments: 1
>
> BestMost VotesNewest to OldestOldest to Newest
>
> Preview
>
> Post
>
> [![LeetCode's avatar](https://tva1.sinaimg.cn/large/007S8ZIlgy1gejri4cfqej305k05kmx8.jpg)](https://leetcode.com/leetcode)
>
> [LeetCode](https://leetcode.com/leetcode)Admin3460
>
> December 17, 2019 9:45 AM
>
> Read More
>
> https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages-
>
> 
>
> Please take a look at the environments for the programming languages above. For Python you may use [sortedcontainers](http://www.grantjenks.com/docs/sortedcontainers/) library for TreeSet/TreeMap data structure.

