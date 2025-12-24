---
layout: default
title: "FGGS-LiDAR: Ultra-Fast, GPU-Accelerated Simulation from General 3DGS Models to LiDAR"
---

# FGGS-LiDAR: Ultra-Fast, GPU-Accelerated Simulation from General 3DGS Models to LiDAR

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.17390" class="toolbar-btn" target="_blank">📄 arXiv: 2509.17390v1</a>
  <a href="https://arxiv.org/pdf/2509.17390.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.17390v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.17390v1', 'FGGS-LiDAR: Ultra-Fast, GPU-Accelerated Simulation from General 3DGS Models to LiDAR')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junzhe Wu, Yufei Jia, Yiyi Yan, Zhixing Chen, Tiao Tan, Zifan Wang, Guangyu Wang

**分类**: cs.RO

**发布日期**: 2025-09-22

**🔗 代码/项目**: [GITHUB](https://github.com/TATP-233/FGGS-LiDAR)

---

## 💡 一句话要点

**FGGS-LiDAR：基于通用3DGS模型的超快速GPU加速LiDAR仿真**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LiDAR仿真` `3D高斯溅射` `GPU加速` `自动驾驶` `机器人` `网格重建` `TSDF` `光线投射`

## 📋 核心要点

1. 现有3DGS资产无法直接用于高性能LiDAR仿真，限制了其在机器人和自动驾驶领域的应用。
2. FGGS-LiDAR通过通用流程将3DGS模型转换为高保真网格，并结合GPU加速光线投射实现快速LiDAR仿真。
3. 实验表明，该方法在室内外场景中实现了卓越的几何保真度，仿真速度超过500 FPS。

## 📝 摘要（中文）

本文提出FGGS-LiDAR框架，旨在弥合3D高斯溅射(3DGS)与高性能LiDAR仿真之间的差距，实现真正的即插即用。该方法将*任何*预训练的3DGS模型转换为高保真、水密的网格，无需LiDAR特定的监督或架构修改。这种转换通过体素离散化和截断符号距离场(TSDF)提取的通用流程实现。同时，结合高度优化的GPU加速光线投射模块，以超过500 FPS的速度模拟LiDAR回波。在室内和室外场景中验证了该方法的有效性，展示了卓越的几何保真度。通过直接重用3DGS资产进行几何精确的深度感知，该框架扩展了其在可视化之外的效用，并为可扩展的多模态仿真解锁了新的能力。该开源实现在https://github.com/TATP-233/FGGS-LiDAR提供。

## 🔬 方法详解

**问题定义**：现有方法无法直接将3D高斯溅射(3DGS)模型用于LiDAR仿真。3DGS模型主要用于渲染，缺乏几何信息，无法直接用于模拟LiDAR传感器的深度感知过程。因此，需要一种方法将3DGS模型转换为适合LiDAR仿真的格式，同时保持几何精度和仿真速度。

**核心思路**：FGGS-LiDAR的核心思路是将3DGS模型转换为高保真、水密的网格模型，然后使用GPU加速的光线投射技术模拟LiDAR的回波。通过体素化和TSDF提取，可以从3DGS模型中恢复出几何信息，并生成高质量的网格。GPU加速的光线投射能够显著提高仿真速度，满足实时应用的需求。

**技术框架**：FGGS-LiDAR框架主要包含两个阶段：1) 3DGS到网格的转换：首先对3DGS模型进行体素化，然后使用截断符号距离场(TSDF)提取表面信息，最后生成水密的网格模型。2) GPU加速的LiDAR仿真：使用GPU加速的光线投射模块，将LiDAR传感器发出的光线投射到网格模型上，计算反射点的位置和强度，模拟LiDAR的回波。

**关键创新**：FGGS-LiDAR的关键创新在于其通用性和高效性。该方法可以处理*任何*预训练的3DGS模型，无需LiDAR特定的监督或架构修改。同时，通过GPU加速的光线投射，实现了超快的仿真速度，远超现有方法。与现有方法相比，FGGS-LiDAR能够更方便地利用大量的3DGS资产进行LiDAR仿真，扩展了3DGS模型的应用范围。

**关键设计**：在3DGS到网格的转换阶段，体素的大小和TSDF的截断距离是两个关键参数。体素大小决定了网格的精度，截断距离影响了表面的平滑度。在GPU加速的LiDAR仿真阶段，光线投射的步长和反射模型的参数需要仔细调整，以保证仿真精度和速度。

## 📊 实验亮点

FGGS-LiDAR在室内和室外场景中实现了卓越的几何保真度，能够准确地模拟LiDAR的回波。通过GPU加速，该框架实现了超过500 FPS的仿真速度，远超现有方法。实验结果表明，FGGS-LiDAR能够有效地将3DGS模型转换为高质量的LiDAR仿真数据，为自动驾驶算法的训练和评估提供了有力的支持。

## 🎯 应用场景

FGGS-LiDAR可广泛应用于机器人和自动驾驶领域。它可以用于生成大规模、高保真的LiDAR仿真数据，用于训练和评估自动驾驶算法。此外，该框架还可以用于虚拟环境的构建和测试，帮助开发者在真实环境中部署机器人系统之前进行充分的验证。该研究为多模态仿真提供了一种新的途径，有望加速自动驾驶技术的研发和应用。

## 📄 摘要（原文）

> While 3D Gaussian Splatting (3DGS) has revolutionized photorealistic rendering, its vast ecosystem of assets remains incompatible with high-performance LiDAR simulation, a critical tool for robotics and autonomous driving. We present \textbf{FGGS-LiDAR}, a framework that bridges this gap with a truly plug-and-play approach. Our method converts \textit{any} pretrained 3DGS model into a high-fidelity, watertight mesh without requiring LiDAR-specific supervision or architectural alterations. This conversion is achieved through a general pipeline of volumetric discretization and Truncated Signed Distance Field (TSDF) extraction. We pair this with a highly optimized, GPU-accelerated ray-casting module that simulates LiDAR returns at over 500 FPS. We validate our approach on indoor and outdoor scenes, demonstrating exceptional geometric fidelity; By enabling the direct reuse of 3DGS assets for geometrically accurate depth sensing, our framework extends their utility beyond visualization and unlocks new capabilities for scalable, multimodal simulation. Our open-source implementation is available at https://github.com/TATP-233/FGGS-LiDAR.

