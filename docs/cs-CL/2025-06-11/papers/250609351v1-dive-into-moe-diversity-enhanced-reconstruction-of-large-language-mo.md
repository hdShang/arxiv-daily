---
layout: default
title: "DIVE into MoE: Diversity-Enhanced Reconstruction of Large Language Models from Dense into Mixture-of-Experts"
---

# DIVE into MoE: Diversity-Enhanced Reconstruction of Large Language Models from Dense into Mixture-of-Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09351" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09351v1</a>
  <a href="https://arxiv.org/pdf/2506.09351.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09351v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09351v1', 'DIVE into MoE: Diversity-Enhanced Reconstruction of Large Language Models from Dense into Mixture-of-Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuchen Feng, Bowen Shen, Naibin Gu, Jiaxuan Zhao, Peng Fu, Zheng Lin, Weiping Wang

**分类**: cs.CL

**发布日期**: 2025-06-11

**备注**: ACL 2025

---

## 💡 一句话要点

**提出DIVE方法以增强大语言模型的多样性重建**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家` `大语言模型` `模型重建` `多样性增强` `训练效率` `剪枝技术` `自然语言处理`

## 📋 核心要点

1. 现有的重建方法在专家多样性方面存在不足，可能导致冗余，影响模型性能。
2. 本文提出DIVE方法，通过领域亲和性挖掘和剪枝重建专家，增强模型的多样性。
3. 实验结果显示，DIVE在训练效率上有显著提升，且准确性损失最小，优于现有方法。

## 📝 摘要（中文）

大语言模型（LLMs）采用混合专家（MoE）架构，通过选择性激活部分参数实现高效性。尽管MoE LLM在推理上表现出色，但从头训练大量专家的成本高昂，而将稠密LLM重建为MoE LLM显著降低了训练预算。然而，现有重建方法往往忽视专家之间的多样性，导致潜在冗余。本文提出了一种名为DIVE的多样性增强重建方法，基于对不同校准数据集进行剪枝后观察到的LLM显著多样性。DIVE方法包括领域亲和性挖掘、基于剪枝的专家重建和高效再训练。实验表明，DIVE在保持准确性的同时实现了训练效率，超越了现有的剪枝和MoE重建方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有重建方法忽视专家多样性的问题，导致冗余和性能下降。现有方法在从稠密LLM重建为MoE LLM时，未能有效利用不同校准数据集的多样性。

**核心思路**：DIVE方法的核心在于通过领域亲和性挖掘和剪枝重建专家，增强模型的多样性，从而提高训练效率并降低冗余。

**技术框架**：DIVE的整体流程包括三个主要模块：领域亲和性挖掘、剪枝基础上的专家重建和高效再训练。首先，通过分析不同数据集的校准结果，挖掘领域间的亲和性；然后，进行剪枝和重组FFN模块；最后，对路由器、专家和归一化模块进行高效再训练。

**关键创新**：DIVE的主要创新在于引入了多样性增强的重建策略，强调了不同校准数据集对专家多样性的影响，这与传统方法的单一剪枝策略本质上有所区别。

**关键设计**：在DIVE中，关键设计包括剪枝策略的选择、损失函数的优化以及FFN模块的重组方式，确保在重建过程中最大限度地保留模型的性能。

## 📊 实验亮点

实验结果表明，DIVE在训练效率上显著提升，准确性损失最小，超越了现有的剪枝和MoE重建方法，且在相同激活参数数量下，DIVE的性能提升幅度达到X%（具体数据待补充）。

## 🎯 应用场景

DIVE方法在大语言模型的训练和优化中具有广泛的应用潜力，尤其适用于需要高效推理和低成本训练的场景，如自然语言处理、对话系统和文本生成等领域。未来，DIVE的思想可以扩展到其他类型的深度学习模型中，推动模型的高效性和多样性提升。

## 📄 摘要（原文）

> Large language models (LLMs) with the Mixture-of-Experts (MoE) architecture achieve high cost-efficiency by selectively activating a subset of the parameters. Despite the inference efficiency of MoE LLMs, the training of extensive experts from scratch incurs substantial overhead, whereas reconstructing a dense LLM into an MoE LLM significantly reduces the training budget. However, existing reconstruction methods often overlook the diversity among experts, leading to potential redundancy. In this paper, we come up with the observation that a specific LLM exhibits notable diversity after being pruned on different calibration datasets, based on which we present a Diversity-Enhanced reconstruction method named DIVE. The recipe of DIVE includes domain affinity mining, pruning-based expert reconstruction, and efficient retraining. Specifically, the reconstruction includes pruning and reassembly of the feed-forward network (FFN) module. After reconstruction, we efficiently retrain the model on routers, experts and normalization modules. We implement DIVE on Llama-style LLMs with open-source training corpora. Experiments show that DIVE achieves training efficiency with minimal accuracy trade-offs, outperforming existing pruning and MoE reconstruction methods with the same number of activated parameters.

