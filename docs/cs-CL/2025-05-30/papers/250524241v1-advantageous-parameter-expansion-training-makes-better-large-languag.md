---
layout: default
title: Advantageous Parameter Expansion Training Makes Better Large Language Models
---

# Advantageous Parameter Expansion Training Makes Better Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24241" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24241v1</a>
  <a href="https://arxiv.org/pdf/2505.24241.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24241v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24241v1', 'Advantageous Parameter Expansion Training Makes Better Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Naibin Gu, Yilong Chen, Zhenyu Zhang, Peng Fu, Zheng Lin, Shuohuan Wang, Yu Sun, Hua Wu, Weiping Wang, Haifeng Wang

**分类**: cs.CL

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出优势参数扩展训练以提升大语言模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `参数扩展` `训练效率` `指令调优` `继续预训练` `性能提升` `机器学习`

## 📋 核心要点

1. 现有方法在增加可训练参数数量时，虽然可以提升模型性能，但计算开销显著增加，效率低下。
2. 本文提出的APEX方法通过逐步扩展优势参数，提升其在模型中的比例，从而提高训练效果。
3. 实验结果显示，APEX在指令调优中使用52%参数超越全参数调优，在继续预训练中仅用33%数据达到相同困惑度。

## 📝 摘要（中文）

尽管在预训练和微调中增加可训练参数的数量可以有效提升大语言模型的性能，但也会导致计算开销增加。本文提出了一种名为优势参数扩展训练（APEX）的方法，该方法逐步将优势参数扩展到劣势参数的空间，从而提高其比例并增强训练效果。理论分析从矩阵有效秩的角度解释了APEX的性能提升。大量实验表明，在指令调优中，APEX在仅使用52%的可训练参数的情况下超越了全参数调优；在继续预训练中，APEX在仅使用33%的训练数据的情况下达到了与传统训练相同的困惑度，并在下游任务上取得了显著改善。

## 🔬 方法详解

**问题定义**：本文旨在解决在大语言模型训练中，增加可训练参数数量导致的计算开销和效率低下的问题。现有方法未能有效利用参数间的差异，导致训练效果不尽如人意。

**核心思路**：APEX方法的核心思想是识别并扩展模型中的优势参数，使其在训练中占据更大比例，从而提升整体性能。通过这种方式，模型能够在减少参数数量的同时，保持或提升性能。

**技术框架**：APEX的整体架构包括两个主要阶段：首先识别优势参数，其次将这些参数逐步扩展到劣势参数的空间。该方法通过动态调整参数的使用比例，优化训练过程。

**关键创新**：APEX的最大创新在于其对优势参数的识别和扩展机制，这与传统的全参数调优方法有本质区别。通过聚焦于对性能影响最大的参数，APEX能够在较少的计算资源下实现更好的训练效果。

**关键设计**：在APEX中，关键的参数设置包括优势参数的识别标准和扩展策略。此外，损失函数的设计也考虑了参数的有效性，以确保训练过程的高效性和稳定性。

## 📊 实验亮点

实验结果显示，APEX在指令调优中仅使用52%的可训练参数，便超越了全参数调优的效果；在继续预训练中，APEX使用33%的训练数据达到了与传统方法相同的困惑度，并在下游任务上取得了显著提升，展示了其优越的训练效率。

## 🎯 应用场景

该研究的潜在应用场景包括自然语言处理、对话系统、文本生成等领域。通过优化大语言模型的训练效率，APEX方法能够在资源受限的情况下，提升模型的实际应用价值，推动智能助手和自动化内容生成等技术的发展。

## 📄 摘要（原文）

> Although scaling up the number of trainable parameters in both pre-training and fine-tuning can effectively improve the performance of large language models, it also leads to increased computational overhead. When delving into the parameter difference, we find that a subset of parameters, termed advantageous parameters, plays a crucial role in determining model performance. Further analysis reveals that stronger models tend to possess more such parameters. In this paper, we propose Advantageous Parameter EXpansion Training (APEX), a method that progressively expands advantageous parameters into the space of disadvantageous ones, thereby increasing their proportion and enhancing training effectiveness. Further theoretical analysis from the perspective of matrix effective rank explains the performance gains of APEX. Extensive experiments on both instruction tuning and continued pre-training demonstrate that, in instruction tuning, APEX outperforms full-parameter tuning while using only 52% of the trainable parameters. In continued pre-training, APEX achieves the same perplexity level as conventional training with just 33% of the training data, and yields significant improvements on downstream tasks.

