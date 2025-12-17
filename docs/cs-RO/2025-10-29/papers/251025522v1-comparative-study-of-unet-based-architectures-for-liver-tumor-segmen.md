---
layout: default
title: Comparative Study of UNet-based Architectures for Liver Tumor Segmentation in Multi-Phase Contrast-Enhanced Computed Tomography
---

# Comparative Study of UNet-based Architectures for Liver Tumor Segmentation in Multi-Phase Contrast-Enhanced Computed Tomography

**arXiv**: [2510.25522v1](https://arxiv.org/abs/2510.25522) | [PDF](https://arxiv.org/pdf/2510.25522.pdf)

**作者**: Doan-Van-Anh Ly, Thi-Thu-Hien Pham, Thanh-Hai Le

---

## 💡 一句话要点

**比较UNet架构结合不同骨干网络与注意力机制，提升多期相CT肝肿瘤分割性能**

**关键词**: `肝肿瘤分割` `UNet架构` `注意力机制` `多期相CT` `医学图像分割`

## 📋 核心要点

1. 核心问题：多期相增强CT中肝肿瘤分割对诊断和治疗规划至关重要
2. 方法要点：评估UNet3+架构，结合ResNet、Transformer和Mamba骨干网络，并引入CBAM注意力模块
3. 实验或效果：ResNetUNet3+加CBAM在Dice、IoU和HD95等指标上表现最佳，优于其他模型

## 📄 摘要（原文）

> Segmentation of liver structures in multi-phase contrast-enhanced computed
> tomography (CECT) plays a crucial role in computer-aided diagnosis and
> treatment planning for liver diseases, including tumor detection. In this
> study, we investigate the performance of UNet-based architectures for liver
> tumor segmentation, starting from the original UNet and extending to UNet3+
> with various backbone networks. We evaluate ResNet, Transformer-based, and
> State-space (Mamba) backbones, all initialized with pretrained weights.
> Surprisingly, despite the advances in modern architecture, ResNet-based models
> consistently outperform Transformer- and Mamba-based alternatives across
> multiple evaluation metrics. To further improve segmentation quality, we
> introduce attention mechanisms into the backbone and observe that incorporating
> the Convolutional Block Attention Module (CBAM) yields the best performance.
> ResNetUNet3+ with CBAM module not only produced the best overlap metrics with a
> Dice score of 0.755 and IoU of 0.662, but also achieved the most precise
> boundary delineation, evidenced by the lowest HD95 distance of 77.911. The
> model's superiority was further cemented by its leading overall accuracy of
> 0.925 and specificity of 0.926, showcasing its robust capability in accurately
> identifying both lesion and healthy tissue. To further enhance
> interpretability, Grad-CAM visualizations were employed to highlight the
> region's most influential predictions, providing insights into its
> decision-making process. These findings demonstrate that classical ResNet
> architecture, when combined with modern attention modules, remain highly
> competitive for medical image segmentation tasks, offering a promising
> direction for liver tumor detection in clinical practice.

