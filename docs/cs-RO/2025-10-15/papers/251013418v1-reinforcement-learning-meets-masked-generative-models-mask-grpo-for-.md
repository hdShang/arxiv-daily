---
layout: default
title: Reinforcement Learning Meets Masked Generative Models: Mask-GRPO for Text-to-Image Generation
---

# Reinforcement Learning Meets Masked Generative Models: Mask-GRPO for Text-to-Image Generation

**arXiv**: [2510.13418v1](https://arxiv.org/abs/2510.13418) | [PDF](https://arxiv.org/pdf/2510.13418.pdf)

**作者**: Yifu Luo, Xinhao Hu, Keyu Fan, Haoyuan Sun, Zeyu Chen, Bo Xia, Tiantian Zhang, Yongzhe Chang, Xueqian Wang

---

## 💡 一句话要点

**提出Mask-GRPO以强化学习优化掩码生成模型用于文本到图像生成**

**关键词**: `文本到图像生成` `强化学习` `掩码生成模型` `策略优化` `多步决策` `偏好对齐`

## 📋 核心要点

1. 现有强化学习方法忽略掩码生成模型，仅针对扩散或自回归模型
2. 重新定义转移概率，将去掩码过程建模为多步决策问题
3. 在标准基准和偏好对齐上超越现有方法，提升基础模型性能

## 📄 摘要（原文）

> Reinforcement learning (RL) has garnered increasing attention in
> text-to-image (T2I) generation. However, most existing RL approaches are
> tailored to either diffusion models or autoregressive models, overlooking an
> important alternative: masked generative models. In this work, we propose
> Mask-GRPO, the first method to incorporate Group Relative Policy Optimization
> (GRPO)-based RL into this overlooked paradigm. Our core insight is to redefine
> the transition probability, which is different from current approaches, and
> formulate the unmasking process as a multi-step decision-making problem. To
> further enhance our method, we explore several useful strategies, including
> removing the KL constraint, applying the reduction strategy, and filtering out
> low-quality samples. Using Mask-GRPO, we improve a base model, Show-o, with
> substantial improvements on standard T2I benchmarks and preference alignment,
> outperforming existing state-of-the-art approaches. The code is available on
> https://github.com/xingzhejun/Mask-GRPO

