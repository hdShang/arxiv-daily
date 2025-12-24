---
layout: default
title: "RLAE: Reinforcement Learning-Assisted Ensemble for LLMs"
---

# RLAE: Reinforcement Learning-Assisted Ensemble for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00439" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00439v1</a>
  <a href="https://arxiv.org/pdf/2506.00439.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00439v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00439v1', 'RLAE: Reinforcement Learning-Assisted Ensemble for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuqian Fu, Yuanheng Zhu, Jiajun Chai, Guojun Yin, Wei Lin, Qichao Zhang, Dongbin Zhao

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-31

---

## 💡 一句话要点

**提出RLAE以解决LLM集成动态权重调整问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `集成学习` `动态权重` `马尔可夫决策过程` `模型泛化` `自然语言处理`

## 📋 核心要点

1. 现有的LLM集成方法依赖固定权重策略，无法适应模型能力的动态变化，导致性能不足。
2. 本文提出的RLAE框架通过强化学习动态调整集成权重，考虑输入上下文和生成状态，提升了集成效果。
3. 实验表明，RLAE在多项任务上相较于传统方法提升了最高3.3%的准确率，并且具有更好的泛化能力。

## 📝 摘要（中文）

集成大型语言模型（LLMs）能够有效结合不同模型的优势，从而提升多种任务的性能。然而，现有方法通常依赖固定的权重策略，无法适应LLM能力的动态和上下文依赖特性。本文提出了一种新颖的框架——强化学习辅助集成（RLAE），通过马尔可夫决策过程（MDP）重新构建LLM集成。该方法引入了一个强化学习代理，动态调整集成权重，考虑输入上下文和中间生成状态，并通过与最终输出质量直接相关的奖励进行训练。实验结果表明，RLAE在多个任务上相较于传统集成方法提升了最高3.3%的准确率，同时展现出更强的泛化能力和更低的时间延迟。

## 🔬 方法详解

**问题定义**：现有的LLM集成方法通常使用固定的权重策略，无法根据输入的上下文和模型的动态状态进行调整，导致性能的局限性。

**核心思路**：RLAE框架通过将LLM集成视为一个马尔可夫决策过程，引入强化学习代理来动态调整权重，从而更好地适应不同任务和上下文。

**技术框架**：RLAE的整体架构包括输入上下文的分析、生成状态的评估和强化学习代理的训练。代理根据最终输出的质量进行权重调整，形成闭环反馈。

**关键创新**：RLAE的主要创新在于使用强化学习动态调整集成权重，这与传统方法的静态权重策略形成了鲜明对比，使得集成模型能够更灵活地适应不同的任务需求。

**关键设计**：在RLAE中，强化学习代理的训练使用与输出质量直接相关的奖励信号，采用了单代理和多代理的强化学习算法（如RLAE_PPO和RLAE_MAPPO），以优化集成效果。具体的参数设置和损失函数设计也经过精心调整，以确保模型的高效性和稳定性。

## 📊 实验亮点

在多项任务的评估中，RLAE相较于传统集成方法提升了最高3.3%的准确率，展现出更强的泛化能力，并且在时间延迟方面表现更优，证明了其在LLM集成中的有效性。

## 🎯 应用场景

RLAE框架在自然语言处理、对话系统和文本生成等领域具有广泛的应用潜力。通过动态调整集成权重，该方法能够在不同任务中提供更高的准确性和响应速度，具有显著的实际价值和未来影响。

## 📄 摘要（原文）

> Ensembling large language models (LLMs) can effectively combine diverse strengths of different models, offering a promising approach to enhance performance across various tasks. However, existing methods typically rely on fixed weighting strategies that fail to adapt to the dynamic, context-dependent characteristics of LLM capabilities. In this work, we propose Reinforcement Learning-Assisted Ensemble for LLMs (RLAE), a novel framework that reformulates LLM ensemble through the lens of a Markov Decision Process (MDP). Our approach introduces a RL agent that dynamically adjusts ensemble weights by considering both input context and intermediate generation states, with the agent being trained using rewards that directly correspond to the quality of final outputs. We implement RLAE using both single-agent and multi-agent reinforcement learning algorithms ($\text{RLAE}_\text{PPO}$ and $\text{RLAE}_\text{MAPPO}$ ), demonstrating substantial improvements over conventional ensemble methods. Extensive evaluations on a diverse set of tasks show that RLAE outperforms existing approaches by up to $3.3\%$ accuracy points, offering a more effective framework for LLM ensembling. Furthermore, our method exhibits superior generalization capabilities across different tasks without the need for retraining, while simultaneously achieving lower time latency.

