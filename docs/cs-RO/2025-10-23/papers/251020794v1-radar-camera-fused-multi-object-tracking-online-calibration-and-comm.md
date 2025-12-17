---
layout: default
title: Radar-Camera Fused Multi-Object Tracking: Online Calibration and Common Feature
---

# Radar-Camera Fused Multi-Object Tracking: Online Calibration and Common Feature

**arXiv**: [2510.20794v1](https://arxiv.org/abs/2510.20794) | [PDF](https://arxiv.org/pdf/2510.20794.pdf)

**作者**: Lei Cheng, Siyang Cao

---

## 💡 一句话要点

**提出雷达-相机融合多目标跟踪框架，利用在线校准和共同特征提升跟踪精度**

**关键词**: `多目标跟踪` `雷达-相机融合` `在线校准` `共同特征` `传感器关联`

## 📋 核心要点

1. 核心问题：雷达在融合中常被低估，无法充分利用其精确深度信息
2. 方法要点：通过在线校准和共同特征匹配，自动关联雷达与相机检测
3. 实验或效果：在控制环境和真实交通场景中验证，提高跟踪精度和效率

## 📄 摘要（原文）

> This paper presents a Multi-Object Tracking (MOT) framework that fuses radar
> and camera data to enhance tracking efficiency while minimizing manual
> interventions. Contrary to many studies that underutilize radar and assign it a
> supplementary role--despite its capability to provide accurate range/depth
> information of targets in a world 3D coordinate system--our approach positions
> radar in a crucial role. Meanwhile, this paper utilizes common features to
> enable online calibration to autonomously associate detections from radar and
> camera. The main contributions of this work include: (1) the development of a
> radar-camera fusion MOT framework that exploits online radar-camera calibration
> to simplify the integration of detection results from these two sensors, (2)
> the utilization of common features between radar and camera data to accurately
> derive real-world positions of detected objects, and (3) the adoption of
> feature matching and category-consistency checking to surpass the limitations
> of mere position matching in enhancing sensor association accuracy. To the best
> of our knowledge, we are the first to investigate the integration of
> radar-camera common features and their use in online calibration for achieving
> MOT. The efficacy of our framework is demonstrated by its ability to streamline
> the radar-camera mapping process and improve tracking precision, as evidenced
> by real-world experiments conducted in both controlled environments and actual
> traffic scenarios. Code is available at
> https://github.com/radar-lab/Radar_Camera_MOT

