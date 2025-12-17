---
layout: default
title: Multi-Scale Correlation-Aware Transformer for Maritime Vessel Re-Identification
---

# Multi-Scale Correlation-Aware Transformer for Maritime Vessel Re-Identification

**arXiv**: [2511.14203v1](https://arxiv.org/abs/2511.14203) | [PDF](https://arxiv.org/pdf/2511.14203.pdf)

**作者**: Yunhe Liu

---

## 💡 一句话要点

**提出多尺度相关感知Transformer以解决船舶重识别中的异常样本问题**

**关键词**: `船舶重识别` `多尺度Transformer` `全局相关模块` `局部相关模块` `异常样本抑制` `特征相关性建模`

## 📋 核心要点

1. 核心问题：船舶图像存在较大类内变化和局部缺失，导致异常样本影响识别性能
2. 方法要点：通过全局和局部相关模块建模多尺度特征相关性，抑制异常样本影响
3. 实验或效果：在三个基准测试中达到最先进性能，验证方法有效性

## 📄 摘要（原文）

> Maritime vessel re-identification (Re-ID) plays a crucial role in advancing maritime monitoring and intelligent situational awareness systems. However, some existing vessel Re-ID methods are directly adapted from pedestrian-focused algorithms, making them ill-suited for mitigating the unique problems present in vessel images, particularly the greater intra-identity variations and more severe missing of local parts, which lead to the emergence of outlier samples within the same identity. To address these challenges, we propose the Multi-scale Correlation-aware Transformer Network (MCFormer), which explicitly models multi-scale correlations across the entire input set to suppress the adverse effects of outlier samples with intra-identity variations or local missing, incorporating two novel modules, the Global Correlation Module (GCM), and the Local Correlation Module (LCM). Specifically, GCM constructs a global similarity affinity matrix across all input images to model global correlations through feature aggregation based on inter-image consistency, rather than solely learning features from individual images as in most existing approaches. Simultaneously, LCM mines and aligns local features of positive samples with contextual similarity to extract local correlations by maintaining a dynamic memory bank, effectively compensating for missing or occluded regions in individual images. To further enhance feature robustness, MCFormer integrates global and local features that have been respectively correlated across multiple scales, effectively capturing latent relationships among image features. Experiments on three benchmarks demonstrate that MCFormer achieves state-of-the-art performance.

