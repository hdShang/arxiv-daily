---
layout: default
title: SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models
---

# SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models

**arXiv**: [2511.15605v1](https://arxiv.org/abs/2511.15605) | [PDF](https://arxiv.org/pdf/2511.15605.pdf)

**作者**: Senyu Fei, Siyin Wang, Li Ji, Ao Li, Shiduo Zhang, Liming Liu, Jinlong Hou, Jingjing Gong, Xianzhong Zhao, Xipeng Qiu

---

## 💡 一句话要点

**提出自参考策略优化以解决视觉-语言-动作模型的奖励稀疏问题**

**关键词**: `视觉-语言-动作模型` `强化学习` `自参考策略优化` `潜在世界表示` `机器人操作` `奖励稀疏问题`

## 📋 核心要点

1. 核心问题：VLA模型依赖专家演示导致演示偏差和奖励稀疏，降低训练效率
2. 方法要点：利用模型自身成功轨迹作为自参考，通过潜在世界表示分配进展奖励
3. 实验或效果：在LIBERO基准上，仅200步强化学习将成功率从48.9%提升至99.2%

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models excel in robotic manipulation but are constrained by their heavy reliance on expert demonstrations, leading to demonstration bias and limiting performance. Reinforcement learning (RL) is a vital post-training strategy to overcome these limits, yet current VLA-RL methods, including group-based optimization approaches, are crippled by severe reward sparsity. Relying on binary success indicators wastes valuable information in failed trajectories, resulting in low training efficiency. To solve this, we propose Self-Referential Policy Optimization (SRPO), a novel VLA-RL framework. SRPO eliminates the need for external demonstrations or manual reward engineering by leveraging the model's own successful trajectories, generated within the current training batch, as a self-reference. This allows us to assign a progress-wise reward to failed attempts. A core innovation is the use of latent world representations to measure behavioral progress robustly. Instead of relying on raw pixels or requiring domain-specific fine-tuning, we utilize the compressed, transferable encodings from a world model's latent space. These representations naturally capture progress patterns across environments, enabling accurate, generalized trajectory comparison. Empirical evaluations on the LIBERO benchmark demonstrate SRPO's efficiency and effectiveness. Starting from a supervised baseline with 48.9% success, SRPO achieves a new state-of-the-art success rate of 99.2% in just 200 RL steps, representing a 103% relative improvement without any extra supervision. Furthermore, SRPO shows substantial robustness, achieving a 167% performance improvement on the LIBERO-Plus benchmark.

