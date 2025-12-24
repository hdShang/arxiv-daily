---
layout: default
title: "XR-NPE: High-Throughput Mixed-precision SIMD Neural Processing Engine for Extended Reality Perception Workloads"
---

# XR-NPE: High-Throughput Mixed-precision SIMD Neural Processing Engine for Extended Reality Perception Workloads

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13049" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13049v1</a>
  <a href="https://arxiv.org/pdf/2508.13049.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13049v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13049v1', 'XR-NPE: High-Throughput Mixed-precision SIMD Neural Processing Engine for Extended Reality Perception Workloads')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tejas Chaudhari, Akarsh J., Tanushree Dewangan, Mukul Lokhande, Santosh Kumar Vishvakarma

**分类**: cs.AR, cs.AI, cs.CV, eess.IV

**发布日期**: 2025-08-18

**🔗 代码/项目**: [GITHUB](https://github.com/mukullokhande99/XR-NPE)

---

## 💡 一句话要点

**提出XR-NPE以解决扩展现实感知工作负载的高效计算问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `扩展现实` `神经处理引擎` `混合精度` `视觉惯性测程` `能效提升` `量化感知训练` `SIMD架构`

## 📋 核心要点

1. 现有方法在处理扩展现实感知工作负载时，面临高能耗和低算力效率的挑战。
2. XR-NPE通过支持多种混合精度格式和量化感知训练，显著提高了计算效率和降低了内存带宽需求。
3. 实验结果表明，XR-NPE在VIO工作负载上提供了23%的能效提升和4%的计算密度提升，且在资源受限的XR设备中具有良好的扩展性。

## 📝 摘要（中文）

本研究提出了XR-NPE，一种高吞吐量的混合精度SIMD神经处理引擎，专为扩展现实（XR）感知工作负载设计，如视觉惯性测程（VIO）、物体分类和眼动提取。XR-NPE首次支持FP4、Posit（4,1）、Posit（8,0）和Posit（16,1）格式，采用层自适应混合算法实现，支持超低位精度以显著降低内存带宽需求，并辅以量化感知训练以最小化精度损失。所提出的可重构尾数乘法和指数处理电路（RMMEC）减少了SIMD MAC计算引擎中的暗硅，结合选择性功率门控降低能耗，提供了2.85倍的算术强度提升。XR-NPE在CMOS 28nm下实现了最大工作频率1.72 GHz，面积0.016 mm²，算术强度14 pJ，相比现有最佳MAC方法减少了42%的面积和38%的功耗。

## 🔬 方法详解

**问题定义**：本论文旨在解决扩展现实（XR）感知工作负载在计算效率和能耗方面的不足，现有方法在处理视觉惯性测程（VIO）等任务时，往往面临高能耗和低算力效率的问题。

**核心思路**：论文提出的XR-NPE通过支持多种混合精度格式（如FP4和Posit格式），结合量化感知训练，能够在保持精度的同时显著降低内存带宽需求，从而提升计算效率。

**技术框架**：XR-NPE的整体架构包括可重构尾数乘法和指数处理电路（RMMEC），通过选择性功率门控技术降低能耗，整体设计旨在提高算术强度和计算密度。

**关键创新**：XR-NPE的主要创新在于首次支持多种低位精度格式，并通过层自适应混合算法实现高效计算，显著减少了暗硅现象，提升了能效。

**关键设计**：在设计中，XR-NPE采用了量化感知训练以减少精度损失，并通过优化电路设计实现了1.72 GHz的最大工作频率和14 pJ的算术强度，展现出优越的性能指标。

## 📊 实验亮点

实验结果显示，XR-NPE在VIO工作负载上实现了23%的能效提升和4%的计算密度提升，相比于现有最先进的加速器，减少了1.4倍的查找表（LUTs）和1.77倍的触发器（FFs），展现出显著的性能优势。

## 🎯 应用场景

XR-NPE的设计适用于各种扩展现实应用，如增强现实和虚拟现实中的实时视觉处理任务。其高效的计算能力和低能耗特性使其在资源受限的设备中具有广泛的应用潜力，能够推动XR技术的进一步发展和普及。

## 📄 摘要（原文）

> This work proposes XR-NPE, a high-throughput Mixed-precision SIMD Neural Processing Engine, designed for extended reality (XR) perception workloads like visual inertial odometry (VIO), object classification, and eye gaze extraction. XR-NPE is first to support FP4, Posit (4,1), Posit (8,0), and Posit (16,1) formats, with layer adaptive hybrid-algorithmic implementation supporting ultra-low bit precision to significantly reduce memory bandwidth requirements, and accompanied by quantization-aware training for minimal accuracy loss. The proposed Reconfigurable Mantissa Multiplication and Exponent processing Circuitry (RMMEC) reduces dark silicon in the SIMD MAC compute engine, assisted by selective power gating to reduce energy consumption, providing 2.85x improved arithmetic intensity. XR-NPE achieves a maximum operating frequency of 1.72 GHz, area 0.016 mm2 , and arithmetic intensity 14 pJ at CMOS 28nm, reducing 42% area, 38% power compared to the best of state-of-the-art MAC approaches. The proposed XR-NPE based AXI-enabled Matrix-multiplication co-processor consumes 1.4x fewer LUTs, 1.77x fewer FFs, and provides 1.2x better energy efficiency compared to SoTA accelerators on VCU129. The proposed co-processor provides 23% better energy efficiency and 4% better compute density for VIO workloads. XR-NPE establishes itself as a scalable, precision-adaptive compute engine for future resource-constrained XR devices. The complete set for codes for results reproducibility are released publicly, enabling designers and researchers to readily adopt and build upon them. https://github.com/mukullokhande99/XR-NPE.

