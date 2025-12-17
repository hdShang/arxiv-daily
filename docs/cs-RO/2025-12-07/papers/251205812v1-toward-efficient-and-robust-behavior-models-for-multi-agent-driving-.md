---
layout: default
title: Toward Efficient and Robust Behavior Models for Multi-Agent Driving Simulation
---

# Toward Efficient and Robust Behavior Models for Multi-Agent Driving Simulation

**arXiv**: [2512.05812v1](https://arxiv.org/abs/2512.05812) | [PDF](https://arxiv.org/pdf/2512.05812.pdf)

**作者**: Fabian Konstantinidis, Moritz Sackmann, Ulrich Hofmann, Christoph Stiller

---

## 💡 一句话要点

**提出基于实例中心表示与对抗逆强化学习的高效鲁棒多智能体驾驶行为模型**

**关键词**: `多智能体驾驶模拟` `实例中心表示` `对抗逆强化学习` `自适应奖励变换` `查询中心编码器` `高效场景编码`

## 📋 核心要点

1. 核心问题：多智能体驾驶模拟需平衡行为模型的真实性与计算效率。
2. 方法要点：采用实例中心场景表示和查询中心对称编码器，结合自适应奖励变换优化训练。
3. 实验效果：模型在位置精度和鲁棒性上优于基线，且训练和推理时间随令牌数高效扩展。

## 📄 摘要（原文）

> Scalable multi-agent driving simulation requires behavior models that are both realistic and computationally efficient. We address this by optimizing the behavior model that controls individual traffic participants. To improve efficiency, we adopt an instance-centric scene representation, where each traffic participant and map element is modeled in its own local coordinate frame. This design enables efficient, viewpoint-invariant scene encoding and allows static map tokens to be reused across simulation steps. To model interactions, we employ a query-centric symmetric context encoder with relative positional encodings between local frames. We use Adversarial Inverse Reinforcement Learning to learn the behavior model and propose an adaptive reward transformation that automatically balances robustness and realism during training. Experiments demonstrate that our approach scales efficiently with the number of tokens, significantly reducing training and inference times, while outperforming several agent-centric baselines in terms of positional accuracy and robustness.

