---
layout: default
title: Translating Informal Proofs into Formal Proofs Using a Chain of States
---

# Translating Informal Proofs into Formal Proofs Using a Chain of States

**arXiv**: [2512.10317v1](https://arxiv.org/abs/2512.10317) | [PDF](https://arxiv.org/pdf/2512.10317.pdf)

**作者**: Ziyu Wang, Bowen Yang, Shihao Zhou, Chenyi Li, Yuan Zhang, Bin Dong, Zaiwen Wen

---

## 💡 一句话要点

**提出基于状态链的两阶段框架，将非正式数学证明转换为Lean4形式化证明**

**关键词**: `形式化证明` `数学证明转换` `状态链` `Lean4` `策略生成` `自然语言处理`

## 📋 核心要点

1. 核心问题：在有限计算预算下，将自然语言非正式数学证明转换为Lean4形式化证明。
2. 方法要点：先提取状态链作为中间表示，再生成连接状态的策略，降低策略生成复杂度。
3. 实验或效果：构建专用数据集和基准，实证显示方法显著优于现有基线，提高证明成功率。

## 📄 摘要（原文）

> We address the problem of translating informal mathematical proofs expressed in natural language into formal proofs in Lean4 under a constrained computational budget. Our approach is grounded in two key insights. First, informal proofs tend to proceed via a sequence of logical transitions - often implications or equivalences - without explicitly specifying intermediate results or auxiliary lemmas. In contrast, formal systems like Lean require an explicit representation of each proof state and the tactics that connect them. Second, each informal reasoning step can be viewed as an abstract transformation between proof states, but identifying the corresponding formal tactics often requires nontrivial domain knowledge and precise control over proof context. To bridge this gap, we propose a two stage framework. Rather than generating formal tactics directly, we first extract a Chain of States (CoS), a sequence of intermediate formal proof states aligned with the logical structure of the informal argument. We then generate tactics to transition between adjacent states in the CoS, thereby constructing the full formal proof. This intermediate representation significantly reduces the complexity of tactic generation and improves alignment with informal reasoning patterns. We build dedicated datasets and benchmarks for training and evaluation, and introduce an interactive framework to support tactic generation from formal states. Empirical results show that our method substantially outperforms existing baselines, achieving higher proof success rates.

