---
layout: default
title: "ScrewSplat: An End-to-End Method for Articulated Object Recognition"
---

# ScrewSplat: An End-to-End Method for Articulated Object Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02146" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02146v2</a>
  <a href="https://arxiv.org/pdf/2508.02146.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02146v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02146v2', 'ScrewSplat: An End-to-End Method for Articulated Object Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seungyeon Kim, Junsu Ha, Young Hun Kim, Yonghyeon Lee, Frank C. Park

**分类**: cs.RO, cs.CV

**发布日期**: 2025-08-04 (更新: 2025-08-22)

**备注**: 26 pages, 12 figures, Conference on Robot Learning (CoRL) 2025

---

## 💡 一句话要点

**提出ScrewSplat以解决关节物体识别问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `关节物体识别` `RGB图像处理` `高斯点云` `机器人操作` `零样本学习`

## 📋 核心要点

1. 现有的关节物体识别方法依赖于强假设或额外输入，限制了其在真实场景中的实用性。
2. ScrewSplat是一种端到端的方法，仅使用RGB图像，通过优化螺旋轴来恢复物体的运动结构。
3. 该方法在多种关节物体上实现了最先进的识别精度，并支持基于文本的零样本操作。

## 📝 摘要（中文）

关节物体识别是识别具有可动部件的物体几何形状和运动关节的任务，对于机器人与日常物体的交互至关重要。然而，现有方法往往依赖于强假设，如已知的关节数量，或需要额外输入（如深度图像），或涉及复杂的中间步骤，限制了其在实际应用中的可行性。本文提出了ScrewSplat，这是一种简单的端到端方法，仅基于RGB观察。该方法通过随机初始化螺旋轴并进行迭代优化，恢复物体的运动结构。通过与高斯点云重建结合，我们同时重建3D几何形状并将物体分割为刚性和可动部件。实验表明，我们的方法在多样化的关节物体上实现了最先进的识别精度，并进一步支持基于文本的零样本操作。

## 🔬 方法详解

**问题定义**：本文旨在解决关节物体识别的问题，现有方法常常依赖于已知的关节数量或额外的深度信息，导致在实际应用中存在局限性。

**核心思路**：ScrewSplat通过随机初始化螺旋轴并进行迭代优化，直接从RGB图像中恢复物体的运动结构，避免了对额外输入的依赖。

**技术框架**：该方法的整体架构包括随机初始化、螺旋轴优化和高斯点云重建三个主要模块，最终实现3D几何形状重建和物体分割。

**关键创新**：ScrewSplat的核心创新在于其端到端的设计，能够在没有深度信息的情况下，直接从RGB图像中提取关节信息，显著简化了传统方法的复杂性。

**关键设计**：在实现过程中，采用了特定的损失函数来优化螺旋轴的配置，并结合高斯点云技术进行几何重建，确保了识别精度和效率。

## 📊 实验亮点

实验结果表明，ScrewSplat在多种关节物体上实现了最先进的识别精度，相较于现有基线方法，识别准确率提升了XX%（具体数据未知），并成功支持了零样本、文本引导的操作。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、智能家居和人机交互等场景。通过提高关节物体的识别精度，ScrewSplat能够使机器人更好地理解和操作日常物体，从而提升其在实际环境中的应用价值和效率。

## 📄 摘要（原文）

> Articulated object recognition -- the task of identifying both the geometry and kinematic joints of objects with movable parts -- is essential for enabling robots to interact with everyday objects such as doors and laptops. However, existing approaches often rely on strong assumptions, such as a known number of articulated parts; require additional inputs, such as depth images; or involve complex intermediate steps that can introduce potential errors -- limiting their practicality in real-world settings. In this paper, we introduce ScrewSplat, a simple end-to-end method that operates solely on RGB observations. Our approach begins by randomly initializing screw axes, which are then iteratively optimized to recover the object's underlying kinematic structure. By integrating with Gaussian Splatting, we simultaneously reconstruct the 3D geometry and segment the object into rigid, movable parts. We demonstrate that our method achieves state-of-the-art recognition accuracy across a diverse set of articulated objects, and further enables zero-shot, text-guided manipulation using the recovered kinematic model. See the project website at: https://screwsplat.github.io.

