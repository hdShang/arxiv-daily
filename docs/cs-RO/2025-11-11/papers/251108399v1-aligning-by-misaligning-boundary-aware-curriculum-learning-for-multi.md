---
layout: default
title: Aligning by Misaligning: Boundary-aware Curriculum Learning for Multimodal Alignment
---

# Aligning by Misaligning: Boundary-aware Curriculum Learning for Multimodal Alignment

**arXiv**: [2511.08399v1](https://arxiv.org/abs/2511.08399) | [PDF](https://arxiv.org/pdf/2511.08399.pdf)

**作者**: Hua Ye, Hang Ding, Siyuan Chen, Yiyang Jiang, Changyuan Zhang, Xuan Zhang

---

## 💡 一句话要点

**提出边界感知课程学习以改进多模态对齐，通过边界负采样和局部注意力损失提升性能。**

**关键词**: `多模态对齐` `课程学习` `边界感知` `对比学习` `负采样` `局部注意力`

## 📋 核心要点

1. 核心问题：多模态模型忽略模糊负样本，导致对齐不精确。
2. 方法要点：使用边界感知负采样器和对比局部注意力损失，构建课程学习信号。
3. 实验或效果：在四个基准测试中实现SOTA，召回率提升高达32%。

## 📄 摘要（原文）

> Most multimodal models treat every negative pair alike, ignoring the ambiguous negatives that differ from the positive by only a small detail. We propose Boundary-Aware Curriculum with Local Attention (BACL), a lightweight add-on that turns these borderline cases into a curriculum signal. A Boundary-aware Negative Sampler gradually raises difficulty, while a Contrastive Local Attention loss highlights where the mismatch occurs. The two modules are fully differentiable and work with any off-the-shelf dual encoder. Theory predicts a fast O(1/n) error rate; practice shows up to +32% R@1 over CLIP and new SOTA on four large-scale benchmarks, all without extra labels.

