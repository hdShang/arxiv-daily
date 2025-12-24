---
layout: default
title: "NaLaFormer: Norm-Aware Linear Attention for Transformer Models"
---

# NaLaFormer: Norm-Aware Linear Attention for Transformer Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21137" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21137v1</a>
  <a href="https://arxiv.org/pdf/2506.21137.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21137v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21137v1', 'NaLaFormer: Norm-Aware Linear Attention for Transformer Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weikang Meng, Yadan Luo, Liangyu Huo, Yaowei Wang, Xin Li, Zheng Zhang

**分类**: cs.LG

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出Norm-Aware Linear Attention以解决线性注意力的熵缺失问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `线性注意力` `范数感知` `熵控制` `多模态任务` `计算机视觉` `自然语言处理`

## 📋 核心要点

1. 现有线性注意力方法忽视了查询范数，导致熵缺失和信息交互不足。
2. 提出的Norm-Aware Linear Attention机制通过解耦查询和键的范数与方向，恢复了动态尖锐性和范数分布。
3. 实验表明，NaLaFormer在多个视觉和语言任务上性能提升显著，最高可达4.2%。

## 📝 摘要（中文）

线性注意力作为软最大注意力的替代方案，通过将序列长度的复杂度从平方降低到线性，得到了广泛关注。现有方法在使用线性可分核函数时忽视了查询向量的范数，导致熵的缺失。为了解决这一问题，本文提出了一种新的Norm-Aware Linear Attention机制，通过解耦查询和键矩阵的范数与方向，实现了范数引导的动态尖锐性控制和范数一致性。实验结果表明，NaLaFormer在视觉和语言任务上性能提升高达4.2%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有线性注意力方法中查询范数被忽视导致的熵缺失问题，影响了信息交互的有效性。

**核心思路**：通过引入Norm-Aware机制，解耦查询和键的范数与方向，动态控制熵的减少，从而恢复信息的表达能力。

**技术框架**：整体架构包括查询和键的解耦、范数一致性维护以及非负约束映射，确保模型在处理信息时的有效性。

**关键创新**：提出的范数感知核函数能够根据查询范数动态调整熵的减少程度，显著改善了线性注意力的性能。

**关键设计**：采用范数保持映射将角度矩阵的所有元素投影到正值，利用余弦相似度抑制方向相反的维度，确保模型的非负性和一致性。

## 📊 实验亮点

实验结果显示，NaLaFormer在视觉和语言任务上相较于基线模型提升了最高4.2%的性能，验证了其在提高表达性和效率方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理等多模态任务，能够提升模型在处理复杂数据时的效率和表达能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Linear attention has emerged as a viable alternative to softmax attention by reducing complexity from quadratic to linear in sequence length. To preserve two fundamental properties of softmax, non-negativity and entropy reduction, current works employ various linearly separatable kernel functions with $L1$ normalization instead of softmax operator. However, query norms are neglected by the normalization operation in linear attention, such degradation heavily leads to an entropy gap. Meanwhile, existing works inhibit negative values of query and key vectors resulting in a missing inner-product interactions after being mapped. To address these dual challenges, we propose a novel Norm-Aware Linear Attention mechanism serving to restore norm-guided dynamic spikiness and recover kernel-perturbed norm distributions. Specifically, we first decouple query and key matrices into two components: norm and direction, to achieve norm-aware spikiness control and norm consistency, respectively. We mathematically reveal that the extent of entropy reduction varies with the query norm in softmax normalization, motivating a query-norm aware kernel function for dynamic control over entropy reduction. Furthermore, to ensure norm consistency and enforce non-negativity constraints, we employ a norm-preserving mapping to project all elements of the angular matrix into positive values, leveraging cosine similarity to inhibit dimensions with opposite directions. We conduct extensive experiments demonstrating that the NaLaFormer improves performance on vision and language tasks, enhancing both expressiveness and efficiency by up to 4.2\%.

