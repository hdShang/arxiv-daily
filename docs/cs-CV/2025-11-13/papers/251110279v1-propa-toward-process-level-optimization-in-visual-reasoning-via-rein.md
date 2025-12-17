---
layout: default
title: PROPA: Toward Process-level Optimization in Visual Reasoning via Reinforcement Learning
---

# PROPA: Toward Process-level Optimization in Visual Reasoning via Reinforcement Learning

**arXiv**: [2511.10279v1](https://arxiv.org/abs/2511.10279) | [PDF](https://arxiv.org/pdf/2511.10279.pdf)

**作者**: Yanbei Jiang, Chao Lei, Yihao Ding, Krista Ehinger, Jey Han Lau

---

## 💡 一句话要点

**提出PROPA框架，通过强化学习优化视觉推理过程，无需人工标注**

**关键词**: `视觉推理优化` `强化学习` `过程级奖励` `蒙特卡洛树搜索` `视觉语言模型` `泛化能力`

## 📋 核心要点

1. 视觉语言模型在复杂推理中易因早期错误传播而失败
2. 结合MCTS与GRPO生成密集过程奖励，并交替使用SFT解决冷启动问题
3. 在多个基准和骨干网络上优于现有方法，提升泛化能力

## 📄 摘要（原文）

> Despite significant progress, Vision-Language Models (VLMs) still struggle with complex visual reasoning, where multi-step dependencies cause early errors to cascade through the reasoning chain. Existing post-training paradigms are limited: Supervised Fine-Tuning (SFT) relies on costly step-level annotations, while Reinforcement Learning with Verifiable Rewards (RLVR) methods like GRPO provide only sparse, outcome-level feedback, hindering stable optimization. We introduce PROPA (Process-level Reasoning Optimization with interleaved Policy Alignment), a novel framework that integrates Monte Carlo Tree Search (MCTS) with GRPO to generate dense, process-level rewards and optimize reasoning at each intermediate step without human annotations. To overcome the cold-start problem, PROPA interleaves GRPO updates with SFT, enabling the model to learn from both successful and failed reasoning trajectories. A Process Reward Model (PRM) is further trained to guide inference-time search, aligning the test-time search with the training signal. Across seven benchmarks and four VLM backbones, PROPA consistently outperforms both SFT- and RLVR-based baselines. It achieves up to 17.0% gains on in-domain tasks and 21.0% gains on out-of-domain tasks compared to existing state-of-the-art, establishing a strong reasoning and generalization capability for visual reasoning tasks. The code isavailable at: https://github.com/YanbeiJiang/PROPA.

