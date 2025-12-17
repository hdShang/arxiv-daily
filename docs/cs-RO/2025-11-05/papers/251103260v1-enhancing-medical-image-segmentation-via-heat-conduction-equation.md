---
layout: default
title: Enhancing Medical Image Segmentation via Heat Conduction Equation
---

# Enhancing Medical Image Segmentation via Heat Conduction Equation

**arXiv**: [2511.03260v1](https://arxiv.org/abs/2511.03260) | [PDF](https://arxiv.org/pdf/2511.03260.pdf)

**作者**: Rong Wu, Yim-Sang Yu

---

## 💡 一句话要点

**提出U-Mamba与热传导方程混合架构以增强医学图像分割**

**关键词**: `医学图像分割` `U-Mamba架构` `热传导方程` `状态空间模型` `长程依赖建模`

## 📋 核心要点

1. 现有模型难以在计算预算下高效建模全局上下文和长程依赖
2. 结合Mamba状态空间模块和热传导算子模拟频域热扩散
3. 在腹部CT和MRI数据集上优于基线，验证有效性和泛化性

## 📄 摘要（原文）

> Medical image segmentation has been significantly advanced by deep learning
> architectures, notably U-Net variants. However, existing models struggle to
> achieve efficient global context modeling and long-range dependency reasoning
> under practical computational budgets simultaneously. In this work, we propose
> a novel hybrid architecture utilizing U-Mamba with Heat Conduction Equation.
> Our model combines Mamba-based state-space modules for efficient long-range
> reasoning with Heat Conduction Operators (HCOs) in the bottleneck layers,
> simulating frequency-domain thermal diffusion for enhanced semantic
> abstraction. Experimental results on multimodal abdominal CT and MRI datasets
> demonstrate that the proposed model consistently outperforms strong baselines,
> validating its effectiveness and generalizability. It suggest that blending
> state-space dynamics with heat-based global diffusion offers a scalable and
> interpretable solution for medical segmentation tasks.

