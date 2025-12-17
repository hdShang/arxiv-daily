---
layout: default
title: Why Prototypes Collapse: Diagnosing and Preventing Partial Collapse in Prototypical Self-Supervised Learning
---

# Why Prototypes Collapse: Diagnosing and Preventing Partial Collapse in Prototypical Self-Supervised Learning

**arXiv**: [2510.20108v1](https://arxiv.org/abs/2510.20108) | [PDF](https://arxiv.org/pdf/2510.20108.pdf)

**作者**: Gabriel Y. Arteaga, Marius Aasan, Rwiddhi Chakraborty, Martine Hjelkrem-Tan, Thalles Silva, Michael Kampffmeyer, Adín Ramírez Rivera

---

## 💡 一句话要点

**提出解耦训练策略以解决原型自监督学习中的部分原型坍缩问题**

**关键词**: `原型自监督学习` `原型坍缩` `解耦训练` `高斯混合模型` `在线EM算法` `表示学习`

## 📋 核心要点

1. 核心问题：原型自监督学习中多个原型收敛到相似表示，削弱表示多样性
2. 方法要点：采用解耦训练，原型通过在线EM更新，独立于编码器优化
3. 实验或效果：消除原型坍缩，提升原型多样性和下游任务性能

## 📄 摘要（原文）

> Prototypical self-supervised learning methods consistently suffer from
> partial prototype collapse, where multiple prototypes converge to nearly
> identical representations. This undermines their central purpose -- providing
> diverse and informative targets to guide encoders toward rich representations
> -- and has led practitioners to over-parameterize prototype sets or add ad-hoc
> regularizers, which mitigate symptoms rather than address the root cause. We
> empirically trace the collapse to the joint optimization of encoders and
> prototypes, which encourages a type of shortcut learning: early in training
> prototypes drift toward redundant representations that minimize loss without
> necessarily enhancing representation diversity. To break the joint
> optimization, we introduce a fully decoupled training strategy that learns
> prototypes and encoders under separate objectives. Concretely, we model
> prototypes as a Gaussian mixture updated with an online EM-style procedure,
> independent of the encoder's loss. This simple yet principled decoupling
> eliminates prototype collapse without explicit regularization and yields
> consistently diverse prototypes and stronger downstream performance.

