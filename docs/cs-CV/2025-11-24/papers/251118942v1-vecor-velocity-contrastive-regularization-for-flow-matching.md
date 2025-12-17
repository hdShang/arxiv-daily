---
layout: default
title: VeCoR - Velocity Contrastive Regularization for Flow Matching
---

# VeCoR - Velocity Contrastive Regularization for Flow Matching

**arXiv**: [2511.18942v1](https://arxiv.org/abs/2511.18942) | [PDF](https://arxiv.org/pdf/2511.18942.pdf)

**作者**: Zong-Wei Hong, Jing-lun Li, Lin-Ze Li, Shen Zhang, Yao Tang

---

## 💡 一句话要点

**提出VeCoR以增强流匹配的稳定性和图像质量，适用于轻量或低步设置。**

**关键词**: `流匹配` `对比正则化` `生成模型` `图像生成` `稳定训练`

## 📋 核心要点

1. 标准流匹配可能累积误差并偏离数据流形，导致感知退化。
2. VeCoR通过对比正则化，提供正负监督以平衡吸引和排斥。
3. 在ImageNet和MS-COCO上显著降低FID，提升收敛和图像质量。

## 📄 摘要（原文）

> Flow Matching (FM) has recently emerged as a principled and efficient alternative to diffusion models. Standard FM encourages the learned velocity field to follow a target direction; however, it may accumulate errors along the trajectory and drive samples off the data manifold, leading to perceptual degradation, especially in lightweight or low-step configurations.
>   To enhance stability and generalization, we extend FM into a balanced attract-repel scheme that provides explicit guidance on both "where to go" and "where not to go." To be formal, we propose \textbf{Velocity Contrastive Regularization (VeCoR)}, a complementary training scheme for flow-based generative modeling that augments the standard FM objective with contrastive, two-sided supervision. VeCoR not only aligns the predicted velocity with a stable reference direction (positive supervision) but also pushes it away from inconsistent, off-manifold directions (negative supervision). This contrastive formulation transforms FM from a purely attractive, one-sided objective into a two-sided training signal, regularizing trajectory evolution and improving perceptual fidelity across datasets and backbones.
>   On ImageNet-1K 256$\times$256, VeCoR yields 22\% and 35\% relative FID reductions on SiT-XL/2 and REPA-SiT-XL/2 backbones, respectively, and achieves further FID gains (32\% relative) on MS-COCO text-to-image generation, demonstrating consistent improvements in stability, convergence, and image quality, particularly in low-step and lightweight settings. Project page: https://p458732.github.io/VeCoR_Project_Page/

