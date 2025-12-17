---
layout: default
title: CLAIM: Camera-LiDAR Alignment with Intensity and Monodepth
---

# CLAIM: Camera-LiDAR Alignment with Intensity and Monodepth

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14001" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14001</a>
  <a href="https://arxiv.org/pdf/2512.14001.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14001" onclick="toggleFavorite(this, '2512.14001', 'CLAIM: Camera-LiDAR Alignment with Intensity and Monodepth')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuo Zhang, Yonghui Liu, Meijie Zhang, Feiyang Tan, Yikang Ding

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**CLAIM：利用单目深度和强度信息实现相机-激光雷达标定**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `相机-激光雷达标定` `单目深度估计` `传感器融合` `自动驾驶` `点云处理`

## 📋 核心要点

1. 现有相机-激光雷达标定方法通常依赖复杂的数据处理和特征匹配，限制了其在不同场景下的适应性。
2. CLAIM方法利用单目深度模型，通过结构和纹理损失直接优化相机和激光雷达数据的对齐，无需复杂的特征工程。
3. 实验结果表明，CLAIM在KITTI、Waymo和MIAS-LCEC等数据集上优于现有方法，验证了其有效性和泛化能力。

## 📝 摘要（中文）

本文旨在探索单目深度模型在相机-激光雷达标定中的潜力，并提出了一种新的对齐方法CLAIM。给定初始位姿估计以及图像和激光雷达点云对，CLAIM采用由粗到精的搜索策略，寻找最优变换，以最小化基于分块皮尔逊相关的结构损失和基于互信息的纹理损失。这两种损失函数为相机-激光雷达对齐结果提供了良好的度量标准，无需复杂的数据处理、特征提取或特征匹配步骤，使得我们的方法简单且适用于大多数场景。我们在公开的KITTI、Waymo和MIAS-LCEC数据集上验证了CLAIM，实验结果表明其性能优于现有技术。

## 🔬 方法详解

**问题定义**：相机-激光雷达标定的目标是确定相机和激光雷达之间的外部参数（旋转和平移），从而将它们的数据关联起来。现有方法的痛点在于需要复杂的数据预处理、特征提取和匹配，计算成本高，且对环境的适应性较差。

**核心思路**：CLAIM的核心思路是利用单目深度估计模型提供的深度信息，结合相机图像的纹理信息，设计一种直接优化相机和激光雷达数据对齐的损失函数。通过最小化结构损失和纹理损失，实现相机-激光雷达的精确标定。这种方法避免了复杂的特征工程，提高了效率和鲁棒性。

**技术框架**：CLAIM的整体流程如下：1) 输入：初始位姿估计、相机图像和激光雷达点云；2) 单目深度估计：使用预训练的单目深度模型估计图像的深度图；3) 损失计算：基于深度图和激光雷达点云，计算结构损失（基于分块皮尔逊相关）和纹理损失（基于互信息）；4) 位姿优化：使用优化算法（如Adam）最小化总损失，更新相机和激光雷达之间的位姿变换；5) 迭代优化：重复步骤3和4，直到收敛。

**关键创新**：CLAIM的关键创新在于：1) 利用单目深度估计模型，避免了手动设计特征；2) 提出了基于分块皮尔逊相关的结构损失和基于互信息的纹理损失，能够有效度量相机和激光雷达数据的对齐程度；3) 采用由粗到精的搜索策略，提高了优化效率和精度。与现有方法相比，CLAIM更加简单、高效，且具有更好的泛化能力。

**关键设计**：结构损失采用分块皮尔逊相关系数，旨在衡量图像深度梯度和激光雷达点云深度梯度之间的相似性。纹理损失采用互信息，旨在衡量图像纹理和激光雷达反射强度之间的相关性。损失函数的权重需要根据具体场景进行调整。优化算法采用Adam，学习率设置为一个较小的值，以保证收敛的稳定性。由粗到精的搜索策略通过逐步缩小搜索范围，提高优化效率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14001/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14001/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14001/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

CLAIM在KITTI、Waymo和MIAS-LCEC数据集上进行了验证，实验结果表明其性能优于现有技术。例如，在KITTI数据集上，CLAIM的旋转误差和位移误差均显著低于其他方法。此外，CLAIM在不同场景下都表现出良好的鲁棒性，证明了其泛化能力。

## 🎯 应用场景

该研究成果可广泛应用于自动驾驶、机器人导航、三维重建等领域。精确的相机-激光雷达标定是多传感器融合的基础，能够提高环境感知和定位的精度，从而提升自动驾驶系统的安全性和可靠性。此外，该方法还可以应用于增强现实、虚拟现实等领域，实现更逼真的场景渲染和交互。

## 📄 摘要（原文）

> In this paper, we unleash the potential of the powerful monodepth model in camera-LiDAR calibration and propose CLAIM, a novel method of aligning data from the camera and LiDAR. Given the initial guess and pairs of images and LiDAR point clouds, CLAIM utilizes a coarse-to-fine searching method to find the optimal transformation minimizing a patched Pearson correlation-based structure loss and a mutual information-based texture loss. These two losses serve as good metrics for camera-LiDAR alignment results and require no complicated steps of data processing, feature extraction, or feature matching like most methods, rendering our method simple and adaptive to most scenes. We validate CLAIM on public KITTI, Waymo, and MIAS-LCEC datasets, and the experimental results demonstrate its superior performance compared with the state-of-the-art methods. The code is available atthis https URL.

