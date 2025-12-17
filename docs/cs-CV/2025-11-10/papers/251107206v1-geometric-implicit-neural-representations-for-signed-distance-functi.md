---
layout: default
title: Geometric implicit neural representations for signed distance functions
---

# Geometric implicit neural representations for signed distance functions

**arXiv**: [2511.07206v1](https://arxiv.org/abs/2511.07206) | [PDF](https://arxiv.org/pdf/2511.07206.pdf)

**作者**: Luiz Schirmer, Tiago Novello, Vinícius da Silva, Guilherme Schardong, Daniel Perazzo, Hélio Lopes, Nuno Gonçalves, Luiz Velho

---

## 💡 一句话要点

**综述几何隐式神经表示在符号距离函数中的应用，提升表面重建精度**

**关键词**: `隐式神经表示` `符号距离函数` `表面重建` `几何正则化` `微分几何` `3D重建`

## 📋 核心要点

1. 核心问题：如何从定向点云或姿态图像中准确重建表面，确保符号距离函数满足全局属性。
2. 方法要点：在损失函数中引入几何正则化项，如单位梯度约束，结合微分几何工具。
3. 实验或效果：几何INRs在表面重建中实现显著进步，适用于多种输入数据。

## 📄 摘要（原文）

> \textit{Implicit neural representations} (INRs) have emerged as a promising
> framework for representing signals in low-dimensional spaces. This survey
> reviews the existing literature on the specialized INR problem of approximating
> \textit{signed distance functions} (SDFs) for surface scenes, using either
> oriented point clouds or a set of posed images. We refer to neural SDFs that
> incorporate differential geometry tools, such as normals and curvatures, in
> their loss functions as \textit{geometric} INRs. The key idea behind this 3D
> reconstruction approach is to include additional \textit{regularization} terms
> in the loss function, ensuring that the INR satisfies certain global properties
> that the function should hold -- such as having unit gradient in the case of
> SDFs. We explore key methodological components, including the definition of
> INR, the construction of geometric loss functions, and sampling schemes from a
> differential geometry perspective. Our review highlights the significant
> advancements enabled by geometric INRs in surface reconstruction from oriented
> point clouds and posed images.

