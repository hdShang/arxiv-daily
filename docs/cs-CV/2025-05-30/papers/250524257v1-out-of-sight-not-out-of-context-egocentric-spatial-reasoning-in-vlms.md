---
layout: default
title: Out of Sight, Not Out of Context? Egocentric Spatial Reasoning in VLMs Across Disjoint Frames
---

# Out of Sight, Not Out of Context? Egocentric Spatial Reasoning in VLMs Across Disjoint Frames

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24257" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24257v1</a>
  <a href="https://arxiv.org/pdf/2505.24257.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24257v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24257v1', 'Out of Sight, Not Out of Context? Egocentric Spatial Reasoning in VLMs Across Disjoint Frames')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sahithya Ravi, Gabriel Sarch, Vibhav Vineet, Andrew D. Wilson, Balasaravanan Thoravi Kumaravel

**分类**: cs.CV

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出Disjoint-3DQA基准以解决长时间空间推理问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长时间空间推理` `视觉语言模型` `生成式问答` `3D场景表示` `具身AI`

## 📋 核心要点

1. 现有的视觉语言模型在处理长时间跨度的空间推理时表现不佳，尤其是在物体不同时帧不可见的情况下。
2. 论文提出Disjoint-3DQA基准，通过生成式问答的方式评估VLMs在不同帧中对物体关系的推理能力。
3. 实验结果显示，VLMs的表现落后于人类28%，并且提供3D坐标能显著提升模型性能20%。

## 📝 摘要（中文）

本文探讨了在自我中心视频中，具身AI助手如何整合时间上的空间线索，以确定物体A与物体B之间的相对位置。我们引入了Disjoint-3DQA，一个生成式问答基准，评估视觉语言模型（VLMs）在不同帧中对不可见物体对的推理能力。评估结果显示，七种最先进的VLMs在性能上落后于人类28%，且随着时间间隔的增加，准确率显著下降。提供轨迹或鸟瞰图对模型的提升有限，而提供真实的3D坐标则能显著提高20%的性能。这一发现突显了多帧VLMs在构建和维护3D场景表示方面的核心瓶颈。

## 🔬 方法详解

**问题定义**：本文旨在解决具身AI助手在自我中心视频中如何有效整合时间上的空间线索的问题。现有方法在处理不可见物体对时，准确率显著下降，尤其是时间间隔较大时。

**核心思路**：论文的核心思路是引入Disjoint-3DQA基准，专注于评估VLMs在不同帧中对物体关系的推理能力，旨在推动VLMs在长时间跨度空间推理方面的研究。

**技术框架**：整体架构包括数据集构建、问题生成和模型评估三个主要模块。数据集包含不同帧中不可见物体对的问题，模型通过生成式问答方式进行推理。

**关键创新**：最重要的技术创新点在于提出了Disjoint-3DQA基准，明确了多帧VLMs在空间推理中的不足，并提供了可量化的评估标准。与现有方法相比，该基准更关注时间跨度对推理能力的影响。

**关键设计**：在实验中，模型的输入包括物体的轨迹、鸟瞰图和真实的3D坐标。研究发现，提供真实的3D坐标能显著提高模型性能，而其他输入方式的提升效果有限。

## 📊 实验亮点

实验结果显示，七种最先进的VLMs在Disjoint-3DQA基准上的表现落后于人类28%。随着时间间隔的增加，模型的准确率从60%下降至30%。提供真实的3D坐标能显著提升模型性能20%，而轨迹和鸟瞰图的提升效果则相对有限。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居助手、自动驾驶系统和增强现实等。通过提升VLMs在长时间空间推理中的能力，能够使具身AI在复杂环境中更好地理解和互动，进而提高用户体验和安全性。未来，随着技术的进步，该研究可能推动更多跨领域的应用。

## 📄 摘要（原文）

> An embodied AI assistant operating on egocentric video must integrate spatial cues across time - for instance, determining where an object A, glimpsed a few moments ago lies relative to an object B encountered later. We introduce Disjoint-3DQA , a generative QA benchmark that evaluates this ability of VLMs by posing questions about object pairs that are not co-visible in the same frame. We evaluated seven state-of-the-art VLMs and found that models lag behind human performance by 28%, with steeper declines in accuracy (60% to 30 %) as the temporal gap widens. Our analysis further reveals that providing trajectories or bird's-eye-view projections to VLMs results in only marginal improvements, whereas providing oracle 3D coordinates leads to a substantial 20% performance increase. This highlights a core bottleneck of multi-frame VLMs in constructing and maintaining 3D scene representations over time from visual signals. Disjoint-3DQA therefore sets a clear, measurable challenge for long-horizon spatial reasoning and aims to catalyze future research at the intersection of vision, language, and embodied AI.

