---
layout: default
title: A Simple Linear Patch Revives Layer-Pruned Large Language Models
---

# A Simple Linear Patch Revives Layer-Pruned Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24680" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24680v2</a>
  <a href="https://arxiv.org/pdf/2505.24680.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24680v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24680v2', 'A Simple Linear Patch Revives Layer-Pruned Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinrui Chen, Haoli Bai, Tao Yuan, Ruikang Liu, Kang Zhao, Xianzhi Yu, Lu Hou, Tian Guan, Yonghong He, Chun Yuan

**分类**: cs.CL

**发布日期**: 2025-05-30 (更新: 2025-10-25)

**备注**: 26 pages, accepted to NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/chenxinrui-tsinghua/LinearPatch)

---

## 💡 一句话要点

**提出LinearPatch以解决层修剪模型性能下降问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `层修剪` `激活对齐` `Hadamard变换` `语言模型压缩` `模型蒸馏` `性能优化` `深度学习`

## 📋 核心要点

1. 现有的层修剪方法在压缩大型语言模型时，往往导致性能显著下降，主要由于激活幅度不匹配问题。
2. 论文提出LinearPatch，通过融合Hadamard变换和通道级缩放，解决了激活幅度不匹配的问题。
3. 在LLaMA-3-8B模型上，LinearPatch修剪5层时保留了94.15%的性能，且通过离线蒸馏进一步提升至95.16%。

## 📝 摘要（中文）

层修剪已成为压缩大型语言模型（LLMs）的广泛应用技术。然而，现有的层修剪方法往往会导致显著的性能下降。我们发现这种下降主要源于一个被忽视的问题：修剪接口处激活幅度的不匹配。修剪前后的激活在规模上存在显著差异，导致在剩余层中传播时出现分布偏移。为了解决这一问题，我们提出了LinearPatch，这是一种轻量级的即插即用技术，它将两种操作融合为一个矩阵乘法：一是Hadamard变换以抑制特定token的巨大异常值，二是通道级缩放以对齐激活统计。在LLaMA-3-8B模型上，LinearPatch在修剪32层中的5层时，保留了原模型94.15%的性能，超越了之前的最优结果4%。该补丁还可以通过内存高效的离线蒸馏进一步优化，保留率在仅30分钟内提升至95.16%。代码可在https://github.com/chenxinrui-tsinghua/LinearPatch获取。

## 🔬 方法详解

**问题定义**：论文要解决的具体问题是层修剪导致的性能下降，主要由于修剪接口处激活幅度的不匹配，造成了激活在后续层中的分布偏移。

**核心思路**：论文的核心解决思路是引入LinearPatch技术，通过将Hadamard变换和通道级缩放结合，来抑制异常值并对齐激活统计，从而减轻性能损失。

**技术框架**：整体架构包括两个主要模块：一是Hadamard变换模块，用于处理特定token的异常值，二是通道级缩放模块，用于调整激活的统计特性。这两个模块在修剪接口处进行融合，形成一个高效的矩阵乘法操作。

**关键创新**：最重要的技术创新点在于将两种操作融合为一个矩阵乘法，解决了激活幅度不匹配的问题，显著提高了修剪后的模型性能。与现有方法相比，这种设计在性能保持上具有本质的优势。

**关键设计**：在参数设置上，LinearPatch采用了特定的Hadamard变换参数和通道缩放因子，以确保在修剪后激活的统计特性能够得到有效对齐。此外，离线蒸馏过程也经过优化，以提高模型的保留率。

## 📊 实验亮点

实验结果表明，LinearPatch在LLaMA-3-8B模型上修剪5层时，保留了94.15%的原始性能，超越了之前的最优结果4%。通过进一步的离线蒸馏，保留率在仅30分钟内提升至95.16%，展示了其优越的性能保持能力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和机器翻译等大型语言模型的优化。通过有效的层修剪技术，能够在保持模型性能的同时，显著降低计算资源的消耗，提升模型的实际应用价值。未来，该技术可能推动更多轻量级模型的开发与应用。

## 📄 摘要（原文）

> Layer pruning has emerged as a widely used technique for compressing large language models (LLMs). However, existing layer pruning approaches often incur substantial performance degradation. We identify the majority of this degradation to a single yet previously overlooked issue: \textit{the mismatch of activation magnitudes at the pruning interface}. The pre-interface activations exhibit significantly different scales from the post-interface ones, causing the distributional shift as it propagates through the remaining layers. To address this issue, we introduce \textsc{LinearPatch}, a lightweight and plug-and-play technique that fuses two operations into one matrix multiply at the pruning interface: (i) a Hadamard transformation that suppresses massive outliers at particular tokens and (ii) a channel-wise scaling that aligns activation statistics. On LLaMA-3-8B, \textsc{LinearPatch} preserves up to \textbf{94.15\%} of the original model's performance when pruning 5 out of 32 layers, outperforming the previous state of the art by \textbf{4\%}. The patch can be further refined with 5K unlabeled samples via memory-efficient offline distillation, pushing the retention to 95.16\% within only 30 minutes on a single GPU. Code is available at https://github.com/chenxinrui-tsinghua/LinearPatch.

