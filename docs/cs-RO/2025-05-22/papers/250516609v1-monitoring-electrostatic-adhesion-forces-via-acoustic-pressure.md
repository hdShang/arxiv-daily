---
layout: default
title: Monitoring Electrostatic Adhesion Forces via Acoustic Pressure
---

# Monitoring Electrostatic Adhesion Forces via Acoustic Pressure

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.16609" class="toolbar-btn" target="_blank">📄 arXiv: 2505.16609v1</a>
  <a href="https://arxiv.org/pdf/2505.16609.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.16609v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.16609v1', 'Monitoring Electrostatic Adhesion Forces via Acoustic Pressure')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huacen Wang, Jiarui Zou, Zeju Zheng, Hongqiang Wang

**分类**: cs.RO, eess.SP

**发布日期**: 2025-05-22

**备注**: 6 pages, 7 figures

---

## 💡 一句话要点

**提出基于声压监测静电附着力的方法以解决传感器复杂性问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `静电附着力` `声压监测` `非接触传感` `移动机器人` `质量估计` `智能制造` `人机交互`

## 📋 核心要点

1. 现有的静电附着力监测方法依赖于昂贵且笨重的传感器，增加了系统的复杂性和重量。
2. 本文提出了一种基于声压的非接触监测方法，通过声学信号捕捉静电附着力的变化。
3. 实验结果表明，声压峰值与附着物体的质量、接触面积及驱动电压的参数呈正相关，验证了方法的有效性。

## 📝 摘要（中文）

静电附着力广泛应用于移动机器人、触觉技术和机器人末端执行器，因其适应多种基材和低能耗而受到青睐。然而，现有的静电附着力监测方法通常依赖于笨重且昂贵的传感器，增加了系统的复杂性和重量。本文提出了一种基于声压的方法，通过非接触方式监测静电附着力。当静电附着垫通过双极方波电压驱动以附着导电物体时，EA系统会产生周期性的声学脉冲。我们使用麦克风捕捉这些声压信号，并研究峰值压力的影响。结果表明，声压的峰值随着附着物体的质量、接触面积以及驱动电压的幅度和频率的增加而增加。该技术可用于各种物体的质量估计及同时监测两个EA系统，并集成到EA末端执行器中，实现运输过程中附着物体质量的监测。该方法提供了一种低成本、非接触和多物体监测的解决方案。

## 🔬 方法详解

**问题定义**：现有静电附着力监测方法依赖于复杂且昂贵的传感器，导致系统重量增加和成本上升，限制了其在移动机器人等领域的应用。

**核心思路**：本文提出了一种基于声压的监测方法，通过非接触方式捕捉声学信号来监测静电附着力，旨在简化系统设计并降低成本。

**技术框架**：该方法的整体架构包括声学信号的捕捉、信号处理和数据分析三个主要模块。首先，使用麦克风捕捉EA系统产生的声学脉冲，然后对信号进行处理以提取峰值压力，最后分析与附着物体特性的关系。

**关键创新**：最重要的技术创新在于通过声压信号实现静电附着力的非接触监测，这与传统依赖物理传感器的方法本质上不同，显著降低了系统复杂性。

**关键设计**：在实验中，驱动电压的幅度和频率被系统地调整，以观察其对声压峰值的影响，同时考虑了附着物体的质量和接触面积等参数，确保了监测结果的准确性。

## 📊 实验亮点

实验结果显示，声压峰值与附着物体的质量和接触面积呈正相关，且通过调整驱动电压的幅度和频率，声压峰值显著提高。这表明该方法在静电附着力监测中的有效性，提供了一种新的性能基准。

## 🎯 应用场景

该研究的潜在应用领域包括移动机器人、智能制造和人机交互等，能够为这些领域提供一种低成本、高效的静电附着力监测解决方案。未来，该技术有望推动智能设备在复杂环境中的应用，提升其操作灵活性和安全性。

## 📄 摘要（原文）

> Electrostatic adhesion is widely used in mobile robotics, haptics, and robotic end effectors for its adaptability to diverse substrates and low energy consumption. Force sensing is important for feedback control, interaction, and monitoring in the EA system. However, EA force monitoring often relies on bulky and expensive sensors, increasing the complexity and weight of the entire system. This paper presents an acoustic-pressure-based method to monitor EA forces without contacting the adhesion pad. When the EA pad is driven by a bipolar square-wave voltage to adhere a conductive object, periodic acoustic pulses arise from the EA system. We employed a microphone to capture these acoustic pressure signals and investigate the influence of peak pressure values. Results show that the peak value of acoustic pressure increased with the mass and contact area of the adhered object, as well as with the amplitude and frequency of the driving voltage. We applied this technique to mass estimation of various objects and simultaneous monitoring of two EA systems. Then, we integrated this technique into an EA end effector that enables monitoring the change of adhered object mass during transport. The proposed technique offers a low-cost, non-contact, and multi-object monitoring solution for EA end effectors in handling tasks.

