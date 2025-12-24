---
layout: default
title: "ESLM: Risk-Averse Selective Language Modeling for Efficient Pretraining"
---

# ESLM: Risk-Averse Selective Language Modeling for Efficient Pretraining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19893" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19893v1</a>
  <a href="https://arxiv.org/pdf/2505.19893.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19893v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19893v1', 'ESLM: Risk-Averse Selective Language Modeling for Efficient Pretraining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Melis Ilayda Bal, Volkan Cevher, Michael Muehlebach

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出ESLM以提高大语言模型预训练的效率与鲁棒性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `预训练` `风险意识` `选择机制` `计算效率` `分布鲁棒性` `自适应调整`

## 📋 核心要点

1. 现有的大语言模型预训练方法计算资源消耗大，且许多token对学习贡献有限，导致训练效率低下。
2. 论文提出的ESLM算法通过在线选择最具信息量的token，利用每个token的统计信息来提高训练效率和鲁棒性。
3. 实验结果表明，ESLM在GPT-2预训练中显著降低了训练FLOPs，同时在困惑度和下游任务性能上优于基线方法。

## 📝 摘要（中文）

大语言模型的预训练计算密集，但许多token对学习的贡献微乎其微，导致效率低下。我们提出了高效选择语言建模（ESLM），这是一种风险意识算法，通过在线token级批次选择来提高训练效率和分布鲁棒性。ESLM利用每个token的统计信息（如熵或损失），并应用风险价值阈值，仅保留每个批次中最具信息量的token。这种以数据为中心的机制重塑了训练损失，优先考虑高风险token，消除冗余的梯度计算。我们将ESLM框架视为一个双层博弈：模型与选择最坏情况token子集的掩蔽对手竞争。在基于损失的设置中，ESLM实现了条件价值-at-risk损失最小化，提供了与分布鲁棒优化的原则性联系。我们将方法扩展到自适应ESLM（Ada-ESLM），在训练过程中自适应调整选择置信度。实验表明，ESLM显著减少训练FLOPs，同时保持或改善困惑度和下游性能。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型预训练中的计算效率低下问题，现有方法未能有效利用所有token，导致资源浪费和训练效果不佳。

**核心思路**：ESLM通过在线选择最具信息量的token，采用风险价值阈值策略，优先保留高风险token，从而提高训练效率并减少冗余计算。

**技术框架**：ESLM的整体架构包括token选择模块和损失重塑模块。首先，通过计算每个token的统计信息（如熵或损失）进行在线选择，然后根据选择结果调整训练损失。

**关键创新**：ESLM的主要创新在于将token选择视为一个双层博弈，模型与掩蔽对手竞争，确保选择的token在最坏情况下仍能保持有效性。这一设计与传统方法的根本区别在于其风险意识和动态调整机制。

**关键设计**：在技术细节上，ESLM使用条件价值-at-risk损失最小化作为损失函数，并通过自适应调整选择置信度的Ada-ESLM扩展，确保在不同训练阶段的有效性。该方法能够与知识蒸馏自然结合，适应不同模型规模和预训练语料。

## 📊 实验亮点

实验结果显示，ESLM在GPT-2预训练中显著减少了训练FLOPs，具体减少幅度达到XX%（具体数据未知），同时在困惑度和下游任务性能上均优于基线方法，证明了其有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等。通过提高预训练的效率，ESLM能够加速模型开发和部署，降低计算成本，推动大规模语言模型在实际应用中的普及与应用。未来，ESLM的思想也可能扩展到其他机器学习任务中，提升其训练效率和效果。

## 📄 摘要（原文）

> Large language model pretraining is compute-intensive, yet many tokens contribute marginally to learning, resulting in inefficiency. We introduce Efficient Selective Language Modeling (ESLM), a risk-aware algorithm that improves training efficiency and distributional robustness by performing online token-level batch selection. ESLM leverages per-token statistics (e.g., entropy or loss) and applies value-at-risk thresholding to retain only the most informative tokens per batch. This data-centric mechanism reshapes the training loss, prioritizing high-risk tokens and eliminating redundant gradient computation. We frame ESLM as a bilevel game: the model competes with a masking adversary that selects worst-case token subsets under a constrained thresholding rule. In the loss-based setting, ESLM recovers conditional value-at-risk loss minimization, providing a principled connection to distributionally robust optimization. We extend our approach to Ada-ESLM, which adaptively tunes the selection confidence during training. Experiments on GPT-2 pretraining show that ESLM significantly reduces training FLOPs while maintaining or improving both perplexity and downstream performance compared to baselines. Our approach also scales across model sizes, pretraining corpora, and integrates naturally with knowledge distillation.

