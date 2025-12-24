---
layout: default
title: "DynamicPose: Real-time and Robust 6D Object Pose Tracking for Fast-Moving Cameras and Objects"
---

# DynamicPose: Real-time and Robust 6D Object Pose Tracking for Fast-Moving Cameras and Objects

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11950" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11950v1</a>
  <a href="https://arxiv.org/pdf/2508.11950.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11950v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11950v1', 'DynamicPose: Real-time and Robust 6D Object Pose Tracking for Fast-Moving Cameras and Objects')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tingbang Liang, Yixin Zeng, Jiatong Xie, Boyu Zhou

**分类**: cs.CV, cs.RO

**发布日期**: 2025-08-16

---

## 💡 一句话要点

**提出DynamicPose以解决快速移动相机和物体的6D姿态跟踪问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `6D姿态跟踪` `视觉惯性里程计` `深度信息` `卡尔曼滤波器` `动态场景` `实时处理` `鲁棒性` `闭环系统`

## 📋 核心要点

1. 现有方法主要适用于静态场景，快速移动的相机和物体会导致跟踪性能显著下降。
2. 提出的DynamicPose框架通过视觉惯性里程计、深度信息驱动的2D跟踪器和VIO引导的卡尔曼滤波器来解决快速移动场景中的姿态跟踪问题。
3. 实验结果表明，DynamicPose在快速移动相机和物体的场景中实现了实时且鲁棒的6D姿态跟踪，显著提升了跟踪精度。

## 📝 摘要（中文）

我们提出了DynamicPose，一个无需重训练的6D姿态跟踪框架，旨在提高快速移动相机和物体场景下的跟踪鲁棒性。以往的方法主要适用于静态或准静态场景，当物体和相机快速移动时，其性能显著下降。为克服这些挑战，我们提出了三个协同组件：视觉惯性里程计用于补偿相机运动引起的兴趣区域（ROI）偏移；深度信息驱动的2D跟踪器修正因大物体平移造成的ROI偏差；VIO引导的卡尔曼滤波器预测物体旋转，生成多个候选姿态，并通过分层优化获得最终姿态。6D姿态跟踪结果指导后续的2D跟踪和卡尔曼滤波器更新，形成闭环系统，确保准确的姿态初始化和精确的姿态跟踪。仿真和实际实验表明我们的方法有效，实现了快速移动相机和物体的实时且鲁棒的6D姿态跟踪。

## 🔬 方法详解

**问题定义**：本论文旨在解决快速移动相机和物体场景下的6D姿态跟踪问题。现有方法在静态或准静态场景中表现良好，但在动态环境中性能显著下降，导致跟踪失败。

**核心思路**：DynamicPose框架通过引入视觉惯性里程计、深度信息驱动的2D跟踪器和VIO引导的卡尔曼滤波器，形成一个闭环系统，以提高快速移动场景中的跟踪鲁棒性和准确性。

**技术框架**：整体架构包括三个主要模块：视觉惯性里程计用于补偿相机运动引起的ROI偏移；深度信息驱动的2D跟踪器用于修正因物体平移造成的ROI偏差；VIO引导的卡尔曼滤波器用于预测物体旋转并优化姿态。

**关键创新**：最重要的创新点在于将视觉惯性里程计与深度信息结合，形成一个闭环系统，确保在快速移动场景中保持高精度的姿态跟踪。这一方法与传统静态跟踪方法有本质区别。

**关键设计**：在设计中，采用了深度信息来增强2D跟踪器的鲁棒性，并通过卡尔曼滤波器的分层优化来生成多个候选姿态，最终通过精细化处理获得准确的姿态输出。

## 📊 实验亮点

实验结果显示，DynamicPose在快速移动相机和物体的场景中实现了实时6D姿态跟踪，跟踪精度相比基线方法提升了显著的百分比，验证了其在动态环境中的有效性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、增强现实和机器人导航等。通过提高快速移动场景下的姿态跟踪精度，DynamicPose能够在复杂环境中实现更高效的物体识别和交互，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We present DynamicPose, a retraining-free 6D pose tracking framework that improves tracking robustness in fast-moving camera and object scenarios. Previous work is mainly applicable to static or quasi-static scenes, and its performance significantly deteriorates when both the object and the camera move rapidly. To overcome these challenges, we propose three synergistic components: (1) A visual-inertial odometry compensates for the shift in the Region of Interest (ROI) caused by camera motion; (2) A depth-informed 2D tracker corrects ROI deviations caused by large object translation; (3) A VIO-guided Kalman filter predicts object rotation, generates multiple candidate poses, and then obtains the final pose by hierarchical refinement. The 6D pose tracking results guide subsequent 2D tracking and Kalman filter updates, forming a closed-loop system that ensures accurate pose initialization and precise pose tracking. Simulation and real-world experiments demonstrate the effectiveness of our method, achieving real-time and robust 6D pose tracking for fast-moving cameras and objects.

