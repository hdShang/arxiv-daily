---
layout: default
title: FRBNet: Revisiting Low-Light Vision through Frequency-Domain Radial Basis Network
---

# FRBNet: Revisiting Low-Light Vision through Frequency-Domain Radial Basis Network

**arXiv**: [2510.23444v1](https://arxiv.org/abs/2510.23444) | [PDF](https://arxiv.org/pdf/2510.23444.pdf)

**作者**: Fangtong Sun, Congyu Li, Ke Yang, Yuchen Pan, Hanwen Yu, Xichuan Zhang, Yiying Li

---

## 💡 一句话要点

**提出FRBNet以解决低光视觉中的光照退化问题**

**关键词**: `低光视觉` `频域分析` `光照不变特征` `目标检测` `图像分割`

## 📋 核心要点

1. 核心问题：低光条件下图像退化严重，影响检测和分割等下游任务性能
2. 方法要点：在频域中利用通道比提取光照不变特征，集成可学习滤波器
3. 实验或效果：在多个任务中表现优异，如目标检测mAP提升2.2

## 📄 摘要（原文）

> Low-light vision remains a fundamental challenge in computer vision due to
> severe illumination degradation, which significantly affects the performance of
> downstream tasks such as detection and segmentation. While recent
> state-of-the-art methods have improved performance through invariant feature
> learning modules, they still fall short due to incomplete modeling of low-light
> conditions. Therefore, we revisit low-light image formation and extend the
> classical Lambertian model to better characterize low-light conditions. By
> shifting our analysis to the frequency domain, we theoretically prove that the
> frequency-domain channel ratio can be leveraged to extract
> illumination-invariant features via a structured filtering process. We then
> propose a novel and end-to-end trainable module named \textbf{F}requency-domain
> \textbf{R}adial \textbf{B}asis \textbf{Net}work (\textbf{FRBNet}), which
> integrates the frequency-domain channel ratio operation with a learnable
> frequency domain filter for the overall illumination-invariant feature
> enhancement. As a plug-and-play module, FRBNet can be integrated into existing
> networks for low-light downstream tasks without modifying loss functions.
> Extensive experiments across various downstream tasks demonstrate that FRBNet
> achieves superior performance, including +2.2 mAP for dark object detection and
> +2.9 mIoU for nighttime segmentation. Code is available at:
> https://github.com/Sing-Forevet/FRBNet.

