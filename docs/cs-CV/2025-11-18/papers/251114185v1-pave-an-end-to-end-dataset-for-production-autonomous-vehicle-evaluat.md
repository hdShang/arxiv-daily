---
layout: default
title: PAVE: An End-to-End Dataset for Production Autonomous Vehicle Evaluation
---

# PAVE: An End-to-End Dataset for Production Autonomous Vehicle Evaluation

**arXiv**: [2511.14185v1](https://arxiv.org/abs/2511.14185) | [PDF](https://arxiv.org/pdf/2511.14185.pdf)

**作者**: Xiangyu Li, Chen Wang, Yumao Liu, Dengbo He, Jiahao Zhang, Ke Ma

---

## 💡 一句话要点

**提出PAVE数据集以评估生产级自动驾驶车辆的行为安全**

**关键词**: `自动驾驶数据集` `行为安全评估` `端到端基准` `轨迹预测` `场景属性标注`

## 📋 核心要点

1. 现有数据集无法评估自动驾驶车辆的真实行为安全
2. 提供首个全自动驾驶模式收集的端到端基准数据集
3. 在自动驾驶帧上轨迹预测平均位移误差为1.4米

## 📄 摘要（原文）

> Most existing autonomous-driving datasets (e.g., KITTI, nuScenes, and the Waymo Perception Dataset), collected by human-driving mode or unidentified driving mode, can only serve as early training for the perception and prediction of autonomous vehicles (AVs). To evaluate the real behavioral safety of AVs controlled in the black box, we present the first end-to-end benchmark dataset collected entirely by autonomous-driving mode in the real world. This dataset contains over 100 hours of naturalistic data from multiple production autonomous-driving vehicle models in the market. We segment the original data into 32,727 key frames, each consisting of four synchronized camera images and high-precision GNSS/IMU data (0.8 cm localization accuracy). For each key frame, 20 Hz vehicle trajectories spanning the past 6 s and future 5 s are provided, along with detailed 2D annotations of surrounding vehicles, pedestrians, traffic lights, and traffic signs. These key frames have rich scenario-level attributes, including driver intent, area type (covering highways, urban roads, and residential areas), lighting (day, night, or dusk), weather (clear or rain), road surface (paved or unpaved), traffic and vulnerable road users (VRU) density, traffic lights, and traffic signs (warning, prohibition, and indication). To evaluate the safety of AVs, we employ an end-to-end motion planning model that predicts vehicle trajectories with an Average Displacement Error (ADE) of 1.4 m on autonomous-driving frames. The dataset continues to expand by over 10 hours of new data weekly, thereby providing a sustainable foundation for research on AV driving behavior analysis and safety evaluation.

