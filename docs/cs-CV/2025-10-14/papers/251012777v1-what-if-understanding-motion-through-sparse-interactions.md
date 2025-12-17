---
layout: default
title: What If : Understanding Motion Through Sparse Interactions
---

# What If : Understanding Motion Through Sparse Interactions

**arXiv**: [2510.12777v1](https://arxiv.org/abs/2510.12777) | [PDF](https://arxiv.org/pdf/2510.12777.pdf)

**作者**: Stefan Andreas Baumann, Nick Stracke, Timy Phan, Björn Ommer

---

## 💡 一句话要点

**提出Flow Poke Transformer以通过稀疏交互预测多模态场景运动分布**

**关键词**: `场景动态理解` `稀疏交互` `运动分布预测` `Transformer模型` `多模态预测`

## 📋 核心要点

1. 核心问题：理解物理场景动态变化，特别是基于局部稀疏交互的多模态运动预测。
2. 方法要点：使用Flow Poke Transformer直接预测局部运动分布，条件于稀疏poke交互。
3. 实验或效果：在密集人脸运动生成和关节物体运动估计等任务中超越基线方法。

## 📄 摘要（原文）

> Understanding the dynamics of a physical scene involves reasoning about the
> diverse ways it can potentially change, especially as a result of local
> interactions. We present the Flow Poke Transformer (FPT), a novel framework for
> directly predicting the distribution of local motion, conditioned on sparse
> interactions termed "pokes". Unlike traditional methods that typically only
> enable dense sampling of a single realization of scene dynamics, FPT provides
> an interpretable directly accessible representation of multi-modal scene
> motion, its dependency on physical interactions and the inherent uncertainties
> of scene dynamics. We also evaluate our model on several downstream tasks to
> enable comparisons with prior methods and highlight the flexibility of our
> approach. On dense face motion generation, our generic pre-trained model
> surpasses specialized baselines. FPT can be fine-tuned in strongly
> out-of-distribution tasks such as synthetic datasets to enable significant
> improvements over in-domain methods in articulated object motion estimation.
> Additionally, predicting explicit motion distributions directly enables our
> method to achieve competitive performance on tasks like moving part
> segmentation from pokes which further demonstrates the versatility of our FPT.
> Code and models are publicly available at
> https://compvis.github.io/flow-poke-transformer.

