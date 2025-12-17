---
layout: default
title: Generation is Required for Data-Efficient Perception
---

# Generation is Required for Data-Efficient Perception

**arXiv**: [2512.08854v1](https://arxiv.org/abs/2512.08854) | [PDF](https://arxiv.org/pdf/2512.08854.pdf)

**作者**: Jack Brady, Bernhard Schölkopf, Thomas Kipf, Simon Buchholz, Wieland Brendel

---

## 💡 一句话要点

**提出生成方法通过解码器归纳偏置实现组合泛化，解决数据高效感知问题**

**关键词**: `组合泛化` `生成模型` `视觉感知` `归纳偏置` `数据高效学习`

## 📋 核心要点

1. 核心问题：生成与非生成方法在组合泛化能力上的差异，以评估人类级视觉感知的必要性
2. 方法要点：理论分析解码器与编码器的归纳偏置，生成方法通过解码器约束和反转实现组合泛化
3. 实验或效果：生成方法在真实图像数据集上显著提升组合泛化，无需额外数据或监督

## 📄 摘要（原文）

> It has been hypothesized that human-level visual perception requires a generative approach in which internal representations result from inverting a decoder. Yet today's most successful vision models are non-generative, relying on an encoder that maps images to representations without decoder inversion. This raises the question of whether generation is, in fact, necessary for machines to achieve human-level visual perception. To address this, we study whether generative and non-generative methods can achieve compositional generalization, a hallmark of human perception. Under a compositional data generating process, we formalize the inductive biases required to guarantee compositional generalization in decoder-based (generative) and encoder-based (non-generative) methods. We then show theoretically that enforcing these inductive biases on encoders is generally infeasible using regularization or architectural constraints. In contrast, for generative methods, the inductive biases can be enforced straightforwardly, thereby enabling compositional generalization by constraining a decoder and inverting it. We highlight how this inversion can be performed efficiently, either online through gradient-based search or offline through generative replay. We examine the empirical implications of our theory by training a range of generative and non-generative methods on photorealistic image datasets. We find that, without the necessary inductive biases, non-generative methods often fail to generalize compositionally and require large-scale pretraining or added supervision to improve generalization. By comparison, generative methods yield significant improvements in compositional generalization, without requiring additional data, by leveraging suitable inductive biases on a decoder along with search and replay.

