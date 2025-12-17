---
layout: default
title: HCC-3D: Hierarchical Compensatory Compression for 98% 3D Token Reduction in Vision-Language Models
---

# HCC-3D: Hierarchical Compensatory Compression for 98% 3D Token Reduction in Vision-Language Models

**arXiv**: [2511.09883v1](https://arxiv.org/abs/2511.09883) | [PDF](https://arxiv.org/pdf/2511.09883.pdf)

**作者**: Liheng Zhang, Jin Wang, Hui Li, Bingfeng Zhang, Weifeng Liu

---

## 💡 一句话要点

**提出HCC-3D以压缩3D令牌，提升视觉语言模型效率与性能。**

**关键词**: `3D视觉语言模型` `令牌压缩` `计算效率优化` `点云处理` `分层补偿压缩`

## 📋 核心要点

1. 核心问题：3D-VLMs中3D令牌处理计算成本高，限制应用。
2. 方法要点：采用全局结构压缩和自适应细节挖掘，保留关键信息。
3. 实验或效果：实现约98%压缩比，性能达新SOTA，效率与性能双提升。

## 📄 摘要（原文）

> 3D understanding has drawn significant attention recently, leveraging Vision-Language Models (VLMs) to enable multi-modal reasoning between point cloud and text data. Current 3D-VLMs directly embed the 3D point clouds into 3D tokens, following large 2D-VLMs with powerful reasoning capabilities. However, this framework has a great computational cost limiting its application, where we identify that the bottleneck lies in processing all 3D tokens in the Large Language Model (LLM) part. This raises the question: how can we reduce the computational overhead introduced by 3D tokens while preserving the integrity of their essential information? To address this question, we introduce Hierarchical Compensatory Compression (HCC-3D) to efficiently compress 3D tokens while maintaining critical detail retention. Specifically, we first propose a global structure compression (GSC), in which we design global queries to compress all 3D tokens into a few key tokens while keeping overall structural information. Then, to compensate for the information loss in GSC, we further propose an adaptive detail mining (ADM) module that selectively recompresses salient but under-attended features through complementary scoring. Extensive experiments demonstrate that HCC-3D not only achieves extreme compression ratios (approximately 98%) compared to previous 3D-VLMs, but also achieves new state-of-the-art performance, showing the great improvements on both efficiency and performance.

