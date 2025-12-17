---
layout: default
title: Image Denoising Using Transformed L1 (TL1) Regularization via ADMM
---

# Image Denoising Using Transformed L1 (TL1) Regularization via ADMM

**arXiv**: [2511.15060v1](https://arxiv.org/abs/2511.15060) | [PDF](https://arxiv.org/pdf/2511.15060.pdf)

**作者**: Nabiha Choudhury, Jianqing Jia, Yifei Lou

---

## 💡 一句话要点

**提出TL1正则化方法以解决图像去噪中的阶梯伪影和对比度损失问题**

**关键词**: `图像去噪` `变换L1正则化` `ADMM算法` `总变差正则化` `近端算子` `FFT图像更新`

## 📋 核心要点

1. 总变差正则化在图像去噪中易产生阶梯伪影和对比度损失
2. 采用变换L1正则化于图像梯度，并通过ADMM求解，具有闭式近端算子和FFT图像更新
3. 实验显示该方法在去噪、边缘保持和对比度增强方面表现优越

## 📄 摘要（原文）

> Total variation (TV) regularization is a classical tool for image denoising, but its convex $\ell_1$ formulation often leads to staircase artifacts and loss of contrast. To address these issues, we introduce the Transformed $\ell_1$ (TL1) regularizer applied to image gradients. In particular, we develop a TL1-regularized denoising model and solve it using the Alternating Direction Method of Multipliers (ADMM), featuring a closed-form TL1 proximal operator and an FFT-based image update under periodic boundary conditions. Experimental results demonstrate that our approach achieves superior denoising performance, effectively suppressing noise while preserving edges and enhancing image contrast.

