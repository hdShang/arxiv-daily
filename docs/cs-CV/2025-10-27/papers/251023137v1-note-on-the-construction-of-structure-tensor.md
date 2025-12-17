---
layout: default
title: Note on the Construction of Structure Tensor
---

# Note on the Construction of Structure Tensor

**arXiv**: [2510.23137v1](https://arxiv.org/abs/2510.23137) | [PDF](https://arxiv.org/pdf/2510.23137.pdf)

**作者**: Josef Bigun, Fernado Alonso-Fernandez

---

## 💡 一句话要点

**统一结构张量构造方法，基于TLS线拟合提升灵活性与简化性**

**关键词**: `结构张量` `总最小二乘` `滤波器设计` `图像处理` `特征提取`

## 📋 核心要点

1. 核心问题：比较两种结构张量构造方法，探讨其差异与统一性。
2. 方法要点：通过TLS线拟合视角统一方法，移除校正项确保正半定性。
3. 实验或效果：简化特征值解释，支持多种滤波器与非角镶嵌。

## 📄 摘要（原文）

> This note presents a theoretical discussion of two structure tensor
> constructions: one proposed by Bigun and Granlund 1987, and the other by
> Granlund and Knutsson 1995. At first glance, these approaches may appear quite
> different--the former is implemented by averaging outer products of gradient
> filter responses, while the latter constructs the tensor from weighted outer
> products of tune-in frequency vectors of quadrature filters. We argue that when
> both constructions are viewed through the common lens of Total Least Squares
> (TLS) line fitting to the power spectrum, they can be reconciled to a large
> extent, and additional benefits emerge. From this perspective, the correction
> term introduced in Granlund and Knutsson 1995 becomes unnecessary. Omitting it
> ensures that the resulting tensor remains positive semi-definite, thereby
> simplifying the interpretation of its eigenvalues. Furthermore, this
> interpretation allows fitting more than a single 0rientation to the input by
> reinterpreting quadrature filter responses without relying on a structure
> tensor. It also removes the constraint that responses must originate strictly
> from quadrature filters, allowing the use of alternative filter types and
> non-angular tessellations. These alternatives include Gabor filters--which,
> although not strictly quadrature, are still suitable for structure tensor
> construction--even when they tessellate the spectrum in a Cartesian fashion,
> provided they are sufficiently concentrated.

