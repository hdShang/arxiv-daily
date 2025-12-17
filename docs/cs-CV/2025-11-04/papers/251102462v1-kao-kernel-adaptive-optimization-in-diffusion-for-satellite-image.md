---
layout: default
title: KAO: Kernel-Adaptive Optimization in Diffusion for Satellite Image
---

# KAO: Kernel-Adaptive Optimization in Diffusion for Satellite Image

**arXiv**: [2511.02462v1](https://arxiv.org/abs/2511.02462) | [PDF](https://arxiv.org/pdf/2511.02462.pdf)

**作者**: Teerapong Panboonyuen

---

## 💡 一句话要点

**提出KAO框架，利用核自适应优化在扩散模型中解决高分辨率卫星图像修复问题。**

**关键词**: `卫星图像修复` `扩散模型` `核自适应优化` `潜在空间条件化` `显式传播` `高分辨率图像处理`

## 📋 核心要点

1. 核心问题：高分辨率卫星图像修复中，现有方法需大量重训练或计算开销高。
2. 方法要点：引入潜在空间条件化和显式传播，优化紧凑潜在空间以提升效率与精度。
3. 实验或效果：在DeepGlobe等数据集上，KAO设定了新基准，平衡效率与灵活性。

## 📄 摘要（原文）

> Satellite image inpainting is a crucial task in remote sensing, where
> accurately restoring missing or occluded regions is essential for robust image
> analysis. In this paper, we propose KAO, a novel framework that utilizes
> Kernel-Adaptive Optimization within diffusion models for satellite image
> inpainting. KAO is specifically designed to address the challenges posed by
> very high-resolution (VHR) satellite datasets, such as DeepGlobe and the
> Massachusetts Roads Dataset. Unlike existing methods that rely on
> preconditioned models requiring extensive retraining or postconditioned models
> with significant computational overhead, KAO introduces a Latent Space
> Conditioning approach, optimizing a compact latent space to achieve efficient
> and accurate inpainting. Furthermore, we incorporate Explicit Propagation into
> the diffusion process, facilitating forward-backward fusion, which improves the
> stability and precision of the method. Experimental results demonstrate that
> KAO sets a new benchmark for VHR satellite image restoration, providing a
> scalable, high-performance solution that balances the efficiency of
> preconditioned models with the flexibility of postconditioned models.

