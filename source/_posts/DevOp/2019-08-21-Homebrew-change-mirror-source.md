---
layout: post
categories: DevOps
---
Homebrew是Mac的软件包管理器，我们可以通过它安装大多数开源软件。但是在使用brew update更新的时候竟然要等待很久。猜测可能是因为brew的官方源被墙或或者响应慢。于是想到的切换Homebrew的更新源的办法, 如果coding.net的源还是很慢的话， 也可以尝试其他的源。具体代码如下



```bash
$ #cd to homebrew foler
$ cd "$(brew --repo)"；
$ #check  git remote status
$ git remote -v;
https://github.com/Homebrew/homebrew.git
$ #update remote url with Coding.net
$ git remote set-url origin https://git.coding.net/homebrew/homebrew.git
$ brew update
```



　

brew镜像源

- 中科大brew镜像源    http://mirrors.ustc.edu.cn/homebrew.git
- 清华brew镜像源  http://mirrors.ustc.edu.cn/homebrew.git