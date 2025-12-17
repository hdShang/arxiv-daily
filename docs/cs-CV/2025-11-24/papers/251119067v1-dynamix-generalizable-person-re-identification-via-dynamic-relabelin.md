---
layout: default
title: DynaMix: Generalizable Person Re-identification via Dynamic Relabeling and Mixed Data Sampling
---

# DynaMix: Generalizable Person Re-identification via Dynamic Relabeling and Mixed Data Sampling

**arXiv**: [2511.19067v1](https://arxiv.org/abs/2511.19067) | [PDF](https://arxiv.org/pdf/2511.19067.pdf)

**作者**: Timur Mamedov, Anton Konushin, Vadim Konushin

---

## 💡 一句话要点

**提出DynaMix方法，结合多相机标注和单相机伪标注数据，提升行人重识别泛化能力**

**关键词**: `行人重识别` `泛化学习` `伪标签优化` `数据采样` `身份表示学习`

## 📋 核心要点

1. 核心问题：行人重识别在未见相机和环境下的泛化能力不足，依赖有限多相机标注数据
2. 方法要点：动态重标伪标签、高效质心模块和混合数据采样，适应数据结构和噪声
3. 实验或效果：在广泛实验中，DynaMix一致优于现有最先进方法

## 📄 摘要（原文）

> Generalizable person re-identification (Re-ID) aims to recognize individuals across unseen cameras and environments. While existing methods rely heavily on limited labeled multi-camera data, we propose DynaMix, a novel method that effectively combines manually labeled multi-camera and large-scale pseudo-labeled single-camera data. Unlike prior works, DynaMix dynamically adapts to the structure and noise of the training data through three core components: (1) a Relabeling Module that refines pseudo-labels of single-camera identities on-the-fly; (2) an Efficient Centroids Module that maintains robust identity representations under a large identity space; and (3) a Data Sampling Module that carefully composes mixed data mini-batches to balance learning complexity and intra-batch diversity. All components are specifically designed to operate efficiently at scale, enabling effective training on millions of images and hundreds of thousands of identities. Extensive experiments demonstrate that DynaMix consistently outperforms state-of-the-art methods in generalizable person Re-ID.

