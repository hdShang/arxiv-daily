---
layout: default
title: A Multi-Stage Optimization Framework for Deploying Learned Image Compression on FPGAs
---

# A Multi-Stage Optimization Framework for Deploying Learned Image Compression on FPGAs

**arXiv**: [2511.17135v1](https://arxiv.org/abs/2511.17135) | [PDF](https://arxiv.org/pdf/2511.17135.pdf)

**作者**: Jiaxun Fang, Li Chen

---

## 💡 一句话要点

**提出多阶段优化框架以在FPGA上高效部署学习型图像压缩模型**

**关键词**: `学习型图像压缩` `FPGA部署` `量化优化` `混合精度搜索` `通道剪枝` `硬件感知优化`

## 📋 核心要点

1. 核心问题：学习型图像压缩模型在FPGA部署时面临量化性能下降和资源限制挑战。
2. 方法要点：采用动态范围感知量化、混合精度搜索和通道剪枝优化硬件实现。
3. 实验或效果：量化方法将BD-rate开销从30%降至6.3%，优化后计算复杂度降低超20%。

## 📄 摘要（原文）

> Deep learning-based image compression (LIC) has achieved state-of-the-art rate-distortion (RD) performance, yet deploying these models on resource-constrained FPGAs remains a major challenge. This work presents a complete, multi-stage optimization framework to bridge the gap between high-performance floating-point models and efficient, hardware-friendly integer-based implementations. First, we address the fundamental problem of quantization-induced performance degradation. We propose a Dynamic Range-Aware Quantization (DRAQ) method that uses statistically-calibrated activation clipping and a novel weight regularization scheme to counteract the effects of extreme data outliers and large dynamic ranges, successfully creating a high-fidelity 8-bit integer model. Second, building on this robust foundation, we introduce two hardware-aware optimization techniques tailored for FPGAs. A progressive mixed-precision search algorithm exploits FPGA flexibility to assign optimal, non-uniform bit-widths to each layer, minimizing complexity while preserving performance. Concurrently, a channel pruning method, adapted to work with the Generalized Divisive Normalization (GDN) layers common in LIC, removes model redundancy by eliminating inactive channels. Our comprehensive experiments show that the foundational DRAQ method reduces the BD-rate overhead of a GDN-based model from $30\%$ to $6.3\%$. The subsequent hardware-aware optimizations further reduce computational complexity by over $20\%$ with negligible impact on RD performance, yielding a final model that is both state-of-the-art in efficiency and superior in quality to existing FPGA-based LIC implementations.

