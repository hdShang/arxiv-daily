---
layout: default
title: Strategy-Augmented Planning for Large Language Models via Opponent Exploitation
---

# Strategy-Augmented Planning for Large Language Models via Opponent Exploitation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08459" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08459v2</a>
  <a href="https://arxiv.org/pdf/2505.08459.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08459v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08459v2', 'Strategy-Augmented Planning for Large Language Models via Opponent Exploitation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuai Xu, Sijia Cui, Yanna Wang, Bo Xu, Qi Wang

**分类**: cs.AI

**发布日期**: 2025-05-13 (更新: 2025-06-01)

**备注**: Accepted to IJCNN 2025

**🔗 代码/项目**: [GITHUB](https://github.com/hsushuai/SAP)

---

## 💡 一句话要点

**提出策略增强规划以解决对手建模问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对手建模` `大型语言模型` `策略增强` `强化学习` `微型实时策略游戏` `策略评估网络` `决策生成`

## 📋 核心要点

1. 现有方法在对手建模方面存在不足，尤其是在缺乏领域专业知识时，LLMs的决策能力受到限制。
2. 本文提出的策略增强规划（SAP）框架通过策略评估网络（SEN）来增强对手利用能力，分为离线和在线两个阶段。
3. 在微型实时策略游戏环境中，SAP相较于基线方法实现了85.35%的性能提升，展现出强大的泛化能力。

## 📝 摘要（中文）

有效建模和利用对手一直是对抗性领域中的长期挑战。近年来，基于大规模文本数据训练的大型语言模型（LLMs）在一般任务中表现出色，为对手建模开辟了新的研究方向。现有研究主要集中在直接使用LLMs根据包含对手描述的详细提示上下文生成决策，但这些方法在LLMs缺乏足够领域专业知识的情况下受到限制。为此，本文提出了一种两阶段的策略增强规划（SAP）框架，通过引入策略评估网络（SEN）显著增强了基于LLM的代理的对手利用能力。实验结果表明，SAP在微型实时策略游戏环境中相较于基线方法实现了85.35%的性能提升，并与最先进的基于规则的AI的强化学习方法相匹配。

## 🔬 方法详解

**问题定义**：本文旨在解决对手建模和利用中的效率问题，现有方法在对手策略不明确或缺乏领域知识时表现不佳。

**核心思路**：提出的策略增强规划（SAP）框架通过构建策略空间和训练策略评估网络（SEN），在离线阶段收集策略-结果对数据，在线阶段动态识别并利用对手策略。

**技术框架**：SAP框架分为两个主要阶段：离线阶段构建策略空间并训练SEN，在线阶段通过SEN识别对手策略并生成最佳响应策略，最终通过精心设计的提示将策略转化为行动。

**关键创新**：最重要的创新在于引入了策略评估网络（SEN），使得LLM能够在缺乏领域知识的情况下有效识别和利用对手策略，显著提升了对手利用能力。

**关键设计**：在离线阶段，构建明确的策略空间并收集数据用于训练SEN；在线阶段则通过贪婪搜索策略来识别对手策略，确保生成的响应策略具有高效性和适应性。

## 📊 实验亮点

实验结果显示，SAP在微型实时策略游戏环境中实现了85.35%的性能提升，展现出对新颖未见策略的强大泛化能力，且与最先进的强化学习方法竞争力相当。

## 🎯 应用场景

该研究的潜在应用领域包括游戏AI、对抗性机器人以及其他需要对手建模的智能系统。通过提升对手利用能力，SAP框架能够在复杂环境中实现更高效的决策，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Efficiently modeling and exploiting opponents is a long-standing challenge in adversarial domains. Large Language Models (LLMs) trained on extensive textual data have recently demonstrated outstanding performance in general tasks, introducing new research directions for opponent modeling. Some studies primarily focus on directly using LLMs to generate decisions based on the elaborate prompt context that incorporates opponent descriptions, while these approaches are limited to scenarios where LLMs possess adequate domain expertise. To address that, we introduce a two-stage Strategy-Augmented Planning (SAP) framework that significantly enhances the opponent exploitation capabilities of LLM-based agents by utilizing a critical component, the Strategy Evaluation Network (SEN). Specifically, in the offline stage, we construct an explicit strategy space and subsequently collect strategy-outcome pair data for training the SEN network. During the online phase, SAP dynamically recognizes the opponent's strategies and greedily exploits them by searching best response strategy on the well-trained SEN, finally translating strategy to a course of actions by carefully designed prompts. Experimental results show that SAP exhibits robust generalization capabilities, allowing it to perform effectively not only against previously encountered opponent strategies but also against novel, unseen strategies. In the MicroRTS environment, SAP achieves a $85.35\%$ performance improvement over baseline methods and matches the competitiveness of reinforcement learning approaches against state-of-the-art (SOTA) rule-based AI. Our code is available at https://github.com/hsushuai/SAP.

