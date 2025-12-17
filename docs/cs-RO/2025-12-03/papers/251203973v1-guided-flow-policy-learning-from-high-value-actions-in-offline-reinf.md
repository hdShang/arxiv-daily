---
layout: default
title: Guided Flow Policy: Learning from High-Value Actions in Offline Reinforcement Learning
---

# Guided Flow Policy: Learning from High-Value Actions in Offline Reinforcement Learning

**arXiv**: [2512.03973v1](https://arxiv.org/abs/2512.03973) | [PDF](https://arxiv.org/pdf/2512.03973.pdf)

**作者**: Franki Nguimatsia Tiofack, Théotime Le Hellard, Fabian Schramm, Nicolas Perrin-Gilbert, Justin Carpentier

---

## 💡 一句话要点

**提出引导流策略以解决离线强化学习中行为正则化无法区分高价值动作的问题**

**关键词**: `离线强化学习` `行为正则化` `流匹配策略` `加权行为克隆` `高价值动作学习` `多步策略优化`

## 📋 核心要点

1. 核心问题：离线强化学习的行为正则化方法对所有状态-动作对进行无差别模仿，未区分高价值和低价值动作。
2. 方法要点：结合多步流匹配策略和蒸馏单步演员，通过加权行为克隆引导流策略专注于克隆数据集中的高价值动作。
3. 实验或效果：在OGBench、Minari和D4RL基准的144个任务中实现先进性能，尤其在次优数据集和挑战性任务上提升显著。

## 📄 摘要（原文）

> Offline reinforcement learning often relies on behavior regularization that enforces policies to remain close to the dataset distribution. However, such approaches fail to distinguish between high-value and low-value actions in their regularization components. We introduce Guided Flow Policy (GFP), which couples a multi-step flow-matching policy with a distilled one-step actor. The actor directs the flow policy through weighted behavior cloning to focus on cloning high-value actions from the dataset rather than indiscriminately imitating all state-action pairs. In turn, the flow policy constrains the actor to remain aligned with the dataset's best transitions while maximizing the critic. This mutual guidance enables GFP to achieve state-of-the-art performance across 144 state and pixel-based tasks from the OGBench, Minari, and D4RL benchmarks, with substantial gains on suboptimal datasets and challenging tasks. Webpage: https://simple-robotics.github.io/publications/guided-flow-policy/

