---
layout: default
title: Visual Anomaly Detection for Reliable Robotic Implantation of Flexible Microelectrode Array
---

# Visual Anomaly Detection for Reliable Robotic Implantation of Flexible Microelectrode Array

**arXiv**: [2510.09071v1](https://arxiv.org/abs/2510.09071) | [PDF](https://arxiv.org/pdf/2510.09071.pdf)

**作者**: Yitong Chen, Xinyao Xu, Ping Zhu, Xinyong Han, Fangbo Qin, Shan Yu

---

## 💡 一句话要点

**提出基于视觉Transformer的异常检测框架，用于机器人柔性微电极植入过程监控**

**关键词**: `视觉异常检测` `机器人植入` `柔性微电极` `视觉Transformer` `特征采样` `脑皮层监控`

## 📋 核心要点

1. 核心问题：柔性微电极植入脑皮层时，因结构变形和生物组织交互，需可靠监控以确保安全。
2. 方法要点：利用预训练ViT提取对齐ROI特征，采用渐进粒度采样和特征通道选择优化检测。
3. 实验或效果：在植入系统收集的图像数据集上验证了方法的有效性。

## 📄 摘要（原文）

> Flexible microelectrode (FME) implantation into brain cortex is challenging
> due to the deformable fiber-like structure of FME probe and the interaction
> with critical bio-tissue. To ensure reliability and safety, the implantation
> process should be monitored carefully. This paper develops an image-based
> anomaly detection framework based on the microscopic cameras of the robotic FME
> implantation system. The unified framework is utilized at four checkpoints to
> check the micro-needle, FME probe, hooking result, and implantation point,
> respectively. Exploiting the existing object localization results, the aligned
> regions of interest (ROIs) are extracted from raw image and input to a
> pretrained vision transformer (ViT). Considering the task specifications, we
> propose a progressive granularity patch feature sampling method to address the
> sensitivity-tolerance trade-off issue at different locations. Moreover, we
> select a part of feature channels with higher signal-to-noise ratios from the
> raw general ViT features, to provide better descriptors for each specific
> scene. The effectiveness of the proposed methods is validated with the image
> datasets collected from our implantation system.

