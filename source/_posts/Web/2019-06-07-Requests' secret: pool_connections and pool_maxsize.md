---
layout: post
categories: Web
date: 2019-06-07
tag: [] 




---



from: https://www.cnblogs.com/pengyusong/p/5802929.html

and https://laike9m.com/blog/requests-secret-pool_connections-and-pool_maxsize,89/



# **Requests' secret: pool_connections and pool_maxsize**

[Requests](http://docs.python-requests.org/en/latest/) 是一个python开发者众所周知的第三方库。因其简单的API和高性能，大多数人倾向于使用requests而不是urllib2作为访问http的标准库。然而很多使用requests库的人可能不知道内部原因，今天我就来解释以下俩个概念: `pool_connections` 和`pool_maxsize`.

从 `Session 开始`:

```python
import requests

s = requests.Session()
s.get('https://www.google.com')
```

这很简单，你可能知道requests' `Session` 持有cookie. 但你知道 `Session` 有一个 [`mount`](http://docs.python-requests.org/en/latest/api/#requests.Session.mount) 方法吗?

> `mount(prefix, adapter)`
> Registers a connection adapter to a prefix.
> Adapters are sorted in descending order by key length.

不知道？很好，实际上你已经使用了这个方法当你初始化一个session对象时:

```python
class Session(SessionRedirectMixin):

    def __init__(self):
        ...
        # Default connection adapters.
        self.adapters = OrderedDict()
        self.mount('https://', HTTPAdapter())
        self.mount('http://', HTTPAdapter())
```

现在，到了有趣的部分。如果你阅读过 Ian Cordasco's 文章 [Retries in Requests](http://www.coglib.com/~icordasc/blog/2014/12/retries-in-requests.html), 你应该知道 `HTTPAdapter` 可以提供重试功能. 但一个 `HTTPAdapter` 真实是什么? Quoted from [doc](http://docs.python-requests.org/en/latest/api/#requests.adapters.HTTPAdapter):

> ```python
> class requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=0, pool_block=False)
> ```
>
> The built-in HTTP Adapter for urllib3.
>
> Provides a general-case interface for Requests sessions to contact HTTP and HTTPS urls by implementing the Transport Adapter interface. This class will usually be created by the Session class under the covers.
>
> Parameters:
>
> - `pool_connections` – The number of urllib3 connection pools to cache.
> - `pool_maxsize` – The maximum number of connections to save in the pool.
> - `max_retries(int)` – The maximum number of retries each connection should attempt. Note, this applies only to failed DNS lookups, socket connections and connection timeouts, never to requests where data has made it to the server. By default, Requests does not retry failed connections. If you need granular control over the conditions under which we retry a request, import urllib3’s Retry class and pass that instead.
> - `pool_block` – Whether the connection pool should block for connections. Usage:
>
> ```python
> >> import requests
> >> s = requests.Session()
> >> a = requests.adapters.HTTPAdapter(max_retries=3)
> >> s.mount('http://', a)
> ```

如果上面的文档使你迷惑，这里是我的解释: HTTP Adapter 所做的就是：根据不同的目标url，对每个不同的请求提供不同的配置，还记得上面的代码吗？

　　　　what HTTP Adapter does is simply **providing different configurations for different requests according to target url**. Remember the code above?

```python
self.mount('https://', HTTPAdapter())
self.mount('http://', HTTPAdapter())
```

它创建了俩个 `HTTPAdapter` 对象使用默认的参数：`pool_connections=10, pool_maxsize=10, max_retries=0, pool_block=False`, 并且挂载到 `https://` 和 `http:// 相对路径`, 意思是第一个配置在你访问 `http://xxx 会使用到， 第二个会在你访问 ``https://xxx`. 尽管上面俩个配置是相同的，请求http和https仍然是隔离的。我们会在下面看到说明。

就像我说的，这篇文章的目的主要是解释 `pool_connections` and `pool_maxsize`.

首先，让我们看看 `pool_connections`. 昨天我在stackoverflow提出了一个问题：[question](http://stackoverflow.com/questions/34837026/whats-the-meaning-of-pool-connections-in-requests-adapters-httpadapter) ，因为我不确定我是否理解正确，这个问题的回答消除了我的不确定性。HTTP，众所周知，是基于TCP协议，一个HTTP连接也是一个TCP连接，它是由一个五元组唯一标识:

```react
(<protocol>, <src addr>, <src port>, <dest addr>, <dest port>)
```

就是说，你针对 `www.example.com 建立了一个HTTP/TCP连接`, 假设服务器支持 `Keep-Alive`, 下一次你发送请求到 `www.example.com/a` or `www.example.com/b`, 你可以使用相同的连接，因为五元组没有改变. 实际上, [requests' Session 自动会帮你处理](http://docs.python-requests.org/en/latest/user/advanced/#keep-alive) 并且重用连接，只要它能.

这个问题是，什么决定了你是否可以重用老的连接？是的，就是 `pool_connections`!

> pool_connections – The number of urllib3 connection pools to cache.

我知道，我知道，我也不想引入很多术语, 这是最后一个，我发誓. 简单的理解它， 一个host对应的一个连接池：**one connection pool corresponds to one host**, 嗯，就是这个意思.

这是一个例子，无关的行已被忽略:

```bash
s = requests.Session()
s.mount('https://', HTTPAdapter(pool_connections=1))
s.get('https://www.baidu.com')
s.get('https://www.zhihu.com')
s.get('https://www.baidu.com')

"""output
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): www.baidu.com
DEBUG:requests.packages.urllib3.connectionpool:"GET / HTTP/1.1" 200 None
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): www.zhihu.com
DEBUG:requests.packages.urllib3.connectionpool:"GET / HTTP/1.1" 200 2621
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): www.baidu.com
DEBUG:requests.packages.urllib3.connectionpool:"GET / HTTP/1.1" 200 None
"""
```

`HTTPAdapter(pool_connections=1)` 被映射到 `https://`, 他意思是在同一时间仅有一个连接池. 在调用 `s.get('https://www.baidu.com')`, 缓存的连接池是 `connectionpool('https://www.baidu.com')`. 现在 `s.get('https://www.zhihu.com')` 来了，这个session发现他不能使用缓存的连接，因为他不是相同的host(one connection pool corresponds to one host, remember?). 因此session不得不创建一个新的连接池. 因为 `pool_connections=1`, session不能在同一时间持有俩个连接池, 因此他丢弃了旧的连接池： `connectionpool('https://www.baidu.com')` 并且保存了新的：`connectionpool('https://www.zhihu.com')`. 下一次get同样如此Next `get` is the same. 这就是我们看见三个 `Starting new HTTPS connection` 日志行的原因

如果我们设置 `pool_connections` 为 2:

```bash
s = requests.Session()
s.mount('https://', HTTPAdapter(pool_connections=2))
s.get('https://www.baidu.com')
s.get('https://www.zhihu.com')
s.get('https://www.baidu.com')
"""output
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): www.baidu.com
DEBUG:requests.packages.urllib3.connectionpool:"GET / HTTP/1.1" 200 None
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): www.zhihu.com
DEBUG:requests.packages.urllib3.connectionpool:"GET / HTTP/1.1" 200 2623
DEBUG:requests.packages.urllib3.connectionpool:"GET / HTTP/1.1" 200 None
"""
```

很好，现在我们可以创建连接俩次了并且保持连接活跃

最后, `pool_maxsize`.

首先, 仅当你在多线程环境下使用session，你才应该关心 `pool_maxsize` , 例如，从多个线程使用同一个session发出并发请求.

实际上，`pool_maxsize` 是一个用来初始化urllib3's `HTTPConnectionPool的参数`, 它才是真正含义上的连接池. `HTTPConnectionPool` 是一个容器，针对于特定的host保存连接的集合, 且 `pool_maxsize` 是这个集合的最大值. 如果你运行你的代码在同一个线程，它是不可能针对多个主机创建多个连接的，因为 requests library 是阻塞的, 因此HTTP请求总是一个接着一个发送.

如果使用多线程就会不一样.

```bash
def thread_get(url):
    s.get(url)

s = requests.Session()
s.mount('https://', HTTPAdapter(pool_connections=1, pool_maxsize=2))
t1 = Thread(target=thread_get, args=('https://www.zhihu.com',))
t2 = Thread(target=thread_get, args=('https://www.zhihu.com/question/36612174',))
t1.start();t2.start()
t1.join();t2.join()
t3 = Thread(target=thread_get, args=('https://www.zhihu.com/question/39420364',))
t4 = Thread(target=thread_get, args=('https://www.zhihu.com/question/21362402',))
t3.start();t4.start()
"""output
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): www.zhihu.com
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (2): www.zhihu.com
DEBUG:requests.packages.urllib3.connectionpool:"GET /question/36612174 HTTP/1.1" 200 21906
DEBUG:requests.packages.urllib3.connectionpool:"GET / HTTP/1.1" 200 2606
DEBUG:requests.packages.urllib3.connectionpool:"GET /question/21362402 HTTP/1.1" 200 57556
DEBUG:requests.packages.urllib3.connectionpool:"GET /question/39420364 HTTP/1.1" 200 28739
"""
```

看见了吗? 它为相同的host建立了俩个连接： `www.zhihu.com`, 就像我说的, 这个仅发生在多线程环境下. 在这个例子中，我们创建了一个连接池，使用了参数 `pool_maxsize=2`, 发现同一时间不会超过俩个连接，因此这是足够的，我们看到`t3` 和 `t4` 没有创建新的连接，他们重用了就的连接.

如果没有足够的大小呢?

```bash
s = requests.Session()
s.mount('https://', HTTPAdapter(pool_connections=1, pool_maxsize=1))
t1 = Thread(target=thread_get, args=('https://www.zhihu.com',))
t2 = Thread(target=thread_get, args=('https://www.zhihu.com/question/36612174',))
t1.start()
t2.start()
t1.join();t2.join()
t3 = Thread(target=thread_get, args=('https://www.zhihu.com/question/39420364',))
t4 = Thread(target=thread_get, args=('https://www.zhihu.com/question/21362402',))
t3.start();t4.start()
t3.join();t4.join()
"""output
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): www.zhihu.com
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (2): www.zhihu.com
DEBUG:requests.packages.urllib3.connectionpool:"GET /question/36612174 HTTP/1.1" 200 21906
DEBUG:requests.packages.urllib3.connectionpool:"GET / HTTP/1.1" 200 2606
WARNING:requests.packages.urllib3.connectionpool:Connection pool is full, discarding connection: www.zhihu.com
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (3): www.zhihu.com
DEBUG:requests.packages.urllib3.connectionpool:"GET /question/39420364 HTTP/1.1" 200 28739
DEBUG:requests.packages.urllib3.connectionpool:"GET /question/21362402 HTTP/1.1" 200 57556
WARNING:requests.packages.urllib3.connectionpool:Connection pool is full, discarding connection: www.zhihu.com
"""
```

现在, `pool_maxsize=1`，会打印警告日志如下，就像下面的:

```
Connection pool is full, discarding connection: www.zhihu.com
```

可以注意到仅有一个连接被保存在连接池中, 为t3或者t4创建一个新的连接. 很明显这是不够的. 这就是为什么在 urllib3's 文档中说明如下:

> 如果你计划在连接池环境下使用一个连接池, 你应该设置连接池最大数量为一个比较高的值，例如和线程的数量相同.

最后, `HTTPAdapter` 实例映射到不同的前缀是相互独立的.

```bash
s = requests.Session()
s.mount('https://', HTTPAdapter(pool_connections=1, pool_maxsize=2))
s.mount('https://baidu.com', HTTPAdapter(pool_connections=1, pool_maxsize=1))
t1 = Thread(target=thread_get, args=('https://www.zhihu.com',))
t2 =Thread(target=thread_get, args=('https://www.zhihu.com/question/36612174',))
t1.start();t2.start()
t1.join();t2.join()
t3 = Thread(target=thread_get, args=('https://www.zhihu.com/question/39420364',))
t4 = Thread(target=thread_get, args=('https://www.zhihu.com/question/21362402',))
t3.start();t4.start()
t3.join();t4.join()
"""output
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): www.zhihu.com
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (2): www.zhihu.com
DEBUG:requests.packages.urllib3.connectionpool:"GET /question/36612174 HTTP/1.1" 200 21906
DEBUG:requests.packages.urllib3.connectionpool:"GET / HTTP/1.1" 200 2623
DEBUG:requests.packages.urllib3.connectionpool:"GET /question/39420364 HTTP/1.1" 200 28739
DEBUG:requests.packages.urllib3.connectionpool:"GET /question/21362402 HTTP/1.1" 200 57669
"""
```

上面的代码很容易，不需要再次解释了.

就这样了，希望这篇文章帮助你更好的理解requests库. 顺便说一下，我创建了一个gist [here](https://gist.github.com/laike9m/ead19c65a416c7022c00) 这里包含这篇文章的测试代码. 随便下载并尝试吧

## Appendix

1. For https, requests uses urllib3's [HTTPSConnectionPool](http://urllib3.readthedocs.org/en/latest/pools.html#urllib3.connectionpool.HTTPSConnectionPool), but it's pretty much the same as HTTPConnectionPool so I didn't differeniate them in this article.

2. `Session`'s `mount` method ensures the longest prefix gets matched first. Its implementation is pretty interesting so I posted it here.

   ```python
   def mount(self, prefix, adapter):
       """Registers a connection adapter to a prefix.
       Adapters are sorted in descending order by key length."""
       self.adapters[prefix] = adapter
       keys_to_move = [k for k in self.adapters if len(k) < len(prefix)]
       for key in keys_to_move:
           self.adapters[key] = self.adapters.pop(key)
   ```

   Note that `self.adapters` is an `OrderedDict`.