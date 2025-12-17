---
layout: default
title: FreqGRL: Suppressing Low-Frequency Bias and Mining High-Frequency Knowledge for Cross-Domain Few-Shot Learning
---

# FreqGRL: Suppressing Low-Frequency Bias and Mining High-Frequency Knowledge for Cross-Domain Few-Shot Learning

**arXiv**: [2511.06648v1](https://arxiv.org/abs/2511.06648) | [PDF](https://arxiv.org/pdf/2511.06648.pdf)

**作者**: Siqi Hui, Sanping Zhou, Ye deng, Wenli Huang, Jinjun Wang

---

## 💡 一句话要点

**提出FreqGRL以解决跨域少样本学习中的频率偏差问题**

**关键词**: `跨域少样本学习` `频率空间分析` `表示学习优化` `数据不平衡处理` `高频特征增强`

## 📋 核心要点

1. 核心问题：数据不平衡导致模型偏向源域低频知识，目标域高频特征学习困难
2. 方法要点：通过低频替换和高频增强模块，在频率空间优化表示学习
3. 实验或效果：在五个标准基准上实现最先进性能，验证框架有效性

## 📄 摘要（原文）

> Cross-domain few-shot learning (CD-FSL) aims to recognize novel classes with
> only a few labeled examples under significant domain shifts. While recent
> approaches leverage a limited amount of labeled target-domain data to improve
> performance, the severe imbalance between abundant source data and scarce
> target data remains a critical challenge for effective representation learning.
> We present the first frequency-space perspective to analyze this issue and
> identify two key challenges: (1) models are easily biased toward
> source-specific knowledge encoded in the low-frequency components of source
> data, and (2) the sparsity of target data hinders the learning of
> high-frequency, domain-generalizable features. To address these challenges, we
> propose \textbf{FreqGRL}, a novel CD-FSL framework that mitigates the impact of
> data imbalance in the frequency space. Specifically, we introduce a
> Low-Frequency Replacement (LFR) module that substitutes the low-frequency
> components of source tasks with those from the target domain to create new
> source tasks that better align with target characteristics, thus reducing
> source-specific biases and promoting generalizable representation learning. We
> further design a High-Frequency Enhancement (HFE) module that filters out
> low-frequency components and performs learning directly on high-frequency
> features in the frequency space to improve cross-domain generalization.
> Additionally, a Global Frequency Filter (GFF) is incorporated to suppress noisy
> or irrelevant frequencies and emphasize informative ones, mitigating
> overfitting risks under limited target supervision. Extensive experiments on
> five standard CD-FSL benchmarks demonstrate that our frequency-guided framework
> achieves state-of-the-art performance.

