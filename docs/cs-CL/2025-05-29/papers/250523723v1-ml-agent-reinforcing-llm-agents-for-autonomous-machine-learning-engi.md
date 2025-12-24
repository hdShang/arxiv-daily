---
layout: default
title: "ML-Agent: Reinforcing LLM Agents for Autonomous Machine Learning Engineering"
---

# ML-Agent: Reinforcing LLM Agents for Autonomous Machine Learning Engineering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23723" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23723v1</a>
  <a href="https://arxiv.org/pdf/2505.23723.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23723v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23723v1', 'ML-Agent: Reinforcing LLM Agents for Autonomous Machine Learning Engineering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zexi Liu, Jingyi Chai, Xinyu Zhu, Shuo Tang, Rui Ye, Bo Zhang, Lei Bai, Siheng Chen

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-29

---

## 💡 一句话要点

**提出ML-Agent以解决自主机器学习工程中的手动提示工程问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自主机器学习` `强化学习` `大型语言模型` `代理学习` `实验优化` `跨任务泛化` `在线学习`

## 📋 核心要点

1. 现有方法过于依赖手动提示工程，难以适应多样的实验需求，限制了自主机器学习的效率和灵活性。
2. 本文提出了一种基于学习的代理ML框架，结合探索丰富的微调、逐步RL和特定奖励模块，提升了代理的学习能力。
3. 实验结果表明，7B参数的ML-Agent在9个任务上训练后，性能超越671B参数的DeepSeek-R1，展现出持续的性能提升和跨任务泛化能力。

## 📝 摘要（中文）

大型语言模型（LLM）驱动的代理的出现显著推动了自主机器学习（ML）工程的发展。然而，大多数现有方法过于依赖手动提示工程，未能根据多样的实验经验进行适应和优化。针对这一问题，本文首次探索了基于学习的代理ML范式，LLM代理通过在线强化学习（RL）在ML任务上进行互动实验学习。为实现这一目标，我们提出了一种新颖的代理ML训练框架，包含三个关键组件：探索丰富的微调、逐步RL和特定于代理ML的奖励模块。利用该框架，我们训练了一个基于7B参数的Qwen-2.5 LLM的ML-Agent，尽管仅在9个ML任务上进行训练，但其表现超越了671B参数的DeepSeek-R1代理，并展现出卓越的跨任务泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自主机器学习方法中对手动提示工程的过度依赖问题，导致适应性和优化能力不足。

**核心思路**：提出基于学习的代理ML范式，通过在线强化学习使LLM代理在ML任务中进行互动实验学习，从而提高其自主学习能力。

**技术框架**：整体架构包括三个主要模块：探索丰富的微调模块用于生成多样化动作，逐步RL模块用于加速经验收集，以及特定于代理ML的奖励模块用于统一反馈信号。

**关键创新**：最重要的创新在于引入了探索丰富的微调和逐步RL的结合，使得代理能够在单步动作上进行高效训练，显著提升了学习效率。

**关键设计**：在奖励模块中，设计了统一的奖励信号以适应不同的ML反馈，优化了RL的训练过程，同时在微调过程中引入了多样化动作生成策略。

## 📊 实验亮点

实验结果显示，尽管ML-Agent仅在9个任务上进行训练，其性能却超越了671B参数的DeepSeek-R1代理，展现出显著的性能提升和跨任务的泛化能力，证明了该方法的有效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括自动化机器学习平台、智能数据分析工具和自主决策系统。通过提升LLM代理的学习能力，能够在多种机器学习任务中实现更高效的自动化处理，降低人工干预的需求，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The emergence of large language model (LLM)-based agents has significantly advanced the development of autonomous machine learning (ML) engineering. However, most existing approaches rely heavily on manual prompt engineering, failing to adapt and optimize based on diverse experimental experiences. Focusing on this, for the first time, we explore the paradigm of learning-based agentic ML, where an LLM agent learns through interactive experimentation on ML tasks using online reinforcement learning (RL). To realize this, we propose a novel agentic ML training framework with three key components: (1) exploration-enriched fine-tuning, which enables LLM agents to generate diverse actions for enhanced RL exploration; (2) step-wise RL, which enables training on a single action step, accelerating experience collection and improving training efficiency; (3) an agentic ML-specific reward module, which unifies varied ML feedback signals into consistent rewards for RL optimization. Leveraging this framework, we train ML-Agent, driven by a 7B-sized Qwen-2.5 LLM for autonomous ML. Remarkably, despite being trained on merely 9 ML tasks, our 7B-sized ML-Agent outperforms the 671B-sized DeepSeek-R1 agent. Furthermore, it achieves continuous performance improvements and demonstrates exceptional cross-task generalization capabilities.

