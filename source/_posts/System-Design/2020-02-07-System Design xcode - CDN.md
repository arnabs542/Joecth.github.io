---
layout: post
categories: System
tag: [] 
date: 2020-02-07
---

### 

# CDN

CDN　content distributed network，也是緩存，更像file system。縣到市市到省

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ghxfthrialj30rs0ff3zy.jpg" alt="img" style="zoom:67%;" />





- 一般是租用全球的，會把同個file replicate 到各個server，fewer hops

- 如果miss了會一層層往上要，最後到orig server



> A content delivery network (CDN) is a globally distributed network of proxy servers, serving content from locations closer to the user. Generally, static files such as HTML/CSS/JS, photos, and videos are served from CDN, although some CDNs such as Amazon's CloudFront support dynamic content. The site's DNS resolution will tell clients which server to contact.
>
> Serving content from CDNs can significantly improve performance in two ways:
>
> - Users receive content from data centers close to them
> - Your servers do not have to serve requests that the CDN fulfills

愈近愈快，網路傳輸很常是很大的bottleneck，netflix有個經典問題，話題帶到如算法優化時，跟disk的io、network的io不值一提哈。

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ghxg0wj7fkj30y40gsnab.jpg" alt="image-20200820181620952" style="zoom:50%;" />



一般而言readability比runtime更重要！因為在實際工作中，網路、disk的latency遠超過算法的runtime。

Q-select就剩個幾個nano seconds，在系統設計面前不值得一提…。



## 補充：

### 秒殺

系統忙不過來，所以商品介紹可以放靜態file在cdn好處理高併發

### Youtube/Netflix

分佈在世界各地、按geolocation，把比較hot的放在cdn，用戶可以放在local cdn去取，會更好



## Push CDNs

> Push CDNs receive new content whenever changes occur on your server. You take full responsibility for providing content, uploading directly to the CDN and rewriting URLs to point to the CDN. You can configure when content expires and when it is updated. Content is uploaded only when it is new or changed, **minimizing traffic, but maximizing storage**.
>
> Sites with a small amount of traffic or sites with content that isn't often updated work well with push CDNs. Content is placed on the CDNs once, instead of being re-pulled at regular intervals.

如果file 內容更新了，得要去告訴cdn server更新，或是就設expire，如cache miss時的情況，如沒找到或expire時沒找到

更新會主動 Push Client，而不是不斷去拿；**但一般是Pull比較多**。

![image-20200820181656677](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghxg1ie3myj30vi0jyn5m.jpg)

![image-20200820181534739](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghxg03u9ggj30vu0k2alt.jpg)



## PULL CDNs

> Pull CDNs grab new content from your server when the first user requests the content. You leave the content on your server and rewrite URLs to point to the CDN. This results in a slower request until the content is cached on the CDN.
>
> A [time-to-live (TTL)](https://en.wikipedia.org/wiki/Time_to_live) determines how long content is cached. Pull CDNs minimize storage space on the CDN, but can create redundant traffic if files expire and are pulled before they have actually changed.
>
> Sites with heavy traffic work well with pull CDNs, as traffic is spread out more evenly with only recently-requested content remaining on the CDN.



- 不斷地pull要是它沒有expire就白pull了。





## Disadvantage(s): CDN

一般不會那麼複雜

一般就是第三方全球性的，自己小公司做不到。

- CDN **costs** could be significant depending on traffic, although this should be weighed with additional costs you would incur not using a CDN.  -- 租別人要花錢；有時不一定要用，貴呀
- Content might be stale if it is updated before the TTL expires it.  -- 我們一般操作會給file設TTLE，有可能TTL還沒有過期，但我更新了源頭的file了，但本地的CDN還沒有expire它，這時去讀到的CDN就是個stale的，不是最新的版本，因為我還沒讓它過期，我以為它是最新的，但它實際不是最新的。
- CDNs require changing URLs for static content to point to the CDN.  -- 我拿CDN時每個file都會有個unique的URL，我要是新的話，我得去改URL，後綴什麼的，畢竟就是不同的FILE了呀。一般可能加個參數如timestamp或版本什麼的，browser會以為是不同的URL，讓cache失效，如在URL後面加  **?v=1&t=2** 這類的，其實就是說URL我必須要改到，去point到新的CDN的file。
- dropbox就要跟file相關啦!

