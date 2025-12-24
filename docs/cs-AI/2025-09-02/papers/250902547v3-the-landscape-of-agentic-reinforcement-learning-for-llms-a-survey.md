---
layout: default
title: "The Landscape of Agentic Reinforcement Learning for LLMs: A Survey"
---

# The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02547" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02547v3</a>
  <a href="https://arxiv.org/pdf/2509.02547.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02547v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02547v3', 'The Landscape of Agentic Reinforcement Learning for LLMs: A Survey')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guibin Zhang, Hejia Geng, Xiaohang Yu, Zhenfei Yin, Zaibin Zhang, Zelin Tan, Heng Zhou, Zhongzhi Li, Xiangyuan Xue, Yijiang Li, Yifan Zhou, Yang Chen, Chen Zhang, Yutao Fan, Zihu Wang, Songtao Huang, Francisco Piedrahita-Velez, Yue Liao, Hongru Wang, Mengyue Yang, Heng Ji, Jun Wang, Shuicheng Yan, Philip Torr, Lei Bai

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-02 (更新: 2025-11-08)

---

## 💡 一句话要点

**提出Agentic RL框架，将LLM从序列生成器转变为自主决策智能体，并全面综述其能力、应用与未来方向。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agentic强化学习` `大型语言模型` `自主智能体` `强化学习` `决策智能`

## 📋 核心要点

1. 传统LLM-RL将LLM视为被动序列生成器，缺乏在复杂动态环境中自主决策的能力。
2. Agentic RL将LLM重塑为自主智能体，通过强化学习赋予其规划、工具使用、记忆等核心能力。
3. 论文全面综述Agentic RL，整理开源环境、基准和框架，为未来研究提供指导。

## 📝 摘要（中文）

Agentic强化学习（Agentic RL）的出现标志着从应用于大型语言模型（LLM RL）的传统强化学习的范式转变，它将LLM从被动的序列生成器重新定义为嵌入在复杂、动态世界中的自主决策智能体。本综述通过对比LLM-RL的退化单步马尔可夫决策过程（MDP）与定义Agentic RL的时序扩展、部分可观察马尔可夫决策过程（POMDP），正式确定了这种概念转变。在此基础上，我们提出了一个全面的双重分类法：一个围绕核心智能体能力组织，包括规划、工具使用、记忆、推理、自我提升和感知，另一个围绕它们在不同任务领域的应用。我们的核心论点是，强化学习是使这些能力从静态的、启发式模块转变为自适应、鲁棒的智能体行为的关键机制。为了支持和加速未来的研究，我们将开源环境、基准和框架整合到一个实用的概要中。通过综合五百多篇最新著作，本综述描绘了这个快速发展领域的轮廓，并强调了将塑造可扩展的通用人工智能智能体发展的机遇和挑战。

## 🔬 方法详解

**问题定义**：现有的大型语言模型强化学习（LLM-RL）方法通常将LLM视为被动的序列生成器，采用单步马尔可夫决策过程（MDP）进行建模。这种方法无法充分利用LLM在复杂、动态环境中进行长期规划和决策的能力。因此，需要一种新的框架，能够将LLM转变为自主的、具有智能体行为的决策者。

**核心思路**：论文的核心思路是将LLM视为智能体，并采用Agentic强化学习（Agentic RL）框架对其进行训练。Agentic RL使用时序扩展、部分可观察马尔可夫决策过程（POMDP）来建模LLM与环境的交互，从而使LLM能够进行长期规划、工具使用、记忆、推理、自我提升和感知等操作。强化学习作为关键机制，将这些能力从静态模块转变为自适应、鲁棒的智能体行为。

**技术框架**：Agentic RL框架主要包含以下几个模块：1) 环境：定义智能体所处的外部世界，提供状态信息和奖励信号。2) 智能体：由LLM驱动，负责观察环境、制定行动策略并执行行动。3) 强化学习算法：用于训练智能体，使其能够根据环境反馈优化行动策略。4) 核心能力模块：包括规划、工具使用、记忆、推理、自我提升和感知等，这些模块可以增强智能体的决策能力。

**关键创新**：该论文的关键创新在于提出了Agentic RL的概念，并将其应用于LLM。与传统的LLM-RL方法相比，Agentic RL能够更好地利用LLM的潜力，使其能够像真正的智能体一样在复杂环境中进行自主决策。此外，该论文还对Agentic RL的核心能力进行了分类，并探讨了如何使用强化学习来提升这些能力。

**关键设计**：论文中没有具体涉及关键参数设置、损失函数或网络结构等技术细节，而是侧重于对Agentic RL框架的整体概念和架构进行阐述。未来的研究可以针对不同的核心能力模块，设计特定的强化学习算法和网络结构，以进一步提升Agentic RL的性能。

## 📊 实验亮点

该论文是一篇综述性文章，主要贡献在于对Agentic RL领域进行了全面的梳理和总结，并提出了一个双重分类法，对Agentic RL的核心能力和应用进行了分类。论文还整理了开源环境、基准和框架，为未来的研究提供了有价值的资源。由于是综述，没有具体的实验结果和性能数据。

## 🎯 应用场景

Agentic RL在多个领域具有广泛的应用前景，包括机器人控制、游戏AI、对话系统、自动化任务执行等。通过赋予LLM自主决策能力，可以使其在复杂环境中完成更具挑战性的任务，例如自动驾驶、智能家居控制、客户服务等。Agentic RL有望推动通用人工智能的发展，并为人类带来更智能、更便捷的生活。

## 📄 摘要（原文）

> The emergence of agentic reinforcement learning (Agentic RL) marks a paradigm shift from conventional reinforcement learning applied to large language models (LLM RL), reframing LLMs from passive sequence generators into autonomous, decision-making agents embedded in complex, dynamic worlds. This survey formalizes this conceptual shift by contrasting the degenerate single-step Markov Decision Processes (MDPs) of LLM-RL with the temporally extended, partially observable Markov decision processes (POMDPs) that define Agentic RL. Building on this foundation, we propose a comprehensive twofold taxonomy: one organized around core agentic capabilities, including planning, tool use, memory, reasoning, self-improvement, and perception, and the other around their applications across diverse task domains. Central to our thesis is that reinforcement learning serves as the critical mechanism for transforming these capabilities from static, heuristic modules into adaptive, robust agentic behavior. To support and accelerate future research, we consolidate the landscape of open-source environments, benchmarks, and frameworks into a practical compendium. By synthesizing over five hundred recent works, this survey charts the contours of this rapidly evolving field and highlights the opportunities and challenges that will shape the development of scalable, general-purpose AI agents.

