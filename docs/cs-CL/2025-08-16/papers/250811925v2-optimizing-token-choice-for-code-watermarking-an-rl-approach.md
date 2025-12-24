---
layout: default
title: "Optimizing Token Choice for Code Watermarking: An RL Approach"
---

# Optimizing Token Choice for Code Watermarking: An RL Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11925" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11925v2</a>
  <a href="https://arxiv.org/pdf/2508.11925.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11925v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11925v2', 'Optimizing Token Choice for Code Watermarking: An RL Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhimeng Guo, Huaisheng Zhu, Siyuan Xu, Hangfan Zhang, Teng Xiao, Minhao Cheng

**分类**: cs.CR, cs.CL, cs.LG

**发布日期**: 2025-08-16 (更新: 2025-11-02)

**备注**: 18 pages, 3 figures

---

## 💡 一句话要点

**提出CodeTracer以解决代码水印嵌入的有效性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `代码水印` `强化学习` `知识产权保护` `水印嵌入` `生成代码` `Gumbel Top-k`

## 📋 核心要点

1. 现有的代码水印方法在保持代码功能的同时，难以有效嵌入水印，导致知识产权保护不足。
2. 本文提出的CodeTracer框架通过强化学习策略优化标记选择，确保水印的有效嵌入与代码功能的保持。
3. 实验结果显示，CodeTracer在水印可检测性和功能保持方面显著优于现有方法，提升幅度明显。

## 📝 摘要（中文）

保护大语言模型生成代码的知识产权需要有效的水印系统，这些系统必须在代码的高度结构化和语法约束的特性中运作。本文提出了CodeTracer，一个创新的自适应代码水印框架，基于一种新颖的强化学习训练范式。CodeTracer采用策略驱动的方法，利用参数化模型智能地偏向下一个标记的选择，确保嵌入的水印在保持代码功能的同时，展现出与典型标记分布的微妙但可统计检测的偏差。为促进策略学习，本文设计了一个综合奖励系统，将执行反馈与水印嵌入信号无缝整合，平衡过程级和结果级奖励。此外，采用Gumbel Top-k重参数化技术，实现离散水印决策的基于梯度的优化。大量比较评估表明，CodeTracer在水印可检测性和生成代码功能保持方面显著优于现有最先进的基线。

## 🔬 方法详解

**问题定义**：本文旨在解决在大语言模型生成代码中有效嵌入水印的问题。现有方法往往无法在保持代码功能的同时实现有效的水印嵌入，导致知识产权保护的不足。

**核心思路**：CodeTracer通过强化学习的策略优化标记选择，确保水印在代码中嵌入时不会影响其功能。该方法利用参数化模型智能地偏向下一个标记的选择，从而实现水印的有效嵌入。

**技术框架**：CodeTracer的整体架构包括策略学习模块、奖励系统和水印嵌入模块。策略学习模块负责优化标记选择，奖励系统则结合执行反馈与水印信号，水印嵌入模块确保水印的有效性与代码功能的保持。

**关键创新**：最重要的技术创新在于引入了基于强化学习的策略优化方法，结合Gumbel Top-k重参数化技术，使得离散水印决策可以通过梯度优化。这一方法与现有的水印技术在嵌入策略上有本质区别。

**关键设计**：在设计中，奖励系统综合考虑了过程级和结果级的反馈，确保水印嵌入的有效性。同时，采用的损失函数和网络结构经过精心设计，以适应代码的语法特性和水印的嵌入需求。

## 📊 实验亮点

实验结果表明，CodeTracer在水印可检测性方面比现有最先进的基线提高了显著的性能，具体提升幅度达到X%（具体数据未知），同时在保持生成代码功能方面也表现出色，确保了水印的有效性与代码的实用性。

## 🎯 应用场景

该研究的潜在应用领域包括软件版权保护、代码审计和安全性验证等。通过有效的水印嵌入，开发者可以保护其知识产权，防止代码被非法复制或篡改。未来，该技术可能在开源软件和商业软件中得到广泛应用，提升代码的安全性与可追溯性。

## 📄 摘要（原文）

> Protecting intellectual property on LLM-generated code necessitates effective watermarking systems that can operate within code's highly structured, syntactically constrained nature. In this work, we introduce CodeTracer, an innovative adaptive code watermarking framework underpinned by a novel reinforcement learning training paradigm. At its core, CodeTracer features a policy-driven approach that utilizes a parameterized model to intelligently bias token choices during next-token prediction. This strategy ensures that embedded watermarks maintain code functionality while exhibiting subtle yet statistically detectable deviations from typical token distributions. To facilitate policy learning, we devise a comprehensive reward system that seamlessly integrates execution feedback with watermark embedding signals, balancing process-level and outcome-level rewards. Additionally, we employ Gumbel Top-k reparameterization to enable gradient-based optimization of discrete watermarking decisions. Extensive comparative evaluations demonstrate CodeTracer's significant superiority over state-of-the-art baselines in both watermark detectability and the preservation of generated code's functionality.

