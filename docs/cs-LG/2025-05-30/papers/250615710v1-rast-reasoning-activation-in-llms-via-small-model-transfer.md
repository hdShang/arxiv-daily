---
layout: default
title: RAST: Reasoning Activation in LLMs via Small-model Transfer
---

# RAST: Reasoning Activation in LLMs via Small-model Transfer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15710" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15710v1</a>
  <a href="https://arxiv.org/pdf/2506.15710.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15710v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15710v1', 'RAST: Reasoning Activation in LLMs via Small-model Transfer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siru Ouyang, Xinyu Zhu, Zilin Xiao, Minhao Jiang, Yu Meng, Jiawei Han

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-30

**🔗 代码/项目**: [PROJECT_PAGE](https://ozyyshr.github.io/RAST/)

---

## 💡 一句话要点

**提出RAST以高效提升大语言模型的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大语言模型` `推理能力` `模型转移` `计算效率` `数学推理` `小模型训练`

## 📋 核心要点

1. 现有的强化学习方法在大规模应用时资源消耗巨大，限制了其推广。
2. 本文提出RAST，通过小模型的RL训练转移概率调整，提升大模型的推理能力。
3. 实验结果显示，RAST在多个基准上显著提升推理能力，且GPU内存消耗显著降低。

## 📝 摘要（中文）

强化学习（RL）已成为提升大语言模型（LLMs）推理能力的有效方法，但其在规模应用时资源消耗巨大。现有研究表明，RL并未为模型赋予新知识，而是重塑了模型的输出分布。基于此，本文假设RL引起的输出概率变化在模型规模上是相对不变的，从而提出RAST方法，通过将小模型中RL训练引起的概率调整转移到大模型中，显著提升其推理能力。实验结果表明，RAST在多个数学推理基准上表现优异，且所需GPU内存显著低于直接RL训练，甚至在某些情况下超越了RL训练的模型。该研究为RL驱动的推理提供了新见解，并提出了在不增加计算成本的情况下扩展其优势的实用策略。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习在大语言模型推理能力提升中的资源消耗问题。现有方法需要多个模型副本和大量GPU计算，限制了其应用。

**核心思路**：论文提出的RAST方法假设RL引起的输出概率变化在不同规模模型中是相对不变的，因此可以通过训练一个小模型并将其概率调整转移到大模型中，从而高效提升推理能力。

**技术框架**：RAST的整体架构包括两个主要阶段：首先，使用强化学习训练一个小模型；其次，将小模型中获得的概率调整应用于更大的基础模型，以增强其推理能力。

**关键创新**：RAST的核心创新在于通过小模型的RL训练实现概率调整的转移，这一方法与传统的直接在大模型上进行RL训练的方式本质上不同，显著降低了计算成本。

**关键设计**：在设计中，RAST关注于小模型的训练过程和输出概率的对齐，确保在转移过程中保持高一致性。此外，论文还探讨了损失函数的选择和模型参数的设置，以优化转移效果。

## 📊 实验亮点

实验结果表明，RAST在多个数学推理基准上显著提升了大模型的推理能力，所需GPU内存比直接RL训练低得多。在某些情况下，RAST的性能甚至超过了经过RL训练的模型，展示了其有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动推理等。通过提升大语言模型的推理能力，RAST可以在教育、金融分析和科学研究等多个领域提供更为精准的决策支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement learning (RL) has become a powerful approach for improving the reasoning capabilities of large language models (LLMs), as evidenced by recent successes such as OpenAI's o1 and Deepseek-R1. However, applying RL at scale remains intimidatingly resource-intensive, requiring multiple model copies and extensive GPU workloads. On the other hand, while being powerful, recent studies suggest that RL does not fundamentally endow models with new knowledge; rather, it primarily reshapes the model's output distribution to activate reasoning capabilities latent in the base model. Building on this insight, we hypothesize that the changes in output probabilities induced by RL are largely model-size invariant, opening the door to a more efficient paradigm: training a small model with RL and transferring its induced probability shifts to larger base models. To verify our hypothesis, we conduct a token-level analysis of decoding trajectories and find high alignment in RL-induced output distributions across model scales, validating our hypothesis. Motivated by this, we propose RAST, a simple yet effective method that transfers reasoning behaviors by injecting RL-induced probability adjustments from a small RL-trained model into larger models. Experiments across multiple mathematical reasoning benchmarks show that RAST substantially and consistently enhances the reasoning capabilities of base models while requiring significantly lower GPU memory than direct RL training, sometimes even yielding better performance than the RL-trained counterparts. Our findings offer new insights into the nature of RL-driven reasoning and practical strategies for scaling its benefits without incurring its full computational cost. The project page of RAST is available at https://ozyyshr.github.io/RAST/.

