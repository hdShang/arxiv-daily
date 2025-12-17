---
layout: default
title: SeFA-Policy: Fast and Accurate Visuomotor Policy Learning with Selective Flow Alignment
---

# SeFA-Policy: Fast and Accurate Visuomotor Policy Learning with Selective Flow Alignment

**arXiv**: [2511.08583v1](https://arxiv.org/abs/2511.08583) | [PDF](https://arxiv.org/pdf/2511.08583.pdf)

**作者**: Rong Xue, Jiageng Mao, Mingtong Zhang, Yue Wang

---

## 💡 一句话要点

**提出选择性流对齐以解决视觉运动策略学习中的动作偏差问题**

**关键词**: `视觉运动策略学习` `选择性流对齐` `整流流方法` `动作一致性校正` `机器人模仿学习`

## 📋 核心要点

1. 核心问题：整流流方法在迭代蒸馏后，生成动作偏离当前视觉观察，导致累积误差和不稳定执行
2. 方法要点：利用专家演示选择性校正生成动作，保持观察一致性和多模态性，同时支持一步推理
3. 实验或效果：在模拟和真实操作任务中超越现有方法，提高准确性和鲁棒性，推理延迟降低超98%

## 📄 摘要（原文）

> Developing efficient and accurate visuomotor policies poses a central challenge in robotic imitation learning. While recent rectified flow approaches have advanced visuomotor policy learning, they suffer from a key limitation: After iterative distillation, generated actions may deviate from the ground-truth actions corresponding to the current visual observation, leading to accumulated error as the reflow process repeats and unstable task execution. We present Selective Flow Alignment (SeFA), an efficient and accurate visuomotor policy learning framework. SeFA resolves this challenge by a selective flow alignment strategy, which leverages expert demonstrations to selectively correct generated actions and restore consistency with observations, while preserving multimodality. This design introduces a consistency correction mechanism that ensures generated actions remain observation-aligned without sacrificing the efficiency of one-step flow inference. Extensive experiments across both simulated and real-world manipulation tasks show that SeFA Policy surpasses state-of-the-art diffusion-based and flow-based policies, achieving superior accuracy and robustness while reducing inference latency by over 98%. By unifying rectified flow efficiency with observation-consistent action generation, SeFA provides a scalable and dependable solution for real-time visuomotor policy learning. Code is available on https://github.com/RongXueZoe/SeFA.

