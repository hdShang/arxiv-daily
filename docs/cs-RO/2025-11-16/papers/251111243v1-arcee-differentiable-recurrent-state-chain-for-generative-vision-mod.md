---
layout: default
title: Arcee: Differentiable Recurrent State Chain for Generative Vision Modeling with Mamba SSMs
---

# Arcee: Differentiable Recurrent State Chain for Generative Vision Modeling with Mamba SSMs

**arXiv**: [2511.11243v1](https://arxiv.org/abs/2511.11243) | [PDF](https://arxiv.org/pdf/2511.11243.pdf)

**作者**: Jitesh Chavan, Rohit Lal, Anand Kamat, Mengjia Xu

---

## 💡 一句话要点

**提出Arcee跨块循环状态链，以改进视觉生成建模中的状态空间模型**

**关键词**: `状态空间模型` `视觉生成` `可微分边界` `Mamba模型` `循环状态链`

## 📋 核心要点

1. 核心问题：Mamba模型在块间重置状态，丢弃前一块的终端状态空间表示
2. 方法要点：通过可微分边界映射，重用终端状态作为下一块初始条件
3. 实验或效果：在CelebA-HQ无条件生成中，FID从82.81降至15.33

## 📄 摘要（原文）

> State-space models (SSMs), Mamba in particular, are increasingly adopted for long-context sequence modeling, providing linear-time aggregation via an input-dependent, causal selective-scan operation. Along this line, recent "Mamba-for-vision" variants largely explore multiple scan orders to relax strict causality for non-sequential signals (e.g., images). Rather than preserving cross-block memory, the conventional formulation of the selective-scan operation in Mamba reinitializes each block's state-space dynamics from zero, discarding the terminal state-space representation (SSR) from the previous block. Arcee, a cross-block recurrent state chain, reuses each block's terminal state-space representation as the initial condition for the next block. Handoff across blocks is constructed as a differentiable boundary map whose Jacobian enables end-to-end gradient flow across terminal boundaries. Key to practicality, Arcee is compatible with all prior "vision-mamba" variants, parameter-free, and incurs constant, negligible cost. As a modeling perspective, we view terminal SSR as a mild directional prior induced by a causal pass over the input, rather than an estimator of the non-sequential signal itself. To quantify the impact, for unconditional generation on CelebA-HQ (256$\times$256) with Flow Matching, Arcee reduces FID$\downarrow$ from $82.81$ to $15.33$ ($5.4\times$ lower) on a single scan-order Zigzag Mamba baseline. Efficient CUDA kernels and training code will be released to support rigorous and reproducible research.

