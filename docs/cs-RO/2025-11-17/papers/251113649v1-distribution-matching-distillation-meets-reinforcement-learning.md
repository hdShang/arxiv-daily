---
layout: default
title: Distribution Matching Distillation Meets Reinforcement Learning
---

# Distribution Matching Distillation Meets Reinforcement Learning

**arXiv**: [2511.13649v1](https://arxiv.org/abs/2511.13649) | [PDF](https://arxiv.org/pdf/2511.13649.pdf)

**作者**: Dengyang Jiang, Dongyang Liu, Zanyi Wang, Qilong Wu, Xin Jin, David Liu, Zhen Li, Mengmeng Wang, Peng Gao, Harry Yang

---

## 💡 一句话要点

**提出DMDR框架，结合强化学习与分布匹配蒸馏，提升少步扩散模型性能。**

**关键词**: `分布匹配蒸馏` `强化学习` `扩散模型` `模型蒸馏` `少步生成`

## 📋 核心要点

1. 核心问题：少步扩散模型性能受限于预训练多步模型，难以超越。
2. 方法要点：引入强化学习优化蒸馏过程，使用DMD损失作为正则化项。
3. 实验效果：DMDR在少步方法中实现领先视觉质量和提示一致性，甚至超越教师模型。

## 📄 摘要（原文）

> Distribution Matching Distillation (DMD) distills a pre-trained multi-step diffusion model to a few-step one to improve inference efficiency. However, the performance of the latter is often capped by the former. To circumvent this dilemma, we propose DMDR, a novel framework that combines Reinforcement Learning (RL) techniques into the distillation process. We show that for the RL of the few-step generator, the DMD loss itself is a more effective regularization compared to the traditional ones. In turn, RL can help to guide the mode coverage process in DMD more effectively. These allow us to unlock the capacity of the few-step generator by conducting distillation and RL simultaneously. Meanwhile, we design the dynamic distribution guidance and dynamic renoise sampling training strategies to improve the initial distillation process. The experiments demonstrate that DMDR can achieve leading visual quality, prompt coherence among few-step methods, and even exhibit performance that exceeds the multi-step teacher.

