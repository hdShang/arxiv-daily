---
layout: default
title: "Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies"
---

# Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19673" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19673v1</a>
  <a href="https://arxiv.org/pdf/2512.19673.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19673v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19673v1', 'Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuqiao Tan, Minzheng Wang, Shizhu He, Huanxuan Liao, Chengfeng Zhao, Qiunan Lu, Tian Liang, Jun Zhao, Kang Liu

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-12-22

**备注**: Preprint. Our code is available at https://github.com/Trae1ounG/BuPO

**🔗 代码/项目**: [GITHUB](https://github.com/Trae1ounG/BuPO)

---

## 💡 一句话要点

**提出自底向上策略优化(BuPO)，通过优化LLM内部策略提升复杂推理能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `策略优化` `内部策略` `复杂推理`

## 📋 核心要点

1. 现有强化学习方法忽略了LLM内部的层级结构和模块化设计，将其视为单一策略，限制了优化潜力。
2. 论文提出自底向上策略优化（BuPO），通过分解LLM策略，优化内部层策略，从而提升整体性能。
3. 实验表明，BuPO通过在底层对齐训练目标，能够有效重建基础推理能力，并在复杂推理任务上取得显著提升。

## 📝 摘要（中文）

现有的强化学习方法将大型语言模型（LLM）视为一个单一的统一策略，忽略了其内部机制。理解策略如何在层和模块之间演变对于实现更有针对性的优化和揭示复杂的推理机制至关重要。本文通过利用Transformer残差流的内在分割以及隐藏状态与unembedding矩阵的组合与可采样策略之间的等价性来分解语言模型策略。这种分解揭示了内部层策略（对应于来自各个层的贡献）和内部模块策略（与每层内的自注意力和前馈网络（FFN）组件对齐）。通过分析内部策略的熵，我们发现：（a）早期层保持高熵以进行探索，顶层收敛到接近零熵以进行细化，并且收敛模式在模型系列之间有所不同。（b）LLama的预测空间在最后一层迅速收敛，而Qwen系列模型，尤其是Qwen3，表现出更像人类的、逐步结构化的推理模式。受这些发现的启发，我们提出了一种新颖的强化学习范例——自底向上策略优化（BuPO），该范例直接优化早期训练期间的内部层策略。通过在较低层对齐训练目标，BuPO重建了基础推理能力并实现了卓越的性能。在复杂推理基准上的大量实验证明了我们方法的有效性。

## 🔬 方法详解

**问题定义**：现有强化学习方法将LLM视为一个黑盒，忽略了其内部结构，无法针对性地优化不同层和模块的功能。这种方法无法充分利用LLM的潜力，尤其是在复杂推理任务中。现有方法缺乏对LLM内部策略演化过程的理解，难以揭示其推理机制。

**核心思路**：论文的核心思路是将LLM的策略分解为内部层策略和内部模块策略，分别对应于Transformer的每一层以及每一层中的自注意力机制和前馈网络。通过分析这些内部策略的熵，可以了解LLM在不同层和模块上的行为模式。基于此，论文提出自底向上策略优化（BuPO），通过在早期训练阶段直接优化底层策略，从而引导LLM学习更有效的推理能力。

**技术框架**：BuPO的技术框架主要包括以下几个步骤：1) **策略分解**：利用Transformer的残差连接和unembedding矩阵，将LLM的整体策略分解为内部层策略和内部模块策略。2) **熵分析**：分析不同层和模块的策略熵，了解LLM在不同阶段的行为模式。3) **自底向上优化**：在早期训练阶段，直接优化底层策略，使其更好地对齐训练目标。4) **整体策略优化**：在底层策略优化完成后，再进行整体策略的优化，从而提升LLM的整体性能。

**关键创新**：BuPO的关键创新在于：1) **策略分解**：首次将LLM的策略分解为内部层策略和内部模块策略，为理解LLM的内部机制提供了新的视角。2) **自底向上优化**：提出了一种新的强化学习范式，通过在早期训练阶段优化底层策略，从而引导LLM学习更有效的推理能力。与现有方法相比，BuPO能够更有效地利用LLM的内部结构，从而提升其性能。

**关键设计**：BuPO的关键设计包括：1) **残差连接和unembedding矩阵的使用**：利用Transformer的残差连接和unembedding矩阵，实现了LLM策略的分解。2) **熵的计算**：通过计算不同层和模块的策略熵，了解LLM在不同阶段的行为模式。3) **底层策略的优化目标**：在底层策略的优化过程中，需要设计合适的优化目标，使其能够更好地对齐整体训练目标。具体的损失函数和优化算法的选择需要根据具体的任务进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19673v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19673v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19673v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，BuPO在复杂推理基准上取得了显著的性能提升。例如，在某些任务上，BuPO的性能超过了现有最先进的方法。通过分析内部策略的熵，论文还发现不同LLM的推理模式存在差异，例如LLama在最后一层迅速收敛，而Qwen系列模型则表现出更像人类的逐步结构化推理模式。

## 🎯 应用场景

该研究成果可应用于各种需要复杂推理能力的场景，例如问答系统、对话生成、代码生成等。通过优化LLM的内部策略，可以提升其推理能力和泛化能力，使其能够更好地解决实际问题。此外，该研究还可以帮助我们更好地理解LLM的内部机制，为未来的模型设计和优化提供指导。

## 📄 摘要（原文）

> Existing reinforcement learning (RL) approaches treat large language models (LLMs) as a single unified policy, overlooking their internal mechanisms. Understanding how policy evolves across layers and modules is therefore crucial for enabling more targeted optimization and raveling out complex reasoning mechanisms. In this paper, we decompose the language model policy by leveraging the intrinsic split of the Transformer residual stream and the equivalence between the composition of hidden states with the unembedding matrix and the resulting samplable policy. This decomposition reveals Internal Layer Policies, corresponding to contributions from individual layers, and Internal Modular Policies, which align with the self-attention and feed-forward network (FFN) components within each layer. By analyzing the entropy of internal policy, we find that: (a) Early layers keep high entropy for exploration, top layers converge to near-zero entropy for refinement, with convergence patterns varying across model series. (b) LLama's prediction space rapidly converges in the final layer, whereas Qwen-series models, especially Qwen3, exhibit a more human-like, progressively structured reasoning pattern. Motivated by these findings, we propose Bottom-up Policy Optimization (BuPO), a novel RL paradigm that directly optimizes the internal layer policy during early training. By aligning training objective at lower layer, BuPO reconstructs foundational reasoning capabilities and achieves superior performance. Extensive experiments on complex reasoning benchmarks demonstrates the effectiveness of our method. Our code is available at https://github.com/Trae1ounG/BuPO.

