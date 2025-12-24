---
layout: default
title: "Uni-LoRA: One Vector is All You Need"
---

# Uni-LoRA: One Vector is All You Need

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00799" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00799v3</a>
  <a href="https://arxiv.org/pdf/2506.00799.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00799v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00799v3', 'Uni-LoRA: One Vector is All You Need')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiyang Li, Shaobo Han, Qing Su, Wei Li, Zhipeng Cai, Shihao Ji

**分类**: cs.LG

**发布日期**: 2025-06-01 (更新: 2025-10-28)

**备注**: NeurIPS 2025 Spotlight

**🔗 代码/项目**: [GITHUB](https://github.com/KaiyangLi1992/Uni-LoRA)

---

## 💡 一句话要点

**提出Uni-LoRA框架以实现高效的参数共享与微调**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低秩适应` `参数高效微调` `大型语言模型` `全局参数共享` `等距投影矩阵` `统一框架` `机器学习`

## 📋 核心要点

1. 现有LoRA变体在参数共享上存在局限，导致参数效率降低，尤其是层间共享受限。
2. 提出的Uni-LoRA框架通过使用等距投影矩阵，实现了全局参数共享，仅需一个可训练向量重构整个LLM的LoRA参数。
3. 在GLUE等基准测试中，Uni-LoRA展现出卓越的参数效率，并在预测性能上与现有方法相当或更优。

## 📝 摘要（中文）

低秩适应（LoRA）已成为大型语言模型（LLMs）参数高效微调的标准方法，通过将权重更新限制为低秩矩阵。本文提出了一个统一框架Uni-LoRA，展示了不同LoRA变体的参数空间缩减策略可以在此框架下进行统一表述。Uni-LoRA通过从低维子空间投影重构高维参数空间，采用等距投影矩阵实现全局参数共享，显著降低计算开销。实验结果表明，Uni-LoRA在GLUE、数学推理和指令微调基准上实现了最先进的参数效率，同时在预测性能上超越或匹配了先前的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LoRA变体在参数共享方面的不足，尤其是层间共享受限的问题，这限制了参数效率的提升。

**核心思路**：Uni-LoRA框架通过引入等距投影矩阵，允许全局参数共享，从而仅需一个可训练向量即可重构LoRA参数，简化了微调过程。

**技术框架**：该框架首先将LoRA参数空间视为高维向量空间，通过从低维子空间进行投影来实现参数重构，核心在于选择合适的投影矩阵。

**关键创新**：Uni-LoRA的主要创新在于其统一的参数空间重构方法和等距投影矩阵的引入，这与现有方法的层级或结构特定投影形成鲜明对比。

**关键设计**：在设计中，Uni-LoRA仅需一个可训练的向量，且通过优化投影矩阵的选择，显著降低了计算开销，同时保持了模型的预测性能。

## 📊 实验亮点

在GLUE、数学推理和指令微调基准上，Uni-LoRA展现出最先进的参数效率，具体实验结果显示其在多个任务上超越或与现有方法持平，证明了其在实际应用中的有效性与优越性。

## 🎯 应用场景

Uni-LoRA框架在大型语言模型的微调中具有广泛的应用潜力，特别是在需要高效参数调整的场景，如自然语言处理、对话系统和智能助手等。其高效的参数共享机制能够降低计算资源消耗，提升模型的适应性和灵活性，未来可能推动更多领域的研究与应用。

## 📄 摘要（原文）

> Low-Rank Adaptation (LoRA) has become the de facto parameter-efficient fine-tuning (PEFT) method for large language models (LLMs) by constraining weight updates to low-rank matrices. Recent works such as Tied-LoRA, VeRA, and VB-LoRA push efficiency further by introducing additional constraints to reduce the trainable parameter space. In this paper, we show that the parameter space reduction strategies employed by these LoRA variants can be formulated within a unified framework, Uni-LoRA, where the LoRA parameter space, flattened as a high-dimensional vector space $R^D$, can be reconstructed through a projection from a subspace R^d, with $d \ll D$. We demonstrate that the fundamental difference among various LoRA methods lies in the choice of the projection matrix, $P \in R^{D \times d}$.Most existing LoRA variants rely on layer-wise or structure-specific projections that limit cross-layer parameter sharing, thereby compromising parameter efficiency. In light of this, we introduce an efficient and theoretically grounded projection matrix that is isometric, enabling global parameter sharing and reducing computation overhead. Furthermore, under the unified view of Uni-LoRA, this design requires only a single trainable vector to reconstruct LoRA parameters for the entire LLM - making Uni-LoRA both a unified framework and a "one-vector-only" solution. Extensive experiments on GLUE, mathematical reasoning, and instruction tuning benchmarks demonstrate that Uni-LoRA achieves state-of-the-art parameter efficiency while outperforming or matching prior approaches in predictive performance. Our code is available at https://github.com/KaiyangLi1992/Uni-LoRA.

