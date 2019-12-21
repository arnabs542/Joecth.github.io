---
layout: "post"
categories: ffmpeg
date: 2019-07-31
---

1.通过ffmpeg对AE直接导出的大文件压缩，(a.mov:16M，a.mp4:2.7M)，(b.mov:13M，a.mp4:1.6M)
`ffmpeg -i a.mov -vcodec png a.mp4`

2.对模板视频时长进行改变，(a.mp4:2.7M，a_fittime.mp4:2.6M)
`ffmpeg -i a.mp4 -vf setpts=0.96*PTS -vcodec png a_fittime.mp4`
模板6.25秒，素材6秒，经过上面的操作模板变成6.08秒

3.视频叠加，(intro_3_4.mp4:1.1M，a_fit_add.mp4:424k)
`ffmpeg -i intro_3_4.mp4 -i a_fittime.mp4 -filter_complex overlay -strict -2 a_fit_add.mp4`

4.Preset

![image](https://tva1.sinaimg.cn/large/006y8mN6gy1g7akqezzvtj30rv0j9dkl.jpg)





```python 
            ffoutputs += "[1:v]scale=if(gt({0}/iw\, {1}/ih)\, -1\, {0})" \
                                   ":if(gt({0}/iw\, {1}/ih)\, {1}\, -1)[video];".format(dest_w, dest_h)
```
