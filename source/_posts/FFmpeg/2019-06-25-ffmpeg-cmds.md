---
layout: post
title:  "ffmpeg_cmds!"
##date: 2019-06-25
date:   2019-06-25 22:16:11 +0800
categories: ffmpeg

---

## rm black sides
```bash
╰─○ ffplay -i vn_hflip.mp4 -t 5 -vf cropdetect
╰─○ ffplay -i vn_hflip.mp4 -t 5 -vf crop=1280:528:0:96
```

## save to json
```bash
ffprobe -hide_banner -print_format json -show_streams -i vn_hflip.mp4 > vn_json_streams.log
```

## check error 
```bash
ffprobe -show_frames vn_hflip.mp4 > vn_show_frames.log
```

## video to pics
```bash
ffmpeg -i vn_hflip.mp4 -r 40 -f image2         -t 1 my%d.jpg        ## 跟下一行比會多了幾張重覆的，因為比來的video就25fps而已
"""2938"""  ffmpeg -i vn_hflip.mp4 -r 25 -f image2 -t 1 my25_%d.jpg ## 跟上一行几乎一样，就是正常的25 rate
ffmpeg -i vn_hflip.mp4 -vcodec mjpeg -ss 0:0:2 -t 0:0:1 0m%04d.jpg  ## 跟上面比主要就是从第二秒开始

2937  ffmpeg -i vn_hflip.mp4 -r 40 -f image2 -t 1 my25_%d.jpg
★★★ -r, -ss, -t  本来的video要变成的rate，开始、抓多久

ffmpeg -i vn_hflip.mp4 -ss 00:00:14.435 -vframes 1 out.png
★★★ -vframes 抓几张
```

## pics to video
把多个图像文件使用h264编码封装成avi文件，如有my0.jpg, my1.jpg ... my99.jpg

```bash
ffmpeg -i my%d.jpg  -vcodec h264 my.avi
```



-r 选项的用法：

预设是

以25FPS读入所有图片，所以len(Images[])会是输出的video的duration. 

作出25FPS的video, 所以如果 -r加在 output前面，会进行插帧、删帧。

如果-r加在 input前面，就是每秒读进来几张图片

如果　ffmpeg -r 10 -i z-%5d.jpeg -vcodec h264 -r 60 out10in60out.mp4

那么因为每秒读进来10张而已，硬做成60fps的video，也是没用，因为中间只是内插成了60fps





## video to gif
```bash
ffmpeg -i vn_hflip.mp4 -ss 0 -r 1 -vframes 6 vn.gif
ffmpeg -i vn_hflip.mp4 -ss 0 -vf fps=1 -vframes 6 vn_fps.gif # 这个似乎比上面的好一些 
```




##EXTRACTION !!!
```bash
 2999  ffmpeg -i ../vn_hflip.mp4 -ss 00:00:00 -t 10 -vf fps=1 fps1_%d.png
(joe_py36) ┌─[joe@JoeMBP2] - [~/Movies/exp/tmp] - [3003]
└─[$] history | grep r1                                                                                                                                                                           [22:06:04]
 2975  ffmpeg -i ../vn_hflip.mp4 -r 1 r1_%d.png
 2977  ffmpeg -i ../vn_hflip.mp4 -r 1 -vframes 6 r1_vframes_%d.png
```







## add logo 
```bash
ffmpeg -i vn_hflip.mp4 -i ~/Pictures/Sackboy_0.jpeg -filter_complex overlay=W-w:H-h vn_logo.avi
    如右下角: ffmpeg -i God.rm -i logo.png -filter_complex overlay=W-w:H-h my.avi
    如居中:  ffmpeg -i God.rm -i logo.png -filter_complex overlay=W/2-w/2:H/2-h/2 my.avi
```



