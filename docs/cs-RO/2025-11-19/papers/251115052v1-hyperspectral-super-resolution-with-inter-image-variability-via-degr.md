---
layout: default
title: Hyperspectral Super-Resolution with Inter-Image Variability via Degradation-based Low-Rank and Residual Fusion Method
---

# Hyperspectral Super-Resolution with Inter-Image Variability via Degradation-based Low-Rank and Residual Fusion Method

**arXiv**: [2511.15052v1](https://arxiv.org/abs/2511.15052) | [PDF](https://arxiv.org/pdf/2511.15052.pdf)

**作者**: Yue Wen, Kunjing Yang, Minru Bai

---

## 💡 一句话要点

**提出基于退化低秩残差融合方法以解决高光谱图像融合中的图像间变异性问题**

**关键词**: `高光谱图像融合` `图像间变异性` `低秩分解` `残差学习` `近端交替优化` `即插即用框架`

## 📋 核心要点

1. 核心问题：高光谱与多光谱图像融合中，图像间变异性导致融合性能下降
2. 方法要点：建模光谱变异性为退化算子变化，分解目标图像为低秩和残差分量
3. 实验或效果：数值实验显示DLRRF在图像间变异性下实现优越融合性能

## 📄 摘要（原文）

> The fusion of hyperspectral image (HSI) with multispectral image (MSI) provides an effective way to enhance the spatial resolution of HSI. However, due to different acquisition conditions, there may exist spectral variability and spatially localized changes between HSI and MSI, referred to as inter-image variability, which can significantly affect the fusion performance. Existing methods typically handle inter-image variability by applying direct transformations to the images themselves, which can exacerbate the ill-posedness of the fusion model. To address this challenge, we propose a Degradation-based Low-Rank and Residual Fusion (DLRRF) model. First, we model the spectral variability as change in the spectral degradation operator. Second, to recover the lost spatial details caused by spatially localized changes, we decompose the target HSI into low rank and residual components, where the latter is used to capture the lost details. By exploiting the spectral correlation within the images, we perform dimensionality reduction on both components. Additionally, we introduce an implicit regularizer to utilize the spatial prior information from the images. The proposed DLRRF model is solved using the Proximal Alternating Optimization (PAO) algorithm within a Plug-and-Play (PnP) framework, where the subproblem regarding implicit regularizer is addressed by an external denoiser. We further provide a comprehensive convergence analysis of the algorithm. Finally, extensive numerical experiments demonstrate that DLRRF achieves superior performance in fusing HSI and MSI with inter-image variability.

