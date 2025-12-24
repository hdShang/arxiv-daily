---
layout: default
title: RICo: Refined In-Context Contribution for Automatic Instruction-Tuning Data Selection
---

# RICo: Refined In-Context Contribution for Automatic Instruction-Tuning Data Selection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05327" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05327v2</a>
  <a href="https://arxiv.org/pdf/2505.05327.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05327v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05327v2', 'RICo: Refined In-Context Contribution for Automatic Instruction-Tuning Data Selection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yixin Yang, Qingxiu Dong, Linli Yao, Fangwei Zhu, Zhifang Sui

**分类**: cs.CL

**发布日期**: 2025-05-08 (更新: 2025-05-18)

---

## 💡 一句话要点

**提出RICo以解决自动指令调优数据选择问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据选择` `指令调优` `大型语言模型` `贡献测量` `上下文学习` `无梯度方法` `模型性能提升`

## 📋 核心要点

1. 现有的数据选择方法在识别高贡献样本方面存在不足，导致指令调优效果不佳。
2. 本文提出RICo，通过无梯度方式量化样本对模型性能的贡献，提升数据选择的准确性。
3. 实验结果表明，使用RICo选择的数据显著提高了模型性能，且在多个基准测试中表现优异。

## 📝 摘要（中文）

数据选择在指令调优中至关重要，它能提高大型语言模型（LLMs）的性能并降低训练成本。本文提出了一种新颖的无梯度方法——精细贡献测量与上下文学习结合的RICo，能够量化单个样本对任务级和全局级模型性能的细粒度贡献。RICo使得高贡献数据的识别更加准确，从而提升指令调优效果。此外，我们引入了一种基于RICo评分的轻量级选择范式，实现了严格线性推理复杂度的可扩展数据选择。在对三种LLM进行的12个基准和5个成对评估集的广泛实验中，RICo展现了其有效性。值得注意的是，在LLaMA3.1-8B上，基于15% RICo选择数据训练的模型比全数据集提高了5.42个百分点，并超越了广泛使用的选择方法2.06个百分点。

## 🔬 方法详解

**问题定义**：本文旨在解决自动指令调优中数据选择的有效性问题。现有方法在识别高贡献样本时存在局限，导致模型性能未能得到充分提升。

**核心思路**：RICo通过精细贡献测量，结合上下文学习，量化每个样本对模型性能的贡献，从而更准确地选择高贡献数据。

**技术框架**：RICo方法包括数据样本的贡献测量和轻量级选择范式。首先，通过上下文学习评估样本贡献，然后基于贡献评分进行数据选择，确保选择过程的线性复杂度。

**关键创新**：RICo的主要创新在于其无梯度的贡献测量方法，能够细致地评估样本对模型性能的影响，这与传统方法的依赖梯度信息的方式有本质区别。

**关键设计**：在RICo中，采用了特定的损失函数和参数设置，以确保贡献测量的准确性和选择过程的高效性。

## 📊 实验亮点

实验结果显示，在LLaMA3.1-8B模型上，使用15% RICo选择的数据训练的模型性能比全数据集提高了5.42个百分点，且超越了其他主流选择方法2.06个百分点，验证了RICo的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等，能够有效提升大型语言模型的训练效率和性能。未来，RICo方法可能在更广泛的机器学习任务中得到应用，推动自动化数据选择技术的发展。

## 📄 摘要（原文）

> Data selection for instruction tuning is crucial for improving the performance of large language models (LLMs) while reducing training costs. In this paper, we propose Refined Contribution Measurement with In-Context Learning (RICo), a novel gradient-free method that quantifies the fine-grained contribution of individual samples to both task-level and global-level model performance. RICo enables more accurate identification of high-contribution data, leading to better instruction tuning. We further introduce a lightweight selection paradigm trained on RICo scores, enabling scalable data selection with a strictly linear inference complexity. Extensive experiments on three LLMs across 12 benchmarks and 5 pairwise evaluation sets demonstrate the effectiveness of RICo. Remarkably, on LLaMA3.1-8B, models trained on 15% of RICo-selected data outperform full datasets by 5.42% points and exceed the best performance of widely used selection methods by 2.06% points. We further analyze high-contribution samples selected by RICo, which show both diverse tasks and appropriate difficulty levels, rather than just the hardest ones.

