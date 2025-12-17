---
layout: default
title: On the Bayes Inconsistency of Disagreement Discrepancy Surrogates
---

# On the Bayes Inconsistency of Disagreement Discrepancy Surrogates

**arXiv**: [2512.05931v1](https://arxiv.org/abs/2512.05931) | [PDF](https://arxiv.org/pdf/2512.05931.pdf)

**作者**: Neil G. Marchant, Andrew C. Cullen, Feng Liu, Sarah M. Erfani

---

## 💡 一句话要点

**提出贝叶斯一致的分歧差异代理损失，以解决分布偏移下深度神经网络失效问题。**

**关键词**: `分布偏移` `分歧差异` `贝叶斯一致性` `代理损失` `深度神经网络` `鲁棒性`

## 📋 核心要点

1. 核心问题：现有分歧差异代理损失非贝叶斯一致，最大化代理可能无法最大化真实分歧差异。
2. 方法要点：引入新理论界，提出结合交叉熵的贝叶斯一致分歧损失作为代理。
3. 实验或效果：在多样基准测试中，新方法提供更准确和鲁棒的分歧差异估计，尤其在对抗条件下。

## 📄 摘要（原文）

> Deep neural networks often fail when deployed in real-world contexts due to distribution shift, a critical barrier to building safe and reliable systems. An emerging approach to address this problem relies on \emph{disagreement discrepancy} -- a measure of how the disagreement between two models changes under a shifting distribution. The process of maximizing this measure has seen applications in bounding error under shifts, testing for harmful shifts, and training more robust models. However, this optimization involves the non-differentiable zero-one loss, necessitating the use of practical surrogate losses. We prove that existing surrogates for disagreement discrepancy are not Bayes consistent, revealing a fundamental flaw: maximizing these surrogates can fail to maximize the true disagreement discrepancy. To address this, we introduce new theoretical results providing both upper and lower bounds on the optimality gap for such surrogates. Guided by this theory, we propose a novel disagreement loss that, when paired with cross-entropy, yields a provably consistent surrogate for disagreement discrepancy. Empirical evaluations across diverse benchmarks demonstrate that our method provides more accurate and robust estimates of disagreement discrepancy than existing approaches, particularly under challenging adversarial conditions.

