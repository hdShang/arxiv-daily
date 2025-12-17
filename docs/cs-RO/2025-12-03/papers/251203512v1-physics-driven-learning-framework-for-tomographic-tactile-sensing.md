---
layout: default
title: Physics-Driven Learning Framework for Tomographic Tactile Sensing
---

# Physics-Driven Learning Framework for Tomographic Tactile Sensing

**arXiv**: [2512.03512v1](https://arxiv.org/abs/2512.03512) | [PDF](https://arxiv.org/pdf/2512.03512.pdf)

**作者**: Xuanxuan Yang, Xiuyang Zhang, Haofeng Chen, Gang Ma, Xiaojie Wang

---

## 💡 一句话要点

**提出PhyDNN物理驱动框架，以提升电阻抗断层扫描触觉传感的重建质量**

**关键词**: `电阻抗断层扫描` `触觉传感` `物理驱动学习` `可微前向算子` `非线性逆问题` `软传感器`

## 📋 核心要点

1. 核心问题：电阻抗断层扫描的非线性逆问题导致重建伪影和接触信息不准确
2. 方法要点：将EIT前向模型嵌入学习目标，设计可微前向算子网络实现物理引导训练
3. 实验或效果：在16电极软传感器上优于传统方法，减少伪影、提升边界清晰度和度量分数

## 📄 摘要（原文）

> Electrical impedance tomography (EIT) provides an attractive solution for large-area tactile sensing due to its minimal wiring and shape flexibility, but its nonlinear inverse problem often leads to severe artifacts and inaccurate contact reconstruction. This work presents PhyDNN, a physics-driven deep reconstruction framework that embeds the EIT forward model directly into the learning objective. By jointly minimizing the discrepancy between predicted and ground-truth conductivity maps and enforcing consistency with the forward PDE, PhyDNN reduces the black-box nature of deep networks and improves both physical plausibility and generalization. To enable efficient backpropagation, we design a differentiable forward-operator network that accurately approximates the nonlinear EIT response, allowing fast physics-guided training. Extensive simulations and real tactile experiments on a 16-electrode soft sensor show that PhyDNN consistently outperforms NOSER, TV, and standard DNNs in reconstructing contact shape, location, and pressure distribution. PhyDNN yields fewer artifacts, sharper boundaries, and higher metric scores, demonstrating its effectiveness for high-quality tomographic tactile sensing.

