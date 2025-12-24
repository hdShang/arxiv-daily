---
layout: default
title: "Pseudo Depth Meets Gaussian: A Feed-forward RGB SLAM Baseline"
---

# Pseudo Depth Meets Gaussian: A Feed-forward RGB SLAM Baseline

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04597" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04597v1</a>
  <a href="https://arxiv.org/pdf/2508.04597.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04597v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04597v1', 'Pseudo Depth Meets Gaussian: A Feed-forward RGB SLAM Baseline')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linqing Zhao, Xiuwei Xu, Yirui Wang, Hao Wang, Wenzhao Zheng, Yansong Tang, Haibin Yan, Jiwen Lu

**分类**: cs.CV

**发布日期**: 2025-08-06

**备注**: IROS 2025

---

## 💡 一句话要点

**提出基于3D高斯映射的RGB SLAM方法以解决深度估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `RGB SLAM` `3D重建` `深度估计` `高斯映射` `前馈网络` `光流推断` `实时处理` `机器人导航`

## 📋 核心要点

1. 现有的RGB SLAM方法在长序列处理和深度传感器依赖上存在显著不足，影响了3D重建的效果。
2. 本文提出了一种结合3D高斯映射和前馈递归预测的在线3D重建方法，旨在提高跟踪速度和准确性。
3. 实验结果显示，该方法在多个数据集上与SplaTAM性能相当，但跟踪时间减少超过90%，展现出显著的效率提升。

## 📝 摘要（中文）

从无姿态的RGB流中逐步恢复真实尺寸的3D几何体是3D重建中的一项挑战，现有方法在长序列处理和深度传感器依赖上存在不足。本文首先将深度估计器集成到RGB-D SLAM系统中，但由于预测深度的几何细节不准确，导致效果受限。通过进一步研究，发现3D高斯映射能够有效解决这一问题。基于此，提出了一种结合3D高斯SLAM和前馈递归预测模块的在线3D重建方法，直接从光流推断相机姿态，显著提高了跟踪速度，并引入局部图形渲染技术以增强前馈姿态预测的鲁棒性。实验结果表明，该方法在Replica和TUM-RGBD数据集上表现与最先进的SplaTAM相当，同时跟踪时间减少超过90%。

## 🔬 方法详解

**问题定义**：本文旨在解决从无姿态RGB流中逐步恢复真实尺寸3D几何体的难题。现有方法在处理长序列时表现不佳，且依赖于深度传感器，导致效率低下。

**核心思路**：通过将深度估计器集成到RGB-D SLAM系统中，结合3D高斯映射，提出了一种新的在线3D重建方法。该方法通过光流直接推断相机姿态，避免了慢速的测试时优化。

**技术框架**：整体架构包括深度估计模块、3D高斯映射模块和前馈递归预测模块。首先通过深度估计获取初步深度信息，然后利用3D高斯映射进行几何重建，最后通过前馈递归模块进行姿态预测。

**关键创新**：最重要的技术创新在于引入3D高斯映射来解决深度估计的不准确性，并通过前馈网络替代传统的测试时优化，大幅提升了跟踪速度。

**关键设计**：在网络结构上，采用了前馈递归网络设计，优化了损失函数以提高姿态预测的准确性，同时引入局部图形渲染技术增强了鲁棒性。实验中对参数设置进行了细致调整，以确保模型的稳定性和高效性。

## 📊 实验亮点

实验结果表明，所提方法在Replica和TUM-RGBD数据集上的表现与最先进的SplaTAM相当，且跟踪时间减少超过90%。这一显著的效率提升展示了该方法在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、增强现实和虚拟现实等场景，能够为实时3D重建提供高效解决方案。其高效的跟踪能力和准确的几何重建将推动相关技术在工业和消费市场的应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Incrementally recovering real-sized 3D geometry from a pose-free RGB stream is a challenging task in 3D reconstruction, requiring minimal assumptions on input data. Existing methods can be broadly categorized into end-to-end and visual SLAM-based approaches, both of which either struggle with long sequences or depend on slow test-time optimization and depth sensors. To address this, we first integrate a depth estimator into an RGB-D SLAM system, but this approach is hindered by inaccurate geometric details in predicted depth. Through further investigation, we find that 3D Gaussian mapping can effectively solve this problem. Building on this, we propose an online 3D reconstruction method using 3D Gaussian-based SLAM, combined with a feed-forward recurrent prediction module to directly infer camera pose from optical flow. This approach replaces slow test-time optimization with fast network inference, significantly improving tracking speed. Additionally, we introduce a local graph rendering technique to enhance robustness in feed-forward pose prediction. Experimental results on the Replica and TUM-RGBD datasets, along with a real-world deployment demonstration, show that our method achieves performance on par with the state-of-the-art SplaTAM, while reducing tracking time by more than 90\%.

