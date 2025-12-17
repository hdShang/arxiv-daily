---
layout: default
title: Robust 3D Brain MRI Inpainting with Random Masking Augmentation
---

# Robust 3D Brain MRI Inpainting with Random Masking Augmentation

**arXiv**: [2511.20202v1](https://arxiv.org/abs/2511.20202) | [PDF](https://arxiv.org/pdf/2511.20202.pdf)

**作者**: Juexin Zhang, Ying Weng, Ke Chen

---

## 💡 一句话要点

**提出基于随机掩码增强的U-Net方法，用于3D脑MRI图像修复以减轻数据集偏差**

**关键词**: `3D脑MRI修复` `随机掩码增强` `U-Net架构` `图像合成` `深度学习框架`

## 📋 核心要点

1. 核心问题：脑肿瘤MRI定量分析中数据集偏差限制深度学习模型泛化能力
2. 方法要点：采用U-Net架构结合随机掩码增强策略，提升模型泛化性能
3. 实验或效果：在BraTS-Inpainting 2025挑战赛中获第一名，验证集SSIM达0.873±0.004

## 📄 摘要（原文）

> The ASNR-MICCAI BraTS-Inpainting Challenge was established to mitigate dataset biases that limit deep learning models in the quantitative analysis of brain tumor MRI. This paper details our submission to the 2025 challenge, a novel deep learning framework for synthesizing healthy tissue in 3D scans. The core of our method is a U-Net architecture trained to inpaint synthetically corrupted regions, enhanced with a random masking augmentation strategy to improve generalization. Quantitative evaluation confirmed the efficacy of our approach, yielding an SSIM of 0.873$\pm$0.004, a PSNR of 24.996$\pm$4.694, and an MSE of 0.005$\pm$0.087 on the validation set. On the final online test set, our method achieved an SSIM of 0.919$\pm$0.088, a PSNR of 26.932$\pm$5.057, and an RMSE of 0.052$\pm$0.026. This performance secured first place in the BraTS-Inpainting 2025 challenge and surpassed the winning solutions from the 2023 and 2024 competitions on the official leaderboard.

