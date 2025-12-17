---
layout: default
title: Rad-GS: Radar-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments
---

# Rad-GS: Radar-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments

**arXiv**: [2511.16091v1](https://arxiv.org/abs/2511.16091) | [PDF](https://arxiv.org/pdf/2511.16091.pdf)

**作者**: Renxiang Xiao, Wei Liu, Yuanfan Zhang, Yushuai Chen, Jinming Chen, Zilu Wang, Liang Hu

---

## 💡 一句话要点

**提出Rad-GS系统，集成雷达与视觉实现户外大规模3D高斯SLAM**

**关键词**: `雷达视觉融合` `3D高斯SLAM` `动态物体掩码` `大规模场景重建` `内存优化`

## 📋 核心要点

1. 核心问题：户外大规模环境中动态物体导致渲染伪影和定位精度下降
2. 方法要点：利用雷达点云和多普勒信息引导动态掩码，结合非同步图像优化3D高斯表示
3. 实验或效果：在千米级真实场景中验证，性能媲美相机或LiDAR方法，减少内存消耗

## 📄 摘要（原文）

> We present Rad-GS, a 4D radar-camera SLAM system designed for kilometer-scale outdoor environments, utilizing 3D Gaussian as a differentiable spatial representation. Rad-GS combines the advantages of raw radar point cloud with Doppler information and geometrically enhanced point cloud to guide dynamic object masking in synchronized images, thereby alleviating rendering artifacts and improving localization accuracy. Additionally, unsynchronized image frames are leveraged to globally refine the 3D Gaussian representation, enhancing texture consistency and novel view synthesis fidelity. Furthermore, the global octree structure coupled with a targeted Gaussian primitive management strategy further suppresses noise and significantly reduces memory consumption in large-scale environments. Extensive experiments and ablation studies demonstrate that Rad-GS achieves performance comparable to traditional 3D Gaussian methods based on camera or LiDAR inputs, highlighting the feasibility of robust outdoor mapping using 4D mmWave radar. Real-world reconstruction at kilometer scale validates the potential of Rad-GS for large-scale scene reconstruction.

