---
layout: default
title: "No Free Lunch: Rethinking Internal Feedback for LLM Reasoning"
---

# No Free Lunch: Rethinking Internal Feedback for LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17219" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17219v2</a>
  <a href="https://arxiv.org/pdf/2506.17219.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17219v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17219v2', 'No Free Lunch: Rethinking Internal Feedback for LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanzhi Zhang, Zhaoxi Zhang, Haoxiang Guan, Yilin Cheng, Yitong Duan, Chen Wang, Yue Wang, Shuxin Zheng, Jiyan He

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-20 (更新: 2025-06-25)

---

## 💡 一句话要点

**提出内部反馈强化学习以提升大语言模型推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大语言模型` `内部反馈` `推理能力` `无监督学习` `模型训练` `数学推理` `性能评估`

## 📋 核心要点

1. 现有的强化学习方法如RLHF和RLVR依赖大量外部监督，限制了其应用的灵活性和效率。
2. 本文提出基于内部反馈的强化学习（RLIF），利用模型内部信号如熵和自我确定性，减少对外部奖励的依赖。
3. 实验表明，RLIF在训练初期显著提升了LLMs的推理性能，但在训练后期性能下降，且对已调优模型效果有限。

## 📝 摘要（中文）

强化学习已成为提升大语言模型（LLMs）推理能力的有效范式。现有方法如基于人类反馈的强化学习（RLHF）和可验证奖励的强化学习（RLVR）虽然表现良好，但依赖大量外部监督。本文探讨了一种替代方法——基于内部反馈的强化学习（RLIF），该方法仅依赖模型内部生成的信号，而非外部奖励。我们利用无监督的奖励代理，如令牌级熵、轨迹级熵和自我确定性。理论分析表明，这些内部目标在一定程度上是等价的。实验结果显示，RLIF在训练初期能够提升基础LLMs的推理性能，甚至在某些任务上超越RLVR。然而，随着训练的进行，性能下降至训练前水平。此外，RLIF对指令调优模型的提升有限，表明内部反馈在模型已调优后收益递减。我们进一步分析了这一限制，并提供了将内部反馈信号整合到LLM训练中的实用指南。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习方法对外部监督的依赖问题，尤其是在大语言模型推理能力提升中的局限性。现有方法在训练过程中需要大量的人类反馈或可验证奖励，导致效率低下和应用受限。

**核心思路**：论文提出基于内部反馈的强化学习（RLIF），该方法依赖模型内部生成的信号，如令牌级熵和轨迹级熵，来替代外部奖励。这种设计旨在减少对外部监督的需求，提高训练的灵活性和效率。

**技术框架**：RLIF的整体架构包括三个主要模块：1) 内部奖励信号生成模块，负责计算熵和自我确定性；2) 强化学习策略优化模块，利用生成的内部信号进行模型训练；3) 性能评估模块，评估模型在推理任务上的表现。

**关键创新**：RLIF的主要创新在于引入内部反馈机制，利用无监督的奖励代理来提升模型推理能力。这与现有方法的本质区别在于，RLIF不依赖外部反馈，从而降低了训练成本和复杂性。

**关键设计**：在RLIF中，关键参数包括熵计算的窗口大小、奖励信号的平滑因子等。此外，损失函数设计上采用了基于内部信号的强化学习损失，确保模型能够有效利用内部反馈进行优化。整体网络结构保持了LLM的基础架构，但在训练过程中引入了新的反馈机制。

## 📊 实验亮点

实验结果显示，RLIF在训练初期能够显著提升基础LLMs的推理性能，甚至在某些数学推理基准任务上超越RLVR。然而，随着训练的深入，性能下降至训练前水平，且对指令调优模型的提升有限，表明内部反馈的收益递减现象。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能对话系统和教育技术等。通过提升大语言模型的推理能力，RLIF可以在自动问答、文本生成和个性化学习等场景中发挥重要作用，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement learning has emerged as a powerful paradigm for post-training large language models (LLMs) to improve reasoning. Approaches like Reinforcement Learning from Human Feedback (RLHF) and Reinforcement Learning with Verifiable Rewards (RLVR) have shown strong results, but they require extensive external supervision. We investigate an alternative class of methods, Reinforcement Learning from Internal Feedback (RLIF), which relies solely on intrinsic model-derived signals instead of external rewards. In particular, we leverage unsupervised reward proxies such as token-level entropy, trajectory-level entropy, and self-certainty. Our theoretical analysis shows these internal objectives are partially equivalent, and we empirically evaluate various RLIF strategies on challenging math reasoning benchmarks. Experimental results demonstrate that RLIF can boost the reasoning performance of base LLMs at the beginning phase of the training, matching or surpassing RLVR techniques on these tasks. However, when training progresses, performance degrades even below the model before training. Moreover, we find that RLIF yields little improvement for instruction-tuned models, indicating diminishing returns of intrinsic feedback once an LLM is already instruction-tuned. We further analyze this limitation by mixing model weights and explain the reason of RLIF's training behaviors, providing practical guidelines for integrating internal feedback signals into LLM training. We hope our analysis of internal feedback will inform more principled and effective strategies for LLM post-training.

