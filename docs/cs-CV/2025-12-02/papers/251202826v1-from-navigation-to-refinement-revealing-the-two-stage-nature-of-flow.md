---
layout: default
title: From Navigation to Refinement: Revealing the Two-Stage Nature of Flow-based Diffusion Models through Oracle Velocity
---

# From Navigation to Refinement: Revealing the Two-Stage Nature of Flow-based Diffusion Models through Oracle Velocity

**arXiv**: [2512.02826v1](https://arxiv.org/abs/2512.02826) | [PDF](https://arxiv.org/pdf/2512.02826.pdf)

**作者**: Haoming Liu, Jinnuo Liu, Yanhao Li, Liuyang Bai, Yunkai Ji, Yuanhe Guo, Shenji Wan, Hongyi Wen

---

## 💡 一句话要点

**通过Oracle Velocity揭示基于流的扩散模型的两阶段训练本质，解释其记忆-泛化行为。**

**关键词**: `流匹配` `扩散模型` `训练动态` `记忆泛化` `速度场分析`

## 📋 核心要点

1. 核心问题：基于流的扩散模型的记忆-泛化行为机制不明确。
2. 方法要点：分析流匹配目标的边际速度场，发现其闭式表达式揭示两阶段训练目标。
3. 实验或效果：解释时间步偏移调度、无分类器引导间隔等实践技巧的有效性。

## 📄 摘要（原文）

> Flow-based diffusion models have emerged as a leading paradigm for training generative models across images and videos. However, their memorization-generalization behavior remains poorly understood. In this work, we revisit the flow matching (FM) objective and study its marginal velocity field, which admits a closed-form expression, allowing exact computation of the oracle FM target. Analyzing this oracle velocity field reveals that flow-based diffusion models inherently formulate a two-stage training target: an early stage guided by a mixture of data modes, and a later stage dominated by the nearest data sample. The two-stage objective leads to distinct learning behaviors: the early navigation stage generalizes across data modes to form global layouts, whereas the later refinement stage increasingly memorizes fine-grained details. Leveraging these insights, we explain the effectiveness of practical techniques such as timestep-shifted schedules, classifier-free guidance intervals, and latent space design choices. Our study deepens the understanding of diffusion model training dynamics and offers principles for guiding future architectural and algorithmic improvements.

