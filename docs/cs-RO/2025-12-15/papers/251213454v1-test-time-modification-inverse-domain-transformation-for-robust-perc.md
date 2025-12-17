---
layout: default
title: Test-Time Modification: Inverse Domain Transformation for Robust Perception
---

# Test-Time Modification: Inverse Domain Transformation for Robust Perception

**arXiv**: [2512.13454v1](https://arxiv.org/abs/2512.13454) | [PDF](https://arxiv.org/pdf/2512.13454.pdf)

**作者**: Arpit Jadon, Joshua Niemeijer, Yuki M. Asano

---

## 💡 一句话要点

**提出测试时逆域变换方法，利用扩散模型将目标图像映射回源分布以提升未知域泛化性能。**

**关键词**: `域泛化` `测试时修改` `扩散模型` `逆域变换` `鲁棒感知`

## 📋 核心要点

1. 核心问题：生成模型用于训练数据增强时，合成全面目标域变体成本高且不完整。
2. 方法要点：在测试时使用扩散模型将目标图像逆变换到源分布，无需大规模合成数据。
3. 实验或效果：在分割、检测和分类任务中，对未知目标分布实现显著性能提升，如BDD100K-Night上相对增益137%。

## 📄 摘要（原文）

> Generative foundation models contain broad visual knowledge and can produce diverse image variations, making them particularly promising for advancing domain generalization tasks. While they can be used for training data augmentation, synthesizing comprehensive target-domain variations remains slow, expensive, and incomplete. We propose an alternative: using diffusion models at test time to map target images back to the source distribution where the downstream model was trained. This approach requires only a source domain description, preserves the task model, and eliminates large-scale synthetic data generation. We demonstrate consistent improvements across segmentation, detection, and classification tasks under challenging environmental shifts in real-to-real domain generalization scenarios with unknown target distributions. Our analysis spans multiple generative and downstream models, including an ensemble variant for enhanced robustness. The method achieves substantial relative gains: 137% on BDD100K-Night, 68% on ImageNet-R, and 62% on DarkZurich.

