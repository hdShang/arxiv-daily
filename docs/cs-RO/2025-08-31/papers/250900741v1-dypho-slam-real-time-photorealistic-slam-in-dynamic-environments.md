---
layout: default
title: "DyPho-SLAM : Real-time Photorealistic SLAM in Dynamic Environments"
---

# DyPho-SLAM : Real-time Photorealistic SLAM in Dynamic Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00741" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00741v1</a>
  <a href="https://arxiv.org/pdf/2509.00741.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00741v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00741v1', 'DyPho-SLAM : Real-time Photorealistic SLAM in Dynamic Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Liu, Keyu Fan, Bin Lan, Houde Liu

**分类**: cs.RO

**发布日期**: 2025-08-31

**备注**: Accepted by ICME 2025(Oral)

---

## 💡 一句话要点

**提出DyPho-SLAM以解决动态环境中的实时视觉SLAM问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉SLAM` `动态环境` `高保真映射` `相机位姿估计` `自适应特征提取` `实时处理` `稠密地图`

## 📋 核心要点

1. 现有视觉SLAM方法在静态环境中表现良好，但在动态环境中容易出现相机跟踪漂移和模糊映射的问题。
2. DyPho-SLAM通过整合先前图像信息生成精细掩模，减少动态物体对映射的干扰，并采用自适应特征提取策略提升系统的鲁棒性。
3. 在公开的动态RGB-D数据集上进行的实验表明，DyPho-SLAM在相机位姿估计和稠密地图重建方面达到了最先进的性能，并且能够实时运行。

## 📝 摘要（中文）

视觉SLAM算法在高保真稠密地图生成方面得到了增强，但在动态环境中，现有方法常常面临相机跟踪漂移和模糊映射的问题。本文提出了DyPho-SLAM，这是一种实时、资源高效的视觉SLAM系统，旨在解决动态物体环境中的定位和高保真映射挑战。该系统通过整合先前图像信息生成精细掩模，有效减少掩模误判带来的噪声。此外，论文还设计了自适应特征提取策略，以增强去除动态障碍物后的优化约束。实验结果表明，该系统在动态场景中实现了相机位姿估计和稠密地图重建的最先进性能。

## 🔬 方法详解

**问题定义**：本文旨在解决动态环境中视觉SLAM系统的定位和高保真映射问题。现有方法在处理动态物体时，常常出现相机跟踪漂移和模糊映射，导致性能下降。

**核心思路**：DyPho-SLAM通过整合先前图像信息生成精细掩模，从而有效减少动态物体对映射的干扰。此外，采用自适应特征提取策略来增强优化约束，提高系统在动态环境中的鲁棒性。

**技术框架**：DyPho-SLAM的整体架构包括图像信息整合模块、掩模生成模块和自适应特征提取模块。系统通过实时处理输入图像，生成高保真稠密地图，并进行相机位姿估计。

**关键创新**：DyPho-SLAM的主要创新在于其掩模生成策略和自适应特征提取方法。这些创新使得系统在动态环境中能够有效减少噪声，提高映射精度，与现有方法相比具有显著优势。

**关键设计**：在设计中，系统采用了优化的损失函数来平衡掩模生成和特征提取的效果，同时在网络结构上进行了调整，以适应动态场景的特征提取需求。

## 📊 实验亮点

DyPho-SLAM在公开的动态RGB-D数据集上表现出色，相机位姿估计和稠密地图重建的性能达到了最先进水平，具体提升幅度超过了现有基线方法，展示了其在动态场景中的强大能力。

## 🎯 应用场景

DyPho-SLAM在动态环境中的高效定位和映射能力使其在自动驾驶、机器人导航和增强现实等领域具有广泛的应用潜力。该系统的实时性能和高保真映射能力将推动相关技术的进步和应用落地。

## 📄 摘要（原文）

> Visual SLAM algorithms have been enhanced through the exploration of Gaussian Splatting representations, particularly in generating high-fidelity dense maps. While existing methods perform reliably in static environments, they often encounter camera tracking drift and fuzzy mapping when dealing with the disturbances caused by moving objects. This paper presents DyPho-SLAM, a real-time, resource-efficient visual SLAM system designed to address the challenges of localization and photorealistic mapping in environments with dynamic objects. Specifically, the proposed system integrates prior image information to generate refined masks, effectively minimizing noise from mask misjudgment. Additionally, to enhance constraints for optimization after removing dynamic obstacles, we devise adaptive feature extraction strategies significantly improving the system's resilience. Experiments conducted on publicly dynamic RGB-D datasets demonstrate that the proposed system achieves state-of-the-art performance in camera pose estimation and dense map reconstruction, while operating in real-time in dynamic scenes.

