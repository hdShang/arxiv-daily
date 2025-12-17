---
layout: default
title: An Integrated System for WEEE Sorting Employing X-ray Imaging, AI-based Object Detection and Segmentation, and Delta Robot Manipulation
---

# An Integrated System for WEEE Sorting Employing X-ray Imaging, AI-based Object Detection and Segmentation, and Delta Robot Manipulation

**arXiv**: [2512.05599v1](https://arxiv.org/abs/2512.05599) | [PDF](https://arxiv.org/pdf/2512.05599.pdf)

**作者**: Panagiotis Giannikos, Lampis Papakostas, Evangelos Katralis, Panagiotis Mavridis, George Chryssinas, Myrto Inglezou, Nikolaos Panagopoulos, Antonis Porichis, Athanasios Mastrogeorgiou, Panagiotis Chatzakos

---

## 💡 一句话要点

**提出集成X射线成像、AI检测与分割及Delta机器人操作的WEEE电池分拣系统**

**关键词**: `WEEE分拣` `X射线成像` `目标检测` `图像分割` `Delta机器人` `电池回收`

## 📋 核心要点

1. 核心问题：电池回收中安全风险高，现有方法难以实现跨类型WEEE的准确分拣
2. 方法要点：结合双能X射线成像与预处理算法，使用YOLO和U-Net进行检测分割，Delta机器人执行提取
3. 实验或效果：在NVIDIA Isaac Sim仿真环境和真实设置中验证系统有效性

## 📄 摘要（原文）

> Battery recycling is becoming increasingly critical due to the rapid growth in battery usage and the limited availability of natural resources. Moreover, as battery energy densities continue to rise, improper handling during recycling poses significant safety hazards, including potential fires at recycling facilities. Numerous systems have been proposed for battery detection and removal from WEEE recycling lines, including X-ray and RGB-based visual inspection methods, typically driven by AI-powered object detection models (e.g., Mask R-CNN, YOLO, ResNets). Despite advances in optimizing detection techniques and model modifications, a fully autonomous solution capable of accurately identifying and sorting batteries across diverse WEEEs types has yet to be realized. In response to these challenges, we present our novel approach which integrates a specialized X-ray transmission dual energy imaging subsystem with advanced pre-processing algorithms, enabling high-contrast image reconstruction for effective differentiation of dense and thin materials in WEEE. Devices move along a conveyor belt through a high-resolution X-ray imaging system, where YOLO and U-Net models precisely detect and segment battery-containing items. An intelligent tracking and position estimation algorithm then guides a Delta robot equipped with a suction gripper to selectively extract and properly discard the targeted devices. The approach is validated in a photorealistic simulation environment developed in NVIDIA Isaac Sim and on the real setup.

