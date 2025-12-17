---
layout: default
title: OpenInsGaussian: Open-vocabulary Instance Gaussian Segmentation with Context-aware Cross-view Fusion
---

# OpenInsGaussian: Open-vocabulary Instance Gaussian Segmentation with Context-aware Cross-view Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.18253" class="toolbar-btn" target="_blank">📄 arXiv: 2510.18253v1</a>
  <a href="https://arxiv.org/pdf/2510.18253.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.18253v1" onclick="toggleFavorite(this, '2510.18253v1', 'OpenInsGaussian: Open-vocabulary Instance Gaussian Segmentation with Context-aware Cross-view Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyu Huang, Runnan Chen, Dongting Hu, Fengming Huang, Mingming Gong, Tongliang Liu

**分类**: cs.CV

**发布日期**: 2025-10-21

---

## 💡 一句话要点

**提出OpenInsGaussian，通过上下文感知跨视角融合实现开放词汇实例高斯分割。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D场景理解` `高斯溅射` `实例分割` `开放词汇` `跨视角融合` `上下文感知` `注意力机制`

## 📋 核心要点

1. 现有方法在3D场景理解中，利用2D视觉模型投影语义特征，但缺乏足够的上下文信息和跨视角一致性。
2. OpenInsGaussian通过上下文感知特征提取和注意力驱动的特征聚合，增强特征表达并提升跨视角融合效果。
3. 实验结果表明，OpenInsGaussian在开放词汇3D高斯分割任务上显著优于现有方法，展现了其优越性能。

## 📝 摘要（中文）

本文提出OpenInsGaussian，一个具有上下文感知跨视角融合的开放词汇实例高斯分割框架。现有语义高斯溅射方法利用大规模2D视觉模型将2D语义特征投影到3D场景中，但存在两个主要限制：(1)预处理期间个体掩码的上下文线索不足；(2)融合来自这些2D模型的多视角特征时，存在不一致和细节缺失。OpenInsGaussian包含两个模块：上下文感知特征提取，增强每个掩码的丰富语义上下文；注意力驱动的特征聚合，选择性地融合多视角特征，以减轻对齐误差和不完整性。在基准数据集上的大量实验表明，OpenInsGaussian在开放词汇3D高斯分割中实现了最先进的结果，大幅优于现有基线。这些发现强调了该方法的鲁棒性和通用性，标志着3D场景理解及其在各种实际场景中的实际部署向前迈出了重要一步。

## 🔬 方法详解

**问题定义**：论文旨在解决开放词汇3D场景理解中的实例分割问题，特别是基于高斯溅射表示的场景。现有方法，如语义高斯溅射，依赖于2D视觉模型提取特征并投影到3D空间，但面临两个主要挑战：一是2D掩码在预处理阶段缺乏足够的上下文信息，导致分割不准确；二是多视角特征融合时存在对齐误差和信息缺失，影响最终的分割效果。

**核心思路**：OpenInsGaussian的核心思路是通过引入上下文感知和跨视角融合机制来增强特征表达和提高分割精度。具体来说，首先通过上下文感知特征提取模块为每个掩码补充丰富的语义上下文信息，然后利用注意力驱动的特征聚合模块选择性地融合多视角特征，从而减轻对齐误差和信息缺失。

**技术框架**：OpenInsGaussian框架主要包含两个模块：(1) 上下文感知特征提取模块：该模块旨在为每个2D掩码提取更丰富的上下文信息，从而提升后续的3D分割效果。(2) 注意力驱动的特征聚合模块：该模块用于融合来自不同视角的特征，并利用注意力机制来选择性地聚合信息，从而减轻对齐误差和信息缺失。整体流程是首先利用2D视觉模型提取多视角特征，然后通过上下文感知特征提取模块增强特征表达，最后通过注意力驱动的特征聚合模块融合多视角特征并进行3D实例分割。

**关键创新**：OpenInsGaussian的关键创新在于其上下文感知特征提取和注意力驱动的特征聚合机制。上下文感知特征提取模块能够有效地为每个掩码补充丰富的语义上下文信息，从而提升分割精度。注意力驱动的特征聚合模块能够选择性地融合多视角特征，从而减轻对齐误差和信息缺失，提高分割的鲁棒性。

**关键设计**：在上下文感知特征提取模块中，具体实现方式未知。在注意力驱动的特征聚合模块中，使用了注意力机制来衡量不同视角特征的重要性，并根据重要性进行加权融合。具体的注意力网络结构和损失函数细节未知。

## 📊 实验亮点

OpenInsGaussian在开放词汇3D高斯分割任务上取得了显著的性能提升，大幅优于现有基线方法。具体性能数据和提升幅度未知，但摘要中强调了其在基准数据集上实现了state-of-the-art的结果，表明其具有很强的竞争力。

## 🎯 应用场景

OpenInsGaussian在自动驾驶、机器人和增强现实等领域具有广泛的应用前景。例如，在自动驾驶中，它可以用于准确地分割场景中的车辆、行人等物体，从而提高驾驶安全性。在机器人领域，它可以用于理解周围环境，从而实现更智能的导航和操作。在增强现实领域，它可以用于将虚拟物体与真实场景进行更自然的融合。

## 📄 摘要（原文）

> Understanding 3D scenes is pivotal for autonomous driving, robotics, and augmented reality. Recent semantic Gaussian Splatting approaches leverage large-scale 2D vision models to project 2D semantic features onto 3D scenes. However, they suffer from two major limitations: (1) insufficient contextual cues for individual masks during preprocessing and (2) inconsistencies and missing details when fusing multi-view features from these 2D models. In this paper, we introduce \textbf{OpenInsGaussian}, an \textbf{Open}-vocabulary \textbf{Ins}tance \textbf{Gaussian} segmentation framework with Context-aware Cross-view Fusion. Our method consists of two modules: Context-Aware Feature Extraction, which augments each mask with rich semantic context, and Attention-Driven Feature Aggregation, which selectively fuses multi-view features to mitigate alignment errors and incompleteness. Through extensive experiments on benchmark datasets, OpenInsGaussian achieves state-of-the-art results in open-vocabulary 3D Gaussian segmentation, outperforming existing baselines by a large margin. These findings underscore the robustness and generality of our proposed approach, marking a significant step forward in 3D scene understanding and its practical deployment across diverse real-world scenarios.

