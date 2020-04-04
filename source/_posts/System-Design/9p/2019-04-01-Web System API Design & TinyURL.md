---
layout: post
categories: SystemDesign
tag: []
date: 2019-04-01
---





> ##### [单选题]www.net.cn 的根域名（不含后缀）是什么？
>
> A.net72.88% 选择
>
> B.www27.12% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是A
>
> **正确答案:**B
>
> **解析:**
>
> www.net.cn 是一个 .net.cn 为后缀的域名，而不是一个 .cn 为后缀的域名。意不意外，惊不惊喜！



## Basics & Flows

網站開發：

跑通流程

申域名、綁ip地址、在AWS買server、在上面跑http server (Apache; Unicorn, Gunicorn; Uwsgi 都ok) 、用任一個框架 flask, django 搭起網站，搭個todo list就OK、message queue搭起來。



> - 可以认为web server 是由http server和web application组成吗？感觉当我们访问了google.com的时候，是这样的流程：浏览器URL->DNS服务器(http request)->Http Server(可以认为是SpringMVC里的DispatcherServlet吗) -> Web App(可以认为是SpringMVC里的Controller吗？就是找到对应哪个action进行处理这个请求)。不好意思对于这些概念和spring mvc都不是很理解，希望助教能指正
>
>   - HTTP Server 不是 Spring 里的任何东西。Web App 才是 Spring。HTTP Server 一般是在 Web APP 的前面会配置起来用作控制 Web App 多进程并发的一个软件，一般典型代表是 UWSGI, Unicorn 这种。你所知道的 Spring 的任何概念，都属于一个 Web App 里的一部分。
>
> - 我除了GET以外的操作（例如PUT和DELETE的操作）都使用POST Method是不是就可以了呢（操作类别通过url或parameter区分）？
>
>   - 一般的Rest API设计规范是要求POST, DELETE, GET, PUT，分别对应增删查改，符合规范会让别人更容易理解你的接口。你说的方法虽然也可以，但是不符合Rest的规范。
>
> - web application在哪里运行的呢？听说用docker来deploy web application，这个是执行application的地方吗？
>
>   - web application 可以在 docker 里执行。 docker 的概念可以理解为在 Operating System 上包装出来的一个独立的小 operating system。其实 web application 就是跑在操作系统上的，可以是 linux，可以是 windows。因为 web application 就是一个程序，一个进程。代码该在什么地方执行就在什么地方执行。
>
> - 请问，Async Server和Web Server在功能上的区别是什么？ 是否Web server一般用来接收用户的request和跑web application，而Async Server就是用来存储message queue的呢？
>
>   - 在News Feed Push model的senario中，fanout本质上是一个写扩散的过程。
>     （1）Web Server主要是接受用户请求并dispatch到不同的wap app经controller直至具体某个处理特定businesslogic的service上。
>     （2）Async server的作用就是从这个人（明星）中frenship service中找到其相应的followers(粉丝)然后，对每一个follower用户对应的news_feed_table[id, owner_id, tweet_id, create]写入相关的记录，这样用户登录使用时就能看到news feeds。
>     如果存储的表(tweet_table, news_feed_table)都在都在同一个数据，那么这个写扩散的过程，其实就是在同一个数据库中创建相应的触发器(trigger)、存储过程(procedure)和定时执行作业，就能实现。
>     但是如果在不同的地理分布位置，而且follower数据量庞大，那么就要借助中间件(message queue)来完成, 利用中间件message queue是采用生产者与消费者的模式实现的publish/subscribe的技术，保证把每一个发布的（tweet）信息，准确返送到每一个subsrriptio端的consumer来完成消息的写扩散（fan out）过程。具体的messge queue的理解请阅读维基百科相关内容https://bit.ly/2kwnxNl, message queue具体实现场景，请阅《蚂蚁金服：消息队列事务型消息原理浅析》https://bit.ly/2lAJOKe
>
>     显示我



## API Design



> ##### [单选题]以下API设计哪个是对的？
>
> API用于获取当前登录用户在题号1000这个题上的所有提交记录
>
> A./api/users/<current_user_id>/submissions/?problem_id=100017.61% 选择
>
> B./api/users/me/submissions/?problem_id=10006.82% 选择
>
> C./api/submissions/?problem_id=1000&user_id=<current_user_id>33.28% 选择
>
> D./api/submissions/?problem_id=100032.01% 选择
>
> E./api/problems/1000/submissions/10.28% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是D
>
> **正确答案:**D

A、B、C不科學，別人可以查自己哦？

E不對, D才符合REST API的約束、規範，一級目錄要是自己要獲取的東西

![image-20200404003659176](https://tva1.sinaimg.cn/large/00831rSTgy1gdh1w428fgj30p419sq94.jpg)



## REST API

> - post request 推荐 return 什么信息最好
>   - it depends。创建一个 instance 一般就 return 这个 instance 的json。
> - get all accounts 呢？
>   - get /api/accounts/?filter=xxx&sort_by=xxx
> - 请问加header 和 加parameter 的区别是什么
>   - 一般验证信息，身份信息会放在 header 里。其他的普通参数放在 parameter 里。
> - 是否header里面的参数是加密的 而url parameter没有加密？
>   - 是可以的，比如在Post/Put/Del的Rest Method中就是在message header中存放加密的Authentication信息（即token内容），在url的参数则是具体操作对象的id值等path variable。



## News Feed API

### Req & Res

> - JSON 和XML 是两种格式。HTTP URL 里的路径不对应文件夹。URL和文件 path 是不同的概念。文件path的是对应有 folder 才行，url 可以随意指定，不一定要有真实的 folder 或者文件与之对应。同一份数据是不需要存两份的，一般都是存在数据库的表单里，如果你需要 JSON 的格式，就组织成 JSON 的格式返回，如果需要 XML 就组织成 XML 的格式返回。



### Pagination

> - ##### [单选题]哪种分页方法更加适合 News Feed？
>
>   A.页码翻页（Page Number）14.95% 选择
>
>   B.光标翻页（Cursor）85.05% 选择
>
>   ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
>   **正确答案:**B

要注意怎麼去避免空白頁的request

秀出100個的話就拿101個！

> - 使用max_id的话，如果用户删除了之前的某一个item，这样不还是会出现第二页出现之前第一页的item吗
>
>   - 不会有影响的。比如第一页的帖子是 `[10, 9, 8]` 第二页是 `[7, 6, 5]`，用户拿到第一页以后，同时得到的 next page max_id 是 7。即便此时用户删除了 10 这个帖子，依然不影响 通过 max_id = 7 拿到的是 7 6 5。如果用户删除了 7 这个帖子，那拿到的就是 `[6, 5, 4]` 也是没有问题的。
>
> - 能不能更具体地讲讲光标翻页的实现。举个例子，一共3页，客户端需要传什么数据给后台，首页，中间和末页。
>
>   - 问：**是不是不管push还是pull模型，如果翻页的话都得pull?**
>     翻页是用户主动操作的过程，所以肯定是由client 发给 server，肯定是一个pull的过程。
>
>     问：**假设前100条中最早的timestamp是T，就分别请求follow的人在T之前的100条feed，然后再进行合并？**
>     答：对
>
>     问：**如果恰好有几条feed的timestamp一样该如何处理？**
>     答：首先不会有帖子的timestamp一样，timestamp的精度很高的（微秒级别）
>
>     通常来说，翻页这个完全可以作为一道单独的系统设计面试题来问你。翻页并不是简单的1-100，101-200这样去翻页。因为当你在翻页的时候，你的news feed可能已经添加了新的 内容，这个时候你再去索引最新的101-200可能和你的1-100就有重叠了。
>
>     通常的做法是，拿第101个帖子的timestamp作为下一页的起始位置，也就是说，当用户在看到第一页的前100个帖子的时候，他还有第101个帖子的timestamp信息（隐藏在你看不到的地方），然后你请求下一页的时候，会带上这个timestamp的信息，server端会去数据库里请求 >= timestamp 的前101个帖子，然后也同样把第101个帖子作为下一页的timestamp。这个方法比直接用第100个帖子的timestamp好的地方是，你如果读不到第101个帖子，说明没有下一页了，如果你刚才只有100个帖子的话，用第100个帖子的timestamp的坏处是，你会有一次`空翻`。
>
>     留给你一个思考题：怎么实现往上翻页（刷朋友圈，查看最新的帖子）
>
>     - 可以利用和向下翻页类似的方法，用当前第一条feed的时间T去数据库取T之后的feeds。
>       如果是pull模型的话，就去所有follow的人的feed list去取然后merge
>       push的话，去直接去queue里面取时间大于T的就好了



> - ##### [单选题]如果 Post 存储在 NoSQL 中，没有 Sequential ID，还可以使用光标翻页法么？
>
>   Sequential ID 是递增的，可以通过 max_id 和 min_id 来筛选。但是如果在 NoSQL 中，ID 是 UUID ，这个是完全无序的字符串，并不是后发的帖子 UUID 就会比先发的帖子 UUID 大。
>
>   A.用不了5.06% 选择
>
>   B.可以用，用 timestamp 之类的有序信息翻页即可94.94% 选择
>
>   ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
>   **正确答案:**B
>
>   **解析:**
>
>   timestamp 的精度是微妙级别的，是足够的，一个人的朋友圈里有两个人在同一个 timestamp 发了帖子的概率几乎为0。如果你还是担心 timestamp 的精度不够的话，一个简单的办法是 + 一个随机后缀，如 timestamp 取出来到微妙是 `1554553786168125` 的话，后面填 5 位随机整数如`13234`，凑成 `155455378616812513234`。当然存储的时候类型上得是 bigint 了，因为很大。不可以用 float / double 存储，精度不够。



### Mentions

讓前端拿到時候可以顯示成可以llink的樣式