---
layout: default
title: Seeing the Whole Picture: Distribution-Guided Data-Free Distillation for Semantic Segmentation
---

# Seeing the Whole Picture: Distribution-Guided Data-Free Distillation for Semantic Segmentation

**arXiv**: [2512.13175v1](https://arxiv.org/abs/2512.13175) | [PDF](https://arxiv.org/pdf/2512.13175.pdf)

**作者**: Hongxuan Sun, Tao Wu

---

## 💡 一句话要点

**提出DFSS框架以解决数据无知识蒸馏在语义分割中忽视结构连续性的问题**

**关键词**: `语义分割` `数据无知识蒸馏` `分布引导` `渐进蒸馏` `BN统计`

## 📋 核心要点

1. 核心问题：现有数据无知识蒸馏方法直接用于语义分割时忽略场景结构连续性，导致性能下降
2. 方法要点：利用教师模型BN统计指导近似分布采样，并引入加权分布渐进蒸馏动态优化样本选择
3. 实验或效果：在标准基准测试中优于现有方法，实现先进结果且减少对辅助数据的依赖

## 📄 摘要（原文）

> Semantic segmentation requires a holistic understanding of the physical world, as it assigns semantic labels to spatially continuous and structurally coherent objects rather than to isolated pixels. However, existing data-free knowledge distillation (DFKD) methods-primarily designed for classification-often disregard this continuity, resulting in significant performance degradation when applied directly to segmentation tasks. In this paper, we introduce DFSS, a novel data-free distillation framework tailored for semantic segmentation. Unlike prior approaches that treat pixels independently, DFSS respects the structural and contextual continuity of real-world scenes. Our key insight is to leverage Batch Normalization (BN) statistics from a teacher model to guide Approximate Distribution Sampling (ADS), enabling the selection of data that better reflects the original training distribution-without relying on potentially misleading teacher predictions. Additionally, we propose Weighted Distribution Progressive Distillation (WDPD), which dynamically prioritizes reliable samples that are more closely aligned with the original data distribution early in training and gradually incorporates more challenging cases, mirroring the natural progression of learning in human perception. Extensive experiments on standard benchmarks demonstrate that DFSS consistently outperforms existing data-free distillation methods for semantic segmentation, achieving state-of-the-art results with significantly reduced reliance on auxiliary data.

