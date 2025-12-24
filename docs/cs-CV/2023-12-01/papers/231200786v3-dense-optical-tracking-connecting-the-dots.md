---
layout: default
title: "Dense Optical Tracking: Connecting the Dots"
---

# Dense Optical Tracking: Connecting the Dots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00786" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00786v3</a>
  <a href="https://arxiv.org/pdf/2312.00786.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00786v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00786v3', 'Dense Optical Tracking: Connecting the Dots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guillaume Le Moing, Jean Ponce, Cordelia Schmid

**分类**: cs.CV

**发布日期**: 2023-12-01 (更新: 2024-03-04)

**备注**: Accepted to CVPR 2024

**🔗 代码/项目**: [PROJECT_PAGE](https://16lemoing.github.io/dot)

---

## 💡 一句话要点

**提出DOT方法以解决视频点跟踪速度慢的问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视频点跟踪` `光流估计` `遮挡处理` `计算机视觉` `实时监控` `机器人导航` `合成数据`

## 📋 核心要点

1. 现有的点跟踪方法在处理视频时速度较慢，无法在合理时间内跟踪每个观察到的点。
2. DOT方法通过提取运动边界的关键区域轨迹，并利用可学习的光流估计器来处理遮挡问题，显著提高了跟踪速度和准确性。
3. 实验结果显示，DOT在准确性上超越了现有光流技术，并且在速度上至少快两个数量级，验证了其有效性。

## 📝 摘要（中文）

近年来的点跟踪方法能够在视频中恢复场景点的轨迹，尽管存在遮挡问题，但在实际应用中跟踪每个点的速度仍然过慢。本文提出了一种新颖、简单且高效的方法DOT，首先通过现成的点跟踪算法从运动边界的关键区域提取一小部分轨迹。然后，DOT在给定源帧和目标帧的情况下，通过最近邻插值计算稠密光流场和可见性掩码的粗略初始估计，接着利用可学习的光流估计器进行精细化处理，该估计器显式处理遮挡，并可以在具有真实对应关系的合成数据上进行训练。实验结果表明，DOT在准确性上显著优于当前的光流技术，并且在速度上至少快两个数量级。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频点跟踪方法在速度和准确性上的不足，尤其是在处理遮挡时的性能问题。现有方法往往无法在合理时间内跟踪每个点，导致实际应用受限。

**核心思路**：DOT方法的核心思想是通过提取运动边界的关键区域轨迹，结合最近邻插值和可学习的光流估计器，来快速且准确地估计稠密光流场和可见性掩码，从而提高跟踪效率。

**技术框架**：DOT的整体架构包括几个主要模块：首先，使用现成的点跟踪算法从关键区域提取轨迹；其次，通过最近邻插值计算初始的光流场和可见性掩码；最后，利用可学习的光流估计器进行精细化处理，特别处理遮挡情况。

**关键创新**：DOT的主要创新在于其高效的处理流程和可学习的光流估计器，能够显式处理遮挡问题，并且在速度上相较于传统方法有显著提升。

**关键设计**：在设计上，DOT采用了简单的最近邻插值方法来初步估计光流场，并通过训练得到的损失函数优化光流估计器，确保其在合成数据上能够有效学习真实对应关系。

## 📊 实验亮点

实验结果表明，DOT在准确性上显著优于当前的光流技术，并且在速度上至少快两个数量级。与复杂的“通用”跟踪器OmniMotion相比，DOT表现更佳，且与最佳点跟踪算法CoTracker相当或更好，展示了其卓越的性能。

## 🎯 应用场景

DOT方法在视频分析、计算机视觉和机器人导航等领域具有广泛的应用潜力。其高效的点跟踪能力能够支持实时监控、自动驾驶以及增强现实等技术的发展，提升这些领域的智能化水平。

## 📄 摘要（原文）

> Recent approaches to point tracking are able to recover the trajectory of any scene point through a large portion of a video despite the presence of occlusions. They are, however, too slow in practice to track every point observed in a single frame in a reasonable amount of time. This paper introduces DOT, a novel, simple and efficient method for solving this problem. It first extracts a small set of tracks from key regions at motion boundaries using an off-the-shelf point tracking algorithm. Given source and target frames, DOT then computes rough initial estimates of a dense flow field and visibility mask through nearest-neighbor interpolation, before refining them using a learnable optical flow estimator that explicitly handles occlusions and can be trained on synthetic data with ground-truth correspondences. We show that DOT is significantly more accurate than current optical flow techniques, outperforms sophisticated "universal" trackers like OmniMotion, and is on par with, or better than, the best point tracking algorithms like CoTracker while being at least two orders of magnitude faster. Quantitative and qualitative experiments with synthetic and real videos validate the promise of the proposed approach. Code, data, and videos showcasing the capabilities of our approach are available in the project webpage: https://16lemoing.github.io/dot .

