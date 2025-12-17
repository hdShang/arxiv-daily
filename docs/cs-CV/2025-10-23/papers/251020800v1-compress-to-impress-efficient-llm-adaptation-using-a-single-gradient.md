---
layout: default
title: Compress to Impress: Efficient LLM Adaptation Using a Single Gradient Step on 100 Samples
---

# Compress to Impress: Efficient LLM Adaptation Using a Single Gradient Step on 100 Samples

**arXiv**: [2510.20800v1](https://arxiv.org/abs/2510.20800) | [PDF](https://arxiv.org/pdf/2510.20800.pdf)

**作者**: Shiva Sreeram, Alaa Maalouf, Pratyusha Sharma, Daniela Rus

---

## 💡 一句话要点

**提出高效LLM适应方法，使用单步梯度和100样本提升下游任务性能**

**关键词**: `LLM适应` `梯度分析` `矩阵分解` `样本效率` `下游任务优化`

## 📋 核心要点

1. 核心问题：LASER方法层间搜索开销大，难以快速部署LLM适应。
2. 方法要点：通过梯度分析选择关键矩阵，扩展分解空间减少过拟合。
3. 实验或效果：在100样本上实现快速适应，准确率提升高达24.6个百分点。

## 📄 摘要（原文）

> Recently, Sharma et al. suggested a method called Layer-SElective-Rank
> reduction (LASER) which demonstrated that pruning high-order components of
> carefully chosen LLM's weight matrices can boost downstream accuracy -- without
> any gradient-based fine-tuning. Yet LASER's exhaustive, per-matrix search (each
> requiring full-dataset forward passes) makes it impractical for rapid
> deployment. We demonstrate that this overhead can be removed and find that: (i)
> Only a small, carefully chosen subset of matrices needs to be inspected --
> eliminating the layer-by-layer sweep, (ii) The gradient of each matrix's
> singular values pinpoints which matrices merit reduction, (iii) Increasing the
> factorization search space by allowing matrices rows to cluster around multiple
> subspaces and then decomposing each cluster separately further reduces
> overfitting on the original training data and further lifts accuracy by up to
> 24.6 percentage points, and finally, (iv) we discover that evaluating on just
> 100 samples rather than the full training data -- both for computing the
> indicative gradients and for measuring the final accuracy -- suffices to
> further reduce the search time; we explain that as adaptation to downstream
> tasks is dominated by prompting style, not dataset size. As a result, we show
> that combining these findings yields a fast and robust adaptation algorithm for
> downstream tasks. Overall, with a single gradient step on 100 examples and a
> quick scan of the top candidate layers and factorization techniques, we can
> adapt LLMs to new datasets -- entirely without fine-tuning.

