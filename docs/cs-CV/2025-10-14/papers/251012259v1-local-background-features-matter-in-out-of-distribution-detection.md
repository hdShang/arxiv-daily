---
layout: default
title: Local Background Features Matter in Out-of-Distribution Detection
---

# Local Background Features Matter in Out-of-Distribution Detection

**arXiv**: [2510.12259v1](https://arxiv.org/abs/2510.12259) | [PDF](https://arxiv.org/pdf/2510.12259.pdf)

**作者**: Jinlun Ye, Zhuohao Sun, Yiqiao Qiu, Qiu Li, Zhijun Tan, Ruixuan Wang

---

## 💡 一句话要点

**提出利用局部背景特征作为伪OOD特征以缓解OOD检测中的过自信问题**

**关键词**: `OOD检测` `背景特征` `过自信缓解` `卷积局部不变性` `伪OOD特征` `模型训练优化`

## 📋 核心要点

1. 核心问题：神经网络在OOD数据上产生过自信预测，影响部署可靠性。
2. 方法要点：从ID图像提取局部背景特征作为伪OOD特征，通过优化降低其L2范数。
3. 实验或效果：在多个标准基准上验证有效性，与现有方法兼容并达到新SOTA。

## 📄 摘要（原文）

> Out-of-distribution (OOD) detection is crucial when deploying deep neural
> networks in the real world to ensure the reliability and safety of their
> applications. One main challenge in OOD detection is that neural network models
> often produce overconfident predictions on OOD data. While some methods using
> auxiliary OOD datasets or generating fake OOD images have shown promising OOD
> detection performance, they are limited by the high costs of data collection
> and training. In this study, we propose a novel and effective OOD detection
> method that utilizes local background features as fake OOD features for model
> training. Inspired by the observation that OOD images generally share similar
> background regions with ID images, the background features are extracted from
> ID images as simulated OOD visual representations during training based on the
> local invariance of convolution. Through being optimized to reduce the
> $L_2$-norm of these background features, the neural networks are able to
> alleviate the overconfidence issue on OOD data. Extensive experiments on
> multiple standard OOD detection benchmarks confirm the effectiveness of our
> method and its wide combinatorial compatibility with existing post-hoc methods,
> with new state-of-the-art performance achieved from our method.

