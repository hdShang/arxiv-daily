---
layout: default
title: "FairMarket-RL: LLM-Guided Fairness Shaping for Multi-Agent Reinforcement Learning in Peer-to-Peer Markets"
---

# FairMarket-RL: LLM-Guided Fairness Shaping for Multi-Agent Reinforcement Learning in Peer-to-Peer Markets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22708" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22708v1</a>
  <a href="https://arxiv.org/pdf/2506.22708.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22708v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22708v1', 'FairMarket-RL: LLM-Guided Fairness Shaping for Multi-Agent Reinforcement Learning in Peer-to-Peer Markets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shrenik Jadhav, Birva Sevak, Srijita Das, Akhtar Hussain, Wencong Su, Van-Hai Bui

**分类**: cs.LG, econ.GN, eess.SY

**发布日期**: 2025-06-28

---

## 💡 一句话要点

**提出FairMarket-RL以解决P2P市场中的公平性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `点对点交易` `公平性评估` `强化学习` `大型语言模型` `自主交易` `去中心化市场` `能源系统` `奖励塑形`

## 📋 核心要点

1. 现有的P2P市场交易方法缺乏有效的公平性保障机制，导致交易结果不均衡。
2. FairMarket-RL结合了大型语言模型和强化学习，通过实时评估交易公平性来优化代理的决策过程。
3. 实验结果显示，FairMarket-RL能够满足90%以上的买方需求，并保持高于0.80的公平性评分，显著改善了交易公平性。

## 📝 摘要（中文）

随着点对点（P2P）交易被越来越多地认可为去中心化市场调节的关键机制，现有方法往往缺乏确保公平性的稳健框架。本文提出了FairMarket-RL，这是一种新颖的混合框架，将大型语言模型（LLM）与强化学习（RL）相结合，以实现公平意识的交易代理。在一个模拟的P2P微电网中，LLM作为实时公平性评估者，使用买方公平性（FTB）和卖方公平性（FBS）两个指标评估每个交易回合。这些公平性评分通过调度的λ系数整合到代理奖励中，形成一个自适应的LLM引导奖励塑形循环，取代了脆弱的基于规则的公平性约束。代理使用独立近端策略优化（IPPO）进行训练，实现了公平的结果，满足了90%以上的买方需求，保持了公平的卖方利润，并始终达到0.80以上的FTB和FBS评分。训练过程表明，公平性反馈改善了收敛性，减少了买方短缺，并缩小了卖方之间的利润差距。FairMarket-RL因此为去中心化能源系统中的自主交易提供了可扩展的、以公平为驱动的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决现有P2P市场交易中公平性不足的问题，现有方法往往依赖于脆弱的规则，无法有效评估和保障交易的公平性。

**核心思路**：FairMarket-RL的核心思路是利用大型语言模型作为实时公平性评估者，通过公平性评分引导代理的奖励机制，从而实现公平意识的交易决策。

**技术框架**：该框架包括多个主要模块：首先，LLM实时评估交易的公平性；其次，通过调度的λ系数将公平性评分整合到代理的奖励中；最后，代理使用独立近端策略优化（IPPO）进行训练。

**关键创新**：最重要的技术创新在于将LLM引入到强化学习中，作为公平性评估的核心组件，替代了传统的基于规则的公平性约束，形成了自适应的奖励塑形机制。

**关键设计**：在设计中，使用了调度的λ系数来动态调整公平性评分对代理奖励的影响，同时确保了训练过程中的公平性反馈能够有效改善代理的收敛性和交易结果。

## 📊 实验亮点

实验结果表明，FairMarket-RL在满足90%以上买方需求的同时，保持了卖方的公平利润，FTB和FBS评分均超过0.80，显示出显著的公平性提升。与传统方法相比，该框架在减少买方短缺和缩小卖方利润差距方面表现出色。

## 🎯 应用场景

FairMarket-RL的研究成果在去中心化能源市场中具有广泛的应用潜力，能够为自主交易提供公平性保障，促进资源的合理分配。未来，该框架还可扩展至更大规模的电力分配系统，提升整体市场效率和公平性。

## 📄 摘要（原文）

> Peer-to-peer (P2P) trading is increasingly recognized as a key mechanism for decentralized market regulation, yet existing approaches often lack robust frameworks to ensure fairness. This paper presents FairMarket-RL, a novel hybrid framework that combines Large Language Models (LLMs) with Reinforcement Learning (RL) to enable fairness-aware trading agents. In a simulated P2P microgrid with multiple sellers and buyers, the LLM acts as a real-time fairness critic, evaluating each trading episode using two metrics: Fairness-To-Buyer (FTB) and Fairness-Between-Sellers (FBS). These fairness scores are integrated into agent rewards through scheduled λ-coefficients, forming an adaptive LLM-guided reward shaping loop that replaces brittle, rule-based fairness constraints. Agents are trained using Independent Proximal Policy Optimization (IPPO) and achieve equitable outcomes, fulfilling over 90% of buyer demand, maintaining fair seller margins, and consistently reaching FTB and FBS scores above 0.80. The training process demonstrates that fairness feedback improves convergence, reduces buyer shortfalls, and narrows profit disparities between sellers. With its language-based critic, the framework scales naturally, and its extension to a large power distribution system with household prosumers illustrates its practical applicability. FairMarket-RL thus offers a scalable, equity-driven solution for autonomous trading in decentralized energy systems.

