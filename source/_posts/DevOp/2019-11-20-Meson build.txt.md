---
layout: post
categories: DevOps
tag: [] 


---

### Meson Build

Meson requires that you have a source directory and a build directory and that these two are different. In your source root must exist a file called `meson.build`. To generate the build system run this command:

```bash
meson <source directory> <build directory>

```

To compile, cd into your build directory and type `ninja`. To run unit tests, type `ninja test`.



```scheme
source_file = ['video_decoder_opencv.cpp']

cc = meson.get_compiler('cpp')


video_dep = [cc.find_library('opencv_core',  dirs:['/root/opencv-3.4.7/cvlib/lib']),
             cc.find_library('opencv_videoio',  dirs:['/root/opencv-3.4.7/cvlib/lib']),
             cc.find_library('opencv_imgcodecs',  dirs:['/root/opencv-3.4.7/cvlib/lib']),
             cc.find_library('opencv_imgproc',  dirs:['/root/opencv-3.4.7/cvlib/lib'])]

video_loader_dep = declare_dependency(
                            include_directories:[include_directories('.'), config_dir, include_directories('/root/opencv-3.4.7/cvlib/include')],
                            dependencies: video_dep,
                            sources: source_file,)
```



```bash 
root@7a96a548d8fd:~/opencv-3.4.7/cvlib# tree -L 2
.
├── include
│   ├── CMakeLists.txt
│   ├── opencv
│   └── opencv2
└── lib
    ├── libopencv_calib3d.so -> libopencv_calib3d.so.3.4
    ├── libopencv_calib3d.so.3.4 -> libopencv_calib3d.so.3.4.7
    ├── libopencv_calib3d.so.3.4.7
    ├── libopencv_core.so -> libopencv_core.so.3.4
    ├── libopencv_core.so.3.4 -> libopencv_core.so.3.4.7
    ├── libopencv_core.so.3.4.7
    ├── libopencv_dnn.so -> libopencv_dnn.so.3.4
    ├── libopencv_dnn.so.3.4 -> libopencv_dnn.so.3.4.7
    ├── libopencv_dnn.so.3.4.7
    ├── libopencv_features2d.so -> libopencv_features2d.so.3.4
    ├── libopencv_features2d.so.3.4 -> libopencv_features2d.so.3.4.7
    ├── libopencv_features2d.so.3.4.7
    ├── libopencv_flann.so -> libopencv_flann.so.3.4
    ├── libopencv_flann.so.3.4 -> libopencv_flann.so.3.4.7
    ├── libopencv_flann.so.3.4.7
    ├── libopencv_highgui.so -> libopencv_highgui.so.3.4
    ├── libopencv_highgui.so.3.4 -> libopencv_highgui.so.3.4.7
    ├── libopencv_highgui.so.3.4.7
    ├── libopencv_imgcodecs.so -> libopencv_imgcodecs.so.3.4
    ├── libopencv_imgcodecs.so.3.4 -> libopencv_imgcodecs.so.3.4.7
    ├── libopencv_imgcodecs.so.3.4.7
    ├── libopencv_imgproc.so -> libopencv_imgproc.so.3.4
    ├── libopencv_imgproc.so.3.4 -> libopencv_imgproc.so.3.4.7
    ├── libopencv_imgproc.so.3.4.7
    ├── libopencv_ml.so -> libopencv_ml.so.3.4
    ├── libopencv_ml.so.3.4 -> libopencv_ml.so.3.4.7
    ├── libopencv_ml.so.3.4.7
    ├── libopencv_objdetect.so -> libopencv_objdetect.so.3.4
    ├── libopencv_objdetect.so.3.4 -> libopencv_objdetect.so.3.4.7
    ├── libopencv_objdetect.so.3.4.7
    ├── libopencv_photo.so -> libopencv_photo.so.3.4
    ├── libopencv_photo.so.3.4 -> libopencv_photo.so.3.4.7
    ├── libopencv_photo.so.3.4.7
    ├── libopencv_shape.so -> libopencv_shape.so.3.4
    ├── libopencv_shape.so.3.4 -> libopencv_shape.so.3.4.7
    ├── libopencv_shape.so.3.4.7
    ├── libopencv_stitching.so -> libopencv_stitching.so.3.4
    ├── libopencv_stitching.so.3.4 -> libopencv_stitching.so.3.4.7
    ├── libopencv_stitching.so.3.4.7
    ├── libopencv_superres.so -> libopencv_superres.so.3.4
    ├── libopencv_superres.so.3.4 -> libopencv_superres.so.3.4.7
    ├── libopencv_superres.so.3.4.7
    ├── libopencv_videoio.so -> libopencv_videoio.so.3.4
    ├── libopencv_videoio.so.3.4 -> libopencv_videoio.so.3.4.7
    ├── libopencv_videoio.so.3.4.7
    ├── libopencv_video.so -> libopencv_video.so.3.4
    ├── libopencv_video.so.3.4 -> libopencv_video.so.3.4.7
    ├── libopencv_video.so.3.4.7
    ├── libopencv_videostab.so -> libopencv_videostab.so.3.4
    ├── libopencv_videostab.so.3.4 -> libopencv_videostab.so.3.4.7
    └── libopencv_videostab.so.3.4.7

4 directories, 52 files
```

