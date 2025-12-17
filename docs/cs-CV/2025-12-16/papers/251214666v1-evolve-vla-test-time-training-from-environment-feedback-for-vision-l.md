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

**提出EVOLVE-VLA测试时训练框架，使视觉-语言-动作模型通过环境交互持续自适应，减少任务特定演示需求。**

**关键词**: `测试时训练` `视觉-语言-动作模型` `环境交互` `进度估计` `自适应学习` `机器人操作` `跨任务泛化` `具身智能`

## 📋 核心要点

1. 现有VLA模型依赖监督微调，需大量演示、记忆轨迹，部署条件变化时无法适应，限制了自适应能力。
2. 提出测试时训练框架，通过学习的进度估计器提供自主反馈，结合累积估计和渐进视野扩展机制驯服噪声信号。
3. 实验显示长视野任务提升8.6%，1-shot学习提升22.0%，跨任务泛化达20.8%成功率，涌现错误恢复和新策略能力。

## 📝 摘要（中文）

实现真正自适应的具身智能需要智能体通过环境交互持续学习，而非仅模仿静态演示。视觉-语言-动作模型虽通过大语言模型推进了机器人操作，但仍受限于监督微调：每任务需数百演示、僵化记忆轨迹、部署条件偏离训练时无法适应。本文提出EVOLVE-VLA，一个测试时训练框架，使VLA模型能以最少或零任务特定演示通过环境交互持续适应。关键技术挑战是用自主反馈替代测试时不可用的oracle奖励信号。我们通过学习的进度估计器提供密集反馈解决此问题，并设计框架通过两种机制“驯服”这一固有噪声信号：(1)累积进度估计机制平滑噪声点估计，(2)渐进视野扩展策略实现逐步策略演化。EVOLVE-VLA取得显著提升：长视野任务+8.6%、1-shot学习+22.0%，并实现跨任务泛化——在未见任务上无任务特定演示训练达到20.8%成功率（纯SFT为0%）。定性分析揭示了演示中不存在的涌现能力，包括错误恢复和新策略。这项工作代表了VLA模型真正学习和适应的关键一步，从静态模仿迈向持续自我改进。

## 🔬 方法详解

EVOLVE-VLA是一个测试时训练框架，使视觉-语言-动作模型在部署时通过环境交互持续自适应。整体框架基于学习的进度估计器，它提供密集反馈替代测试时不可用的oracle奖励信号。关键技术创新点包括：累积进度估计机制，通过平滑点估计减少噪声影响；渐进视野扩展策略，逐步扩展策略优化范围以实现稳定演化。与现有方法的主要区别在于，它不依赖大量任务特定演示，而是利用自主反馈实现在线适应，突破了监督微调的静态限制，支持动态环境交互和跨任务泛化。

## 📊 实验亮点

EVOLVE-VLA在长视野任务上提升8.6%，1-shot学习提升22.0%，跨任务泛化在未见任务上达到20.8%成功率（纯SFT为0%），并涌现错误恢复和新策略能力，显著超越传统监督微调方法。

## 🎯 应用场景

该研究可应用于机器人操作、自主导航和智能家居等领域，使智能体在真实世界中通过交互持续改进，减少对人工演示的依赖，提升适应性和泛化能力，推动具身智能向更灵活、自适应的方向发展。

## 📄 摘要（原文）

> Achieving truly adaptive embodied intelligence requires agents that learn not just by imitating static demonstrations, but by continuously improving through environmental interaction, which is akin to how humans master skills through practice. Vision-Language-Action (VLA) models have advanced robotic manipulation by leveraging large language models, yet remain fundamentally limited by Supervised Finetuning (SFT): requiring hundreds of demonstrations per task, rigidly memorizing trajectories, and failing to adapt when deployment conditions deviate from training. We introduce EVOLVE-VLA, a test-time training framework enabling VLAs to continuously adapt through environment interaction with minimal or zero task-specific demonstrations. The key technical challenge is replacing oracle reward signals (unavailable at test time) with autonomous feedback. We address this through a learned progress estimator providing dense feedback, and critically, we design our framework to ``tame'' this inherently noisy signal via two mechanisms: (1) an accumulative progress estimation mechanism smoothing noisy point-wise estimates, and (2) a progressive horizon extension strategy enabling gradual policy evolution. EVOLVE-VLA achieves substantial gains: +8.6\% on long-horizon tasks, +22.0\% in 1-shot learning, and enables cross-task generalization -- achieving 20.8\% success on unseen tasks without task-specific demonstrations training (vs. 0\% for pure SFT). Qualitative analysis reveals emergent capabilities absent in demonstrations, including error recovery and novel strategies. This work represents a critical step toward VLAs that truly learn and adapt, moving beyond static imitation toward continuous self-improvements.

