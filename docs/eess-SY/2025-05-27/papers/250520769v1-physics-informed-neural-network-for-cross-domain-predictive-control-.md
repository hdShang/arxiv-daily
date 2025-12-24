---
layout: default
title: Physics-Informed Neural Network for Cross-Domain Predictive Control of Tapered Amplifier Thermal Stabilization
---

# Physics-Informed Neural Network for Cross-Domain Predictive Control of Tapered Amplifier Thermal Stabilization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20769" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20769v1</a>
  <a href="https://arxiv.org/pdf/2505.20769.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20769v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20769v1', 'Physics-Informed Neural Network for Cross-Domain Predictive Control of Tapered Amplifier Thermal Stabilization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanpei Shi, Bo Feng, Yuxin Zhong, Haochen Guo, Bangcheng Han, Rui Feng

**分类**: eess.SY

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出物理信息神经网络以解决锥形放大器热稳定性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `物理信息神经网络` `模型预测控制` `锥形放大器` `热稳定性` `量子传感器` `激光技术` `智能控制`

## 📋 核心要点

1. 现有方法在锥形放大器中面临热引起的激光噪声问题，影响量子传感器的灵敏度。
2. 本文提出了一种将物理信息神经网络与模型预测控制相结合的控制策略，以增强系统的物理一致性和外推能力。
3. 实验结果表明，该方法在高功率操作下的预测精度提高了58.2%，温度稳定性提高了69.1%，显示出良好的泛化能力。

## 📝 摘要（中文）

热引起的激光噪声对采用超稳定放大激光的量子传感器阵列的灵敏度构成了关键限制，主要源于锥形放大器中的非线性增益-温度耦合效应。为应对这一挑战，本文提出了一种强健的智能控制策略，将编码器-解码器物理信息门控递归单元（PI-GRU）网络与模型预测控制（MPC）框架协同集成。该方法将物理软约束纳入神经网络架构，生成具有增强物理一致性的预测模型，展现出超越训练数据分布的强大外推能力。利用PI-GRU模型的准确多步预测性能，我们实现了一种层次并行的MPC架构，能够实时补偿热不稳定性。该混合方法在不同激光功率操作下实现了锥形放大器的跨域一致热稳定性。值得注意的是，尽管仅在低功率操作数据上训练，我们的系统在先前未见的高功率操作范围内表现出卓越的泛化能力，预测精度提高了58.2%，温度稳定性提高了69.1%。

## 🔬 方法详解

**问题定义**：本文旨在解决锥形放大器中因热引起的激光噪声问题，这种噪声限制了量子传感器的灵敏度。现有方法在处理非线性增益-温度耦合效应时存在局限性，难以实现有效的热稳定控制。

**核心思路**：论文的核心思路是将物理信息神经网络（PI-GRU）与模型预测控制（MPC）框架相结合，通过引入物理软约束，提升预测模型的物理一致性和外推能力，从而实现更为精准的热稳定控制。

**技术框架**：整体架构包括PI-GRU网络作为预测模型，结合MPC进行实时控制。PI-GRU负责多步预测，而MPC则利用这些预测结果进行控制决策，形成层次并行的控制架构。

**关键创新**：最重要的技术创新在于将物理信息神经网络与MPC框架的同步应用，克服了传统建模方法的局限性，实现了跨域预测控制的稳健性。

**关键设计**：在网络设计中，采用了特定的损失函数以确保物理一致性，并通过调整网络结构和参数设置，优化了模型的预测性能。

## 📊 实验亮点

实验结果显示，尽管模型仅在低功率数据上训练，但在高功率操作下，预测精度提高了58.2%，温度稳定性提高了69.1%。这一显著提升验证了方法的有效性和泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括量子传感器、激光技术及其他需要高稳定性的光学系统。通过实现更好的热稳定性，能够提升相关技术的性能和可靠性，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Thermally induced laser noise poses a critical limitation to the sensitivity of quantum sensor arrays employing ultra-stable amplified lasers, primarily stemming from nonlinear gain-temperature coupling effects in tapered amplifiers (TAs). To address this challenge, we present a robust intelligent control strategy that synergistically integrates an encoder-decoder physics-informed gated recurrent unit (PI-GRU) network with a model predictive control (MPC) framework. Our methodology incorporates physical soft constraints into the neural network architecture, yielding a predictive model with enhanced physical consistency that demonstrates robust extrapolation capabilities beyond the training data distribution. Leveraging the PI-GRU model's accurate multi-step predictive performance, we implement a hierarchical parallel MPC architecture capable of real-time thermal instability compensation. This hybrid approach achieves cross-domain consistent thermal stabilization in TAs under diverse laser power operations. Remarkably, while trained exclusively on low-power operational data, our system demonstrates exceptional generalization, improving prediction accuracy by 58.2% and temperature stability by 69.1% in previously unseen high-power operating regimes, as experimentally validated. The novel synchronization of physics-informed neural networks with advanced MPC frameworks presented in this work establishes a groundbreaking paradigm for addressing robustness challenges in cross-domain predictive control applications, overcoming conventional modeling limitations.

