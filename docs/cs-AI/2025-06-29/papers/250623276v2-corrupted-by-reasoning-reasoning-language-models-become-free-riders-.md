---
layout: default
title: "Corrupted by Reasoning: Reasoning Language Models Become Free-Riders in Public Goods Games"
---

# Corrupted by Reasoning: Reasoning Language Models Become Free-Riders in Public Goods Games

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23276" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23276v2</a>
  <a href="https://arxiv.org/pdf/2506.23276.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23276v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23276v2', 'Corrupted by Reasoning: Reasoning Language Models Become Free-Riders in Public Goods Games')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: David Guzman Piedrahita, Yongjin Yang, Mrinmaya Sachan, Giorgia Ramponi, Bernhard Schölkopf, Zhijing Jin

**分类**: cs.AI, cs.CL

**发布日期**: 2025-06-29 (更新: 2025-07-24)

**备注**: Published at COLM 2025

**🔗 代码/项目**: [GITHUB](https://github.com/davidguzmanp/SanctSim)

---

## 💡 一句话要点

**探讨语言模型在公共物品博弈中的合作机制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `公共物品博弈` `多智能体系统` `合作机制` `推理能力` `社会困境` `行为经济学`

## 📋 核心要点

1. 当前LLM在合作与自我利益之间的平衡面临重大挑战，影响其对齐性和安全部署。
2. 本文通过适应公共物品博弈，研究LLM在多智能体系统中的合作决策机制。
3. 实验结果显示，推理能力强的LLM在合作上表现不佳，而传统LLM则能维持高水平的合作。

## 📝 摘要（中文）

随着大型语言模型（LLMs）作为自主代理的广泛应用，理解它们的合作与社会机制变得愈发重要。本文研究了多智能体LLM系统中，代理在激励合作或惩罚背叛时的资源投资决策。通过适应行为经济学中的公共物品博弈，观察不同LLM在重复互动中的社会困境表现，发现四种不同的行为模式。令人惊讶的是，推理能力强的LLM在合作上表现不佳，而一些传统LLM则能持续实现高水平的合作。这一发现为在需要持续协作的环境中部署LLM代理提供了重要的见解。

## 🔬 方法详解

**问题定义**：本文旨在解决多智能体LLM系统中，代理在激励合作与惩罚背叛时的资源投资决策问题。现有方法未能有效促进LLM之间的合作，导致合作水平不稳定。

**核心思路**：通过适应行为经济学中的公共物品博弈，观察不同LLM在重复互动中的行为模式，分析其在社会困境中的表现。这样的设计使得研究者能够深入理解LLM的合作机制。

**技术框架**：整体架构包括公共物品博弈的设置、LLM的行为观察与记录、以及对不同模型的比较分析。主要模块包括代理决策模块、合作行为评估模块和结果分析模块。

**关键创新**：最重要的技术创新在于将公共物品博弈引入LLM的合作研究，揭示了推理能力与合作能力之间的反向关系，这与现有方法的假设形成鲜明对比。

**关键设计**：在实验中，设置了不同的资源投资参数和惩罚机制，使用了多种LLM模型进行对比，确保了实验结果的可靠性与有效性。

## 📊 实验亮点

实验结果显示，推理能力强的LLM在合作方面的表现显著低于一些传统LLM，后者能够持续维持高水平的合作。这一发现挑战了当前对LLM推理能力提升的普遍看法，强调了合作机制的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括多智能体系统、自动化协作平台和社会网络分析等。通过理解LLM在合作中的表现，可以为设计更高效的智能体系统提供理论支持，促进其在实际应用中的安全与有效性。

## 📄 摘要（原文）

> As large language models (LLMs) are increasingly deployed as autonomous agents, understanding their cooperation and social mechanisms is becoming increasingly important. In particular, how LLMs balance self-interest and collective well-being is a critical challenge for ensuring alignment, robustness, and safe deployment. In this paper, we examine the challenge of costly sanctioning in multi-agent LLM systems, where an agent must decide whether to invest its own resources to incentivize cooperation or penalize defection. To study this, we adapt a public goods game with institutional choice from behavioral economics, allowing us to observe how different LLMs navigate social dilemmas over repeated interactions. Our analysis reveals four distinct behavioral patterns among models: some consistently establish and sustain high levels of cooperation, others fluctuate between engagement and disengagement, some gradually decline in cooperative behavior over time, and others rigidly follow fixed strategies regardless of outcomes. Surprisingly, we find that reasoning LLMs, such as the o1 series, struggle significantly with cooperation, whereas some traditional LLMs consistently achieve high levels of cooperation. These findings suggest that the current approach to improving LLMs, which focuses on enhancing their reasoning capabilities, does not necessarily lead to cooperation, providing valuable insights for deploying LLM agents in environments that require sustained collaboration. Our code is available at https://github.com/davidguzmanp/SanctSim

