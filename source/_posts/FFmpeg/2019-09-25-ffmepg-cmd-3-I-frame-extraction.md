---
layout: post
# title:  "ffmpeg_cmd_3 I frame extraction"
# date:   2019-09-25 22:16:11 +0800
categories: ffmpeg
---

### I-frame extraction

```bash
ffmpeg -i vn_hflip.mp4 -vf select='eq(pict_type\,I)' -vsync 2 -s 1280*720 -f image2 keyframe-%03d.jpeg
```

-vf:是一个命令行，表示过滤图形的描述。选择过滤器select会选择帧进行输出：pict_type和对应的类型:PICT_TYPE_I 表示是I帧，即关键帧；
-vsync 2:阻止每个关键帧产生多余的拷贝；
-f image2 name_%02d.jpeg:将视频帧写入到图片中，样式的格式一般是: “%d” 或者 “%0Nd”



### Index of I-frame

```bash
ffprobe -i vn_hflip.mp4 -select_streams v -show_frames -show_entries frame=pict_type -of csv | grep -n I | cut -d ':' -f 1 > frame_index.txt
```



### Relates the twos

```bash
ls -1 keyframe*.jpeg > keyframe.txt
paste frame_index.txt  keyframe.txt> result.txt
```

(joe_py36)
~/workspace/exp/FFmpeg_
☺  more result.txt
☺  more result.txt
1       keyframe-01.jpeg
3       keyframe-02.jpeg
16      keyframe-03.jpeg
25      keyframe-04.jpeg
30      keyframe-05.jpeg
46      keyframe-06.jpeg
55      keyframe-07.jpeg
59      keyframe-08.jpeg
70      keyframe-09.jpeg
83      keyframe-10.jpeg
100     keyframe-11.jpeg
116     keyframe-12.jpeg



### [翻译ffmpeg-all文档（40），多媒体滤镜](http://blog.chinaunix.net/uid-10062010-id-5137275.html)

http://blog.chinaunix.net/uid-10062010-id-5137275.html



Ref: https://superuser.com/questions/885452/extracting-the-index-of-key-frames-from-a-video-using-ffmpeg

