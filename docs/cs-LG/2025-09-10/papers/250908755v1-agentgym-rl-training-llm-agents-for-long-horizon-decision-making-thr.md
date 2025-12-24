---
layout: default
title: "AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning"
---

# AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08755" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08755v1</a>
  <a href="https://arxiv.org/pdf/2509.08755.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08755v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08755v1', 'AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiheng Xi, Jixuan Huang, Chenyang Liao, Baodai Huang, Honglin Guo, Jiaqi Liu, Rui Zheng, Junjie Ye, Jiazheng Zhang, Wenxiang Chen, Wei He, Yiwen Ding, Guanyu Li, Zehui Chen, Zhengyin Du, Xuesong Yao, Yufei Xu, Jiecao Chen, Tao Gui, Zuxuan Wu, Qi Zhang, Xuanjing Huang, Yu-Gang Jiang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-10

**备注**: preprint, 39 pages, 16 figures. Project: https://AgentGym-RL.github.io/. Framework and Code: https://github.com/woooodyy/AgentGym, https://github.com/woooodyy/AgentGym-RL

---

## 💡 一句话要点

**AgentGym-RL：通过多轮强化学习训练LLM智能体进行长程决策**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `LLM智能体` `长程决策` `多轮交互` `探索-利用平衡`

## 📋 核心要点

1. 现有方法缺乏统一的交互式强化学习框架，难以从零开始训练LLM智能体，且缺乏对多样化现实环境的有效支持。
2. AgentGym-RL框架通过模块化设计和ScalingInter-RL训练方法，平衡探索与利用，实现LLM智能体在复杂环境下的稳定训练。
3. 实验表明，AgentGym-RL训练的智能体在27个任务上达到或超过商业模型的性能，验证了框架的有效性和稳定性。

## 📝 摘要（中文）

本文提出了AgentGym-RL，一个用于通过强化学习（RL）训练LLM智能体进行多轮交互式决策的新框架。该框架具有模块化和解耦的架构，保证了高度的灵活性和可扩展性。它包含各种真实世界的场景，并支持主流的RL算法。此外，本文还提出了一种名为ScalingInter-RL的训练方法，该方法旨在平衡探索-利用，并实现稳定的RL优化。在早期阶段，它通过限制交互次数来强调利用，并逐渐转向具有更大范围的探索，以鼓励多样化的问题解决策略。通过这种方式，智能体可以发展出更多样化的行为，并且在长程情况下不易崩溃。大量的实验验证了AgentGym-RL框架和ScalingInter-RL方法的稳定性和有效性。在各种环境中的27个任务上，本文的智能体匹配或超过了商业模型。本文提供了关键的见解，并将开源完整的AgentGym-RL框架（包括代码和数据集），以支持研究社区开发下一代智能智能体。

## 🔬 方法详解

**问题定义**：现有方法在训练LLM智能体进行长程决策时，缺乏一个统一且灵活的强化学习框架。以往方法通常依赖于监督微调（SFT），难以从零开始训练智能体，并且在处理多样化和真实的交互式环境时存在局限性。因此，如何设计一个能够有效训练LLM智能体，使其具备在复杂环境中进行多轮交互决策能力的强化学习框架，是一个亟待解决的问题。

**核心思路**：本文的核心思路是构建一个模块化、可扩展的强化学习框架AgentGym-RL，并提出一种名为ScalingInter-RL的训练方法，以平衡探索与利用。通过逐步增加交互范围，鼓励智能体在早期阶段进行充分的利用，并在后期进行更广泛的探索，从而避免智能体在长程决策中崩溃，并学习到更多样化的行为策略。

**技术框架**：AgentGym-RL框架采用模块化和解耦的架构，主要包含以下几个核心模块：环境交互模块（负责与各种真实环境进行交互）、智能体模块（包含LLM智能体及其策略）、奖励函数模块（定义智能体行为的奖励信号）和训练模块（实现RL算法的优化）。ScalingInter-RL训练方法则是在训练过程中动态调整交互范围，从短程交互逐步过渡到长程交互，以平衡探索和利用。

**关键创新**：本文最重要的技术创新在于提出了AgentGym-RL框架和ScalingInter-RL训练方法。AgentGym-RL框架的模块化设计使得其具有高度的灵活性和可扩展性，可以方便地集成不同的环境和RL算法。ScalingInter-RL训练方法则有效地解决了长程决策中探索-利用的平衡问题，避免了智能体在训练过程中崩溃，并提高了智能体的泛化能力。

**关键设计**：ScalingInter-RL训练方法的关键设计在于动态调整交互范围。在训练初期，限制交互次数，鼓励智能体充分利用已有的知识和经验。随着训练的进行，逐步增加交互范围，鼓励智能体进行更广泛的探索，发现新的策略和行为。此外，奖励函数的设计也至关重要，需要能够准确地反映智能体的行为质量，并引导智能体朝着期望的方向发展。具体的参数设置，例如学习率、折扣因子等，需要根据具体的环境和任务进行调整。

## 📊 实验亮点

实验结果表明，使用AgentGym-RL框架和ScalingInter-RL训练方法训练的LLM智能体在27个不同的任务上，性能达到或超过了商业模型。这充分验证了该框架的有效性和稳定性。尤其是在长程决策任务中，ScalingInter-RL方法能够有效地避免智能体崩溃，并学习到更优的策略。

## 🎯 应用场景

该研究成果可广泛应用于各种需要智能体进行长程决策的领域，例如游戏AI、机器人控制、自动驾驶、智能客服等。通过AgentGym-RL框架，可以训练出能够在复杂环境中自主完成任务的LLM智能体，从而提高工作效率、降低成本，并为人们提供更智能化的服务。未来，该框架有望成为开发下一代智能智能体的基础平台。

## 📄 摘要（原文）

> Developing autonomous LLM agents capable of making a series of intelligent decisions to solve complex, real-world tasks is a fast-evolving frontier. Like human cognitive development, agents are expected to acquire knowledge and skills through exploration and interaction with the environment. Despite advances, the community still lacks a unified, interactive reinforcement learning (RL) framework that can effectively train such agents from scratch -- without relying on supervised fine-tuning (SFT) -- across diverse and realistic environments. To bridge this gap, we introduce AgentGym-RL, a new framework to train LLM agents for multi-turn interactive decision-making through RL. The framework features a modular and decoupled architecture, ensuring high flexibility and extensibility. It encompasses a wide variety of real-world scenarios, and supports mainstream RL algorithms. Furthermore, we propose ScalingInter-RL, a training approach designed for exploration-exploitation balance and stable RL optimization. In early stages, it emphasizes exploitation by restricting the number of interactions, and gradually shifts towards exploration with larger horizons to encourage diverse problem-solving strategies. In this way, the agent develops more diverse behaviors and is less prone to collapse under long horizons. We perform extensive experiments to validate the stability and effectiveness of both the AgentGym-RL framework and the ScalingInter-RL approach. Our agents match or surpass commercial models on 27 tasks across diverse environments. We offer key insights and will open-source the complete AgentGym-RL framework -- including code and datasets -- to empower the research community in developing the next generation of intelligent agents.

