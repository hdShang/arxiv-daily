---
layout: default
title: "TGDPO: Harnessing Token-Level Reward Guidance for Enhancing Direct Preference Optimization"
---

# TGDPO: Harnessing Token-Level Reward Guidance for Enhancing Direct Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14574" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14574v1</a>
  <a href="https://arxiv.org/pdf/2506.14574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14574v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14574v1', 'TGDPO: Harnessing Token-Level Reward Guidance for Enhancing Direct Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingkang Zhu, Xi Chen, Zhongdao Wang, Bei Yu, Hengshuang Zhao, Jiaya Jia

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-17

**备注**: ICML 2025

**🔗 代码/项目**: [GITHUB](https://github.com/dvlab-research/TGDPO)

---

## 💡 一句话要点

**提出TGDPO以解决直接偏好优化中的奖励指导问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `直接偏好优化` `token级奖励` `近端策略优化` `强化学习` `人类反馈`

## 📋 核心要点

1. 现有的直接偏好优化方法在利用token级奖励指导时面临挑战，难以有效对齐模型输出。
2. 本文通过将序列级PPO分解为token级问题，提出了一种新的token级奖励指导框架，解决了DPO中的奖励利用问题。
3. 实验结果显示，所提方法在MT-Bench、AlpacaEval 2和Arena-Hard上分别提升了7.5、6.2和4.3点的胜率，显著优于传统DPO。

## 📝 摘要（中文）

近年来，基于人类反馈的强化学习进展表明，利用细粒度的token级奖励模型可以显著提升近端策略优化（PPO）在对齐大型语言模型中的表现。然而，将token级奖励作为直接偏好优化（DPO）的指导存在挑战，因为DPO被表述为序列级的赌博问题。为了解决这一挑战，本文将序列级PPO分解为一系列token级的近端策略优化问题，并构建了token级PPO的框架，推导出闭式的最优token级策略及其对应的token级奖励。通过所获得的奖励和Bradley-Terry模型，本文建立了可计算的损失函数框架，并提出了一种基于诱导DPO奖励的实用奖励指导。实验结果表明，该方法在DPO上实现了显著的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决直接偏好优化（DPO）中如何有效利用token级奖励的问题。现有方法难以将token级奖励有效转化为DPO的指导，导致模型对人类偏好的对齐效果不佳。

**核心思路**：论文的核心思路是将序列级PPO分解为一系列token级的优化问题，利用token级奖励指导来优化每个token的策略。这种设计使得模型能够根据不同token的奖励进行灵活调整，从而更好地对齐人类偏好。

**技术框架**：整体架构包括两个主要模块：首先是token级PPO的框架，其次是基于Bradley-Terry模型的奖励计算模块。通过这两个模块，论文实现了token级奖励的有效利用和策略优化。

**关键创新**：最重要的技术创新在于提出了一种新的token级奖励指导框架，使得DPO能够在token级别上进行优化。这与现有方法的本质区别在于，传统方法通常在序列级别进行优化，未能充分利用token级信息。

**关键设计**：关键设计包括损失函数的构建和token级奖励的计算方式，确保了模型在优化过程中能够灵活调整策略。此外，论文还设计了具体的参数设置，以适应不同任务的需求。

## 📊 实验亮点

实验结果表明，TGDPO在多个基准测试上均显著优于传统DPO方法，具体表现为在MT-Bench上提升7.5点、在AlpacaEval 2上提升6.2点、在Arena-Hard上提升4.3点的胜率，展示了其强大的性能优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和推荐系统等。通过提升模型对人类偏好的对齐能力，TGDPO可以在实际应用中提高用户体验和满意度，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advancements in reinforcement learning from human feedback have shown that utilizing fine-grained token-level reward models can substantially enhance the performance of Proximal Policy Optimization (PPO) in aligning large language models. However, it is challenging to leverage such token-level reward as guidance for Direct Preference Optimization (DPO), since DPO is formulated as a sequence-level bandit problem. To address this challenge, this work decomposes the sequence-level PPO into a sequence of token-level proximal policy optimization problems and then frames the problem of token-level PPO with token-level reward guidance, from which closed-form optimal token-level policy and the corresponding token-level reward can be derived. Using the obtained reward and Bradley-Terry model, this work establishes a framework of computable loss functions with token-level reward guidance for DPO, and proposes a practical reward guidance based on the induced DPO reward. This formulation enables different tokens to exhibit varying degrees of deviation from reference policy based on their respective rewards. Experiment results demonstrate that our method achieves substantial performance improvements over DPO, with win rate gains of up to 7.5 points on MT-Bench, 6.2 points on AlpacaEval 2, and 4.3 points on Arena-Hard. Code is available at https://github.com/dvlab-research/TGDPO.

