---
layout: default
title: Divide, Conquer and Unite: Hierarchical Style-Recalibrated Prototype Alignment for Federated Medical Image Segmentation
---

# Divide, Conquer and Unite: Hierarchical Style-Recalibrated Prototype Alignment for Federated Medical Image Segmentation

**arXiv**: [2511.10945v1](https://arxiv.org/abs/2511.10945) | [PDF](https://arxiv.org/pdf/2511.10945.pdf)

**作者**: Xingyue Zhao, Wenke Huang, Xingguang Wang, Haoyu Zhao, Linghao Zhuang, Anwen Jiang, Guancheng Wan, Mang Ye

---

## 💡 一句话要点

**提出FedBCS以解决联邦医学图像分割中的特征异构性问题**

**关键词**: `联邦学习` `医学图像分割` `原型对齐` `风格重校准` `特征异构性`

## 📋 核心要点

1. 核心问题：联邦学习中特征异构性导致分割性能下降，现有方法忽略多层级上下文和风格偏差累积。
2. 方法要点：引入频率域自适应风格重校准和上下文感知双层级原型对齐，构建域不变原型。
3. 实验或效果：在公开数据集上验证，方法表现出显著性能提升。

## 📄 摘要（原文）

> Federated learning enables multiple medical institutions to train a global model without sharing data, yet feature heterogeneity from diverse scanners or protocols remains a major challenge. Many existing works attempt to address this issue by leveraging model representations (e.g., mean feature vectors) to correct local training; however, they often face two key limitations: 1) Incomplete Contextual Representation Learning: Current approaches primarily focus on final-layer features, overlooking critical multi-level cues and thus diluting essential context for accurate segmentation. 2) Layerwise Style Bias Accumulation: Although utilizing representations can partially align global features, these methods neglect domain-specific biases within intermediate layers, allowing style discrepancies to build up and reduce model robustness. To address these challenges, we propose FedBCS to bridge feature representation gaps via domain-invariant contextual prototypes alignment. Specifically, we introduce a frequency-domain adaptive style recalibration into prototype construction that not only decouples content-style representations but also learns optimal style parameters, enabling more robust domain-invariant prototypes. Furthermore, we design a context-aware dual-level prototype alignment method that extracts domain-invariant prototypes from different layers of both encoder and decoder and fuses them with contextual information for finer-grained representation alignment. Extensive experiments on two public datasets demonstrate that our method exhibits remarkable performance.

