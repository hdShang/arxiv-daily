---
layout: default
title: LiteVGGT: Boosting Vanilla VGGT via Geometry-aware Cached Token Merging
---

# LiteVGGT: Boosting Vanilla VGGT via Geometry-aware Cached Token Merging

**arXiv**: [2512.04939v1](https://arxiv.org/abs/2512.04939) | [PDF](https://arxiv.org/pdf/2512.04939.pdf)

**作者**: Zhijian Shu, Cheng Lin, Tao Xie, Wei Yin, Ben Li, Zhiyuan Pu, Weize Li, Yao Yao, Xun Cao, Xiaoyang Guo, Xiao-Xiao Long

---

## 💡 一句话要点

**提出LiteVGGT通过几何感知缓存令牌合并，加速VGGT处理大规模3D场景。**

**关键词**: `3D视觉基础模型` `令牌合并` `几何感知优化` `计算效率提升` `大规模场景处理`

## 📋 核心要点

1. 核心问题：VGGT处理长序列时计算和内存开销大，限制大规模场景应用。
2. 方法要点：基于几何相关性和层间稳定性，设计令牌合并策略，优化锚令牌选择和缓存复用。
3. 实验或效果：实现最高10倍加速和内存减少，支持1000图像场景，保持核心性能。

## 📄 摘要（原文）

> 3D vision foundation models like Visual Geometry Grounded Transformer (VGGT) have advanced greatly in geometric perception. However, it is time-consuming and memory-intensive for long sequences, limiting application to large-scale scenes beyond hundreds of images. To address this, we propose LiteVGGT, achieving up to 10x speedup and substantial memory reduction, enabling efficient processing of 1000-image scenes. We derive two key insights for 3D reconstruction: (1) tokens from local image regions have inherent geometric correlations, leading to high similarity and computational redundancy; (2) token similarity across adjacent network layers remains stable, allowing for reusable merge decisions. Guided by these, we design a simple yet efficient strategy, dubbed geometry-aware cached token merging. We analyze each token's geometric importance, optimizing anchor token selection to better preserve key information for reconstruction. We also cache and reuse merge indices across layers, substantially reducing latency with minimal accuracy impact. This strategy retains VGGT's core performance, enabling efficient fine-tuning and FP8 quantization for further gains. Extensive experiments validate LiteVGGT's effectiveness, scalability, and robustness. Project page: https://garlicba.github.io/LiteVGGT/

