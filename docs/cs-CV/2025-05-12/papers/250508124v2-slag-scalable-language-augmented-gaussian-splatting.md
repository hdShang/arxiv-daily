---
layout: default
title: SLAG: Scalable Language-Augmented Gaussian Splatting
---

# SLAG: Scalable Language-Augmented Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08124" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08124v2</a>
  <a href="https://arxiv.org/pdf/2505.08124.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08124v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08124v2', 'SLAG: Scalable Language-Augmented Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Laszlo Szilagyi, Francis Engelmann, Jeannette Bohg

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-05-12 (更新: 2025-08-17)

**🔗 代码/项目**: [PROJECT_PAGE](https://slag-project.github.io/)

---

## 💡 一句话要点

**提出SLAG以解决大规模场景编码效率问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `高斯点云` `语言增强` `多GPU计算` `场景表示` `机器人技术` `嵌入计算` `智能城市` `实时应用`

## 📋 核心要点

1. 现有方法在处理大规模场景时面临计算资源限制和速度瓶颈，难以满足实时应用需求。
2. SLAG通过多GPU框架和高效的嵌入计算方法，提升了大规模场景的编码速度和可扩展性。
3. 实验结果显示，SLAG在嵌入计算上比OpenGaussian快18倍，同时保持了高质量的嵌入效果。

## 📝 摘要（中文）

语言增强的场景表示在大规模机器人应用中具有巨大潜力，如搜索与救援、智能城市和矿业等。这些场景通常对时间敏感，要求快速编码，同时又数据密集，亟需可扩展的解决方案。为此，本文提出SLAG，一个多GPU框架，通过语言增强的高斯点云加速大场景的嵌入速度和可扩展性。该方法将2D视觉语言模型特征整合到3D场景中，消除了以往方法中计算每个高斯语言嵌入所需的损失函数，而是通过归一化加权平均从3D高斯场景参数中推导嵌入。实验表明，SLAG在16-GPU设置下的嵌入计算速度比OpenGaussian快18倍，同时在ScanNet和LERF数据集上保持了嵌入质量。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模场景编码的效率问题，现有方法在计算资源有限的情况下难以实现快速且高质量的场景表示。

**核心思路**：SLAG通过多GPU并行处理和语言增强的高斯点云表示，消除了传统方法中对损失函数的依赖，从而实现高效的嵌入计算。

**技术框架**：SLAG的整体架构包括数据输入模块、2D视觉语言模型特征提取、3D高斯场景参数计算和嵌入存储与检索模块，支持高效的多GPU并行处理。

**关键创新**：SLAG的主要创新在于通过归一化加权平均从3D高斯场景参数中直接推导语言嵌入，显著提高了计算速度和并行化能力。

**关键设计**：在设计中，SLAG采用了高效的向量数据库用于嵌入存储与检索，确保了在大规模场景下的快速访问和处理。

## 📊 实验亮点

SLAG在16-GPU设置下的嵌入计算速度比OpenGaussian快18倍，展示了其在处理大规模场景时的卓越性能。同时，SLAG在ScanNet和LERF数据集上保持了高质量的嵌入效果，验证了其有效性和实用性。

## 🎯 应用场景

SLAG的研究成果在多个领域具有广泛的应用潜力，包括搜索与救援、智能城市管理和矿业等。这些领域通常需要快速处理和分析复杂的场景数据，SLAG的高效编码能力能够显著提升机器人在这些任务中的表现和反应速度，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Language-augmented scene representations hold great promise for large-scale robotics applications such as search-and-rescue, smart cities, and mining. Many of these scenarios are time-sensitive, requiring rapid scene encoding while also being data-intensive, necessitating scalable solutions. Deploying these representations on robots with limited computational resources further adds to the challenge. To address this, we introduce SLAG, a multi-GPU framework for language-augmented Gaussian splatting that enhances the speed and scalability of embedding large scenes. Our method integrates 2D visual-language model features into 3D scenes using SAM and CLIP. Unlike prior approaches, SLAG eliminates the need for a loss function to compute per-Gaussian language embeddings. Instead, it derives embeddings from 3D Gaussian scene parameters via a normalized weighted average, enabling highly parallelized scene encoding. Additionally, we introduce a vector database for efficient embedding storage and retrieval. Our experiments show that SLAG achieves an 18 times speedup in embedding computation on a 16-GPU setup compared to OpenGaussian, while preserving embedding quality on the ScanNet and LERF datasets. For more details, visit our project website: https://slag-project.github.io/.

