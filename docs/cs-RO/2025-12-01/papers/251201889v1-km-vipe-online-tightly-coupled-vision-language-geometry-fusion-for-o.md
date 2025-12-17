---
layout: default
title: KM-ViPE: Online Tightly Coupled Vision-Language-Geometry Fusion for Open-Vocabulary Semantic SLAM
---

# KM-ViPE: Online Tightly Coupled Vision-Language-Geometry Fusion for Open-Vocabulary Semantic SLAM

**arXiv**: [2512.01889v1](https://arxiv.org/abs/2512.01889) | [PDF](https://arxiv.org/pdf/2512.01889.pdf)

**作者**: Zaid Nasser, Mikhail Iumanov, Tianhao Li, Maxim Popov, Jaafar Mahmoud, Malik Mohrat, Ilya Obrubov, Ekaterina Derevyanka, Ivan Sosin, Sergey Kolyubin

---

## 💡 一句话要点

**提出KM-ViPE框架，通过视觉-语言-几何紧耦合实现动态环境中未标定单目相机的实时开放词汇语义SLAM。**

**关键词**: `开放词汇语义SLAM` `视觉-语言-几何融合` `动态场景鲁棒性` `未标定单目相机` `在线实时操作` `自适应鲁棒核`

## 📋 核心要点

1. 核心问题：现有SLAM系统依赖深度传感器、离线校准或缺乏动态场景鲁棒性，限制了在未标定单目相机和动态环境中的应用。
2. 方法要点：紧耦合DINO视觉特征与几何约束，使用基于高级特征的自适应鲁棒核处理移动和可移动静态物体，在线融合几何与语言对齐的视觉特征。
3. 实验或效果：在实时操作中实现竞争性性能，适用于自主机器人和AR/VR，提升具身AI的空间智能能力。

## 📄 摘要（原文）

> We present KM-ViPE (Knowledge Mapping Video Pose Engine), a real-time open-vocabulary SLAM framework for uncalibrated monocular cameras in dynamic environments. Unlike systems requiring depth sensors and offline calibration, KM-ViPE operates directly on raw RGB streams, making it ideal for ego-centric applications and harvesting internet-scale video data for training. KM-ViPE tightly couples DINO visual features with geometric constraints through a high-level features based adaptive robust kernel that handles both moving objects and movable static objects (e.g., moving furniture in ego-centric views). The system performs simultaneous online localization and open-vocabulary semantic mapping by fusing geometric and deep visual features aligned with language embeddings. Our results are competitive with state-of-the-art approaches, while existing solutions either operate offline, need depth data and/or odometry estimation, or lack dynamic scene robustness. KM-ViPE benefits from internet-scale training and uniquely combines online operation, uncalibrated monocular input, and robust handling of dynamic scenes, which makes it a good fit for autonomous robotics and AR/VR applications and advances practical spatial intelligence capabilities for embodied AI.

