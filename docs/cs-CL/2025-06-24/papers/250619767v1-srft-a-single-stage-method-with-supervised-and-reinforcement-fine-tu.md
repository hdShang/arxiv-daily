---
layout: default
title: "SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning"
---

# SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19767" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19767v1</a>
  <a href="https://arxiv.org/pdf/2506.19767.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19767v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19767v1', 'SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuqian Fu, Tinghong Chen, Jiajun Chai, Xihuai Wang, Songjun Tu, Guojun Yin, Wei Lin, Qichao Zhang, Yuanheng Zhu, Dongbin Zhao

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-24

---

## 💡 一句话要点

**提出SRFT方法以优化大语言模型推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `监督微调` `强化学习` `推理能力` `熵感知机制` `单阶段优化` `数学推理` `分布外推理`

## 📋 核心要点

1. 现有方法在整合监督微调和强化学习时存在效率低下和效果不佳的问题。
2. SRFT方法通过熵感知加权机制，将SFT和RL统一为单阶段优化，提升了模型的推理能力。
3. SRFT在多个基准测试中表现优异，特别是在数学推理和分布外推理任务上显著提高了准确率。

## 📝 摘要（中文）

大型语言模型（LLMs）在推理任务中取得了显著进展，但如何最佳地整合监督微调（SFT）和强化学习（RL）仍然是一个基本挑战。通过对标记分布、学习动态和集成机制的全面分析，我们揭示了这两种范式之间的关键差异：SFT引入了粗粒度的全局变化，而RL则进行细粒度的选择性优化，熵作为训练有效性的关键指标。基于这些观察，我们提出了监督强化微调（SRFT），这是一种通过熵感知加权机制统一两种微调范式的单阶段方法。我们的方案同时应用SFT和RL，直接优化LLM，实验表明SRFT在五个数学推理基准上平均准确率达到59.1%，比零强化学习方法提高了9.0%。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在推理任务中，监督微调（SFT）与强化学习（RL）整合不佳的问题，现有方法往往采用两阶段的顺序优化，导致效率低下。

**核心思路**：我们提出的SRFT方法通过熵感知加权机制，将SFT和RL结合为单阶段优化，能够同时利用示例和自我探索的回合进行训练，从而提高模型的推理能力。

**技术框架**：SRFT的整体架构包括数据输入、熵计算、SFT和RL的联合优化模块。首先，通过熵计算评估当前模型的学习状态，然后根据熵值动态调整SFT和RL的权重，最后进行联合训练。

**关键创新**：SRFT的主要创新在于其熵感知加权机制，这一机制使得模型能够在训练过程中自适应地调整SFT和RL的影响力，从而实现更有效的学习。与现有方法相比，SRFT避免了两阶段训练的复杂性，提升了训练效率。

**关键设计**：在SRFT中，我们设计了特定的损失函数以平衡SFT和RL的影响，并采用了动态学习率策略来优化训练过程。此外，模型结构上采用了多层次的神经网络，以增强其表达能力和推理能力。

## 📊 实验亮点

SRFT在五个数学推理基准上平均准确率达到59.1%，比零强化学习方法提高了9.0%。在三个分布外基准上，SRFT的表现也显著提升，准确率提高了10.9%，展示了其在推理任务中的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括教育、金融和医疗等需要复杂推理的场景。SRFT方法能够提升大语言模型在这些领域的推理能力，从而为决策支持和智能助手等应用提供更为准确的结果，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved remarkable progress in reasoning tasks, yet the optimal integration of Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) remains a fundamental challenge. Through comprehensive analysis of token distributions, learning dynamics, and integration mechanisms from entropy-based perspectives, we reveal key differences between these paradigms: SFT induces coarse-grained global changes to LLM policy distributions, while RL performs fine-grained selective optimizations, with entropy serving as a critical indicator of training effectiveness. Building on these observations, we propose Supervised Reinforcement Fine-Tuning (SRFT), a single-stage method that unifies both fine-tuning paradigms through entropy-aware weighting mechanisms. Our approach simultaneously applies SFT and RL to directly optimize the LLM using demonstrations and self-exploration rollouts rather than through two-stage sequential methods. Extensive experiments show that SRFT achieves 59.1% average accuracy, outperforming zero-RL methods by 9.0% on five mathematical reasoning benchmarks and 10.9% on three out-of-distribution benchmarks.

