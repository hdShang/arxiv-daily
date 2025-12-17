---
layout: default
title: Much Ado About Noising: Dispelling the Myths of Generative Robotic Control
---

# Much Ado About Noising: Dispelling the Myths of Generative Robotic Control

**arXiv**: [2512.01809v1](https://arxiv.org/abs/2512.01809) | [PDF](https://arxiv.org/pdf/2512.01809.pdf)

**作者**: Chaoyi Pan, Giri Anantharaman, Nai-Chieh Huang, Claire Jin, Daniel Pfrommer, Chenyang Yuan, Frank Permenter, Guannan Qu, Nicholas Boffi, Guanya Shi, Max Simchowitz

---

## 💡 一句话要点

**揭示生成式机器人控制成功源于迭代计算而非多模态建模，提出最小迭代策略匹配性能**

**关键词**: `生成式机器人控制` `行为克隆` `迭代计算` `策略蒸馏` `随机性监督` `控制性能优化`

## 📋 核心要点

1. 核心问题：生成式控制策略成功因素被误认为多模态建模或复杂映射能力
2. 方法要点：通过全面评估发现优势源于训练中监督的迭代计算与适当随机性
3. 实验或效果：最小迭代策略在行为克隆基准上匹配流模型性能，常优于蒸馏模型

## 📄 摘要（原文）

> Generative models, like flows and diffusions, have recently emerged as popular and efficacious policy parameterizations in robotics. There has been much speculation as to the factors underlying their successes, ranging from capturing multi-modal action distribution to expressing more complex behaviors. In this work, we perform a comprehensive evaluation of popular generative control policies (GCPs) on common behavior cloning (BC) benchmarks. We find that GCPs do not owe their success to their ability to capture multi-modality or to express more complex observation-to-action mappings. Instead, we find that their advantage stems from iterative computation, as long as intermediate steps are supervised during training and this supervision is paired with a suitable level of stochasticity. As a validation of our findings, we show that a minimum iterative policy (MIP), a lightweight two-step regression-based policy, essentially matches the performance of flow GCPs, and often outperforms distilled shortcut models. Our results suggest that the distribution-fitting component of GCPs is less salient than commonly believed, and point toward new design spaces focusing solely on control performance. Project page: https://simchowitzlabpublic.github.io/much-ado-about-noising-project/

