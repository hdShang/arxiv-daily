---
layout: default
title: Fast and Explicit: Slice-to-Volume Reconstruction via 3D Gaussian Primitives with Analytic Point Spread Function Modeling
---

# Fast and Explicit: Slice-to-Volume Reconstruction via 3D Gaussian Primitives with Analytic Point Spread Function Modeling

**arXiv**: [2512.11624v1](https://arxiv.org/abs/2512.11624) | [PDF](https://arxiv.org/pdf/2512.11624.pdf)

**作者**: Maik Dannecker, Steven Jia, Nil Stolt-Ansó, Nadine Girard, Guillaume Auzias, François Rousseau, Daniel Rueckert

---

## 💡 一句话要点

**提出基于3D高斯基元的显式表示方法，以解决医学成像中自监督切片到体积重建的计算瓶颈问题。**

**关键词**: `切片到体积重建` `3D高斯基元` `点扩散函数建模` `医学成像` `自监督学习` `计算加速`

## 📋 核心要点

1. 核心问题：隐式神经表示在建模点扩散函数时需昂贵蒙特卡洛采样，导致计算瓶颈。
2. 方法要点：使用各向异性高斯基元参数化3D图像，通过闭式解析解实现精确前向模型，避免随机采样。
3. 实验或效果：在新生儿和胎儿数据上匹配SOTA重建质量，速度提升5-10倍，收敛时间常低于30秒。

## 📄 摘要（原文）

> Recovering high-fidelity 3D images from sparse or degraded 2D images is a fundamental challenge in medical imaging, with broad applications ranging from 3D ultrasound reconstruction to MRI super-resolution. In the context of fetal MRI, high-resolution 3D reconstruction of the brain from motion-corrupted low-resolution 2D acquisitions is a prerequisite for accurate neurodevelopmental diagnosis. While implicit neural representations (INRs) have recently established state-of-the-art performance in self-supervised slice-to-volume reconstruction (SVR), they suffer from a critical computational bottleneck: accurately modeling the image acquisition physics requires expensive stochastic Monte Carlo sampling to approximate the point spread function (PSF). In this work, we propose a shift from neural network based implicit representations to Gaussian based explicit representations. By parameterizing the HR 3D image volume as a field of anisotropic Gaussian primitives, we leverage the property of Gaussians being closed under convolution and thus derive a \textit{closed-form analytical solution} for the forward model. This formulation reduces the previously intractable acquisition integral to an exact covariance addition ($\mathbfΣ_{obs} = \mathbfΣ_{HR} + \mathbfΣ_{PSF}$), effectively bypassing the need for compute-intensive stochastic sampling while ensuring exact gradient propagation. We demonstrate that our approach matches the reconstruction quality of self-supervised state-of-the-art SVR frameworks while delivering a 5$\times$--10$\times$ speed-up on neonatal and fetal data. With convergence often reached in under 30 seconds, our framework paves the way towards translation into clinical routine of real-time fetal 3D MRI. Code will be public at {https://github.com/m-dannecker/Gaussian-Primitives-for-Fast-SVR}.

