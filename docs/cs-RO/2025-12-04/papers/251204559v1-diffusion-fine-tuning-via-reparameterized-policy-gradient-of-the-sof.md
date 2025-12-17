---
layout: default
title: Diffusion Fine-Tuning via Reparameterized Policy Gradient of the Soft Q-Function
---

# Diffusion Fine-Tuning via Reparameterized Policy Gradient of the Soft Q-Function

**arXiv**: [2512.04559v1](https://arxiv.org/abs/2512.04559) | [PDF](https://arxiv.org/pdf/2512.04559.pdf)

**作者**: Hyeongyu Kang, Jaewoo Lee, Woocheol Shin, Kiyoung Om, Jinkyoo Park

---

## 💡 一句话要点

**提出SQDF方法以解决扩散模型微调中的奖励过优化问题**

**关键词**: `扩散模型微调` `奖励过优化` `软Q函数` `策略梯度` `文本到图像对齐` `在线优化`

## 📋 核心要点

1. 核心问题：扩散模型微调易导致奖励过优化，生成高奖励但不自然且多样性差的样本。
2. 方法要点：基于软Q函数的重参数化策略梯度，结合KL正则化、折扣因子、一致性模型和离策略回放缓冲区。
3. 实验效果：在文本到图像对齐中实现高目标奖励并保持多样性，在在线黑盒优化中样本效率高且自然多样。

## 📄 摘要（原文）

> Diffusion models excel at generating high-likelihood samples but often require alignment with downstream objectives. Existing fine-tuning methods for diffusion models significantly suffer from reward over-optimization, resulting in high-reward but unnatural samples and degraded diversity. To mitigate over-optimization, we propose \textbf{Soft Q-based Diffusion Finetuning (SQDF)}, a novel KL-regularized RL method for diffusion alignment that applies a reparameterized policy gradient of a training-free, differentiable estimation of the soft Q-function. SQDF is further enhanced with three innovations: a discount factor for proper credit assignment in the denoising process, the integration of consistency models to refine Q-function estimates, and the use of an off-policy replay buffer to improve mode coverage and manage the reward-diversity trade-off. Our experiments demonstrate that SQDF achieves superior target rewards while preserving diversity in text-to-image alignment. Furthermore, in online black-box optimization, SQDF attains high sample efficiency while maintaining naturalness and diversity.

