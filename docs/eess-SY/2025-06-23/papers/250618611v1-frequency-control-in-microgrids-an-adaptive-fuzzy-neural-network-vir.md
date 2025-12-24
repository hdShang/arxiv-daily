---
layout: default
title: "Frequency Control in Microgrids: An Adaptive Fuzzy-Neural-Network Virtual Synchronous Generator"
---

# Frequency Control in Microgrids: An Adaptive Fuzzy-Neural-Network Virtual Synchronous Generator

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18611" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18611v1</a>
  <a href="https://arxiv.org/pdf/2506.18611.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18611v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18611v1', 'Frequency Control in Microgrids: An Adaptive Fuzzy-Neural-Network Virtual Synchronous Generator')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Waleed Breesam, Rezvan Alamian, Nima Tashakor, Brahim Elkhalil Youcefa, Stefan M. Goetz

**分类**: eess.SY, cs.AI

**发布日期**: 2025-06-23

**备注**: 11 pages, 17 figures

---

## 💡 一句话要点

**提出自适应模糊神经网络虚拟同步发电机以解决微电网频率控制问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `虚拟同步发电机` `模糊神经网络` `频率控制` `微电网` `可再生能源`

## 📋 核心要点

1. 现有的虚拟同步发电机在频率调节方面存在固定参数无法适应动态变化的问题，导致频率控制效果不佳。
2. 本文提出了一种基于模糊神经网络的控制器，能够动态调整虚拟同步发电机的惯性、阻尼和下垂参数，以实现更稳定的频率控制。
3. 实验结果显示，该方法将频率偏差降低至0.03 Hz以下，并显著缩短了系统的稳定和恢复时间，相较于传统方法有显著提升。

## 📝 摘要（中文）

近年来，分布式可再生能源的依赖性增加，导致基于电力电子的分布式发电机取代了同步发电机，改变了微电网的动态特性，尤其是降低了系统的惯性和阻尼。虚拟同步发电机通过模仿同步发电机的动态行为来解决这一问题。然而，固定的虚拟同步发电机参数无法保证频率调节在可接受的容差范围内。本文提出了一种通过模糊神经网络控制器动态调整惯性、阻尼和下垂参数的方法，该控制器能够在线自我训练以选择适当的虚拟参数值。通过MATLAB/Simulink模型进行系统研究，并在基于嵌入式ARM系统的硬件在环实验中进行验证。与传统和模糊逻辑控制器方法相比，结果表明该方法显著降低频率偏差至0.03 Hz以下，并缩短了稳定/恢复时间。

## 🔬 方法详解

**问题定义**：本文旨在解决微电网中由于可再生能源的渗透导致的频率控制问题，现有方法的固定参数无法适应系统动态变化，造成频率调节不稳定。

**核心思路**：通过引入模糊神经网络控制器，动态调整虚拟同步发电机的关键参数（惯性、阻尼和下垂），以实现更灵活和稳定的频率控制。该设计能够实时响应系统状态变化，优化频率调节效果。

**技术框架**：整体架构包括模糊神经网络控制器、虚拟同步发电机模型和微电网系统。控制器根据实时数据调整虚拟参数，确保频率在可接受范围内。

**关键创新**：最重要的创新在于使用模糊神经网络进行在线自我训练，动态选择虚拟同步发电机的参数，这一方法与传统固定参数的控制策略形成鲜明对比。

**关键设计**：控制器的设计包括模糊逻辑推理机制和神经网络学习算法，参数设置经过多次实验优化，确保控制器能够快速响应并有效降低频率偏差。损失函数设计用于最小化频率偏差，网络结构采用多层感知器以增强学习能力。

## 📊 实验亮点

实验结果表明，所提方法将频率偏差降低至0.03 Hz以下，相较于传统控制方法，频率稳定性显著提升，并且系统的稳定和恢复时间显著缩短，展示了其优越的性能。

## 🎯 应用场景

该研究的潜在应用领域包括智能电网、微电网控制和可再生能源集成等。通过提高频率控制的稳定性和响应速度，能够有效提升微电网的运行效率和可靠性，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> The reliance on distributed renewable energy has increased recently. As a result, power electronic-based distributed generators replaced synchronous generators which led to a change in the dynamic characteristics of the microgrid. Most critically, they reduced system inertia and damping. Virtual synchronous generators emulated in power electronics, which mimic the dynamic behaviour of synchronous generators, are meant to fix this problem. However, fixed virtual synchronous generator parameters cannot guarantee a frequency regulation within the acceptable tolerance range. Conversely, a dynamic adjustment of these virtual parameters promises robust solution with stable frequency. This paper proposes a method to adapt the inertia, damping, and droop parameters dynamically through a fuzzy neural network controller. This controller trains itself online to choose appropriate values for these virtual parameters. The proposed method can be applied to a typical AC microgrid by considering the penetration and impact of renewable energy sources. We study the system in a MATLAB/Simulink model and validate it experimentally in real time using hardware-in-the-loop based on an embedded ARM system (SAM3X8E, Cortex-M3). Compared to traditional and fuzzy logic controller methods, the results demonstrate that the proposed method significantly reduces the frequency deviation to less than 0.03 Hz and shortens the stabilizing/recovery time.

