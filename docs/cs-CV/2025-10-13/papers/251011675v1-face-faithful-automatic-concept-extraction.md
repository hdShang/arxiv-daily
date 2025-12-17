---
layout: default
title: FACE: Faithful Automatic Concept Extraction
---

# FACE: Faithful Automatic Concept Extraction

**arXiv**: [2510.11675v1](https://arxiv.org/abs/2510.11675) | [PDF](https://arxiv.org/pdf/2510.11675.pdf)

**作者**: Dipkamal Bhusal, Michael Clifford, Sara Rampazzi, Nidhi Rastogi

---

## 💡 一句话要点

**提出FACE框架以解决自动概念提取中解释忠实性问题**

**关键词**: `概念提取` `解释忠实性` `非负矩阵分解` `KL散度正则化` `深度学习解释`

## 📋 核心要点

1. 现有自动概念发现方法常与模型决策过程不一致，影响解释忠实性。
2. FACE结合NMF与KL散度正则化，确保概念预测与原预测对齐。
3. 在ImageNet等数据集上评估，FACE在忠实性和稀疏性上优于现有方法。

## 📄 摘要（原文）

> Interpreting deep neural networks through concept-based explanations offers a
> bridge between low-level features and high-level human-understandable
> semantics. However, existing automatic concept discovery methods often fail to
> align these extracted concepts with the model's true decision-making process,
> thereby compromising explanation faithfulness. In this work, we propose FACE
> (Faithful Automatic Concept Extraction), a novel framework that augments
> Non-negative Matrix Factorization (NMF) with a Kullback-Leibler (KL) divergence
> regularization term to ensure alignment between the model's original and
> concept-based predictions. Unlike prior methods that operate solely on encoder
> activations, FACE incorporates classifier supervision during concept learning,
> enforcing predictive consistency and enabling faithful explanations. We provide
> theoretical guarantees showing that minimizing the KL divergence bounds the
> deviation in predictive distributions, thereby promoting faithful local
> linearity in the learned concept space. Systematic evaluations on ImageNet,
> COCO, and CelebA datasets demonstrate that FACE outperforms existing methods
> across faithfulness and sparsity metrics.

