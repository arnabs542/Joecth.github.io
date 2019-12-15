---
layout: post
categories: ffmpy3
tag: [] 



---

### Transition

```python
def video_create(self):
    logger.info("In video creating")
    jpgs_folder = os.path.join(self.template_dir, "jpgs")
    jpgs = os.path.join(jpgs_folder, 'data_%5d.jpg')
    ffinputs = {jpgs: ['-r', '24', '-t', str(self.duration)]}
    if not (self.audio_file and self.duration):
        raise Exception("NO AUDIO PARA IN {}".format(self.task_name))
    ffinputs[self.audio_file] = None

    cmd, video = ffmpeg_run.stage_run_lottie(ffinputs, None, self.outputpath)
```



![image-20191126120655290](https://tva1.sinaimg.cn/large/006y8mN6ly1g9bb9zf2qvj324803adh4.jpg)

/usr/bin/ffmpeg -loglevel warning -y -r 24 -t 5.279 -i /mnt/raid3/home/huangjiancong/workspace/monsters_1688_leo/monsters_1688_leo/tmp_materials/tmp_通用模板_红粉记忆_9_cd5d171c-1000-11ea-b566-6fc61ea5942f/3_4_detail_res2_sc1_00f5685e-1001-11ea-b566-6fc61ea5942f/jpgs/data_%5d.jpg -i /mnt/raid3/home/huangjiancong/workspace/monsters_1688_leo/monsters_1688_leo/tmp_materials/tmp_通用模板_红粉记忆_9_cd5d171c-1000-11ea-b566-6fc61ea5942f/0355ecf4-1001-11ea-b566-6fc61ea5942f.wav -ac 2 -ar 44100 -r 24 -pix_fmt yuv420p -strict -2 -preset ultrafast -qscale:v 2 /mnt/raid3/home/huangjiancong/workspace/monsters_1688_leo/monsters_1688_leo/tmp_materials/tmp_通用模板_红粉记忆_9_cd5d171c-1000-11ea-b566-6fc61ea5942f/fb770798-1000-11ea-b566-6fc61ea5942f_video1.mp4