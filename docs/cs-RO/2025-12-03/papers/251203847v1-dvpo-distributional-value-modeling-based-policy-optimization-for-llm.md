---
layout: default
title: DVPO: Distributional Value Modeling-based Policy Optimization for LLM Post-Training
---

# DVPO: Distributional Value Modeling-based Policy Optimization for LLM Post-Training

**arXiv**: [2512.03847v1](https://arxiv.org/abs/2512.03847) | [PDF](https://arxiv.org/pdf/2512.03847.pdf)

**作者**: Dingwei Zhu, Zhiheng Xi, Shihan Dou, Yuhui Wang, Sixian Li, Junjie Ye, Honglin Guo, Shichun Liu, Chenhao Huang, Yajie Yang, Junlin Shang, Senjie Jin, Ming Zhang, Jiazheng Zhang, Caishuang Huang, Yunke Zhang, Demei Yan, Yuran Wang, Tao Gui

---

## 💡 一句话要点

**提出DVPO框架，结合条件风险理论与分布价值建模，以在噪声监督下优化LLM后训练。**

**关键词**: `强化学习` `大语言模型后训练` `分布价值建模` `风险正则化` `噪声监督` `泛化优化`

## 📋 核心要点

1. 核心问题：真实世界LLM后训练中，噪声或不完整监督信号导致训练不稳定和泛化能力下降。
2. 方法要点：学习令牌级价值分布，应用非对称风险正则化，收缩下尾抑制噪声，扩展上尾保持探索多样性。
3. 实验或效果：在多轮对话、数学推理和科学QA任务中，DVPO在噪声监督下优于PPO、GRPO和基于鲁棒贝尔曼的PPO。

## 📄 摘要（原文）

> Reinforcement learning (RL) has shown strong performance in LLM post-training, but real-world deployment often involves noisy or incomplete supervision. In such settings, complex and unreliable supervision signals can destabilize training and harm generalization. While existing approaches such as worst-case optimization (e.g., RFQI, CQL) and mean-based methods (e.g., PPO, GRPO) can improve stability, they often overlook generalization and may produce overly conservative policies, leading to uneven performance across diverse real scenarios. To this end, we introduce DVPO (Distributional Value Modeling with Risk-aware Policy Optimization), a new RL framework that combines conditional risk theory with distributional value modeling to better balance robustness and generalization. DVPO learns token-level value distributions to provide fine-grained supervision, and applies an asymmetric risk regularization to shape the distribution tails: it contracts the lower tail to dampen noisy negative deviations, while expanding the upper tail to preserve exploratory diversity. Across extensive experiments and analysis in multi-turn dialogue, math reasoning, and scientific QA, DVPO consistently outperforms PPO, GRPO, and robust Bellman-based PPO under noisy supervision, showing its potential for LLM post-training in the real-world.

