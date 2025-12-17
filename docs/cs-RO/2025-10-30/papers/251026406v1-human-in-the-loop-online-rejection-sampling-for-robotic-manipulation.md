---
layout: default
title: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation
---

# Human-in-the-loop Online Rejection Sampling for Robotic Manipulation

**arXiv**: [2510.26406v1](https://arxiv.org/abs/2510.26406) | [PDF](https://arxiv.org/pdf/2510.26406.pdf)

**作者**: Guanxing Lu, Rui Zhao, Haitao Lin, He Zhang, Yansong Tang

---

## 💡 一句话要点

**提出Hi-ORS方法，通过拒绝采样和人机交互提升机器人操作策略的稳定性和鲁棒性。**

**关键词**: `机器人操作` `拒绝采样` `人机交互` `强化学习微调` `视觉-语言-动作模型`

## 📋 核心要点

1. 核心问题：强化学习微调视觉-语言-动作模型时，价值估计不准确和中间步骤监督稀疏导致不稳定。
2. 方法要点：使用拒绝采样过滤负奖励样本，结合奖励加权监督训练提供密集中间监督。
3. 实验或效果：在真实世界任务中，1.5小时训练即超越基线，实现高效错误恢复行为。

## 📄 摘要（原文）

> Reinforcement learning (RL) is widely used to produce robust robotic
> manipulation policies, but fine-tuning vision-language-action (VLA) models with
> RL can be unstable due to inaccurate value estimates and sparse supervision at
> intermediate steps. In contrast, imitation learning (IL) is easy to train but
> often underperforms due to its offline nature. In this paper, we propose
> Hi-ORS, a simple yet effective post-training method that utilizes rejection
> sampling to achieve both training stability and high robustness. Hi-ORS
> stabilizes value estimation by filtering out negatively rewarded samples during
> online fine-tuning, and adopts a reward-weighted supervised training objective
> to provide dense intermediate-step supervision. For systematic study, we
> develop an asynchronous inference-training framework that supports flexible
> online human-in-the-loop corrections, which serve as explicit guidance for
> learning error-recovery behaviors. Across three real-world tasks and two
> embodiments, Hi-ORS fine-tunes a pi-base policy to master contact-rich
> manipulation in just 1.5 hours of real-world training, outperforming RL and IL
> baselines by a substantial margin in both effectiveness and efficiency.
> Notably, the fine-tuned policy exhibits strong test-time scalability by
> reliably executing complex error-recovery behaviors to achieve better
> performance.

