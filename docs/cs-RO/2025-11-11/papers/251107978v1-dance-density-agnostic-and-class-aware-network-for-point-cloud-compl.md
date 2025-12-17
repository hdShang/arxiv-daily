---
layout: default
title: DANCE: Density-agnostic and Class-aware Network for Point Cloud Completion
---

# DANCE: Density-agnostic and Class-aware Network for Point Cloud Completion

**arXiv**: [2511.07978v1](https://arxiv.org/abs/2511.07978) | [PDF](https://arxiv.org/pdf/2511.07978.pdf)

**作者**: Da-Yeong Kim, Yeong-Jun Cho

---

## 💡 一句话要点

**提出DANCE网络以解决点云补全中密度变化和语义一致性问题**

**关键词**: `点云补全` `密度无关网络` `语义引导` `Transformer解码器` `射线采样`

## 📋 核心要点

1. 核心问题：点云补全在输入密度可变和有限监督下难以保持几何结构。
2. 方法要点：使用射线采样生成候选点，Transformer解码器优化位置和预测不透明度。
3. 实验或效果：在PCN和MVP基准上优于现有方法，对密度变化和噪声鲁棒。

## 📄 摘要（原文）

> Point cloud completion aims to recover missing geometric structures from incomplete 3D scans, which often suffer from occlusions or limited sensor viewpoints. Existing methods typically assume fixed input/output densities or rely on image-based representations, making them less suitable for real-world scenarios with variable sparsity and limited supervision. In this paper, we introduce Density-agnostic and Class-aware Network (DANCE), a novel framework that completes only the missing regions while preserving the observed geometry. DANCE generates candidate points via ray-based sampling from multiple viewpoints. A transformer decoder then refines their positions and predicts opacity scores, which determine the validity of each point for inclusion in the final surface. To incorporate semantic guidance, a lightweight classification head is trained directly on geometric features, enabling category-consistent completion without external image supervision. Extensive experiments on the PCN and MVP benchmarks show that DANCE outperforms state-of-the-art methods in accuracy and structural consistency, while remaining robust to varying input densities and noise levels.

