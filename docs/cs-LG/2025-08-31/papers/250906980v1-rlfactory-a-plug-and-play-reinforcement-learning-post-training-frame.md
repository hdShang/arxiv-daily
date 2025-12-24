---
layout: default
title: "RLFactory: A Plug-and-Play Reinforcement Learning Post-Training Framework for LLM Multi-Turn Tool-Use"
---

# RLFactory: A Plug-and-Play Reinforcement Learning Post-Training Framework for LLM Multi-Turn Tool-Use

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06980" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06980v1</a>
  <a href="https://arxiv.org/pdf/2509.06980.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06980v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06980v1', 'RLFactory: A Plug-and-Play Reinforcement Learning Post-Training Framework for LLM Multi-Turn Tool-Use')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiajun Chai, Guojun Yin, Zekun Xu, Chuhuai Yue, Yi Jia, Siyu Xia, Xiaohan Wang, Jiwen Jiang, Xiaoguang Li, Chengqi Dong, Hang He, Wei Lin

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-31

**🔗 代码/项目**: [GITHUB](https://github.com/Simple-Efficient/RL-Factory)

---

## 💡 一句话要点

**提出RLFactory以解决大型语言模型多轮工具使用问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `工具调用` `多轮交互` `异步架构` `动态策略优化` `自然语言处理`

## 📋 核心要点

1. 现有大型语言模型在与外部工具交互时存在稳定性和适应性不足的问题，限制了其在复杂任务中的应用。
2. RLFactory通过异步调用器和解耦架构解决工具调用的稳定性，同时引入奖励层以满足多样化评估需求。
3. 在实验中，RLFactory在自然问题数据集上取得了0.486的测试分数，显著超越了其他模型，并提高了训练效率。

## 📝 摘要（中文）

大型语言模型在基本推理方面表现出色，但在需要与外部工具交互的任务中却面临挑战。本文提出了RLFactory，一个即插即用的强化学习后训练框架，旨在解决多轮工具使用中的工具调用稳定性和适应性问题。RLFactory通过异步调用器和解耦的工具/训练架构来应对工具异质性和接口问题，并通过支持基于规则、模型判断和工具验证信号的奖励层来满足多样化的评估需求。该框架通过引入工具反馈的观察标记重构马尔可夫决策过程（MDP），实现模型、工具和环境之间的闭环，并实施生成-解析-调用-更新的动态策略优化工作流。在Search-R1上，RLFactory在自然问题（NQ）数据集上取得了0.486的测试分数，超越了使用类似技术训练的更大模型（如Qwen2.5-7B-Instruct-GRPO的0.473），并提高了训练吞吐量6.8倍。RLFactory为增强大型语言模型在现实场景中的多轮工具使用提供了低门槛、高适应性的框架。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多轮工具使用中面临的工具调用稳定性和适应性不足的问题。现有方法在工具异质性和接口问题上表现不佳，导致模型在实际应用中的效果受限。

**核心思路**：RLFactory的核心思路是通过异步调用器和解耦的工具/训练架构来提升工具调用的稳定性，并通过奖励层来满足多样化的评估需求。这样的设计使得模型能够更灵活地适应不同工具的使用场景。

**技术框架**：RLFactory的整体架构包括异步调用器、解耦的工具和训练模块，以及一个支持多种奖励信号的奖励层。该框架通过引入工具反馈的观察标记重构马尔可夫决策过程（MDP），并实施生成-解析-调用-更新的工作流以优化策略。

**关键创新**：RLFactory的主要创新在于其异步调用机制和解耦架构，这与现有方法的紧耦合设计形成鲜明对比。通过这种创新，RLFactory能够更好地处理工具的异质性和接口问题。

**关键设计**：在关键设计方面，RLFactory采用了异步调用器以提高工具调用的效率，并设计了支持多种奖励信号的奖励层，以便在不同评估需求下进行灵活调整。

## 📊 实验亮点

在实验中，RLFactory在自然问题（NQ）数据集上取得了0.486的测试分数，超越了使用类似技术的更大模型（如Qwen2.5-7B-Instruct-GRPO的0.473），并且训练吞吐量提高了6.8倍，展示了其在效率和效果上的显著提升。

## 🎯 应用场景

RLFactory的研究成果具有广泛的应用潜力，尤其是在需要与外部工具进行复杂交互的场景中，如智能助手、自动化客服和数据分析等领域。通过增强大型语言模型的多轮工具使用能力，RLFactory能够提升这些系统在实际应用中的智能化水平和用户体验。

## 📄 摘要（原文）

> Large language models excel at basic reasoning but struggle with tasks that require interaction with external tools. We present RLFactory, a plug-and-play reinforcement learning post-training framework for multi-round tool use. RLFactory tackles (i) tool-call stability and adaptability amid tool heterogeneity and interface issues via an asyncio-based asynchronous caller and a decoupled tool/training architecture, and (ii) diverse evaluation needs via a reward layer supporting rule-based, model-judgment, and tool-verification signals. It reconstructs the MDP by introducing observation markers from tool feedback, closing the loop among model, tools, and environment, and implements a generate-parse-invoke-update workflow for dynamic policy optimization. On Search-R1 with Qwen3-4B, RLFactory achieves a 0.486 test score on the Natural Questions (NQ) dataset, surpassing larger models trained with similar techniques (e.g., Qwen2.5-7B-Instruct-GRPO at 0.473), and increases training throughput by 6.8x. RLFactory provides a low-barrier, highly adaptable framework for strengthening multi-round tool use of LLMs in real-world scenarios. Code: https://github.com/Simple-Efficient/RL-Factory.

