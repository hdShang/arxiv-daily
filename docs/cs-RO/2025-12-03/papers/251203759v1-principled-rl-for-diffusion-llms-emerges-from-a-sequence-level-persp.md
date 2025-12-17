---
layout: default
title: Principled RL for Diffusion LLMs Emerges from a Sequence-Level Perspective
---

# Principled RL for Diffusion LLMs Emerges from a Sequence-Level Perspective

**arXiv**: [2512.03759v1](https://arxiv.org/abs/2512.03759) | [PDF](https://arxiv.org/pdf/2512.03759.pdf)

**作者**: Jingyang Ou, Jiaqi Han, Minkai Xu, Shaoxuan Xu, Jianwen Xie, Stefano Ermon, Yi Wu, Chongxuan Li

---

## 💡 一句话要点

**提出基于ELBO的序列级策略优化（ESPO），以解决扩散大语言模型中的强化学习适配难题。**

**关键词**: `扩散大语言模型` `强化学习` `序列级优化` `ELBO` `策略优化` `数学推理`

## 📋 核心要点

1. 核心问题：扩散大语言模型缺乏自回归模型的token级概率分解，导致传统token级RL方法不适用。
2. 方法要点：将序列生成视为单一动作，使用ELBO作为序列级似然代理，结合token级归一化和稳健KL散度估计。
3. 实验或效果：在数学推理、编码和规划任务中显著超越基线，如在Countdown任务上提升20-40分。

## 📄 摘要（原文）

> Reinforcement Learning (RL) has proven highly effective for autoregressive language models, but adapting these methods to diffusion large language models (dLLMs) presents fundamental challenges. The core difficulty lies in likelihood approximation: while autoregressive models naturally provide token-level conditional probabilities essential for token-level RL objectives (e.g., GRPO), dLLMs generate sequences through iterative non-autoregressive denoising steps that lack this factorization. To address this fundamental mismatch, we propose ELBO-based Sequence-level Policy Optimization (ESPO), a principled RL framework that treats entire sequence generation as a single action and uses the ELBO as a tractable sequence-level likelihood proxy. Our method incorporates per-token normalization of importance ratios and robust KL-divergence estimation to ensure stable large-scale training. Extensive experiments on mathematical reasoning, coding, and planning tasks demonstrate that ESPO significantly outperforms token-level baselines, achieving dramatic improvements of 20-40 points on the Countdown task, while maintaining consistent gains on math and coding benchmarks. Our approach establishes sequence-level optimization as a principled and empirically effective paradigm for RL in dLLMs. Our code is available at https://github.com/ML-GSAI/ESPO.

