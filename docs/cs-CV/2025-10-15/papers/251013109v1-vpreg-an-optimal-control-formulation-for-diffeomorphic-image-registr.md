---
layout: default
title: VPREG: An Optimal Control Formulation for Diffeomorphic Image Registration Based on the Variational Principle Grid Generation Method
---

# VPREG: An Optimal Control Formulation for Diffeomorphic Image Registration Based on the Variational Principle Grid Generation Method

**arXiv**: [2510.13109v1](https://arxiv.org/abs/2510.13109) | [PDF](https://arxiv.org/pdf/2510.13109.pdf)

**作者**: Zicong Zhou, Baihan Zhao, Andreas Mang, Guojun Liao

---

## 💡 一句话要点

**提出VPreg方法以优化脑图像配准，确保变换可逆且无折叠。**

**关键词**: `图像配准` `微分同胚变换` `变分原理` `脑成像` `雅可比行列式` `逆变换计算`

## 📋 核心要点

1. 核心问题：传统图像配准方法难以保证变换的可逆性和无折叠性。
2. 方法要点：基于变分原理网格生成，控制雅可比行列式和旋度。
3. 实验或效果：在OASIS-1数据集上，VPreg在Dice分数和变换规律性上优于现有方法。

## 📄 摘要（原文）

> This paper introduces VPreg, a novel diffeomorphic image registration method.
> This work provides several improvements to our past work on mesh generation and
> diffeomorphic image registration. VPreg aims to achieve excellent registration
> accuracy while controlling the quality of the registration transformations. It
> ensures a positive Jacobian determinant of the spatial transformation and
> provides an accurate approximation of the inverse of the registration, a
> crucial property for many neuroimaging workflows. Unlike conventional methods,
> VPreg generates this inverse transformation within the group of diffeomorphisms
> rather than operating on the image space. The core of VPreg is a grid
> generation approach, referred to as \emph{Variational Principle} (VP), which
> constructs non-folding grids with prescribed Jacobian determinant and curl.
> These VP-generated grids guarantee diffeomorphic spatial transformations
> essential for computational anatomy and morphometry, and provide a more
> accurate inverse than existing methods. To assess the potential of the proposed
> approach, we conduct a performance analysis for 150 registrations of brain
> scans from the OASIS-1 dataset. Performance evaluation based on Dice scores for
> 35 regions of interest, along with an empirical analysis of the properties of
> the computed spatial transformations, demonstrates that VPreg outperforms
> state-of-the-art methods in terms of Dice scores, regularity properties of the
> computed transformation, and accuracy and consistency of the provided inverse
> map. We compare our results to ANTs-SyN, Freesurfer-Easyreg, and FSL-Fnirt.

