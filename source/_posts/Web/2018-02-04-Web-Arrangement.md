---
layout: post
categories: Web
tag: [] 

---



### TCP vs UDP

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200205172545061.png" alt="image-20200205172545061" style="zoom:50%;" />

ISO, the International Organization for Standardization

Open System Interconnection Model，

|                          | TCP                                                          | UDP                                                          |
| -----------------------: | :----------------------------------------------------------- | ------------------------------------------------------------ |
|              Acronym for | Transmission Control Protocol                                | User Datagram Protocol or Universal Datagram Protocol        |
|               Connection | Transmission Control Protocol is a connection-oriented protocol. | User Datagram Protocol is a connectionless protocol.         |
|                 Function | As a message makes its way across the [internet](https://www.diffen.com/difference/Internet_vs_World_Wide_Web) from one computer to another. This is connection based. | UDP is also a protocol used in message transport or transfer. This is not connection based which means that one program can send a load of packets to another and that would be the end of the relationship. |
|                    Usage | TCP is suited for applications that require high reliability, and transmission time is relatively less critical. | UDP is suitable for applications that need fast, efficient transmission, such as games. UDP's stateless nature is also useful for servers that answer small queries from huge numbers of clients. |
|   Use by other protocols | HTTP, HTTPs, FTP, SMTP, Telnet                               | DNS, DHCP, TFTP, SNMP, RIP, VOIP.                            |
| Ordering of data packets | TCP rearranges [data](https://www.diffen.com/difference/Data_vs_Information) packets in the order specified. | UDP has no inherent order as all packets are independent of each other. If ordering is required, it has to be managed by the application layer. |
|        Speed of transfer | The speed for TCP is slower than UDP.                        | UDP is faster because error recovery is not attempted. It is a "best effort" protocol. |
|              Reliability | There is absolute guarantee that the data transferred remains intact and arrives in the same order in which it was sent. | There is no guarantee that the messages or packets sent would reach at all. |
|              Header Size | TCP header size is 20 bytes                                  | UDP Header size is 8 bytes.                                  |
|     Common Header Fields | Source port, Destination port, Check Sum                     | Source port, Destination port, Check Sum                     |
|        Streaming of data | Data is read as a byte stream, no distinguishing indications are transmitted to signal message (segment) boundaries. | Packets are sent individually and are checked for integrity only if they arrive. Packets have definite boundaries which are honored upon receipt, meaning a read operation at the receiver socket will yield an entire message as it was originally sent. |
|                   Weight | TCP is heavy-weight. TCP requires three packets to set up a socket connection, before any user data can be sent. TCP handles reliability and congestion control. | UDP is lightweight. There is no ordering of messages, no tracking connections, etc. It is a small transport layer designed on top of IP. |
|        Data Flow Control | TCP does Flow Control. TCP requires three packets to set up a socket connection, before any user data can be sent. TCP handles reliability and congestion control. | UDP does not have an option for flow control                 |
|           Error Checking | TCP does error checking and error recovery. Erroneous packets are retransmitted from the source to the destination. | UDP does error checking but simply discards erroneous packets. Error recovery is not attempted. |
|                   Fields | 1. Sequence Number, 2. AcK number, 3. Data offset, 4. Reserved, 5. Control bit, 6. Window, 7. Urgent Pointer 8. Options, 9. Padding, 10. Check Sum, 11. Source port, 12. Destination port | 1. Length, 2. Source port, 3. Destination port, 4. Check Sum |
|          Acknowledgement | Acknowledgement segments                                     | No Acknowledgment                                            |
|                Handshake | SYN, SYN-ACK, ACK                                            | No handshake (connectionless protocol)                       |





### TCP Keep Alive

刚刚被问到请求头的keep-alive，虽然没能答上来，但回头一查，真是好问题！

【补习ing……】

1、什么是**Keep-Alive模式**？

HTTP协议采用请求-应答模式，有普通的非KeepAlive模式，也有KeepAlive模式。

非KeepAlive模式时，每个请求/应答客户和服务器都要新建一个连接，完成 之后立即断开连接（HTTP协议为无连接的协议）；当使用Keep-Alive模式（又称持久连接、连接重用）时，Keep-Alive功能使客户端到服 务器端的连接持续有效，当出现对服务器的后继请求时，Keep-Alive功能避免了建立或者重新建立连接。

2、如何启用或者关闭**Keep-Alive模式？**

**浏览器发起建议，服务器视情况统一。**

（1）http 1.0中默认是关闭的，如果客户端浏览器支持Keep-Alive，那么就在HTTP请求头中添加一个字段 **Connection: Keep-Alive**，当服务器收到附带有Connection: Keep-Alive的请求时，它也会在响应头中添加一个同样的字段来使用Keep-Alive。这样一来，客户端和服务器之间的HTTP连接就会被保持，不会断开（超过Keep-Alive规定的时间，意外断电等情况除外），当客户端发送另外一个请求时，就使用这条已经建立的连接。

也有可能是Keep-Alive

```text
Keep-Alive: timeout=5, max=100
timeout：过期时间5秒（对应httpd.conf里的参数是：KeepAliveTimeout），max是最多一百次请求，强制断掉连接
```



（2）http 1.1中默认启用Keep-Alive， 默认情况下所在HTTP1.1中所有连接都被保持，除非在请求头或响应头中指明要关闭：Connection: Close ，这也就是为什么Connection: Keep-Alive字段再没有意义的原因。另外，还添加了一个新的字段Keep-Alive:，因为这个字段并没有详细描述用来做什么，可忽略它



目前大部分浏览器都是用http1.1协议，也就是说默认都会发起Keep-Alive的连接请求了，所以是否能完成一个完整的Keep- Alive连接就看服务器设置情况。

3、启用Keep-Alive的优点

从上面的分析来看，启用Keep-Alive模式肯定更高效，性能更高。因为避免了建立/释放连接的开销。下面是RFC 2616 上的总结：

（1）TCP连接更少，这样就会节约TCP连接在建立、释放过程中，主机和路由器上的CPU和内存开销。
By opening and closing fewer TCP connections, CPU time is saved in routers and hosts (clients, servers, proxies, gateways, tunnels, or caches), and memory used for TCP protocol control blocks can be saved in hosts.
**HTTP requests and responses can be pipelined on a connection. Pipelining allows a client to make multiple requests without waiting for each response, allowing a single TCP connection to be used much more efficiently, with much lower elapsed time.**

（2）网络拥塞也减少了，拿到响应的延时也减少了
**Network congestion** is reduced by reducing the number of packets caused by TCP opens, and by allowing TCP sufficient time to determine the congestion state of the network.
**Latency** on subsequent requests is reduced since there is no time spent in TCP's connection opening handshake.

（3）错误处理更优雅：不会粗暴地直接关闭连接，而是report，retry
HTTP can evolve more gracefully, since errors can be reported without the penalty of closing the TCP connection. Clients using future versions of HTTP might optimistically try a new feature, but if communicating with an older server, retry with old semantics after an error is reported.
RFC 2616 （P47）还指出：单用户客户端与任何服务器或代理之间的连接数不应该超过2个。一个代理与其它服务器或代码之间应该使用不超过2 * N的活跃并发连接。这是为了提高HTTP响应时间，避免拥塞（冗余的连接并不能代码执行性能的提升）。



4、Keep-Alive模式，客户端如何判断请求所得到的响应数据已经接收完成（或者说如何知道服务器已经发生完了数据）？

对于非持续连接，浏览器可以通过连接是否关闭来界定请求或响应实体的边界；而对于持续连接，这种方法显然不奏效。有时，尽管我已经发送完所有数据，但浏览器并不知道这一点，它无法得知这个打开的连接上是否还会有新数据进来，只能傻傻地等了。


（1）使用消息首部字段Conent-Length

Conent-Length表示实体内容长度，当客户端向服务器请求一个静态页面或者一张图片时，服务器可以很清楚的知道内容大小，然后通过Content-length消息首部字段告诉客户端 需要接收多少数据。

（2）使用消息首部字段Transfer-Encoding

如果是动态页面等时，服务器是不可能预先知道内容大小。因为对于动态生成的内容来说，在内容创建完之前，长度是不可知的。这时候要想准确获取长度，只能开一个足够大的 buffer，等内容全部生成好再计算。但这样做一方面需要更大的内存开销，另一方面也会让客户端等更久。所以不可能这么做。Conent-Length就失效了。



这时就可以使用Transfer-Encoding：chunk模式：服务器就需要使用Transfer-Encoding: chunked这样的方式来代替Content-Length。即如果要一边产生数据，一边发给客户端。





5、 分块编码（Transfer-Encoding: chunked）

1. Transfer-Encoding，是一个 HTTP 头部字段（响应头域），字面意思是「传输编码」。最新的 HTTP 规范里，只定义了一种编码传输：分块编码(chunked)。

2. 分块传输编码（Chunked transfer encoding）是超文本传输协议（HTTP）中的一种数据传输机制，允许HTTP由网页服务器发送给客户端的数据可以分成多个部分。分块传输编码只在HTTP协议1.1版本（HTTP/1.1）中提供。

3. 数据分解成一系列数据块，并以一个或多个块发送，这样服务器可以发送数据而不需要预先知道发送内容的总大小。

4. 具体方法

5. 1. 在头部加入 Transfer-Encoding: chunked 之后，就代表这个报文采用了分块编码。这时，报文中的实体需要改为用一系列分块来传输。
   2. 每个分块包含十六进制的长度值和数据，长度值独占一行，长度不包括它结尾的 CRLF(\r\n)，也不包括分块数据结尾的 CRLF。
   3. 最后一个分块长度值必须为 0，对应的分块数据没有内容，表示实体结束。

6. Content-Encoding 和 Transfer-Encoding 二者经常会结合来用，其实就是针对 Transfer-Encoding 的分块再进行 Content-Encoding压缩。

例子：

```text
HTTP/1.1 200 OK
Content-Type: text/plain
Transfer-Encoding: chunked

25\r\n
This is the data in the first chunk\r\n

1C\r\n
and this is the second one\r\n

3\r\n
con\r\n

8\r\n
sequence\r\n

0\r\n
\r\n
```



### 3 ways handshake

https://notfalse.net/7/three-way-handshake

![三向交握 範例](https://tva1.sinaimg.cn/large/006tNbRwgy1gblnwn98uhj30fq0gedgq.jpg)

![TCP-Header-Format](https://tva1.sinaimg.cn/large/006tNbRwgy1gblnxhmf7cj30xs0mfwi6.jpg)



### HTTP methods

Restfule API - GET POST PUT DELETE