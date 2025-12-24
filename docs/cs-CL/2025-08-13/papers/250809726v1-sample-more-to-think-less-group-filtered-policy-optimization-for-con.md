---
layout: default
title: "Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning"
---

# Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09726" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09726v1</a>
  <a href="https://arxiv.org/pdf/2508.09726.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09726v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09726v1', 'Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vaishnavi Shrivastava, Ahmed Awadallah, Vidhisha Balachandran, Shivam Garg, Harkirat Behl, Dimitris Papailiopoulos

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出GFPO以解决长文本生成中的冗余问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本生成` `强化学习` `语言模型` `文本优化` `动态资源分配`

## 📋 核心要点

1. 现有方法在生成长文本时，往往会出现冗余和无效的填充内容，影响生成效率。
2. GFPO通过在训练时采样更大的问题组，并根据响应长度和token效率进行过滤，优化生成过程。
3. 在多个STEM和编码基准测试中，GFPO显著减少了生成文本的长度，同时保持了高准确性。

## 📝 摘要（中文）

大型语言模型在使用可验证奖励的强化学习训练时，往往会为了提高准确性而导致生成文本长度的膨胀。尽管在处理复杂问题时，较长的回答是合理的，但许多文本仅为“填充”，即重复和冗长的内容，未能实质性推进。本文提出了GFPO（Group Filtered Policy Optimization），通过在训练期间对每个问题进行更大组的采样，并基于响应长度和每个token的奖励比率这两个关键指标进行过滤，从而抑制文本长度的膨胀。GFPO在Phi-4推理模型上，显著减少了46-71%的长度膨胀，同时保持了准确性。优化每个token的奖励比率进一步将长度膨胀的减少提升至71-85%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成文本时出现的冗长和无效填充问题。现有方法在追求准确性时，往往导致生成文本长度的显著膨胀，影响了生成效率和实用性。

**核心思路**：GFPO的核心思想是通过在训练阶段对每个问题进行更大组的采样，从而减少生成时的冗余内容。通过过滤响应，模型能够在保持准确性的同时，显著降低生成文本的长度。

**技术框架**：GFPO的整体架构包括两个主要阶段：首先是对问题进行大规模采样，其次是基于响应长度和token效率进行过滤。通过这种方式，模型在训练时能够学习到更有效的生成策略。

**关键创新**：GFPO的主要创新在于通过动态调整训练资源，针对更难的问题分配更多的计算资源，从而提高了模型在复杂问题上的表现。这一方法与传统的静态训练方法形成鲜明对比。

**关键设计**：在GFPO中，关键参数设置包括响应长度和token效率的权重调整。此外，损失函数的设计也考虑了生成文本的有效性，以确保模型在训练过程中能够优化生成质量。通过这些设计，GFPO实现了在生成效率和准确性之间的良好平衡。

## 📊 实验亮点

GFPO在Phi-4推理模型上实现了46-71%的长度膨胀减少，同时保持了高准确性。优化每个token的奖励比率后，长度膨胀的减少幅度进一步提升至71-85%。这些结果表明，GFPO在生成效率和准确性之间实现了有效的平衡。

## 🎯 应用场景

GFPO的研究成果在多个领域具有广泛的应用潜力，尤其是在需要生成长文本的任务中，如教育、编程辅助和科学研究等。通过减少冗余内容，GFPO能够提高文本生成的效率和质量，未来可能在智能助手和自动化内容生成等领域发挥重要作用。

## 📄 摘要（原文）

> Large language models trained with reinforcement learning with verifiable rewards tend to trade accuracy for length--inflating response lengths to achieve gains in accuracy. While longer answers may be warranted for harder problems, many tokens are merely "filler": repetitive, verbose text that makes no real progress. We introduce GFPO (Group Filtered Policy Optimization), which curbs this length explosion by sampling larger groups per problem during training and filtering responses to train on based on two key metrics: (1) response length and (2) token efficiency: reward per token ratio. By sampling more at training time, we teach models to think less at inference time. On the Phi-4-reasoning model, GFPO cuts GRPO's length inflation by 46-71% across challenging STEM and coding benchmarks (AIME 24/25, GPQA, Omni-MATH, LiveCodeBench) while maintaining accuracy. Optimizing for reward per token further increases reductions in length inflation to 71-85%. We also propose Adaptive Difficulty GFPO, which dynamically allocates more training resources to harder problems based on real-time difficulty estimates, improving the balance between computational efficiency and accuracy especially on difficult questions. GFPO demonstrates that increased training-time compute directly translates to reduced test-time compute--a simple yet effective trade-off for efficient reasoning.

