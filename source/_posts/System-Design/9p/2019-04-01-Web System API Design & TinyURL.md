---
layout: post
categories: SystemDesign
tag: []
date: 2019-04-01
---



# General 



## Web Framework

- 登錄, session, cookies

- CSRF攻擊 - Cross-site Request Forgery 如果拿的link是建數據的post請求，現在也是server會給browser一個CSRF token，去防無效token。
  - python - django，flask輕巧要裝一堆插件，把密碼md5哈希，現在是SHA256
  - java - spring
  - ruby - ruby on rail

- ORM 

- 登入登出

- **http server** is between user and web framwork, 管理多進程。
  - Uwsgi 多進程啟多個Django的進程，服務如100個用戶就自己刪了重啟之類
  - Apache
  - Unicorn
  - Gunicorn
  - Nginx 不同網站去不同站口避免打架



# APIs

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

> - 不是说返回的是Json么？这里为什么是HTML？
>
>   - 总体的数据是 JSON 的，这里的 html 是其中的某个数据的值。比如：
>
>     ```json
>     {
>        "title": "hello",
>     	 "content": "<html>hello world</html>"
>     }
>     ```
>
> - mobile的格式是什么样子的？
>
>   - API 返回给 mobile 的格式通常就是 JSON 格式，直接只有具体的数据内容。如
>
>     ```json
>     {
>        "content": "Thanks to <user username='someone'>hello world</user>",
>     	 ...
>     }
>     ```



# TinyURL

eg. bitly.com/, goo.gl/

## Scenario

就是創一個post請求，建一個短網址

給了一個301跳轉，讓browser去完成跳轉的動作。

- 長跟短的URL要是一一對應嗎？

> ##### [单选投票题]Long Url 和 Short Url 是否需要一一对应？
>
> 您选择的答案是B
>
> 感谢您参与投票！
>
> A.需要41.63% 选择
>
> B.不需要58.37% 选择

> ##### [单选投票题]Short Url 长时间不用是否需要释放？
>
> 您选择的答案是B
>
> 感谢您参与投票！
>
> A.需要58.08% 选择
>
> B.不需要41.92% 选择

這兩個是開放的問題

不同的設計有不同的體驗。各有好壞處。

沒釋放出去就存disk，又不占什麼空間，又便宜。



## QPS

是否是真需要很多的機器？

ave QPS = 日活跃*每个用户平均请求次数/一天多少秒

系統一般不是特別頻繁

QPS這問題跟Storage都還好。



## Service

就陽春一個而已



## Storage

> ##### [单选题]TinyUrl 用什么类型的数据库比较合适？
>
> A.SQL / 关系型数据库10.37% 选择
>
> B.NoSQL / 非关系型数据库17.76% 选择
>
> C.都可以，取决于算法是什么71.88% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是B
>
> **正确答案:**C
>
> **解析:**
>
> 如果你需要用 Auto-increment ID，就用关系型数据库，否则可以用非关系型数据库，操作更简单一些。

> - 为什么sql比nosql要写的代码少呢？
>   - 因为很多的 web framework，调用 SQL 部分的接口什么的代码都帮你写得很丰富，很多事儿你也都不用管。很多 NoSQL 的调用，包括 Serialization 之类的事情程序员都需要额外的代码去做。所以会长一些。
> - 除了seq id，还有什么方法确保两个不同的longUrl 得到不同的shorturl呢
>   - 还可以随机生成一个 shortUrl 然后用数据库来判断用过没有，用过就再生成一个。



## Alg.

- HASH --> 再好的也會有conflict; md5本身就有，更不用說基於它再取６位
- 隨機生成再去DB去重

> ##### [多选题]下面哪些“码”可能是随机生成+数据库去重的？
>
> A.短信验证码20.86% 选择
>
> B.邮箱激活码21.60% 选择
>
> C.酒店订单确认码28.84% 选择
>
> D.机票订单确认码28.70% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是ABCD
>
> **正确答案:**CD
>
> **解析:**
>
> 验证码和激活码没有去重的需求。订单确认码才有去重的需求。

驗證碼一下就過期了。訂單本身碼很長，所以有確認碼跟客服比較好溝通。

> - sequential id vs. non-sequential id 是怎么用的？ 为什么很重要？
>
>   - sequential id就是关系型数据库中每增加一行系统会自动给这一行数据分配一个自增id，这样可以保证每一行的id递增且不重复。如果id是随机生成的而不是有顺序的那就叫non sequenctial id，一般需要手动生成。
>
> - 随机生成函数是什么？可以具体讲讲么
>
>   - 比如这样：
>
>     ```
>     ''.join([for i in range(6) random.choice("ABCDEF")])
>     ```
>
>     这段python 代码就是一个 for 循环，循环6次，每次从一个字符串里随机挑一个字符出来。这样就随机生成了一个 6位的code。
>
> - 不是说Hash的冲突概率很小吗?
>   - Hash冲突小的前提是，获得的 hashcode 的长度要足够长，一般生产的类似 UUID 这样的 hash 值，好几十位字符串，这样才不会冲突。只有6位字符很容易冲突。
> - 算法二除了速度慢外，如要处理并发问题吗，如果需要，如何处理？加锁吗？谢谢
>   - 不需要做任何代码的修改。不需要加锁。并发没有问题。首先就算并发，两个 process 调用了 Random 函数之后得到的也是不同的随机串，冲突的概率很小。第二，就算有冲突，数据库也会进行加锁保证不会出现2个重复的被插入。第三如果因为 Race Condition 的原因，刚好会向数据库里插入两次一样的 short_key 的话，那么可以设置 short_key 是 unique 的，然后其中一次 fail 掉，报错给用户，用户重试一次即可解决问题。
> - 感觉可以随机生成10个candidate 然后batch query。这样就可以最大限度避免DDB read。
>   - 这样是不对的。相当于你为了解决一个1%的case，降低了 99% 的case的运行效率。
> - database.filter(shortURL)不会很慢么？
>   - 不会，shortUrl有index。
> - 进制转换的方法是如何把longUrl 转换成 shortUrl的呢？
>   - 将 long url 插入 database, 拿到 auto-increment id (sequential id)
>   - 将 id 进制转换得到 shortUrl
> - sequential ID数据类型是整型啊？
>   - 是的，整数。要不然做不到 sequential。sequential id 又叫做 auto-increment id
> - 那如果有人用同样的longUrl要求做shortUrl, 是会每次返回不一样的shortUrl么？
>   - 相同的 longUrl 可以先查一下是否有和这个 longUrl对应的 shortUrl。查询的办法一方面可以通过数据库对 longUrl 建立 Index 来加速查询。另外也可以再加上 cache，把 longUrl to ShortUrl 的映射 cache 起来。先查 cache，查不到再去 db 查，这样就更快了。

> [单选投票题]随机生成和进制转换两种算法你认为哪种更好？
>
> 你的选择:A
>
> 感谢您参与投票！
>
> A:随机生成(36.58% 选择)
>
> B:进制转换(63.42% 选择)



## 表單結構＆可行解

### 隨機生成法

​	不好

> - short long，这2个存在sql，哪一个做pk呢？这个是一一对应的么？是说，建了index，就可以用其他column去查pk也是可以的么？
>   - Primary Key 可以用 short，因为一个short 不能用两次，一个long 可以对应多个 short 所以可以存多次。用任意 column 做pk是可以的只要这个column 是 unique 的，不允许重复的。一一对应在课程中有讲到，short 到 long 是 1 short 对应 1 个 long。反过来一个 long 可以对应多个 short。
> - 为了快速查找而对short->long, long->short都建立index，那么index也就要求long url之间不能重复，对吗？如果允许long url重复，也就不能建立log的index
>   - ***好问题！您对 index 的理解有误。 index 是可以有重复的，没有重复的 index 叫做 unique index。SQL 语句里如果你执行 `create index on long_url` 是可以重复的。如果你希望不重复，就`create unique index on long_url`。在 long url 建立 index 的情况下，您可以使用 index filter 出相同的 long_url 记录的第一条记录就可以了。***



## Scale 優化response time

- 提速，讀多的用Cache 優化，可用Cache Aside，存兩個表long2short, and short2long。

- 提速：地理上server靠近訪問地點。或中心化的，靠兩邊都還ok中間的。
  - DNS根據用戶地區給不同的IP去美國的web server找memcached裡的，找不到再去Shared DB。
  - 用戶一次的request等於Web Server對DB一次的請求。
  - 如果Web對DB請求是多次的，那最好吧DB放到跟Server一樣的地方，異地的SErver頂多再來訪問本地的Server，也就一次，這樣Server 對DB的延遲不會被放大。



> - ##### [单选题]TinyUrl 是读多写少还是读少写多？
>
>   A.读多写少94.90% 选择
>
>   B.读少写多5.10% 选择
>
>   ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是A
>
>   **正确答案:**A



> - 两个cache和DB之间的sync怎么解决
>   - 写入一般都是先写db再写cache的，允许cache写入失败，但是db要写入成功。两者之间可以允许不一致
> - **memcached 如何跟shared db sync**
>   - **这个就是典型的cache aside。从shared db读取结果到之后将结果放在memchached，这样再次查询同样的数据就可以直接从cache取。当有数据发生变动的时候，先写数据库，然后delete缓存里面受影响的数据。**
> - 为啥create short url 也需要 memcache？如果使用呢？
>   - 因为create short url要先查询一下当前的long url是否已经有对应的short url了，这个可以查缓存里的long2short信息，如果缓存里有的话就不用创建了，如果缓存里没有再查db里有没有，如果有就直接返回现有的shorturl，如果没有就创建一个新的。



### How to Scale

要是量翻了10倍，怎麼用多台數據庫怎麼去解決TinyURL的架構問題？

- 什麼時候要多台DB Server
  - Cache hit rate小
  - 寫操作比較多 => 無法透過 Cache優化

> ##### [单选题]TinyUrl 最主要要解决的是存不下还是忙不过来？
>
> A.存不下22.14% 选择	Storage
>
> B.忙不过来77.86% 选择　QPS issue
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B



> ##### [单选投票题]Tiny Url 你会选择用什么做 Sharding Key?
>
> 您选择的答案是A
>
> 感谢您参与投票！
>
> A.Long Url17.21% 选择
>
> B.Short Url82.79% 选择

> - 多机随机生成URL算法，如何处理并发问题呢？
>   - 并发没有问题。首先就算并发，两个 process 调用了 Random 函数之后得到的也是不同的随机串，冲突的概率很小。第二，就算有冲突，数据库也会进行加锁保证不会出现2个重复的被插入。第三如果因为 Race Condition 的原因，刚好会向数据库里插入两次一样的 short_key 的话，那么可以设置 short_key 是 unique 的，然后其中一次 fail 掉，报错给用户，用户重试一次即可解决问题。
> - 专门一台db做seq id服务，请问下，db table的schema长什么样子？
>   - schema 里就一个 column 一个数据，就是 last_seq_id，大整数。
> - 有一点想确定一下 最后介绍的base62 sharding key方法是用来解决原本查询需要broadcast的情况 对吧？全局自增ID问题依旧需要有专项服务器处理吧
>   - 是的，你的理解是对的。
> - 用base 62的方法做sharding key, 我们还需要存两份映射吗？
>   - 如果你用 SQL 数据库的话，都 long 和short 都建了 index 就不需要了。通过sharding key找到机器，通过这台机器上的 index 找到具体数据。
> - hash（long_url）就是得到的short url么？
>   - `hash(long_url) % 62`得到的是 short url 的第一位字符
> - 这个并不解决全局自增ID的问题啊？？
>   - 这并没有解决自增id的问题，只是在查询的时候不用broadcast了。要做全局自增id还是需要使用前述方法。
> - 能否在储存shorturl的表单里加入sharding_key，这样就没有62台机器的数量限制了
>   - 在存储shorturl的表单里加入sharding_key的话仍然没有解决查询short2long时需要广播的问题。这里说的方案是把sharding key给embed到shorturl中，因此需要占用一定的shorturl位数。当sharding key占shorturl中的一位的时候就是限定62台机器，占两位的时候就是62 * 62台，只能是在这个占的位数上做trade off。



### Multi Region Optimization

- 數據庫在美、台各地各放一份？
  - 一致性問題難解決
- 可根據網站的地域信息作Sharding ，避免存多份的不一致
  - 域名- 可根據長尾理論作白名單
  - Short url的前置位
  - 大不了跨境需求讓它慢一點

> - db usa 和db cn 如果保持数据一致性？
>   - 不需要保持一致，两边存储的是不一样的数据。DB USA只存属于美国的long2short和short2long，而DB CN是只存中国的long2short和short2long。如果担心分配的shorturl有冲突的话可以给不同的区域分别分配不同的可用shorturl范围。
> - 分布式DB的机器距离变远之后（一个在中国，一个在美国），进行操作所需要的时间会变慢吗？影响大不大？
>   - 会，但是你可以将美国那边近期的热点ur（中国用户最近访问得比较多得美国url)做一个中国本地的cache，这样可以很大程度上减轻这种影响。



## Summary

一般是各方法有自己的優缺、優劣

- TinyURL related 
  - 知乎 http://bit.ly/22FHP5o
  -  The System Design Process http://bit.ly/1B6HOEc
- 用Django搭建一个网站 http://bit.ly/21LApIb
  - 搭建一个tiny url的网站
- Emoji URL
  - http://www.xn--vi8hiv.ws



## Extension



# Q&A

> ![image-20200404230945535](https://tva1.sinaimg.cn/large/00831rSTgy1gdi4zq7rxxj30r80tw783.jpg)

![image-20200404231317707](https://tva1.sinaimg.cn/large/00831rSTgy1gdi53cccn3j30r80tugqk.jpg)

![image-20200404231410186](https://tva1.sinaimg.cn/large/00831rSTgy1gdi548ss55j30qe0o8dil.jpg)

![image-20200404231430477](https://tva1.sinaimg.cn/large/00831rSTgy1gdi54ljrx1j30qe0siwis.jpg)