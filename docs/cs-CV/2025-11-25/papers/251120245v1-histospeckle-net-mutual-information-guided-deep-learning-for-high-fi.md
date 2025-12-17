---
layout: default
title: HistoSpeckle-Net: Mutual Information-Guided Deep Learning for high-fidelity reconstruction of complex OrganAMNIST images via perturbed Multimode Fibers
---

# HistoSpeckle-Net: Mutual Information-Guided Deep Learning for high-fidelity reconstruction of complex OrganAMNIST images via perturbed Multimode Fibers

**arXiv**: [2511.20245v1](https://arxiv.org/abs/2511.20245) | [PDF](https://arxiv.org/pdf/2511.20245.pdf)

**作者**: Jawaria Maqbool, M. Imran Cheema

---

## 💡 一句话要点

**提出HistoSpeckle-Net以通过多模光纤高保真重建复杂医学图像**

**关键词**: `多模光纤成像` `互信息损失` `图像重建` `深度学习` `医学图像处理`

## 📋 核心要点

1. 现有多模光纤成像方法依赖大数据且难以处理复杂图像
2. 引入基于直方图的互信息损失和三尺度特征细化模块
3. 在OrganAMNIST数据集上优于基线模型，减少数据依赖和光纤弯曲影响

## 📄 摘要（原文）

> Existing deep learning methods in multimode fiber (MMF) imaging often focus on simpler datasets, limiting their applicability to complex, real-world imaging tasks. These models are typically data-intensive, a challenge that becomes more pronounced when dealing with diverse and complex images. In this work, we propose HistoSpeckle-Net, a deep learning architecture designed to reconstruct structurally rich medical images from MMF speckles. To build a clinically relevant dataset, we develop an optical setup that couples laser light through a spatial light modulator (SLM) into an MMF, capturing output speckle patterns corresponding to input OrganAMNIST images. Unlike previous MMF imaging approaches, which have not considered the underlying statistics of speckles and reconstructed images, we introduce a distribution-aware learning strategy. We employ a histogram-based mutual information loss to enhance model robustness and reduce reliance on large datasets. Our model includes a histogram computation unit that estimates smooth marginal and joint histograms for calculating mutual information loss. It also incorporates a unique Three-Scale Feature Refinement Module, which leads to multiscale Structural Similarity Index Measure (SSIM) loss computation. Together, these two loss functions enhance both the structural fidelity and statistical alignment of the reconstructed images. Our experiments on the complex OrganAMNIST dataset demonstrate that HistoSpeckle-Net achieves higher fidelity than baseline models such as U-Net and Pix2Pix. It gives superior performance even with limited training samples and across varying fiber bending conditions. By effectively reconstructing complex anatomical features with reduced data and under fiber perturbations, HistoSpeckle-Net brings MMF imaging closer to practical deployment in real-world clinical environments.

