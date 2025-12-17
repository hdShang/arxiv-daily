---
layout: default
title: Diffusion-Driven Progressive Target Manipulation for Source-Free Domain Adaptation
---

# Diffusion-Driven Progressive Target Manipulation for Source-Free Domain Adaptation

**arXiv**: [2510.25279v1](https://arxiv.org/abs/2510.25279) | [PDF](https://arxiv.org/pdf/2510.25279.pdf)

**作者**: Yuyang Huang, Yabo Chen, Junyu Zhou, Wenrui Dai, Xiaopeng Zhang, Junni Zou, Hongkai Xiong, Qi Tian

---

## 💡 一句话要点

**提出扩散驱动渐进目标操纵框架以解决源自由域适应中的大域差异问题**

**关键词**: `源自由域适应` `扩散模型` `伪标签生成` `渐进细化` `域差异减少`

## 📋 核心要点

1. 源自由域适应面临大域差异导致伪标签不可靠和生成方法性能下降的核心问题
2. 方法包括基于伪标签可靠性划分样本集、使用潜在扩散模型进行语义转换和渐进细化机制
3. 实验在四个基准数据集上实现SOTA性能，大域差异场景下性能提升高达18.6%

## 📄 摘要（原文）

> Source-free domain adaptation (SFDA) is a challenging task that tackles
> domain shifts using only a pre-trained source model and unlabeled target data.
> Existing SFDA methods are restricted by the fundamental limitation of
> source-target domain discrepancy. Non-generation SFDA methods suffer from
> unreliable pseudo-labels in challenging scenarios with large domain
> discrepancies, while generation-based SFDA methods are evidently degraded due
> to enlarged domain discrepancies in creating pseudo-source data. To address
> this limitation, we propose a novel generation-based framework named
> Diffusion-Driven Progressive Target Manipulation (DPTM) that leverages
> unlabeled target data as references to reliably generate and progressively
> refine a pseudo-target domain for SFDA. Specifically, we divide the target
> samples into a trust set and a non-trust set based on the reliability of
> pseudo-labels to sufficiently and reliably exploit their information. For
> samples from the non-trust set, we develop a manipulation strategy to
> semantically transform them into the newly assigned categories, while
> simultaneously maintaining them in the target distribution via a latent
> diffusion model. Furthermore, we design a progressive refinement mechanism that
> progressively reduces the domain discrepancy between the pseudo-target domain
> and the real target domain via iterative refinement. Experimental results
> demonstrate that DPTM outperforms existing methods by a large margin and
> achieves state-of-the-art performance on four prevailing SFDA benchmark
> datasets with different scales. Remarkably, DPTM can significantly enhance the
> performance by up to 18.6% in scenarios with large source-target gaps.

