---
layout: default
title: Each Prompt Matters: Scaling Reinforcement Learning Without Wasting Rollouts on Hundred-Billion-Scale MoE
---

# Each Prompt Matters: Scaling Reinforcement Learning Without Wasting Rollouts on Hundred-Billion-Scale MoE

**arXiv**: [2512.07710v1](https://arxiv.org/abs/2512.07710) | [PDF](https://arxiv.org/pdf/2512.07710.pdf)

**作者**: Anxiang Zeng, Haibo Zhang, Hailing Zhang, Kaixiang Mo, Liang Yao, Ling Hu, Long Zhang, Shuman Liu, Shuyi Xie, Yanshi Li, Yizhang Chen, Yuepeng Sheng, Yuwei Huang, Zhaochen Xu, Zhiqiang Zhou, Ziqin Liew

---

## 💡 一句话要点

**提出基于每个提示都重要的RL框架，以高效训练百亿规模MoE推理模型**

**关键词**: `百亿规模MoE模型` `强化学习框架` `零方差提示消除` `熵自适应优化` `路由器重放` `高吞吐系统`

## 📋 核心要点

1. 核心问题：百亿规模MoE模型RL训练存在零方差提示浪费rollouts、重要性采样不稳定、优势反转和系统瓶颈。
2. 方法要点：引入多阶段零方差消除、熵自适应优化ESPO、路由器重放策略和FP8高吞吐系统。
3. 实验或效果：模型在内部和公开评估中表现强劲，实现稳定高效训练。

## 📄 摘要（原文）

> We present CompassMax-V3-Thinking, a hundred-billion-scale MoE reasoning model trained with a new RL framework built on one principle: each prompt must matter. Scaling RL to this size exposes critical inefficiencies-zero-variance prompts that waste rollouts, unstable importance sampling over long horizons, advantage inversion from standard reward models, and systemic bottlenecks in rollout processing. To overcome these challenges, we introduce several unified innovations: (1) Multi-Stage Zero-Variance Elimination, which filters out non-informative prompts and stabilizes group-based policy optimization (e.g. GRPO) by removing wasted rollouts; (2) ESPO, an entropy-adaptive optimization method that balances token-level and sequence-level importance sampling to maintain stable learning dynamics; (3) a Router Replay strategy that aligns training-time MoE router decisions with inference-time behavior to mitigate train-infer discrepancies, coupled with a reward model adjustment to prevent advantage inversion; (4) a high-throughput RL system with FP8-precision rollouts, overlapped reward computation, and length-aware scheduling to eliminate performance bottlenecks. Together, these contributions form a cohesive pipeline that makes RL on hundred-billion-scale MoE models stable and efficient. The resulting model delivers strong performance across both internal and public evaluations.

