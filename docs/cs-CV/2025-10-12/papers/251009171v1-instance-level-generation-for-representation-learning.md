---
layout: default
title: Instance-Level Generation for Representation Learning
---

# Instance-Level Generation for Representation Learning

**arXiv**: [2510.09171v1](https://arxiv.org/abs/2510.09171) | [PDF](https://arxiv.org/pdf/2510.09171.pdf)

**作者**: Yankun Wu, Zakaria Laskar, Giorgos Kordopatis-Zilos, Noa Garcia, Giorgos Tolias

---

## 💡 一句话要点

**提出实例级生成方法以解决细粒度识别数据稀缺问题**

**关键词**: `实例级识别` `数据合成` `表示学习` `图像检索` `多领域应用`

## 📋 核心要点

1. 实例级识别因细粒度特性导致大规模标注数据获取困难
2. 方法从多领域合成多样实例，不依赖真实图像进行训练
3. 在七个基准测试中显著提升检索性能，解锁广泛应用

## 📄 摘要（原文）

> Instance-level recognition (ILR) focuses on identifying individual objects
> rather than broad categories, offering the highest granularity in image
> classification. However, this fine-grained nature makes creating large-scale
> annotated datasets challenging, limiting ILR's real-world applicability across
> domains. To overcome this, we introduce a novel approach that synthetically
> generates diverse object instances from multiple domains under varied
> conditions and backgrounds, forming a large-scale training set. Unlike prior
> work on automatic data synthesis, our method is the first to address
> ILR-specific challenges without relying on any real images. Fine-tuning
> foundation vision models on the generated data significantly improves retrieval
> performance across seven ILR benchmarks spanning multiple domains. Our approach
> offers a new, efficient, and effective alternative to extensive data collection
> and curation, introducing a new ILR paradigm where the only input is the names
> of the target domains, unlocking a wide range of real-world applications.

