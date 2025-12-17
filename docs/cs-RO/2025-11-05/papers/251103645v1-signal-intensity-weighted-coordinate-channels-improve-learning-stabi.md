---
layout: default
title: Signal Intensity-weighted coordinate channels improve learning stability and generalisation in 1D and 2D CNNs in localisation tasks on biomedical signals
---

# Signal Intensity-weighted coordinate channels improve learning stability and generalisation in 1D and 2D CNNs in localisation tasks on biomedical signals

**arXiv**: [2511.03645v1](https://arxiv.org/abs/2511.03645) | [PDF](https://arxiv.org/pdf/2511.03645.pdf)

**作者**: Vittal L. Rao

---

## 💡 一句话要点

**提出信号强度加权坐标通道，提升生物医学信号定位任务中CNN的学习稳定性和泛化能力**

**关键词**: `坐标通道` `信号强度加权` `生物医学信号定位` `卷积神经网络` `泛化性能` `学习稳定性`

## 📋 核心要点

1. 生物医学信号定位需从复杂强度分布中学习空间或时间关系
2. 用信号强度加权坐标通道替代纯坐标通道，引入强度-位置耦合偏置
3. 在ECG和细胞图像定位任务中，实现更快收敛和更高泛化性能

## 📄 摘要（原文）

> Localisation tasks in biomedical data often require models to learn
> meaningful spatial or temporal relationships from signals with complex
> intensity distributions. A common strategy, exemplified by CoordConv layers, is
> to append coordinate channels to convolutional inputs, enabling networks to
> learn absolute positions. In this work, we propose a signal intensity-weighted
> coordinate representation that replaces the pure coordinate channels with
> channels scaled by local signal intensity. This modification embeds an
> intensity-position coupling directly in the input representation, introducing a
> simple and modality-agnostic inductive bias. We evaluate the approach on two
> distinct localisation problems: (i) predicting the time of morphological
> transition in 20-second, two-lead ECG signals, and (ii) regressing the
> coordinates of nuclear centres in cytological images from the SiPaKMeD dataset.
> In both cases, the proposed representation yields faster convergence and higher
> generalisation performance relative to conventional coordinate-channel
> approaches, demonstrating its effectiveness across both one-dimensional and
> two-dimensional biomedical signals.

