---
layout: default
title: "SparseMM: Head Sparsity Emerges from Visual Concept Responses in MLLMs"
---

# SparseMM: Head Sparsity Emerges from Visual Concept Responses in MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05344" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05344v2</a>
  <a href="https://arxiv.org/pdf/2506.05344.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05344v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05344v2', 'SparseMM: Head Sparsity Emerges from Visual Concept Responses in MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahui Wang, Zuyan Liu, Yongming Rao, Jiwen Lu

**分类**: cs.CV

**发布日期**: 2025-06-05 (更新: 2025-07-05)

**备注**: Accepted to ICCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/CR400AF-A/SparseMM)

---

## 💡 一句话要点

**提出SparseMM以优化多模态大语言模型的视觉理解效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉理解` `注意力机制` `KV-Cache优化` `稀疏性` `计算资源分配` `性能优化`

## 📋 核心要点

1. 现有的多模态大语言模型在处理视觉输入时，存在注意力头利用不均的问题，导致计算资源浪费。
2. 本研究提出SparseMM，通过分析注意力机制识别出对视觉理解有贡献的稀疏注意力头，并优化计算资源分配。
3. 实验结果表明，SparseMM在生成过程中实现了1.38倍的实时加速和52%的内存减少，同时保持了性能的平衡。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）通常通过扩展预训练的大语言模型（LLMs）来实现视觉能力的增强。本研究通过分析注意力机制，揭示了一个意外的稀疏现象：在LLMs中，只有约5%的注意力头积极参与视觉理解，称为视觉头。为高效识别这些头，我们设计了一种无训练框架，通过目标响应分析量化头级视觉相关性。在此基础上，我们提出了SparseMM，一种KV-Cache优化策略，根据视觉得分为LLMs中的头分配不对称计算预算，利用视觉头的稀疏性加速MLLMs的推理。与忽视视觉特性的先前KV-Cache加速方法相比，SparseMM在解码过程中优先考虑视觉语义的保留和压力。广泛的评估显示，SparseMM在主流多模态基准上实现了优越的准确性与效率平衡。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态大语言模型在视觉理解中注意力头利用不均的问题，现有方法未能有效识别和利用对视觉理解有贡献的注意力头，导致计算资源浪费。

**核心思路**：论文的核心思路是通过设计一种无训练的框架，量化头级视觉相关性，从而识别出稀疏的视觉头，并基于这些视觉得分优化计算预算，以提高推理效率。

**技术框架**：整体架构包括两个主要模块：首先是通过目标响应分析识别视觉头，其次是SparseMM策略，根据视觉得分为不同的注意力头分配计算资源，优化KV-Cache的使用。

**关键创新**：最重要的技术创新在于提出了SparseMM策略，利用视觉头的稀疏性进行计算优化，与现有方法相比，SparseMM更关注视觉语义的保留和解码过程中的压力管理。

**关键设计**：在设计中，SparseMM通过分析注意力头的视觉得分来动态调整计算预算，确保高效利用计算资源，同时在损失函数和网络结构上进行了优化，以支持这一策略的实现。

## 📊 实验亮点

实验结果显示，SparseMM在多模态基准测试中实现了1.38倍的实时加速和52%的内存减少，同时在效率测试中保持了性能的平衡。这一显著提升证明了SparseMM在优化多模态大语言模型推理效率方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能视觉系统、自动驾驶、机器人视觉等多模态任务。通过优化多模态大语言模型的推理效率，SparseMM能够在实时处理和资源受限的环境中提供更高效的解决方案，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) are commonly derived by extending pre-trained Large Language Models (LLMs) with visual capabilities. In this work, we investigate how MLLMs process visual inputs by analyzing their attention mechanisms. We reveal a surprising sparsity phenomenon: only a small subset (approximately less than 5%) of attention heads in LLMs actively contribute to visual understanding, termed visual heads. To identify these heads efficiently, we design a training-free framework that quantifies head-level visual relevance through targeted response analysis. Building on this discovery, we introduce SparseMM, a KV-Cache optimization strategy that allocates asymmetric computation budgets to heads in LLMs based on their visual scores, leveraging the sparity of visual heads for accelerating the inference of MLLMs. Compared with prior KV-Cache acceleration methods that ignore the particularity of visual, SparseMM prioritizes stress and retaining visual semantics during decoding. Extensive evaluations across mainstream multimodal benchmarks demonstrate that SparseMM achieves superior accuracy-efficiency trade-offs. Notably, SparseMM delivers 1.38x real-time acceleration and 52% memory reduction during generation while maintaining performance parity on efficiency test. Our project is open sourced at https://github.com/CR400AF-A/SparseMM.

