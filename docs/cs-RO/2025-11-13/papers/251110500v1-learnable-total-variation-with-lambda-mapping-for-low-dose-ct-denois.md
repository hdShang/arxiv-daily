---
layout: default
title: Learnable Total Variation with Lambda Mapping for Low-Dose CT Denoising
---

# Learnable Total Variation with Lambda Mapping for Low-Dose CT Denoising

**arXiv**: [2511.10500v1](https://arxiv.org/abs/2511.10500) | [PDF](https://arxiv.org/pdf/2511.10500.pdf)

**作者**: Yusuf Talha Basak, Mehmet Ozan Unal, Metin Ertas, Isa Yildirim

---

## 💡 一句话要点

**提出可学习全变差框架，结合LambdaNet预测逐像素正则化图，用于低剂量CT去噪。**

**关键词**: `低剂量CT去噪` `可学习全变差` `空间自适应正则化` `Lambda映射网络` `端到端训练`

## 📋 核心要点

1. 核心问题：传统全变差方法依赖lambda参数，效率受限且难以有效使用。
2. 方法要点：将展开TV求解器与数据驱动LambdaNet耦合，端到端训练实现空间自适应平滑。
3. 实验或效果：在DeepLesion数据集上，平均PSNR提升2.9 dB，SSIM提升6%。

## 📄 摘要（原文）

> Although Total Variation (TV) performs well in noise reduction and edge preservation on images, its dependence on the lambda parameter limits its efficiency and makes it difficult to use effectively. In this study, we present a Learnable Total Variation (LTV) framework that couples an unrolled TV solver with a data-driven Lambda Mapping Network (LambdaNet) predicting a per-pixel regularization map. The pipeline is trained end-to-end so that reconstruction and regularization are optimized jointly, yielding spatially adaptive smoothing: strong in homogeneous regions, relaxed near anatomical boundaries. Experiments on the DeepLesion dataset, using a realistic noise model adapted from the LoDoPaB-CT methodology, show consistent gains over classical TV and FBP+U-Net: +2.9 dB PSNR and +6% SSIM on average. LTV provides an interpretable alternative to black-box CNNs and a basis for 3D and data-consistency-driven reconstruction. Our codes are available at: https://github.com/itu-biai/deep_tv_for_ldct

