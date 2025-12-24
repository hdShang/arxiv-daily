---
layout: default
title: "CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models"
---

# CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09675" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09675v1</a>
  <a href="https://arxiv.org/pdf/2509.09675.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09675v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09675v1', 'CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Runpeng Dai, Linfeng Song, Haolin Liu, Zhenwen Liang, Dian Yu, Haitao Mi, Zhaopeng Tu, Rui Liu, Tong Zheng, Hongtu Zhu, Dong Yu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-11

**备注**: 21 pages

---

## 💡 一句话要点

**提出好奇心驱动探索(CDE)框架，提升大型语言模型在强化学习中的探索效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `好奇心驱动探索` `探索奖励` `策略学习`

## 📋 核心要点

1. 现有RLVR方法在增强LLM推理能力时，存在探索不足的问题，导致模型过早收敛和熵崩溃。
2. CDE框架利用模型自身的好奇心指导探索，通过actor的困惑度和critic的价值估计方差作为探索奖励。
3. 实验表明，CDE在AIME基准测试中相比标准RLVR方法有显著提升，并揭示了RLVR中的校准崩溃机制。

## 📝 摘要（中文）

本文提出了一种名为好奇心驱动探索(CDE)的框架，旨在解决大型语言模型(LLM)在基于可验证奖励的强化学习(RLVR)中探索不足，导致过早收敛和熵崩溃的问题。CDE利用模型自身的内在好奇心来指导探索，通过actor和critic的信号来形式化好奇心：对于actor，使用生成响应的困惑度；对于critic，使用多头架构中价值估计的方差。这些信号作为RLVR框架内的探索奖励来引导模型。理论分析表明，actor奖励能够惩罚过度自信的错误并促进正确响应的多样性；critic奖励与强化学习中基于计数的探索奖励相关。实验结果表明，在AIME基准测试中，CDE使用GRPO/PPO算法相比标准RLVR方法提升了约3个百分点。进一步分析揭示了RLVR中的校准崩溃机制，阐明了LLM常见的失败模式。

## 🔬 方法详解

**问题定义**：现有基于可验证奖励的强化学习(RLVR)方法在训练大型语言模型(LLM)时，面临探索效率低下的问题。模型容易陷入局部最优，无法充分探索潜在的解空间，导致性能受限。现有方法缺乏有效的探索机制，难以平衡利用(exploitation)和探索(exploration)。

**核心思路**：本文的核心思路是引入好奇心驱动的探索(Curiosity-Driven Exploration, CDE)机制，利用模型自身的内在好奇心来引导探索过程。通过奖励模型探索新的、不确定的状态，鼓励模型跳出局部最优，发现更优的策略。这种方法旨在提高探索效率，避免过早收敛。

**技术框架**：CDE框架在标准的RLVR框架基础上，增加了好奇心奖励项。整体流程如下：1) LLM (Actor) 生成响应；2) Critic评估响应的质量并给出奖励；3) Actor根据奖励更新策略；4) 同时，计算Actor的困惑度和Critic的价值估计方差，作为好奇心奖励；5) 将好奇心奖励与外部奖励结合，共同指导Actor的策略更新。

**关键创新**：CDE的关键创新在于利用Actor的困惑度和Critic的价值估计方差来量化好奇心。Actor的困惑度反映了模型对生成响应的不确定性，困惑度越高，说明模型对该响应越好奇。Critic的价值估计方差反映了模型对状态价值的不确定性，方差越高，说明模型对该状态越好奇。将这两种信号结合起来，可以更全面地衡量模型的好奇心，并指导探索。

**关键设计**：Actor的好奇心奖励采用生成响应的困惑度，困惑度越高，奖励越高。Critic的好奇心奖励采用多头Critic网络中价值估计的方差，方差越高，奖励越高。总奖励是外部奖励和好奇心奖励的加权和，权重系数是可调节的超参数。损失函数结合了策略梯度损失和价值函数损失，并加入了正则化项，以防止过拟合。

## 📊 实验亮点

实验结果表明，在AIME基准测试中，CDE使用GRPO/PPO算法相比标准RLVR方法提升了约3个百分点。这表明CDE能够有效提高LLM的探索效率，并学习到更优的策略。此外，论文还分析了RLVR中的校准崩溃机制，为理解LLM的失败模式提供了新的视角。

## 🎯 应用场景

CDE框架可应用于各种需要LLM进行策略学习和决策的任务中，例如对话生成、文本摘要、代码生成、游戏AI等。通过提高探索效率，CDE可以帮助LLM更快地学习到更优的策略，提升任务性能。该研究对于提升LLM的通用性和智能化水平具有重要意义，并有望推动LLM在更多实际场景中的应用。

## 📄 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) is a powerful paradigm for enhancing the reasoning ability of Large Language Models (LLMs). Yet current RLVR methods often explore poorly, leading to premature convergence and entropy collapse. To address this challenge, we introduce Curiosity-Driven Exploration (CDE), a framework that leverages the model's own intrinsic sense of curiosity to guide exploration. We formalize curiosity with signals from both the actor and the critic: for the actor, we use perplexity over its generated response, and for the critic, we use the variance of value estimates from a multi-head architecture. Both signals serve as an exploration bonus within the RLVR framework to guide the model. Our theoretical analysis shows that the actor-wise bonus inherently penalizes overconfident errors and promotes diversity among correct responses; moreover, we connect the critic-wise bonus to the well-established count-based exploration bonus in RL. Empirically, our method achieves an approximate +3 point improvement over standard RLVR using GRPO/PPO on AIME benchmarks. Further analysis identifies a calibration collapse mechanism within RLVR, shedding light on common LLM failure modes.

