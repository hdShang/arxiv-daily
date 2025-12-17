---
layout: default
title: CLAIM: Camera-LiDAR Alignment with Intensity and Monodepth
---

# CLAIM: Camera-LiDAR Alignment with Intensity and Monodepth

**arXiv**: [2512.14001v1](https://arxiv.org/abs/2512.14001) | [PDF](https://arxiv.org/pdf/2512.14001.pdf)

**作者**: Zhuo Zhang, Yonghui Liu, Meijie Zhang, Feiyang Tan, Yikang Ding

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-16

**备注**: Accepted by IROS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Tompson11/claim)

---

## 💡 一句话要点

**提出CLAIM方法，利用单目深度模型和粗到精搜索策略，解决相机与LiDAR数据对齐问题，无需复杂特征处理。**

🎯 **匹配领域**: **自动驾驶**

**关键词**: `相机-LiDAR对齐` `单目深度模型` `粗到精搜索` `结构损失` `纹理损失` `多模态融合` `自动驾驶` `点云处理`

## 📋 核心要点

1. 现有相机-LiDAR对齐方法通常依赖复杂的数据处理、特征提取或匹配步骤，导致计算成本高且适应性受限。
2. CLAIM利用单目深度模型，通过粗到精搜索最小化结构损失和纹理损失，实现高效对齐，无需复杂特征处理。
3. 在KITTI、Waymo和MIAS-LCEC数据集上，CLAIM表现出优于现有方法的性能，验证了其有效性和泛化能力。

## 📝 摘要（中文）

本文释放了强大单目深度模型在相机-LiDAR标定中的潜力，提出了CLAIM，一种新颖的相机与LiDAR数据对齐方法。给定初始猜测和图像-LiDAR点云对，CLAIM采用粗到精搜索策略，寻找最优变换以最小化基于补丁皮尔逊相关的结构损失和基于互信息的纹理损失。这两种损失作为相机-LiDAR对齐结果的良好度量，无需像大多数方法那样进行复杂的数据处理、特征提取或特征匹配步骤，使我们的方法简单且适应大多数场景。我们在公开的KITTI、Waymo和MIAS-LCEC数据集上验证了CLAIM，实验结果表明其性能优于最先进的方法。代码可在https://github.com/Tompson11/claim获取。

## 🔬 方法详解

CLAIM的整体框架基于粗到精搜索策略，输入初始变换猜测和图像-LiDAR点云对，迭代优化变换参数。关键技术创新包括：使用基于补丁皮尔逊相关的结构损失来度量几何对齐，以及基于互信息的纹理损失来评估外观一致性。与现有方法的主要区别在于，CLAIM无需复杂的特征提取或匹配步骤，直接利用单目深度模型和损失函数，简化了流程并提高了适应性。

## 📊 实验亮点

在KITTI、Waymo和MIAS-LCEC数据集上的实验显示，CLAIM在相机-LiDAR对齐任务中性能优于最先进方法，验证了其损失函数的有效性和方法的泛化能力，代码已开源。

## 🎯 应用场景

该研究可应用于自动驾驶、机器人导航和增强现实等领域，通过精确对齐相机与LiDAR数据，提升多模态感知系统的准确性和鲁棒性，支持环境建模和物体检测任务。

## 📄 摘要（原文）

> In this paper, we unleash the potential of the powerful monodepth model in camera-LiDAR calibration and propose CLAIM, a novel method of aligning data from the camera and LiDAR. Given the initial guess and pairs of images and LiDAR point clouds, CLAIM utilizes a coarse-to-fine searching method to find the optimal transformation minimizing a patched Pearson correlation-based structure loss and a mutual information-based texture loss. These two losses serve as good metrics for camera-LiDAR alignment results and require no complicated steps of data processing, feature extraction, or feature matching like most methods, rendering our method simple and adaptive to most scenes. We validate CLAIM on public KITTI, Waymo, and MIAS-LCEC datasets, and the experimental results demonstrate its superior performance compared with the state-of-the-art methods. The code is available at https://github.com/Tompson11/claim.

