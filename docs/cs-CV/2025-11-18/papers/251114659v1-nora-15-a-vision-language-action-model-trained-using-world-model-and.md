---
layout: default
title: NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards
---

# NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards

**arXiv**: [2511.14659v1](https://arxiv.org/abs/2511.14659) | [PDF](https://arxiv.org/pdf/2511.14659.pdf)

**作者**: Chia-Yu Hung, Navonil Majumder, Haoyuan Deng, Liu Renhang, Yankang Ang, Amir Zadeh, Chuan Li, Dorien Herremans, Ziwei Wang, Soujanya Poria

---

## 💡 一句话要点

**提出NORA-1.5 VLA模型，通过世界模型和动作奖励增强可靠性，适用于具身任务部署。**

**关键词**: `视觉-语言-动作模型` `世界模型奖励` `直接偏好优化` `具身智能` `后训练强化`

## 📋 核心要点

1. 核心问题：VLA模型在跨环境和具身任务中可靠性和泛化能力不足。
2. 方法要点：结合流匹配动作专家和基于世界模型与动作偏差的奖励模型进行后训练优化。
3. 实验或效果：在模拟和真实机器人基准测试中性能显著提升，验证奖励后训练的有效性。

## 📄 摘要（原文）

> Vision--language--action (VLA) models have recently shown promising performance on a variety of embodied tasks, yet they still fall short in reliability and generalization, especially when deployed across different embodiments or real-world environments. In this work, we introduce NORA-1.5, a VLA model built from the pre-trained NORA backbone by adding to it a flow-matching-based action expert. This architectural enhancement alone yields substantial performance gains, enabling NORA-1.5 to outperform NORA and several state-of-the-art VLA models across both simulated and real-world benchmarks. To further improve robustness and task success, we develop a set of reward models for post-training VLA policies. Our rewards combine (i) an action-conditioned world model (WM) that evaluates whether generated actions lead toward the desired goal, and (ii) a deviation-from-ground-truth heuristic that distinguishes good actions from poor ones. Using these reward signals, we construct preference datasets and adapt NORA-1.5 to target embodiments through direct preference optimization (DPO). Extensive evaluations show that reward-driven post-training consistently improves performance in both simulation and real-robot settings, demonstrating significant VLA model-reliability gains through simple yet effective reward models. Our findings highlight NORA-1.5 and reward-guided post-training as a viable path toward more dependable embodied agents suitable for real-world deployment.

