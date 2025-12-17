---
layout: default
title: CheXmask-U: Quantifying uncertainty in landmark-based anatomical segmentation for X-ray images
---

# CheXmask-U: Quantifying uncertainty in landmark-based anatomical segmentation for X-ray images

**arXiv**: [2512.10715v1](https://arxiv.org/abs/2512.10715) | [PDF](https://arxiv.org/pdf/2512.10715.pdf)

**作者**: Matias Cosarinsky, Nicolas Gaggion, Rodrigo Echeveste, Enzo Ferrante

---

## 💡 一句话要点

**提出CheXmask-U方法，量化X射线图像中基于解剖标志点分割的不确定性以增强临床部署安全性**

**关键词**: `医学图像分割` `不确定性估计` `X射线图像` `解剖标志点` `变分潜在空间` `数据集发布`

## 📋 核心要点

1. 核心问题：医学图像分割系统需不确定性估计来识别不可靠预测，但基于标志点的分割不确定性研究不足
2. 方法要点：结合卷积编码器和图生成解码器的混合架构，从变分潜在空间推导潜在不确定性和预测不确定性
3. 实验或效果：通过扰动实验验证不确定性随扰动增加，支持不可靠预测识别和分布外检测，并发布大规模不确定性数据集

## 📄 摘要（原文）

> Uncertainty estimation is essential for the safe clinical deployment of medical image segmentation systems, enabling the identification of unreliable predictions and supporting human oversight. While prior work has largely focused on pixel-level uncertainty, landmark-based segmentation offers inherent topological guarantees yet remains underexplored from an uncertainty perspective. In this work, we study uncertainty estimation for anatomical landmark-based segmentation on chest X-rays. Inspired by hybrid neural network architectures that combine standard image convolutional encoders with graph-based generative decoders, and leveraging their variational latent space, we derive two complementary measures: (i) latent uncertainty, captured directly from the learned distribution parameters, and (ii) predictive uncertainty, obtained by generating multiple stochastic output predictions from latent samples. Through controlled corruption experiments we show that both uncertainty measures increase with perturbation severity, reflecting both global and local degradation. We demonstrate that these uncertainty signals can identify unreliable predictions by comparing with manual ground-truth, and support out-of-distribution detection on the CheXmask dataset. More importantly, we release CheXmask-U (huggingface.co/datasets/mcosarinsky/CheXmask-U), a large scale dataset of 657,566 chest X-ray landmark segmentations with per-node uncertainty estimates, enabling researchers to account for spatial variations in segmentation quality when using these anatomical masks. Our findings establish uncertainty estimation as a promising direction to enhance robustness and safe deployment of landmark-based anatomical segmentation methods in chest X-ray. A fully working interactive demo of the method is available at huggingface.co/spaces/matiasky/CheXmask-U and the source code at github.com/mcosarinsky/CheXmask-U.

