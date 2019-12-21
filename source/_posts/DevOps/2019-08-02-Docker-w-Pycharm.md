---
layout: post
categories: DevOps
date: 2019-08-02
---
### docker ssh配置

##### Concept

进行实验时用挂载的，让本地跟docker内的文件夹一样

#####新建docker container

```bash
sudo nvidia-docker run -it -p [host_port]:[container_port](do not use 8888) --name:[container_name] [image_name] -v [container_path]:[host_path] /bin/bash
```

例如：

```bash
sudo nvidia-docker run -p 5592:5592 -p 5593:5593 -p 8022:22 --name="liuzhen_tf" -v ~/workspace/liuzhen/remote_workspace:/workspace/liuzhen/remote_workspace -it tensorflow/tensorflow:latest-gpu /bin/bash
```

##### 配置ssh服务

在新建的容器内配置ssh，安装openssh-server

```bash
$ apt update
$ apt install -y openssh-server
```

设置ssh

```bash
$ mkdir /var/run/sshd
$ echo 'root:passwd' | chpasswd
# 这里使用你自己想设置的用户名和密码，passwd是此处设置的密码
$ sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
$ sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
$ echo "export VISIBLE=now" >> /etc/profile
```

##### 重启ssh激活配置 

(<u>最常见的问题</u>就是docker容器停了以后里面的SSH服务也会相应停止，因此当你发现自己某一天连不上的时候，记得去docker里重启一下ssh服务：)

```bash
$ service ssh restart
```

在服务器（宿主机）上（不是服务器的docker里）测试刚刚新建docker容器中哪个端口转发到了服务器的22端口：

```bash
$ sudo docker port [your_container_name] 22
# 如果前面的配置生效了，你会看到如下输出
# 0.0.0.0:8022
```

最后测试能否用SSH连接到远程docker：

```bash
$ ssh root@[your_host_ip] -p 8022
# 密码是你前面自己设置的
```

### pycharm配置

##### 打开本地代码

打开PyCharm`Tools > Deployment > Configuration`

#####新建服务器SFTP

![image-20190828175349739](https://tva1.sinaimg.cn/large/006y8mN6ly1g6gtkcxaeaj315r0u03zh.jpg)

输入如下图配置，注意这里的端口是你刚刚设置的映射到容器22端口的宿主机中的端口，我这里使用的是8022，账号密码是你刚刚自己设置的，这里的Root Path设置一个远程docker容器里的路径。

在Mappings中配置路径，这里的路径是你本地存放代码的路径，与刚刚配置的*Root Path*相互映射（意思是Mapping里本机的路径映射到远程的Root Path）*，*方便以后在本地和远程docker中进行代码和其他文件同步。

#####配置远程解释器

打开PyCharm`Preferences > Project Interpreter`

![image-20190828190716498](https://tva1.sinaimg.cn/large/006y8mN6ly1g6gtlykktsj317a0u0q4w.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6gtrxo163j307705et8o.jpg)

新建ssh Interpreter

![image-20190828191025481](https://tva1.sinaimg.cn/large/006y8mN6ly1g6gtml7aj1j31d30u0aam.jpg)

##### 配置运行环境变量

`run > edit confuriguration`

![image-20190828191253964](https://tva1.sinaimg.cn/large/006y8mN6ly1g6gtmztm35j30r80sk758.jpg)

### docker jupyter使用

jupyter-notebook的默认端口号是8888，映射几个外部端口，如前面的5592

更新apt

```
apt-get update
```

安装jupyter

```shell
pip install jupyter
```

(注意pip install jupyter notebook==5.7.5，高版本有bug)

配置jupyter

```shell
#生成jupyter配置文件，这个会生成配置文件.jupyter/jupyter_notebook_config.py
jupyter notebook --generate-config

#使用ipython生成密码
In [1]: from notebook.auth import passwd
In [2]: passwd()
Enter password: 
Verify password: 
Out[2]: 'sha1:38a5ecdf288b:c82dace8d3c7a212ec0bd49bbb99c9af3bae076e'

#去配置文件.jupyter/jupyter_notebook_config.py中修改以下参数
c.NotebookApp.ip='*'                          #绑定所有地址
c.NotebookApp.password = u'sha1:38a5ecdf288b:c82dace8d3c7a212ec0bd49bbb99c9af3bae076e'
c.NotebookApp.open_browser = False            #启动后是否在浏览器中自动打开
c.NotebookApp.port =5592                      #指定一个访问端口，默认8888，注意和映射的docker端口对应
c.NotebookApp.allow_remote_access = True
c.NotebookApp.allow_root = True               #allow the user to run the notebook as root
```

```shell
$ jupyter notebook 
```

