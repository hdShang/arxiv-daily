---
layout: default
title: CuMPerLay: Learning Cubical Multiparameter Persistence Vectorizations
---

# CuMPerLay: Learning Cubical Multiparameter Persistence Vectorizations

**arXiv**: [2510.12795v1](https://arxiv.org/abs/2510.12795) | [PDF](https://arxiv.org/pdf/2510.12795.pdf)

**作者**: Caner Korkmaz, Brighton Nuwagira, Barış Coşkunuzer, Tolga Birdal

---

## 💡 一句话要点

**提出CuMPerLay以将立方多参数持久性集成到深度学习管道中**

**关键词**: `多参数持久性` `深度学习集成` `拓扑数据分析` `图像分析` `可微分层`

## 📋 核心要点

1. 立方多参数持久性向量化复杂，阻碍其在图像拓扑分析中的应用
2. CuMPerLay将多参数持久性分解为可学习的单参数持久性组合
3. 实验显示在医学影像和计算机视觉任务中提升分类和分割性能

## 📄 摘要（原文）

> We present CuMPerLay, a novel differentiable vectorization layer that enables
> the integration of Cubical Multiparameter Persistence (CMP) into deep learning
> pipelines. While CMP presents a natural and powerful way to topologically work
> with images, its use is hindered by the complexity of multifiltration
> structures as well as the vectorization of CMP. In face of these challenges, we
> introduce a new algorithm for vectorizing MP homologies of cubical complexes.
> Our CuMPerLay decomposes the CMP into a combination of individual, learnable
> single-parameter persistence, where the bifiltration functions are jointly
> learned. Thanks to the differentiability, its robust topological feature
> vectors can be seamlessly used within state-of-the-art architectures such as
> Swin Transformers. We establish theoretical guarantees for the stability of our
> vectorization under generalized Wasserstein metrics. Our experiments on
> benchmark medical imaging and computer vision datasets show the benefit
> CuMPerLay on classification and segmentation performance, particularly in
> limited-data scenarios. Overall, CuMPerLay offers a promising direction for
> integrating global structural information into deep networks for structured
> image analysis.

