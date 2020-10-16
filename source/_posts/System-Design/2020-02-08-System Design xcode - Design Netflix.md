---
layout: post
categories: System
tag: [] 
date: 2020-02-08
---

### 

# Design Netflix



1. **Processing Queue:** Each uploaded video will be pushed to a processing queue, to be de-queued later for encoding, thumbnail generation, and storage.
2. **Encoder:** To encode each uploaded video into multiple formats.
3. **Thumbnails generator:** We need to have a few thumbnails for each video.
4. **Video and Thumbnail storage:** We need to store video and thumbnail files in some distributed file storage.
5. **User Database:** We would need some database to store user’s information, e.g., name, email, address, etc.
6. **Video metadata storage:** Metadata database will store all the information about videos like title, file path in the system, uploading user, total views, likes, dislikes, etc. Also, it will be used to store all the video comments.

![image-20200902103236968](https://tva1.sinaimg.cn/large/007S8ZIlgy1gic3oe2dd1j30yk0doadp.jpg)



