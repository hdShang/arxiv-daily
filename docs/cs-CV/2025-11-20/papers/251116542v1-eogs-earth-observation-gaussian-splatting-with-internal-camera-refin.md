---
layout: default
title: EOGS++: Earth Observation Gaussian Splatting with Internal Camera Refinement and Direct Panchromatic Rendering
---

# EOGS++: Earth Observation Gaussian Splatting with Internal Camera Refinement and Direct Panchromatic Rendering

**arXiv**: [2511.16542v1](https://arxiv.org/abs/2511.16542) | [PDF](https://arxiv.org/pdf/2511.16542.pdf)

**作者**: Pierrick Bournez, Luca Savant Aira, Thibaud Ehret, Gabriele Facciolo

---

## 💡 一句话要点

**提出EOGS++方法以改进卫星图像三维重建，通过内部相机优化和直接全色渲染提升精度与效率。**

**关键词**: `地球观测三维重建` `高斯泼溅` `相机姿态优化` `全色渲染` `卫星图像处理` `几何精度提升`

## 📋 核心要点

1. 核心问题：卫星图像三维重建依赖外部预处理和相机姿态估计，影响精度与效率。
2. 方法要点：引入内部相机优化和直接全色渲染，避免外部工具，改进几何准确性。
3. 实验效果：在IARPA 2016和DFC2019数据集上，MAE误差从1.33降至1.19，优于现有方法。

## 📄 摘要（原文）

> Recently, 3D Gaussian Splatting has been introduced as a compelling alternative to NeRF for Earth observation, offering com- petitive reconstruction quality with significantly reduced training times. In this work, we extend the Earth Observation Gaussian Splatting (EOGS) framework to propose EOGS++, a novel method tailored for satellite imagery that directly operates on raw high-resolution panchromatic data without requiring external preprocessing. Furthermore, leveraging optical flow techniques we embed bundle adjustment directly within the training process, avoiding reliance on external optimization tools while improving camera pose estimation. We also introduce several improvements to the original implementation, including early stopping and TSDF post-processing, all contributing to sharper reconstructions and better geometric accuracy. Experiments on the IARPA 2016 and DFC2019 datasets demonstrate that EOGS++ achieves state-of-the-art performance in terms of reconstruction quality and effi- ciency, outperforming the original EOGS method and other NeRF-based methods while maintaining the computational advantages of Gaussian Splatting. Our model demonstrates an improvement from 1.33 to 1.19 mean MAE errors on buildings compared to the original EOGS models

