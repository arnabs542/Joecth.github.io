---
layout: post
categories: CV
tag: [] 



---

### Install.sh

```bash
mkdir opencv
cd opencv
cp /root/3.4.7.zip ./
unzip 3.4.7.zip
apt-get update
apt-get install -y cmake
apt-get install -y build-essential libgtk2.0-dev libavcodec-dev libavformat-dev libjpeg.dev libtiff4.dev libswscale-dev libjasper-dev
cd opencv-3.4.7
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
make install -j8
```