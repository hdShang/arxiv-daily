---
layout: default
title: FastHMR: Accelerating Human Mesh Recovery via Token and Layer Merging with Diffusion Decoding
---

# FastHMR: Accelerating Human Mesh Recovery via Token and Layer Merging with Diffusion Decoding

**arXiv**: [2510.10868v1](https://arxiv.org/abs/2510.10868) | [PDF](https://arxiv.org/pdf/2510.10868.pdf)

**作者**: Soroush Mehraban, Andrea Iaboni, Babak Taati

---

## 💡 一句话要点

**提出FastHMR方法，通过层与令牌合并及扩散解码加速3D人体网格恢复**

**关键词**: `3D人体网格恢复` `Transformer加速` `层合并` `令牌合并` `扩散解码` `计算效率`

## 📋 核心要点

1. 核心问题：基于Transformer的3D人体网格恢复模型计算成本高、复杂度大，存在冗余令牌和层
2. 方法要点：引入误差约束层合并和掩码引导令牌合并策略，结合扩散解码器利用时间上下文和姿态先验
3. 实验或效果：在多个基准测试中实现最高2.3倍加速，同时性能略有提升

## 📄 摘要（原文）

> Recent transformer-based models for 3D Human Mesh Recovery (HMR) have
> achieved strong performance but often suffer from high computational cost and
> complexity due to deep transformer architectures and redundant tokens. In this
> paper, we introduce two HMR-specific merging strategies: Error-Constrained
> Layer Merging (ECLM) and Mask-guided Token Merging (Mask-ToMe). ECLM
> selectively merges transformer layers that have minimal impact on the Mean Per
> Joint Position Error (MPJPE), while Mask-ToMe focuses on merging background
> tokens that contribute little to the final prediction. To further address the
> potential performance drop caused by merging, we propose a diffusion-based
> decoder that incorporates temporal context and leverages pose priors learned
> from large-scale motion capture datasets. Experiments across multiple
> benchmarks demonstrate that our method achieves up to 2.3x speed-up while
> slightly improving performance over the baseline.

