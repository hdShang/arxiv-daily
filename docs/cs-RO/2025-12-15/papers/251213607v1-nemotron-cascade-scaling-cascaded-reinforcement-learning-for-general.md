---
layout: default
title: Nemotron-Cascade: Scaling Cascaded Reinforcement Learning for General-Purpose Reasoning Models
---

# Nemotron-Cascade: Scaling Cascaded Reinforcement Learning for General-Purpose Reasoning Models

**arXiv**: [2512.13607v1](https://arxiv.org/abs/2512.13607) | [PDF](https://arxiv.org/pdf/2512.13607.pdf)

**作者**: Boxin Wang, Chankyu Lee, Nayeon Lee, Sheng-Chieh Lin, Wenliang Dai, Yang Chen, Yangyi Chen, Zhuolin Yang, Zihan Liu, Mohammad Shoeybi, Bryan Catanzaro, Wei Ping

---

## 💡 一句话要点

**提出级联域强化学习以构建通用推理模型，解决跨域异质性挑战。**

**关键词**: `级联强化学习` `通用推理模型` `跨域异质性` `RLHF对齐` `基准测试` `模型训练`

## 📋 核心要点

1. 核心问题：跨域异质性如响应长度和验证延迟差异，使RL基础设施复杂化并阻碍训练。
2. 方法要点：采用级联域强化学习，按域顺序训练，降低工程复杂度并提升性能。
3. 实验或效果：14B模型在RL后超越SFT教师，在多个基准和IOI中表现优异。

## 📄 摘要（原文）

> Building general-purpose reasoning models with reinforcement learning (RL) entails substantial cross-domain heterogeneity, including large variation in inference-time response lengths and verification latency. Such variability complicates the RL infrastructure, slows training, and makes training curriculum (e.g., response length extension) and hyperparameter selection challenging. In this work, we propose cascaded domain-wise reinforcement learning (Cascade RL) to develop general-purpose reasoning models, Nemotron-Cascade, capable of operating in both instruct and deep thinking modes. Departing from conventional approaches that blend heterogeneous prompts from different domains, Cascade RL orchestrates sequential, domain-wise RL, reducing engineering complexity and delivering state-of-the-art performance across a wide range of benchmarks. Notably, RLHF for alignment, when used as a pre-step, boosts the model's reasoning ability far beyond mere preference optimization, and subsequent domain-wise RLVR stages rarely degrade the benchmark performance attained in earlier domains and may even improve it (see an illustration in Figure 1). Our 14B model, after RL, outperforms its SFT teacher, DeepSeek-R1-0528, on LiveCodeBench v5/v6/Pro and achieves silver-medal performance in the 2025 International Olympiad in Informatics (IOI). We transparently share our training and data recipes.

