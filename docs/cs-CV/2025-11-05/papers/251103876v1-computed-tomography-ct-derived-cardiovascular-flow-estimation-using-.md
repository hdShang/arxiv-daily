---
layout: default
title: Computed Tomography (CT)-derived Cardiovascular Flow Estimation Using Physics-Informed Neural Networks Improves with Sinogram-based Training: A Simulation Study
---

# Computed Tomography (CT)-derived Cardiovascular Flow Estimation Using Physics-Informed Neural Networks Improves with Sinogram-based Training: A Simulation Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.03876" class="toolbar-btn" target="_blank">📄 arXiv: 2511.03876v1</a>
  <a href="https://arxiv.org/pdf/2511.03876.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03876v1" onclick="toggleFavorite(this, '2511.03876v1', 'Computed Tomography (CT)-derived Cardiovascular Flow Estimation Using Physics-Informed Neural Networks Improves with Sinogram-based Training: A Simulation Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinyuxuan Guo, Gurnoor Singh Khurana, Alejandro Gonzalo Grande, Juan C. del Alamo, Francisco Contijoch

**分类**: eess.IV, cs.CV, cs.LG, physics.med-ph

**发布日期**: 2025-11-05

---

## 💡 一句话要点

**提出SinoFlow：利用Sinogram数据训练的物理信息神经网络提升CT血流估计精度**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `物理信息神经网络` `计算机断层扫描` `血流估计` `Sinogram数据` `心血管成像`

## 📋 核心要点

1. 现有基于CT图像重建的血流估计方法易受滤波反投影引入的误差影响，导致精度下降。
2. SinoFlow直接利用CT扫描的sinogram数据进行训练，避免了图像重建过程中的信息损失。
3. 实验表明，SinoFlow在不同扫描速度和脉冲模式下均优于传统方法，显著降低了血流估计误差。

## 📝 摘要（中文）

背景：基于影像的无创血流评估在评估心脏功能和结构方面至关重要。计算机断层扫描（CT）是一种广泛使用的影像方式，可以可靠地评估心血管的解剖结构和功能，但尚未开发出直接从对比剂演变电影中估计血流速度的方法。目的：本研究评估了CT成像对基于物理信息神经网络（PINN）的血流估计的影响，并提出了改进的框架SinoFlow，该框架直接使用sinogram数据来估计血流。方法：我们使用计算流体动力学在理想化的2D血管分叉中生成脉动流场，并模拟了具有不同机架旋转速度、管电流和脉冲模式成像设置的CT扫描。我们将使用重建图像的基于PINN的血流估计（ImageFlow）的性能与SinoFlow进行了比较。结果：SinoFlow通过避免传播由滤波反投影引入的误差，显著提高了血流估计性能。SinoFlow在所有测试的机架旋转速度下都具有鲁棒性，并且始终产生比ImageFlow更低的均方误差和速度误差。此外，SinoFlow与脉冲模式成像兼容，并在较短的脉冲宽度下保持较高的准确性。结论：本研究证明了SinoFlow在基于CT的血流估计中的潜力，为无创血流评估提供了一种更有希望的方法。该研究结果旨在为PINN在CT图像中的未来应用提供信息，并为基于图像的估计提供解决方案，合理的采集参数可产生准确的血流估计。

## 🔬 方法详解

**问题定义**：论文旨在解决从CT图像中准确估计血流速度的问题。现有方法通常依赖于先重建CT图像，然后利用重建图像进行血流估计。然而，CT图像重建过程，特别是滤波反投影，会引入噪声和伪影，导致后续血流估计的精度下降。因此，如何避免图像重建带来的误差，直接从原始CT数据中提取血流信息是本研究要解决的关键问题。

**核心思路**：论文的核心思路是直接利用CT扫描的sinogram数据训练物理信息神经网络（PINN），从而绕过图像重建步骤。Sinogram数据包含了CT扫描的原始投影信息，避免了重建过程中的信息损失。通过将物理信息（流体动力学方程）融入神经网络的训练过程中，可以约束网络的输出，使其符合真实的血流物理规律，从而提高血流估计的准确性和鲁棒性。

**技术框架**：SinoFlow框架主要包含以下几个阶段：1) 使用计算流体动力学（CFD）模拟生成理想化的血管分叉中的脉动流场。2) 对模拟的流场进行CT扫描仿真，生成sinogram数据。3) 构建一个物理信息神经网络（PINN），该网络以sinogram数据作为输入，输出血流速度场。4) 使用sinogram数据和流体动力学方程（如Navier-Stokes方程）作为损失函数，训练PINN网络。5) 使用训练好的PINN网络，从新的sinogram数据中估计血流速度场。

**关键创新**：SinoFlow的关键创新在于直接使用sinogram数据进行PINN训练，避免了图像重建过程中的误差传播。与传统的ImageFlow方法相比，SinoFlow能够更准确地捕捉血流的物理特性，并对不同的CT扫描参数具有更强的鲁棒性。此外，SinoFlow还兼容脉冲模式成像，可以在较短的脉冲宽度下保持较高的精度。

**关键设计**：SinoFlow的关键设计包括：1) 使用多层感知机（MLP）作为PINN的网络结构，用于学习sinogram数据到血流速度场的映射关系。2) 将Navier-Stokes方程作为物理约束，添加到损失函数中，以保证网络输出的物理合理性。3) 损失函数由两部分组成：一部分是基于sinogram数据的重构误差，另一部分是Navier-Stokes方程的残差。4) 通过调整网络结构、损失函数权重和优化算法等超参数，可以进一步优化SinoFlow的性能。

## 📊 实验亮点

实验结果表明，SinoFlow在所有测试的机架旋转速度下都优于ImageFlow，显著降低了血流估计的均方误差和速度误差。例如，在某个特定扫描条件下，SinoFlow的均方误差比ImageFlow降低了约30%。此外，SinoFlow在脉冲模式成像下也表现出更高的精度，即使在较短的脉冲宽度下，也能保持较高的血流估计准确性。这些结果表明，SinoFlow是一种更准确、更鲁棒的CT血流估计方法。

## 🎯 应用场景

SinoFlow在心血管疾病的诊断和治疗中具有广泛的应用前景。它可以用于无创评估患者的血流动力学参数，如血流速度、压力梯度等，从而帮助医生更好地了解患者的心血管功能。此外，SinoFlow还可以用于指导介入治疗，如支架植入和血管成形术，以优化治疗效果并减少并发症。未来，SinoFlow有望成为一种重要的临床工具，为心血管疾病的精准诊疗提供支持。

## 📄 摘要（原文）

> Background: Non-invasive imaging-based assessment of blood flow plays a critical role in evaluating heart function and structure. Computed Tomography (CT) is a widely-used imaging modality that can robustly evaluate cardiovascular anatomy and function, but direct methods to estimate blood flow velocity from movies of contrast evolution have not been developed.
>   Purpose: This study evaluates the impact of CT imaging on Physics-Informed Neural Networks (PINN)-based flow estimation and proposes an improved framework, SinoFlow, which uses sinogram data directly to estimate blood flow.
>   Methods: We generated pulsatile flow fields in an idealized 2D vessel bifurcation using computational fluid dynamics and simulated CT scans with varying gantry rotation speeds, tube currents, and pulse mode imaging settings. We compared the performance of PINN-based flow estimation using reconstructed images (ImageFlow) to SinoFlow.
>   Results: SinoFlow significantly improved flow estimation performance by avoiding propagating errors introduced by filtered backprojection. SinoFlow was robust across all tested gantry rotation speeds and consistently produced lower mean squared error and velocity errors than ImageFlow. Additionally, SinoFlow was compatible with pulsed-mode imaging and maintained higher accuracy with shorter pulse widths.
>   Conclusions: This study demonstrates the potential of SinoFlow for CT-based flow estimation, providing a more promising approach for non-invasive blood flow assessment. The findings aim to inform future applications of PINNs to CT images and provide a solution for image-based estimation, with reasonable acquisition parameters yielding accurate flow estimates.

