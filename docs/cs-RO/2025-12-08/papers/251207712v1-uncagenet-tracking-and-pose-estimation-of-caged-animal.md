---
layout: default
title: UnCageNet: Tracking and Pose Estimation of Caged Animal
---

# UnCageNet: Tracking and Pose Estimation of Caged Animal

**arXiv**: [2512.07712v1](https://arxiv.org/abs/2512.07712) | [PDF](https://arxiv.org/pdf/2512.07712.pdf)

**作者**: Sayak Dutta, Harish Katti, Shashikant Verma, Shanmuganathan Raman

---

## 💡 一句话要点

**提出UnCageNet三阶段预处理流程，以解决笼子遮挡下动物追踪与姿态估计性能下降问题**

**关键词**: `笼子分割` `姿态估计` `动物追踪` `遮挡修复` `Gabor滤波器` `预处理流程`

## 📋 核心要点

1. 核心问题：现有动物追踪与姿态估计系统在笼子结构和系统性遮挡下性能显著下降
2. 方法要点：采用Gabor增强ResNet-UNet进行笼子分割，CRFill进行笼子修复，再评估去遮挡后的帧
3. 实验或效果：通过去除笼子遮挡，实现与无遮挡环境相当的姿态估计和追踪性能，关键点检测精度和轨迹一致性显著提升

## 📄 摘要（原文）

> Animal tracking and pose estimation systems, such as STEP (Simultaneous Tracking and Pose Estimation) and ViTPose, experience substantial performance drops when processing images and videos with cage structures and systematic occlusions. We present a three-stage preprocessing pipeline that addresses this limitation through: (1) cage segmentation using a Gabor-enhanced ResNet-UNet architecture with tunable orientation filters, (2) cage inpainting using CRFill for content-aware reconstruction of occluded regions, and (3) evaluation of pose estimation and tracking on the uncaged frames. Our Gabor-enhanced segmentation model leverages orientation-aware features with 72 directional kernels to accurately identify and segment cage structures that severely impair the performance of existing methods. Experimental validation demonstrates that removing cage occlusions through our pipeline enables pose estimation and tracking performance comparable to that in environments without occlusions. We also observe significant improvements in keypoint detection accuracy and trajectory consistency.

