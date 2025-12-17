---
layout: default
title: In-context Inverse Optimality for Fair Digital Twins: A Preference-based approach
---

# In-context Inverse Optimality for Fair Digital Twins: A Preference-based approach

**arXiv**: [2512.01650v1](https://arxiv.org/abs/2512.01650) | [PDF](https://arxiv.org/pdf/2512.01650.pdf)

**作者**: Daniele Masti, Francesco Basciani, Arianna Fedeli, Girgio Gnecco, Francesco Smarra

---

## 💡 一句话要点

**提出基于偏好的公平数字孪生框架，通过上下文学习隐式公平目标以解决决策与人类期望的差距。**

**关键词**: `数字孪生` `公平性学习` `偏好驱动优化` `上下文学习` `资源分配` `孪生神经网络`

## 📋 核心要点

1. 核心问题：数字孪生最优决策与人类期望存在差距，需嵌入人类感知的公平性。
2. 方法要点：开发孪生神经网络，从人类成对偏好推断上下文相关的凸二次成本函数作为公平目标。
3. 实验或效果：在COVID-19医院资源分配场景中验证，优化结果与人类公平感知对齐且计算高效。

## 📄 摘要（原文）

> Digital Twins (DTs) are increasingly used as autonomous decision-makers in complex socio-technical systems. Their mathematically optimal decisions often diverge from human expectations, exposing a persistent gap between algorithmic and bounded human rationality. This work addresses this gap by proposing a framework that operationalizes fairness as a learnable objective within optimization-based Digital Twins. We introduce a preference-driven learning pipeline that infers latent fairness objectives directly from human pairwise preferences over feasible decisions. A novel Siamese neural network is developed to generate convex quadratic cost functions conditioned on contextual information. The resulting surrogate objectives align optimization outcomes with human-perceived fairness while maintaining computational efficiency. The approach is demonstrated on a COVID-19 hospital resource allocation scenario. This study provides an actionable path toward embedding human-centered fairness in the design of autonomous decision-making systems.

