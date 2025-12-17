---
layout: default
title: Entropy Ratio Clipping as a Soft Global Constraint for Stable Reinforcement Learning
---

# Entropy Ratio Clipping as a Soft Global Constraint for Stable Reinforcement Learning

**arXiv**: [2512.05591v1](https://arxiv.org/abs/2512.05591) | [PDF](https://arxiv.org/pdf/2512.05591.pdf)

**作者**: Zhenpeng Su, Leiyu Pan, Minxuan Lv, Tiehua Mei, Zijia Lin, Yuntao Li, Wenping Hu, Ruiming Tang, Kun Gai, Guorui Zhou

---

## 💡 一句话要点

**提出熵比裁剪机制以稳定大语言模型后训练中的强化学习过程**

**关键词**: `强化学习` `策略熵` `分布偏移` `大语言模型后训练` `稳定训练`

## 📋 核心要点

1. 核心问题：离策略训练导致分布偏移，引发策略熵波动和梯度不稳定
2. 方法要点：引入熵比作为全局度量，通过双向裁剪约束策略更新
3. 实验或效果：在多个基准测试中，ERC集成到DAPO和GPPO算法中均提升性能

## 📄 摘要（原文）

> Large language model post-training relies on reinforcement learning to improve model capability and alignment quality. However, the off-policy training paradigm introduces distribution shift, which often pushes the policy beyond the trust region, leading to training instabilities manifested as fluctuations in policy entropy and unstable gradients. Although PPO-Clip mitigates this issue through importance clipping, it still overlooks the global distributional shift of actions. To address these challenges, we propose using the entropy ratio between the current and previous policies as a new global metric that effectively quantifies the relative change in policy exploration throughout updates. Building on this metric, we introduce an \textbf{Entropy Ratio Clipping} (ERC) mechanism that imposes bidirectional constraints on the entropy ratio. This stabilizes policy updates at the global distribution level and compensates for the inability of PPO-clip to regulate probability shifts of un-sampled actions. We integrate ERC into both DAPO and GPPO reinforcement learning algorithms. Experiments across multiple benchmarks show that ERC consistently improves performance.

