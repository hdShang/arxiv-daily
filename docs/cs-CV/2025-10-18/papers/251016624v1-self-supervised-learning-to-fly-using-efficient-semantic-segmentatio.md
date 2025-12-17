---
layout: default
title: Self-Supervised Learning to Fly using Efficient Semantic Segmentation and Metric Depth Estimation for Low-Cost Autonomous UAVs
---

# Self-Supervised Learning to Fly using Efficient Semantic Segmentation and Metric Depth Estimation for Low-Cost Autonomous UAVs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16624" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16624v1</a>
  <a href="https://arxiv.org/pdf/2510.16624.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16624v1" onclick="toggleFavorite(this, '2510.16624v1', 'Self-Supervised Learning to Fly using Efficient Semantic Segmentation and Metric Depth Estimation for Low-Cost Autonomous UAVs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sebastian Mocanu, Emil Slusanschi, Marius Leordeanu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-18

---

## 💡 一句话要点

**提出一种基于语义分割和单目深度估计的低成本无人机自主飞行方法。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `无人机自主导航` `语义分割` `单目深度估计` `知识蒸馏` `视觉SLAM` `度量深度估计` `低成本无人机`

## 📋 核心要点

1. 现有无人机自主导航依赖GPS或激光雷达等昂贵传感器，限制了其在资源受限环境中的应用。
2. 该论文提出了一种基于视觉的自主飞行系统，利用语义分割和单目深度估计实现避障和安全着陆。
3. 实验表明，该方法在真实和数字孪生环境中均表现良好，提高了任务成功率和效率。

## 📝 摘要（中文）

本文提出了一种仅使用视觉的小型无人机自主飞行系统，该系统在受控室内环境中运行。该系统结合了语义分割和单目深度估计，无需GPS或昂贵的传感器（如激光雷达）即可实现避障、场景探索和自主安全着陆操作。一个关键创新是自适应尺度因子算法，该算法通过利用语义地面平面检测和相机内部参数，将非度量单目深度预测转换为准确的度量距离测量，实现了14.4厘米的平均距离误差。该方法使用知识蒸馏框架，其中基于颜色的支持向量机（SVM）教师为轻量级U-Net学生网络（160万个参数）生成训练数据，该网络能够进行实时语义分割。对于更复杂的环境，SVM教师可以替换为最先进的分割模型。测试在一个受控的5x4米实验室环境中进行，其中包含八个模拟城市结构的纸板障碍物。在真实环境中进行的30次飞行测试和在数字孪生环境中进行的100次飞行测试的广泛验证表明，组合的分割和深度方法增加了监视期间的行驶距离并减少了任务时间，同时保持了100％的成功率。该系统通过端到端学习得到进一步优化，其中紧凑的学生神经网络从我们性能最佳的方法生成的演示数据中学习完整的飞行策略，从而实现了87.5％的自主任务成功率。这项工作推进了结构化环境中基于视觉的实用无人机导航，展示了度量深度估计和计算效率挑战的解决方案，从而可以在资源受限的平台上进行部署。

## 🔬 方法详解

**问题定义**：无人机在室内等GPS受限环境中自主导航，同时降低对昂贵传感器的依赖。现有方法通常依赖激光雷达或立体视觉，成本高昂且计算量大，难以在低成本无人机上部署。

**核心思路**：利用单目视觉信息，通过语义分割识别场景中的关键元素（如地面），并结合单目深度估计获取场景的几何信息。通过自适应尺度因子算法，将非度量深度信息转换为度量信息，从而实现准确的距离测量和导航。

**技术框架**：该系统包含以下主要模块：1) 语义分割模块：使用轻量级U-Net网络进行实时语义分割，识别地面等关键区域。2) 单目深度估计模块：估计场景的深度信息。3) 自适应尺度因子模块：将非度量深度信息转换为度量信息。4) 飞行控制模块：根据感知到的环境信息，控制无人机进行避障、探索和着陆等操作。

**关键创新**：1) 自适应尺度因子算法：该算法利用语义分割结果（地面检测）和相机内参，将单目深度估计的相对深度转换为绝对深度，从而实现准确的距离测量。2) 知识蒸馏框架：使用SVM教师网络生成训练数据，训练轻量级的U-Net学生网络，保证了实时性和准确性。

**关键设计**：1) 语义分割网络：采用轻量级的U-Net结构，参数量为1.6M，保证了实时性。2) 损失函数：未知。3) 自适应尺度因子：根据检测到的地面区域，计算深度图的尺度因子，将深度图转换为度量单位。

## 📊 实验亮点

该系统在真实环境中进行了30次飞行测试，在数字孪生环境中进行了100次飞行测试，均实现了100%的任务成功率。自适应尺度因子算法实现了14.4厘米的平均距离误差。通过端到端学习，系统实现了87.5%的自主任务成功率。

## 🎯 应用场景

该研究成果可应用于室内无人机自主导航、物流配送、安防巡检等领域。特别是在资源受限的环境中，例如仓库、地下停车场、矿井等，该系统能够以较低的成本实现无人机的自主飞行，具有重要的实际应用价值和商业前景。

## 📄 摘要（原文）

> This paper presents a vision-only autonomous flight system for small UAVs operating in controlled indoor environments. The system combines semantic segmentation with monocular depth estimation to enable obstacle avoidance, scene exploration, and autonomous safe landing operations without requiring GPS or expensive sensors such as LiDAR. A key innovation is an adaptive scale factor algorithm that converts non-metric monocular depth predictions into accurate metric distance measurements by leveraging semantic ground plane detection and camera intrinsic parameters, achieving a mean distance error of 14.4 cm. The approach uses a knowledge distillation framework where a color-based Support Vector Machine (SVM) teacher generates training data for a lightweight U-Net student network (1.6M parameters) capable of real-time semantic segmentation. For more complex environments, the SVM teacher can be replaced with a state-of-the-art segmentation model. Testing was conducted in a controlled 5x4 meter laboratory environment with eight cardboard obstacles simulating urban structures. Extensive validation across 30 flight tests in a real-world environment and 100 flight tests in a digital-twin environment demonstrates that the combined segmentation and depth approach increases the distance traveled during surveillance and reduces mission time while maintaining 100% success rates. The system is further optimized through end-to-end learning, where a compact student neural network learns complete flight policies from demonstration data generated by our best-performing method, achieving an 87.5% autonomous mission success rate. This work advances practical vision-based drone navigation in structured environments, demonstrating solutions for metric depth estimation and computational efficiency challenges that enable deployment on resource-constrained platforms.

