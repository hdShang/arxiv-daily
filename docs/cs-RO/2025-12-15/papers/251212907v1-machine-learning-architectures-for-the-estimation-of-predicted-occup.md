---
layout: default
title: Machine Learning Architectures for the Estimation of Predicted Occupancy Grids in Road Traffic
---

# Machine Learning Architectures for the Estimation of Predicted Occupancy Grids in Road Traffic

**arXiv**: [2512.12907v1](https://arxiv.org/abs/2512.12907) | [PDF](https://arxiv.org/pdf/2512.12907.pdf)

**作者**: Parthasarathy Nadarajan, Michael Botsch, Sebastian Sardina

---

## 💡 一句话要点

**提出基于堆叠去噪自编码器和随机森林的机器学习架构，用于高效估计道路交通场景的预测占用网格。**

**关键词**: `预测占用网格` `堆叠去噪自编码器` `随机森林` `自动驾驶` `交通场景预测` `主动安全系统`

## 📋 核心要点

1. 核心问题：预测复杂交通场景的未来时空表示，对自动驾驶和主动安全系统至关重要。
2. 方法要点：先识别交通场景类型，再通过机器学习将当前状态映射到未来状态，输入为增强占用网格，输出为预测占用网格。
3. 实验或效果：与现有架构比较，在模拟中验证准确性和计算时间，并概述预测占用网格在主动安全中的应用。

## 📄 摘要（原文）

> This paper introduces a novel machine learning architecture for an efficient estimation of the probabilistic space-time representation of complex traffic scenarios. A detailed representation of the future traffic scenario is of significant importance for autonomous driving and for all active safety systems. In order to predict the future space-time representation of the traffic scenario, first the type of traffic scenario is identified and then the machine learning algorithm maps the current state of the scenario to possible future states. The input to the machine learning algorithms is the current state representation of a traffic scenario, termed as the Augmented Occupancy Grid (AOG). The output is the probabilistic space-time representation which includes uncertainties regarding the behaviour of the traffic participants and is termed as the Predicted Occupancy Grid (POG). The novel architecture consists of two Stacked Denoising Autoencoders (SDAs) and a set of Random Forests. It is then compared with the other two existing architectures that comprise of SDAs and DeconvNet. The architectures are validated with the help of simulations and the comparisons are made both in terms of accuracy and computational time. Also, a brief overview on the applications of POGs in the field of active safety is presented.

