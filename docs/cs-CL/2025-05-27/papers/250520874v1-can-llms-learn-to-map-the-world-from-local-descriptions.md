---
layout: default
title: Can LLMs Learn to Map the World from Local Descriptions?
---

# Can LLMs Learn to Map the World from Local Descriptions?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20874" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20874v1</a>
  <a href="https://arxiv.org/pdf/2505.20874.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20874v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20874v1', 'Can LLMs Learn to Map the World from Local Descriptions?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sirui Xia, Aili Chen, Xintao Wang, Tinghui Zhu, Yikai Zhang, Jiangjie Chen, Yanghua Xiao

**分类**: cs.CL

**发布日期**: 2025-05-27

**备注**: 19 pages, 11 figures

---

## 💡 一句话要点

**提出利用LLMs构建全球空间认知以解决局部描述映射问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `空间认知` `路径规划` `空间感知` `动态导航`

## 📋 核心要点

1. 现有方法在空间认知方面的研究相对不足，尤其是如何从局部描述构建全球空间认知仍然是一个挑战。
2. 本研究提出通过整合局部关系描述，利用LLMs进行空间感知和导航，从而实现全球空间认知的构建。
3. 实验结果表明，LLMs能够有效推广未见的空间关系，并在路径规划和动态导航中展现出优越的性能。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在代码和数学等任务中展现出强大的能力。然而，它们在内化结构化空间知识方面的潜力仍未得到充分探索。本研究调查了LLMs是否能够基于局部相对的人类观察，整合零散的关系描述，构建连贯的全球空间认知。我们关注空间认知的两个核心方面：空间感知和空间导航。实验结果表明，LLMs不仅能够推广到未见的兴趣点（POI）之间的空间关系，还能学习道路连通性，实现准确的路径规划和动态空间意识。

## 🔬 方法详解

**问题定义**：本论文旨在解决如何从局部描述中构建全球空间认知的问题。现有方法在处理空间关系时往往无法有效整合局部信息，导致全球布局的推断不准确。

**核心思路**：论文的核心思路是利用大型语言模型（LLMs）整合局部相对描述，构建一致的全球空间认知。通过这种方式，模型能够从局部信息中推断出全局布局，并学习道路连通性。

**技术框架**：整体架构包括两个主要模块：空间感知模块和空间导航模块。空间感知模块负责从局部关系中推断全球布局，而空间导航模块则基于轨迹数据学习道路连接性并进行路径规划。

**关键创新**：最重要的技术创新在于LLMs能够有效整合局部描述，生成与真实世界空间分布相一致的潜在表示。这一方法与传统的空间认知模型相比，能够更好地处理复杂的空间关系。

**关键设计**：在模型设计中，采用了特定的损失函数以优化空间布局的推断准确性，并通过调整网络结构来增强模型对局部信息的敏感性。

## 📊 实验亮点

实验结果显示，LLMs能够有效推广到未见的空间关系，且在路径规划任务中表现出较高的准确性。与基线模型相比，LLMs在空间布局推断和动态导航方面的性能提升显著，证明了其在空间认知领域的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能导航系统、城市规划和机器人路径规划等。通过提升LLMs在空间认知方面的能力，可以为自动驾驶、无人机导航等技术提供更为精准的支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in Large Language Models (LLMs) have demonstrated strong capabilities in tasks such as code and mathematics. However, their potential to internalize structured spatial knowledge remains underexplored. This study investigates whether LLMs, grounded in locally relative human observations, can construct coherent global spatial cognition by integrating fragmented relational descriptions. We focus on two core aspects of spatial cognition: spatial perception, where models infer consistent global layouts from local positional relationships, and spatial navigation, where models learn road connectivity from trajectory data and plan optimal paths between unconnected locations. Experiments conducted in a simulated urban environment demonstrate that LLMs not only generalize to unseen spatial relationships between points of interest (POIs) but also exhibit latent representations aligned with real-world spatial distributions. Furthermore, LLMs can learn road connectivity from trajectory descriptions, enabling accurate path planning and dynamic spatial awareness during navigation.

