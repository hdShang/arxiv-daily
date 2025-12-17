---
layout: default
title: Learning Compact Latent Space for Representing Neural Signed Distance Functions with High-fidelity Geometry Details
---

# Learning Compact Latent Space for Representing Neural Signed Distance Functions with High-fidelity Geometry Details

**arXiv**: [2511.14539v1](https://arxiv.org/abs/2511.14539) | [PDF](https://arxiv.org/pdf/2511.14539.pdf)

**作者**: Qiang Bai, Bojian Wu, Xi Yang, Zhizhong Han

---

## 💡 一句话要点

**提出紧凑潜在空间方法以在神经SDF中恢复高保真几何细节**

**关键词**: `神经符号距离函数` `紧凑潜在空间` `高保真几何` `采样策略` `3D形状表示`

## 📋 核心要点

1. 核心问题：神经SDF潜在空间信息有限，导致多SDF分析时几何细节丢失
2. 方法要点：结合泛化与过拟合学习策略，使用紧凑潜在码保留高保真细节
3. 实验或效果：在基准测试中验证，优于最新方法，提升表示能力和紧凑性

## 📄 摘要（原文）

> Neural signed distance functions (SDFs) have been a vital representation to represent 3D shapes or scenes with neural networks. An SDF is an implicit function that can query signed distances at specific coordinates for recovering a 3D surface. Although implicit functions work well on a single shape or scene, they pose obstacles when analyzing multiple SDFs with high-fidelity geometry details, due to the limited information encoded in the latent space for SDFs and the loss of geometry details. To overcome these obstacles, we introduce a method to represent multiple SDFs in a common space, aiming to recover more high-fidelity geometry details with more compact latent representations. Our key idea is to take full advantage of the benefits of generalization-based and overfitting-based learning strategies, which manage to preserve high-fidelity geometry details with compact latent codes. Based on this framework, we also introduce a novel sampling strategy to sample training queries. The sampling can improve the training efficiency and eliminate artifacts caused by the influence of other SDFs. We report numerical and visual evaluations on widely used benchmarks to validate our designs and show advantages over the latest methods in terms of the representative ability and compactness.

