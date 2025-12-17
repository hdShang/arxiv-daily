---
layout: default
title: MM-UNet: Morph Mamba U-shaped Convolutional Networks for Retinal Vessel Segmentation
---

# MM-UNet: Morph Mamba U-shaped Convolutional Networks for Retinal Vessel Segmentation

**arXiv**: [2511.02193v1](https://arxiv.org/abs/2511.02193) | [PDF](https://arxiv.org/pdf/2511.02193.pdf)

**作者**: Jiawen Liu, Yuanbo Zeng, Jiaming Liang, Yizhen Yang, Yiheng Zhang, Enhui Cai, Xiaoqi Sheng, Hongmin Cai

---

## 💡 一句话要点

**提出MM-UNet以解决视网膜血管分割中细分支结构感知不足的问题**

**关键词**: `视网膜血管分割` `U形网络` `状态空间建模` `形态感知` `深度学习` `医学图像分析`

## 📋 核心要点

1. 视网膜血管结构细薄且形态多变，影响分割精度与鲁棒性
2. 引入Morph Mamba卷积层增强分支拓扑感知，并采用反向选择性状态引导模块提升边界感知
3. 在DRIVE和STARE数据集上F1分数分别提升1.64%和1.25%，代码已开源

## 📄 摘要（原文）

> Accurate detection of retinal vessels plays a critical role in reflecting a
> wide range of health status indicators in the clinical diagnosis of ocular
> diseases. Recently, advances in deep learning have led to a surge in retinal
> vessel segmentation methods, which have significantly contributed to the
> quantitative analysis of vascular morphology. However, retinal vasculature
> differs significantly from conventional segmentation targets in that it
> consists of extremely thin and branching structures, whose global morphology
> varies greatly across images. These characteristics continue to pose challenges
> to segmentation precision and robustness. To address these issues, we propose
> MM-UNet, a novel architecture tailored for efficient retinal vessel
> segmentation. The model incorporates Morph Mamba Convolution layers, which
> replace pointwise convolutions to enhance branching topological perception
> through morph, state-aware feature sampling. Additionally, Reverse Selective
> State Guidance modules integrate reverse guidance theory with state-space
> modeling to improve geometric boundary awareness and decoding efficiency.
> Extensive experiments conducted on two public retinal vessel segmentation
> datasets demonstrate the superior performance of the proposed method in
> segmentation accuracy. Compared to the existing approaches, MM-UNet achieves
> F1-score gains of 1.64 $\%$ on DRIVE and 1.25 $\%$ on STARE, demonstrating its
> effectiveness and advancement. The project code is public via
> https://github.com/liujiawen-jpg/MM-UNet.

