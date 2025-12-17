---
layout: default
title: USV Obstacles Detection and Tracking in Marine Environments
---

# USV Obstacles Detection and Tracking in Marine Environments

**arXiv**: [2511.07950v1](https://arxiv.org/abs/2511.07950) | [PDF](https://arxiv.org/pdf/2511.07950.pdf)

**作者**: Yara AlaaEldin, Enrico Simetti, Francesca Odone

---

## 💡 一句话要点

**提出混合方法融合相机与LiDAR，提升USV在海洋环境中的障碍物检测与跟踪**

**关键词**: `障碍物检测` `传感器融合` `ROS平台` `海洋环境` `LiDAR点云` `实时跟踪`

## 📋 核心要点

1. 核心问题：海洋环境中USV障碍物检测与跟踪的鲁棒性挑战。
2. 方法要点：集成相机与LiDAR传感器融合，并在ROS平台上实时测试。
3. 实验或效果：评估两种方法性能，提出混合方法构建环境障碍物地图。

## 📄 摘要（原文）

> Developing a robust and effective obstacle detection and tracking system for Unmanned Surface Vehicle (USV) at marine environments is a challenging task. Research efforts have been made in this area during the past years by GRAAL lab at the university of Genova that resulted in a methodology for detecting and tracking obstacles on the image plane and, then, locating them in the 3D LiDAR point cloud. In this work, we continue on the developed system by, firstly, evaluating its performance on recently published marine datasets. Then, we integrate the different blocks of the system on ROS platform where we could test it in real-time on synchronized LiDAR and camera data collected in various marine conditions available in the MIT marine datasets. We present a thorough experimental analysis of the results obtained using two approaches; one that uses sensor fusion between the camera and LiDAR to detect and track the obstacles and the other uses only the LiDAR point cloud for the detection and tracking. In the end, we propose a hybrid approach that merges the advantages of both approaches to build an informative obstacles map of the surrounding environment to the USV.

