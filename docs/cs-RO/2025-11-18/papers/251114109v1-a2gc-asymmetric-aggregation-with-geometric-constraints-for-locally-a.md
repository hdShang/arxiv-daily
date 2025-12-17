---
layout: default
title: $A^2$GC: $A$symmetric $A$ggregation with Geometric Constraints for Locally Aggregated Descriptors
---

# $A^2$GC: $A$symmetric $A$ggregation with Geometric Constraints for Locally Aggregated Descriptors

**arXiv**: [2511.14109v1](https://arxiv.org/abs/2511.14109) | [PDF](https://arxiv.org/pdf/2511.14109.pdf)

**作者**: Zhenyu Li, Tianyi Shang

---

## 💡 一句话要点

**提出A²GC-VPR方法以解决视觉地点识别中特征分布不对称问题**

**关键词**: `视觉地点识别` `不对称聚合` `几何约束` `最优传输` `局部聚合描述符` `特征匹配`

## 📋 核心要点

1. 核心问题：标准Sinkhorn算法对称处理特征与聚类分布，限制不对称分布下的匹配效果。
2. 方法要点：采用行列归一化平均与独立边际校准，实现不对称聚合和几何约束融合。
3. 实验或效果：在MSLS等数据集上验证了匹配精度和鲁棒性的提升。

## 📄 摘要（原文）

> Visual Place Recognition (VPR) aims to match query images against a database using visual cues. State-of-the-art methods aggregate features from deep backbones to form global descriptors. Optimal transport-based aggregation methods reformulate feature-to-cluster assignment as a transport problem, but the standard Sinkhorn algorithm symmetrically treats source and target marginals, limiting effectiveness when image features and cluster centers exhibit substantially different distributions. We propose an asymmetric aggregation VPR method with geometric constraints for locally aggregated descriptors, called $A^2$GC-VPR. Our method employs row-column normalization averaging with separate marginal calibration, enabling asymmetric matching that adapts to distributional discrepancies in visual place recognition. Geometric constraints are incorporated through learnable coordinate embeddings, computing compatibility scores fused with feature similarities, thereby promoting spatially proximal features to the same cluster and enhancing spatial awareness. Experimental results on MSLS, NordLand, and Pittsburgh datasets demonstrate superior performance, validating the effectiveness of our approach in improving matching accuracy and robustness.

