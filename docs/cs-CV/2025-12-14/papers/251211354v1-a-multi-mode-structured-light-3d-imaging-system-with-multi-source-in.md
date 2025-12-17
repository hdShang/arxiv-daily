---
layout: default
title: A Multi-Mode Structured Light 3D Imaging System with Multi-Source Information Fusion for Underwater Pipeline Detection
---

# A Multi-Mode Structured Light 3D Imaging System with Multi-Source Information Fusion for Underwater Pipeline Detection

**arXiv**: [2512.11354v1](https://arxiv.org/abs/2512.11354) | [PDF](https://arxiv.org/pdf/2512.11354.pdf)

**作者**: Qinghan Hu, Haijiang Zhu, Na Sun, Lei Chen, Zhengqiang Fan, Zhiqing Li

---

## 💡 一句话要点

**提出多模式水下结构光三维成像系统，融合多源信息以检测水下管道缺陷。**

**关键词**: `水下三维成像` `结构光` `多源信息融合` `点云配准` `管道检测` `自适应滤波`

## 📋 核心要点

1. 核心问题：水下管道易腐蚀，需高精度三维成像系统进行实时检测。
2. 方法要点：采用多模式成像策略、多源信息融合和自适应扩展卡尔曼滤波，提升稳定性和精度。
3. 实验或效果：在不同操作模式、速度和深度下实验，系统展现出高准确性、适应性和鲁棒性。

## 📄 摘要（原文）

> Underwater pipelines are highly susceptible to corrosion, which not only shorten their service life but also pose significant safety risks. Compared with manual inspection, the intelligent real-time imaging system for underwater pipeline detection has become a more reliable and practical solution. Among various underwater imaging techniques, structured light 3D imaging can restore the sufficient spatial detail for precise defect characterization. Therefore, this paper develops a multi-mode underwater structured light 3D imaging system for pipeline detection (UW-SLD system) based on multi-source information fusion. First, a rapid distortion correction (FDC) method is employed for efficient underwater image rectification. To overcome the challenges of extrinsic calibration among underwater sensors, a factor graph-based parameter optimization method is proposed to estimate the transformation matrix between the structured light and acoustic sensors. Furthermore, a multi-mode 3D imaging strategy is introduced to adapt to the geometric variability of underwater pipelines. Given the presence of numerous disturbances in underwater environments, a multi-source information fusion strategy and an adaptive extended Kalman filter (AEKF) are designed to ensure stable pose estimation and high-accuracy measurements. In particular, an edge detection-based ICP (ED-ICP) algorithm is proposed. This algorithm integrates pipeline edge detection network with enhanced point cloud registration to achieve robust and high-fidelity reconstruction of defect structures even under variable motion conditions. Extensive experiments are conducted under different operation modes, velocities, and depths. The results demonstrate that the developed system achieves superior accuracy, adaptability and robustness, providing a solid foundation for autonomous underwater pipeline detection.

