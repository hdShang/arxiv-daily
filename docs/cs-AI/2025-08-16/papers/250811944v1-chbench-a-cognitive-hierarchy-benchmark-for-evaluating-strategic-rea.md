---
layout: default
title: "CHBench: A Cognitive Hierarchy Benchmark for Evaluating Strategic Reasoning Capability of LLMs"
---

# CHBench: A Cognitive Hierarchy Benchmark for Evaluating Strategic Reasoning Capability of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11944" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11944v1</a>
  <a href="https://arxiv.org/pdf/2508.11944.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11944v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11944v1', 'CHBench: A Cognitive Hierarchy Benchmark for Evaluating Strategic Reasoning Capability of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongtao Liu, Zhicheng Du, Zihe Wang, Weiran Shen

**分类**: cs.AI, cs.CL, cs.HC

**发布日期**: 2025-08-16

---

## 💡 一句话要点

**提出CHBench以解决LLMs战略推理能力评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `战略推理` `大型语言模型` `认知层次` `评估框架` `行为经济学` `记忆机制` `聊天机制` `游戏理论`

## 📋 核心要点

1. 现有方法主要依赖效用性能指标，缺乏对对手行为和游戏结构变化的鲁棒性，导致评估结果不稳定。
2. 本文提出CHBench评估框架，基于认知层次模型，假设代理在推理深度上存在差异，从而更全面地评估LLMs的战略推理能力。
3. 实验结果显示，LLMs在不同对手中表现出一致的战略推理水平，并且记忆机制提升了推理能力，而聊天机制则有负面影响。

## 📝 摘要（中文）

游戏能力作为评估大型语言模型（LLMs）战略推理能力的指标，现有研究多依赖于效用性能指标，但由于对手行为和游戏结构的变化，这些指标的鲁棒性不足。为了解决这一问题，本文提出了认知层次基准（CHBench），这是一个新的评估框架，灵感来源于行为经济学中的认知层次模型。我们假设代理具有有限理性，不同代理在推理深度/层次上表现不同。通过对六种最先进的LLMs在十五个精心选择的标准形式游戏中的行为数据进行评估，实验结果表明，LLMs在不同对手中展现出一致的战略推理水平，验证了该框架的鲁棒性和泛化能力。我们还分析了两种关键机制（聊天机制和记忆机制）对战略推理性能的影响，结果表明聊天机制显著降低了战略推理能力，而记忆机制则增强了这一能力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有评估LLMs战略推理能力方法的鲁棒性不足问题，尤其是在对手行为和游戏结构变化时的评估不稳定性。

**核心思路**：提出CHBench评估框架，基于认知层次模型，假设不同代理在推理深度上存在差异，从而更准确地评估LLMs的战略推理能力。

**技术框架**：CHBench框架分为三个阶段：首先收集行为数据，其次进行推理深度评估，最后分析不同机制对推理性能的影响。

**关键创新**：CHBench的创新之处在于引入认知层次模型，允许对不同推理深度的代理进行评估，克服了传统方法的局限性。

**关键设计**：在实验中，设置了聊天机制和记忆机制的影响，发现聊天机制会降低推理能力，而记忆机制则显著提升了推理表现。具体的参数设置和损失函数设计在实验中进行了详细说明。

## 📊 实验亮点

实验结果表明，LLMs在不同对手中展现出一致的战略推理水平，验证了CHBench的鲁棒性和泛化能力。具体而言，记忆机制的引入使得推理能力提升了显著的幅度，而聊天机制则导致了性能的显著下降，显示出两者对战略推理的不同影响。

## 🎯 应用场景

CHBench的提出为评估大型语言模型的战略推理能力提供了一个新的工具，具有广泛的应用潜力。该框架不仅可以用于学术研究，还可以在游戏AI、决策支持系统等实际应用中发挥重要作用，推动相关领域的发展。

## 📄 摘要（原文）

> Game-playing ability serves as an indicator for evaluating the strategic reasoning capability of large language models (LLMs). While most existing studies rely on utility performance metrics, which are not robust enough due to variations in opponent behavior and game structure. To address this limitation, we propose \textbf{Cognitive Hierarchy Benchmark (CHBench)}, a novel evaluation framework inspired by the cognitive hierarchy models from behavioral economics. We hypothesize that agents have bounded rationality -- different agents behave at varying reasoning depths/levels. We evaluate LLMs' strategic reasoning through a three-phase systematic framework, utilizing behavioral data from six state-of-the-art LLMs across fifteen carefully selected normal-form games. Experiments show that LLMs exhibit consistent strategic reasoning levels across diverse opponents, confirming the framework's robustness and generalization capability. We also analyze the effects of two key mechanisms (Chat Mechanism and Memory Mechanism) on strategic reasoning performance. Results indicate that the Chat Mechanism significantly degrades strategic reasoning, whereas the Memory Mechanism enhances it. These insights position CHBench as a promising tool for evaluating LLM capabilities, with significant potential for future research and practical applications.

