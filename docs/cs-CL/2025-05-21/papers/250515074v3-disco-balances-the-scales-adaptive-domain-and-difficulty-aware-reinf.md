---
layout: default
title: DISCO Balances the Scales: Adaptive Domain- and Difficulty-Aware Reinforcement Learning on Imbalanced Data
---

# DISCO Balances the Scales: Adaptive Domain- and Difficulty-Aware Reinforcement Learning on Imbalanced Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.15074" class="toolbar-btn" target="_blank">📄 arXiv: 2505.15074v3</a>
  <a href="https://arxiv.org/pdf/2505.15074.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.15074v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.15074v3', 'DISCO Balances the Scales: Adaptive Domain- and Difficulty-Aware Reinforcement Learning on Imbalanced Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhang Zhou, Jing Zhu, Shengyi Qian, Zhuokai Zhao, Xiyao Wang, Xiaoyu Liu, Ming Li, Paiheng Xu, Wei Ai, Furong Huang

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-21 (更新: 2025-09-24)

**备注**: Accepted by EMNLP 2025 Findings

**🔗 代码/项目**: [GITHUB](https://github.com/Tonyzhou98/disco_grpo)

---

## 💡 一句话要点

**提出DISCO以解决不平衡数据下的强化学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `不平衡数据` `多域学习` `奖励机制` `语言模型` `公平性` `泛化能力`

## 📋 核心要点

1. 现有的GRPO方法在处理多域不平衡数据时，容易优化主导域，忽视弱势域，导致泛化能力和公平性不足。
2. DISCO通过域感知奖励缩放和难度感知奖励缩放，针对不同域的频率和不确定性进行优化，提升学习效果。
3. DISCO在多个LLM上进行广泛实验，较现有GRPO变体提升5%，并在多域对齐基准上取得了新的最优结果。

## 📝 摘要（中文）

大型语言模型（LLMs）通过人类反馈强化学习（RLHF）逐渐与人类偏好对齐。现有的群体相对策略优化（GRPO）方法在处理多域不平衡数据时，容易优化主导域而忽视弱势域，导致泛化能力和公平性不足。为此，本文提出了域信息自一致性策略优化（DISCO），通过域感知奖励缩放和难度感知奖励缩放两大创新，平衡不同域间的优化，促进更公平有效的策略学习。实验结果表明，DISCO在多个LLM和偏斜训练分布上均表现优异，较现有GRPO变体提升5%，并在多域对齐基准上创下新纪录。

## 🔬 方法详解

**问题定义**：本文旨在解决GRPO在多域不平衡数据下的优化偏差问题。现有方法假设域分布均衡，导致在实际应用中无法有效处理弱势域。

**核心思路**：DISCO通过引入域感知和难度感知的奖励缩放机制，旨在平衡不同域的优化过程，确保弱势域也能得到足够的关注和学习。

**技术框架**：DISCO的整体架构包括两个主要模块：域感知奖励缩放和难度感知奖励缩放。前者根据域的出现频率调整优化权重，后者则通过自一致性评估识别和优先处理不确定的提示。

**关键创新**：DISCO的主要创新在于其奖励缩放机制，能够有效应对数据不平衡问题，与传统GRPO方法相比，显著提升了对弱势域的学习能力。

**关键设计**：在参数设置上，DISCO采用动态调整的奖励权重，损失函数设计上结合了域频率和提示不确定性，确保模型在训练过程中能够自适应地优化不同域的策略。

## 📊 实验亮点

DISCO在多个大型语言模型上进行了广泛的实验，结果显示其在处理偏斜训练分布时，较现有GRPO变体提升了5%的性能，并在多域对齐基准上创下了新的最优结果，展示了其在实际应用中的有效性和优势。

## 🎯 应用场景

DISCO的研究成果在多领域的语言模型训练中具有广泛的应用潜力，特别是在需要处理不平衡数据的场景，如社交媒体分析、在线推荐系统和多语言翻译等。其公平性和泛化能力的提升将对实际应用产生积极影响，推动相关领域的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly aligned with human preferences through Reinforcement Learning from Human Feedback (RLHF). Among RLHF methods, Group Relative Policy Optimization (GRPO) has gained attention for its simplicity and strong performance, notably eliminating the need for a learned value function. However, GRPO implicitly assumes a balanced domain distribution and uniform semantic alignment across groups, assumptions that rarely hold in real-world datasets. When applied to multi-domain, imbalanced data, GRPO disproportionately optimizes for dominant domains, neglecting underrepresented ones and resulting in poor generalization and fairness. We propose Domain-Informed Self-Consistency Policy Optimization (DISCO), a principled extension to GRPO that addresses inter-group imbalance with two key innovations. Domain-aware reward scaling counteracts frequency bias by reweighting optimization based on domain prevalence. Difficulty-aware reward scaling leverages prompt-level self-consistency to identify and prioritize uncertain prompts that offer greater learning value. Together, these strategies promote more equitable and effective policy learning across domains. Extensive experiments across multiple LLMs and skewed training distributions show that DISCO improves generalization, outperforms existing GRPO variants by 5% on Qwen3 models, and sets new state-of-the-art results on multi-domain alignment benchmarks. Our code and data are available at https://github.com/Tonyzhou98/disco_grpo.

