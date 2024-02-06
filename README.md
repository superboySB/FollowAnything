# Follow Anything复现
```sh
docker build -t sam_image:1.0 .

docker run -itd --privileged -v /tmp/.X11-unix:/tmp/.X11-unix:ro -e DISPLAY=$DISPLAY --gpus all --network=host --name=sam sam_image:1.0 /bin/bash

pip install torch torchvision gradio mavsdk rtsp natsort PyQt5 numpy opencv-python pycocotools matplotlib Pillow scikit-image spatial-correlation-sampler timm

# 若在服务器上运行：pip uninstall opencv-python && pip install opencv-python-headless

cd /workspace && git clone https://github.com/superboySB/FollowAnything 

```
在`FollowAnything/Segment-and-Track-Anything/ckpt`位置下载[SAM-VIT-B](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth)以及[R50-DeAOT-L](https://drive.google.com/file/d/1QoChMkTVxdYZ_eBlZhK2acq9KMQZccPJ/view)
```sh
cd /workspace/FollowAnything/Segment-and-Track-Anything/sam && pip install -e .
```
测试效果
```sh
cd /workspace/FollowAnything/

python follow_anything.py --desired_height 240 --desired_width 320 --path_to_video example_videos/car_following.avi --save_images_to outputs/ --detect dino --redetect_by tracker --use_sam --tracker siammask --queries_dir queries/toy_car_following --desired_feature 0 
```
如果有图形界面可以加`--plot_visualization`.

部署侧额外依赖
```
conda install pytorch=0.4.1 cuda92 -c pytorch
```