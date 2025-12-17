---
layout: default
title: Hierarchical Spatial-Frequency Aggregation for Spectral Deconvolution Imaging
---

# Hierarchical Spatial-Frequency Aggregation for Spectral Deconvolution Imaging

**arXiv**: [2511.06751v1](https://arxiv.org/abs/2511.06751) | [PDF](https://arxiv.org/pdf/2511.06751.pdf)

**作者**: Tao Lv, Daoming Zhou, Chenglong Huang, Chongde Zi, Linsen Chen, Xun Cao

---

## 💡 一句话要点

**提出HSFAUT方法以解决光谱解卷积成像中的场景依赖性问题**

**关键词**: `光谱成像` `解卷积成像` `Transformer` `深度展开` `空间-频率聚合` `逆问题求解`

## 📋 核心要点

1. 核心问题：SDI方法中系数矩阵场景依赖，阻碍先验利用和重建精度
2. 方法要点：通过分层空间-频率聚合展开框架，将非线性过程线性化求解
3. 实验或效果：在模拟和真实实验中超越SOTA方法，内存和计算成本更低

## 📄 摘要（原文）

> Computational spectral imaging (CSI) achieves real-time hyperspectral imaging
> through co-designed optics and algorithms, but typical CSI methods suffer from
> a bulky footprint and limited fidelity. Therefore, Spectral Deconvolution
> imaging (SDI) methods based on PSF engineering have been proposed to achieve
> high-fidelity compact CSI design recently. However, the composite
> convolution-integration operations of SDI render the normal-equation
> coefficient matrix scene-dependent, which hampers the efficient exploitation of
> imaging priors and poses challenges for accurate reconstruction. To tackle the
> inherent data-dependent operators in SDI, we introduce a Hierarchical
> Spatial-Spectral Aggregation Unfolding Framework (HSFAUF). By decomposing
> subproblems and projecting them into the frequency domain, HSFAUF transforms
> nonlinear processes into linear mappings, thereby enabling efficient solutions.
> Furthermore, to integrate spatial-spectral priors during iterative refinement,
> we propose a Spatial-Frequency Aggregation Transformer (SFAT), which explicitly
> aggregates information across spatial and frequency domains. By integrating
> SFAT into HSFAUF, we develop a Transformer-based deep unfolding method,
> \textbf{H}ierarchical \textbf{S}patial-\textbf{F}requency \textbf{A}ggregation
> \textbf{U}nfolding \textbf{T}ransformer (HSFAUT), to solve the inverse problem
> of SDI. Systematic simulated and real experiments show that HSFAUT surpasses
> SOTA methods with cheaper memory and computational costs, while exhibiting
> optimal performance on different SDI systems.

