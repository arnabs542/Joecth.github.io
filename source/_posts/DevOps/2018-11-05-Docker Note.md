---
layout: post
categories: DevOps
tag: [] 
date: 2018-11-05
---



```Dockerfile
Docker:
$ docker pull ubuntu:18.04
因此将会获取官方镜像 library/ubuntu 仓库

$ docker run -it (—rm 表示exit后自动删除掉) ubuntu:18.04 bash  或 把it 改成dt
root@569c032785f2:/# pwd
/
root@aaa:# exit
$ docker exec -it $CON_ID bash

$ docker ps -a  <==例出所有containers ;  docker rm $CON_ID
$ docker ps -n5
$ docker stop $CON_ID
$ docker start $CON_ID

╰$ cat Dockerfile
FROM registry.cn-hangzhou.aliyuncs.com/eigenlab/ideal-video:latest
RUN echo 'aaaaaaaaaaaaaaaaa' > ./test_aaa.log
╰$ docker build -t aaa:v1
╰$ docker image prune
WARNING! This will remove all dangling images.
Are you sure you want to continue? [y/N] y
Deleted Images:
deleted: sha256:0015c03359ec60e4f133bb382dc0662f976dbebed7cdf70bf50bd9efca82052e

Total reclaimed space: 0B









Docker:
$ docker pull ubuntu:18.04
因此将会获取官方镜像 library/ubuntu 仓库

$ docker run -it (—rm 表示exit后自动删除掉) ubuntu:18.04 bash  或 把it 改成dt
root@569c032785f2:/# pwd
/
root@aaa:# exit
$ docker exec -it $CON_ID bash

$ docker ps -a  <==例出所有containers ;  docker rm $CON_ID
$ docker ps -n5
$ docker stop $CON_ID
$ docker start $CON_ID

╰$ cat Dockerfile
FROM registry.cn-hangzhou.aliyuncs.com/eigenlab/ideal-video:latest
RUN echo 'aaaaaaaaaaaaaaaaa' > ./test_aaa.log
╰$ docker build -t aaa:v1
╰$ docker image prune
WARNING! This will remove all dangling images.
Are you sure you want to continue? [y/N] y
Deleted Images:
deleted: sha256:0015c03359ec60e4f133bb382dc0662f976dbebed7cdf70bf50bd9efca82052e

Total reclaimed space: 0B
```





```bash 
docker run  -p 5599:5599 -p 8023:22 --name="wazowski_joe_1106" -v ~/workspace:/remote_workspace -it registry.cn-hangzhou.aliyuncs.com/eigenlab/wazowski_1688_leo:44 bash
```

```bash 
huangjiancong@hpc3:~$ sudo docker port wazowski_joe_1106  22
[sudo] password for huangjiancong:
Sorry, try again.
[sudo] password for huangjiancong:
0.0.0.0:8023
huangjiancong@hpc3:~$ ss -tulwn | grep 8023
tcp    LISTEN     0      128      :::8023                 :::*
```



不过没有关系，知道原理就行，根据提示 **Offending ECDSA key in /root/.ssh/known_hosts:9** ，删除路径中的第九行：

```bash 
sudo sed -i '9d' /root/.ssh/known_hosts
```



Docker check mounted path 

```bash 
docker inspect -f "{{ .Mounts }}"  7a96
```

[{bind  /home/$USER/workspace/exp/docker_/opencv347 /workspace/remote_opencv347   true rprivate}]