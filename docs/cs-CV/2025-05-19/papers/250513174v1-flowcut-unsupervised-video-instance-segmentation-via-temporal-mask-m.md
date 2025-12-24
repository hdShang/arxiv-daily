---
layout: default
title: "FlowCut: Unsupervised Video Instance Segmentation via Temporal Mask Matching"
---

# FlowCut: Unsupervised Video Instance Segmentation via Temporal Mask Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13174" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13174v1</a>
  <a href="https://arxiv.org/pdf/2505.13174.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13174v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13174v1', 'FlowCut: Unsupervised Video Instance Segmentation via Temporal Mask Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alp Eren Sari, Paolo Favaro

**分类**: cs.CV

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**提出FlowCut以解决无监督视频实例分割问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `无监督学习` `视频实例分割` `伪标签生成` `时间匹配` `深度学习`

## 📋 核心要点

1. 现有的无监督视频实例分割方法在伪标签生成和一致性保持方面存在挑战，导致分割效果不理想。
2. FlowCut通过三阶段框架生成高质量的伪标签，利用图像和光流特征的亲和性来提升分割精度。
3. 在多个基准测试中，FlowCut展示了优越的性能，超越了现有的最先进方法，证明了其有效性。

## 📝 摘要（中文）

我们提出FlowCut，一种简单而有效的无监督视频实例分割方法，包含三个阶段的框架，用于构建高质量的伪标签视频数据集。根据我们的了解，这是首次尝试为无监督视频实例分割策划带有伪标签的视频数据集。在第一阶段，我们通过利用图像和光流特征的亲和性生成伪实例掩码。在第二阶段，我们通过在帧间进行时间匹配，构建包含高质量、一致的伪实例掩码的短视频片段。在第三阶段，我们使用YouTubeVIS-2021视频数据集提取训练实例分割集，并训练视频分割模型。FlowCut在YouTubeVIS-2019、YouTubeVIS-2021、DAVIS-2017和DAVIS-2017 Motion基准测试中达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决无监督视频实例分割中的伪标签生成和一致性问题。现有方法往往依赖于人工标注或缺乏有效的伪标签生成机制，导致分割效果不佳。

**核心思路**：FlowCut的核心思路是通过三阶段的框架生成高质量的伪标签，利用图像和光流特征的亲和性来实现伪实例掩码的生成和时间匹配，从而提高分割的准确性和一致性。

**技术框架**：FlowCut的整体架构包括三个主要阶段：第一阶段生成伪实例掩码，第二阶段通过时间匹配构建短视频片段，第三阶段使用YouTubeVIS-2021数据集提取训练集并训练分割模型。

**关键创新**：FlowCut的主要创新在于首次提出了为无监督视频实例分割策划带有伪标签的视频数据集，并通过时间匹配提高了伪标签的一致性，显著提升了分割性能。

**关键设计**：在技术细节上，FlowCut利用了图像和光流特征的亲和性来生成伪标签，同时在损失函数设计上考虑了时间一致性，以确保生成的伪标签在不同帧间保持一致性。网络结构上，FlowCut采用了适应性强的深度学习模型，以便更好地处理视频数据的时序特性。

## 📊 实验亮点

在实验中，FlowCut在YouTubeVIS-2019、YouTubeVIS-2021、DAVIS-2017和DAVIS-2017 Motion基准测试中取得了最先进的性能，具体表现为在多个数据集上相较于现有方法提升了分割精度，验证了其有效性和优越性。

## 🎯 应用场景

FlowCut的研究成果在视频监控、自动驾驶、视频分析等领域具有广泛的应用潜力。通过无监督的方式进行视频实例分割，可以降低人工标注的成本，提高数据处理的效率，推动相关领域的技术进步和应用落地。

## 📄 摘要（原文）

> We propose FlowCut, a simple and capable method for unsupervised video instance segmentation consisting of a three-stage framework to construct a high-quality video dataset with pseudo labels. To our knowledge, our work is the first attempt to curate a video dataset with pseudo-labels for unsupervised video instance segmentation. In the first stage, we generate pseudo-instance masks by exploiting the affinities of features from both images and optical flows. In the second stage, we construct short video segments containing high-quality, consistent pseudo-instance masks by temporally matching them across the frames. In the third stage, we use the YouTubeVIS-2021 video dataset to extract our training instance segmentation set, and then train a video segmentation model. FlowCut achieves state-of-the-art performance on the YouTubeVIS-2019, YouTubeVIS-2021, DAVIS-2017, and DAVIS-2017 Motion benchmarks.

