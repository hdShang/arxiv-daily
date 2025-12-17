---
layout: default
title: ClusterMine: Robust Label-Free Visual Out-Of-Distribution Detection via Concept Mining from Text Corpora
---

# ClusterMine: Robust Label-Free Visual Out-Of-Distribution Detection via Concept Mining from Text Corpora

**arXiv**: [2511.07068v1](https://arxiv.org/abs/2511.07068) | [PDF](https://arxiv.org/pdf/2511.07068.pdf)

**作者**: Nikolas Adaloglou, Diana Petrusheva, Mohamed Asker, Felix Michels, Markus Kollmann

---

## 💡 一句话要点

**提出ClusterMine方法，通过文本语料库挖掘概念实现无标签视觉分布外检测**

**关键词**: `视觉分布外检测` `概念挖掘` `零样本学习` `CLIP模型` `无监督学习`

## 📋 核心要点

1. 核心问题：现有视觉分布外检测依赖预定义标签，难以应对标签缺失或分布偏移
2. 方法要点：结合视觉聚类和零样本图文一致性，从文本语料库自动挖掘正概念
3. 实验或效果：在多种CLIP模型上实现SOTA性能，对分布偏移具有强鲁棒性

## 📄 摘要（原文）

> Large-scale visual out-of-distribution (OOD) detection has witnessed
> remarkable progress by leveraging vision-language models such as CLIP. However,
> a significant limitation of current methods is their reliance on a pre-defined
> set of in-distribution (ID) ground-truth label names (positives). These fixed
> label names can be unavailable, unreliable at scale, or become less relevant
> due to in-distribution shifts after deployment. Towards truly unsupervised OOD
> detection, we utilize widely available text corpora for positive label mining,
> bypassing the need for positives. In this paper, we utilize widely available
> text corpora for positive label mining under a general concept mining paradigm.
> Within this framework, we propose ClusterMine, a novel positive label mining
> method. ClusterMine is the first method to achieve state-of-the-art OOD
> detection performance without access to positive labels. It extracts positive
> concepts from a large text corpus by combining visual-only sample consistency
> (via clustering) and zero-shot image-text consistency. Our experimental study
> reveals that ClusterMine is scalable across a plethora of CLIP models and
> achieves state-of-the-art robustness to covariate in-distribution shifts. The
> code is available at https://github.com/HHU-MMBS/clustermine_wacv_official.

