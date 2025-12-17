---
layout: default
title: A methodology for clinically driven interactive segmentation evaluation
---

# A methodology for clinically driven interactive segmentation evaluation

**arXiv**: [2510.09499v1](https://arxiv.org/abs/2510.09499) | [PDF](https://arxiv.org/pdf/2510.09499.pdf)

**作者**: Parhom Esmaeili, Virginia Fernandez, Pedro Borges, Eli Gibson, Sebastien Ourselin, M. Jorge Cardoso

---

## 💡 一句话要点

**提出临床驱动的交互式分割评估方法以解决医学图像分割评估不一致问题**

**关键词**: `交互式分割` `医学图像评估` `临床驱动方法` `标准化框架` `模型鲁棒性`

## 📋 核心要点

1. 核心问题：交互式分割评估不一致且临床不现实，阻碍公平比较和真实性能评估
2. 方法要点：定义临床基础评估任务与指标，构建标准化评估软件框架
3. 实验或效果：评估先进算法，发现交互处理信息损失最小化、自适应缩放等关键因素

## 📄 摘要（原文）

> Interactive segmentation is a promising strategy for building robust,
> generalisable algorithms for volumetric medical image segmentation. However,
> inconsistent and clinically unrealistic evaluation hinders fair comparison and
> misrepresents real-world performance. We propose a clinically grounded
> methodology for defining evaluation tasks and metrics, and built a software
> framework for constructing standardised evaluation pipelines. We evaluate
> state-of-the-art algorithms across heterogeneous and complex tasks and observe
> that (i) minimising information loss when processing user interactions is
> critical for model robustness, (ii) adaptive-zooming mechanisms boost
> robustness and speed convergence, (iii) performance drops if validation
> prompting behaviour/budgets differ from training, (iv) 2D methods perform well
> with slab-like images and coarse targets, but 3D context helps with large or
> irregularly shaped targets, (v) performance of non-medical-domain models (e.g.
> SAM2) degrades with poor contrast and complex shapes.

