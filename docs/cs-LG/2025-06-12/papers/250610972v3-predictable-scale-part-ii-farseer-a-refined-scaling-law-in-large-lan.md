---
layout: default
title: "Predictable Scale: Part II, Farseer: A Refined Scaling Law in Large Language Models"
---

# Predictable Scale: Part II, Farseer: A Refined Scaling Law in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10972" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10972v3</a>
  <a href="https://arxiv.org/pdf/2506.10972.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10972v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10972v3', 'Predictable Scale: Part II, Farseer: A Refined Scaling Law in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Houyi Li, Wenzhen Zheng, Qiufeng Wang, Zhenyu Ding, Haoying Wang, Zili Wang, Shijie Xuyang, Ning Ding, Shuigeng Zhou, Xiangyu Zhang, Daxin Jiang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-12 (更新: 2025-07-16)

**备注**: 34

**🔗 代码/项目**: [GITHUB](https://github.com/Farseer-Scaling-Law/Farseer)

---

## 💡 一句话要点

**提出Farseer以解决大规模语言模型训练中的预测精度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `缩放法则` `模型训练` `预测精度` `计算资源分配` `外推能力` `深度学习`

## 📋 核心要点

1. 现有方法在大规模语言模型训练中存在显著的预测精度不足，导致小规模实验结果难以有效转移。
2. Farseer通过构建模型损失面$L(N,D)$，提供了一种新的缩放法则，显著提高了跨尺度的预测准确性。
3. 实验结果表明，Farseer在外推能力上优于Chinchilla法则，外推误差降低了433%，并支持对训练策略的可靠评估。

## 📝 摘要（中文）

训练大型语言模型（LLMs）成本高昂，导致小规模实验的洞察难以转移到资源密集型的生产系统中，从而阻碍了高效创新。为此，我们提出Farseer，一种新颖且精炼的缩放法则，提供了跨尺度的增强预测精度。通过系统构建模型损失面$L(N,D)$，Farseer在拟合经验数据方面显著优于以往的法则（如Chinchilla法则），并将外推误差降低了433%。这使得能够可靠地评估不同训练策略，并自信地将小规模消融研究的结论外推至大规模性能。此外，Farseer还提供了关于最佳计算资源分配的新见解，更好地反映了现代LLM训练的细微需求。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型训练中的预测精度问题，现有方法在小规模实验与大规模应用之间存在显著的缩放差距，导致无法有效转移实验结果。

**核心思路**：Farseer的核心思想是通过系统构建模型损失面$L(N,D)$，实现对不同规模下模型性能的精确预测，从而提高预测的准确性和可靠性。

**技术框架**：Farseer的整体架构包括数据收集、模型训练、损失面构建和预测评估四个主要模块。首先收集多种规模的模型训练数据，然后构建损失面以拟合这些数据，最后进行性能预测和策略评估。

**关键创新**：Farseer的最重要创新在于其损失面构建方法，能够更好地拟合经验数据，显著降低外推误差，与现有方法（如Chinchilla法则）相比，提供了更高的预测精度。

**关键设计**：在关键设计方面，Farseer采用了优化的损失函数和参数设置，确保模型在不同规模下的泛化能力，同时通过大量实验验证了其有效性。

## 📊 实验亮点

实验结果显示，Farseer在外推能力上显著优于Chinchilla法则，外推误差降低了433%。通过训练约1000个不同规模和配置的LLM，Farseer展示了其在各个$(N,D)$设置下的可靠性和准确性，为训练策略的评估提供了强有力的支持。

## 🎯 应用场景

Farseer的研究成果在多个领域具有潜在应用价值，包括自然语言处理、机器翻译和对话系统等。通过提高大规模语言模型的训练效率和预测准确性，Farseer能够帮助研究人员和工程师更有效地设计和优化模型，从而推动相关技术的进步和应用落地。

## 📄 摘要（原文）

> Training Large Language Models (LLMs) is prohibitively expensive, creating a critical scaling gap where insights from small-scale experiments often fail to transfer to resource-intensive production systems, thereby hindering efficient innovation. To bridge this, we introduce Farseer, a novel and refined scaling law offering enhanced predictive accuracy across scales. By systematically constructing a model loss surface $L(N,D)$, Farseer achieves a significantly better fit to empirical data than prior laws (e.g., Chinchilla's law). Our methodology yields accurate, robust, and highly generalizable predictions, demonstrating excellent extrapolation capabilities, improving upon Chinchilla's law by reducing extrapolation error by 433\%. This allows for the reliable evaluation of competing training strategies across all $(N,D)$ settings, enabling conclusions from small-scale ablation studies to be confidently extrapolated to predict large-scale performance. Furthermore, Farseer provides new insights into optimal compute allocation, better reflecting the nuanced demands of modern LLM training. To validate our approach, we trained an extensive suite of approximately 1,000 LLMs across diverse scales and configurations, consuming roughly 3 million NVIDIA H100 GPU hours. We are comprehensively open-sourcing all models, data, results, and logs at https://github.com/Farseer-Scaling-Law/Farseer to foster further research.

