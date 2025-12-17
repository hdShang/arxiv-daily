---
layout: default
title: EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models
---

# EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models

**arXiv**: [2512.14666v1](https://arxiv.org/abs/2512.14666) | [PDF](https://arxiv.org/pdf/2512.14666.pdf)

**作者**: Zechen Bai, Chen Gao, Mike Zheng Shou

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-16

**备注**: 15 pages

---

## 💡 一句话要点

**提出EVOLVE-VLA框架，通过环境反馈实现视觉-语言-动作模型的测试时训练，解决静态模仿学习的适应性问题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `测试时训练` `视觉-语言-动作模型` `环境反馈` `进度估计` `噪声驯服` `跨任务泛化` `具身智能` `自适应学习`

## 📋 核心要点

1. 现有VLA模型依赖监督微调，需要大量演示、记忆轨迹，部署条件变化时无法适应，限制了自适应能力。
2. 提出EVOLVE-VLA框架，通过环境反馈实现测试时训练，利用学习进度估计器和噪声驯服机制，使模型持续自我改进。
3. 实验显示，EVOLVE-VLA在长视野任务提升8.6%，单样本学习提升22.0%，跨任务泛化达20.8%成功率，涌现错误恢复等能力。

## 📝 摘要（中文）

实现真正的自适应具身智能需要智能体通过环境交互持续学习，而不仅仅是模仿静态演示。视觉-语言-动作模型通过利用大语言模型推动了机器人操作的发展，但仍受限于监督微调：每个任务需要数百次演示、僵化地记忆轨迹，且在部署条件偏离训练时无法适应。我们提出了EVOLVE-VLA，这是一个测试时训练框架，使VLA模型能够通过环境交互以最少或零任务特定演示持续适应。关键技术挑战是用自主反馈替代测试时不可用的oracle奖励信号。我们通过一个提供密集反馈的学习进度估计器来解决这一问题，并关键地设计了两个机制来“驯服”这种固有噪声信号：(1) 累积进度估计机制平滑噪声点估计，(2) 渐进式视野扩展策略实现逐步策略演化。EVOLVE-VLA取得了显著提升：长视野任务提升8.6%，单样本学习提升22.0%，并实现跨任务泛化——在未见任务上达到20.8%的成功率（纯SFT为0%）。定性分析揭示了演示中不存在的涌现能力，包括错误恢复和新策略。这项工作代表了VLA模型向真正学习和适应迈出的关键一步，从静态模仿转向持续自我改进。

## 🔬 方法详解

EVOLVE-VLA是一个测试时训练框架，整体基于视觉-语言-动作模型，通过环境交互实现持续适应。关键技术创新包括：学习进度估计器提供密集反馈以替代oracle奖励信号，以及两个噪声驯服机制——累积进度估计平滑点估计噪声，渐进式视野扩展策略逐步演化策略。与现有方法的主要区别在于，它不依赖大量任务特定演示，而是利用环境反馈进行在线学习，解决了监督微调的静态性和适应性不足问题，实现了从模仿学习到交互学习的转变。

## 📊 实验亮点

EVOLVE-VLA在长视野任务上提升8.6%成功率，单样本学习提升22.0%，跨任务泛化在未见任务上达到20.8%成功率（纯SFT为0%），并涌现出错误恢复和新策略等能力，验证了测试时训练的有效性。

## 🎯 应用场景

该研究可应用于机器人操作、自动驾驶、智能家居等具身智能领域，使智能体能在动态环境中通过交互持续学习和适应，减少对人工演示的依赖，提升实际部署的鲁棒性和泛化能力。

## 📄 摘要（原文）

> Achieving truly adaptive embodied intelligence requires agents that learn not just by imitating static demonstrations, but by continuously improving through environmental interaction, which is akin to how humans master skills through practice. Vision-Language-Action (VLA) models have advanced robotic manipulation by leveraging large language models, yet remain fundamentally limited by Supervised Finetuning (SFT): requiring hundreds of demonstrations per task, rigidly memorizing trajectories, and failing to adapt when deployment conditions deviate from training. We introduce EVOLVE-VLA, a test-time training framework enabling VLAs to continuously adapt through environment interaction with minimal or zero task-specific demonstrations. The key technical challenge is replacing oracle reward signals (unavailable at test time) with autonomous feedback. We address this through a learned progress estimator providing dense feedback, and critically, we design our framework to ``tame'' this inherently noisy signal via two mechanisms: (1) an accumulative progress estimation mechanism smoothing noisy point-wise estimates, and (2) a progressive horizon extension strategy enabling gradual policy evolution. EVOLVE-VLA achieves substantial gains: +8.6\% on long-horizon tasks, +22.0\% in 1-shot learning, and enables cross-task generalization -- achieving 20.8\% success on unseen tasks without task-specific demonstrations training (vs. 0\% for pure SFT). Qualitative analysis reveals emergent capabilities absent in demonstrations, including error recovery and novel strategies. This work represents a critical step toward VLAs that truly learn and adapt, moving beyond static imitation toward continuous self-improvements.

