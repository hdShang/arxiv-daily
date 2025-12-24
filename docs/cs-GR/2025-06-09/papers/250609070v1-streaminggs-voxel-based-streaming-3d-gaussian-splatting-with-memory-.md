---
layout: default
title: "STREAMINGGS: Voxel-Based Streaming 3D Gaussian Splatting with Memory Optimization and Architectural Support"
---

# STREAMINGGS: Voxel-Based Streaming 3D Gaussian Splatting with Memory Optimization and Architectural Support

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09070" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09070v1</a>
  <a href="https://arxiv.org/pdf/2506.09070.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09070v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09070v1', 'STREAMINGGS: Voxel-Based Streaming 3D Gaussian Splatting with Memory Optimization and Architectural Support')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenqi Zhang, Yu Feng, Jieru Zhao, Guangda Liu, Wenchao Ding, Chentao Wu, Minyi Guo

**分类**: cs.GR, cs.AI

**发布日期**: 2025-06-09

---

## 💡 一句话要点

**提出STREAMINGGS以解决移动设备上3D高斯渲染效率不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯渲染` `内存优化` `实时渲染` `移动设备` `算法架构协同设计`

## 📋 核心要点

1. 现有的3D高斯渲染方法在移动设备上无法达到实时性能，导致用户体验不佳。
2. STREAMINGGS通过算法与架构的协同设计，优化内存使用，提升渲染效率，解决了DRAM流量冗余的问题。
3. 实验结果显示，STREAMINGGS在速度和能耗方面分别比移动Ampere GPU提升了45.7倍和62.9倍。

## 📝 摘要（中文）

3D高斯渲染（3DGS）因其高效的稀疏高斯表示而受到关注。然而，3DGS在资源受限的移动设备上无法满足每秒90帧的实时要求，仅能达到2到9帧。现有加速器专注于计算效率，却忽视了内存效率，导致冗余的DRAM流量。我们提出了STREAMINGGS，这是一种完全流式的3DGS算法-架构协同设计，通过从以块为中心的渲染转变为以内存为中心的渲染，实现了细粒度的流水线处理，并减少了DRAM流量。结果表明，我们的设计在移动Ampere GPU上实现了高达45.7倍的速度提升和62.9倍的能耗节省。

## 🔬 方法详解

**问题定义**：本论文旨在解决3D高斯渲染在移动设备上无法实现实时性能的问题。现有方法在计算效率上有所突破，但在内存效率方面存在不足，导致DRAM流量冗余，影响整体性能。

**核心思路**：STREAMINGGS的核心思路是通过算法与架构的协同设计，转变渲染方式，从以块为中心的渲染转向以内存为中心的渲染。这种设计旨在优化内存访问模式，提高数据流动性，从而提升渲染速度。

**技术框架**：STREAMINGGS的整体架构包括数据预处理模块、内存管理模块和渲染模块。数据预处理模块负责将输入数据转换为适合流式处理的格式，内存管理模块优化数据存取，渲染模块则执行实际的3D高斯渲染。

**关键创新**：本研究的关键创新在于实现了细粒度的流水线处理，显著减少了DRAM流量。这一创新与现有方法的本质区别在于其内存中心的渲染策略，能够有效降低内存带宽的需求。

**关键设计**：在设计中，STREAMINGGS采用了动态内存分配策略，以适应不同场景下的数据需求。同时，优化了数据缓存策略，减少了不必要的数据传输，提升了整体渲染效率。具体的参数设置和损失函数设计则根据实验反馈不断调整，以确保最佳性能。

## 📊 实验亮点

STREAMINGGS在实验中表现出色，相较于移动Ampere GPU，其渲染速度提升高达45.7倍，能耗节省达到62.9倍。这些结果表明，该方法在实际应用中具有显著的性能优势，能够满足高帧率的实时渲染需求。

## 🎯 应用场景

STREAMINGGS的研究成果在多个领域具有广泛的应用潜力，包括虚拟现实、增强现实和移动游戏等。其高效的渲染能力能够为用户提供更流畅的体验，推动移动设备在3D图形处理方面的进一步发展。未来，该技术还可能在智能城市、自动驾驶等领域发挥重要作用。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has gained popularity for its efficiency and sparse Gaussian-based representation. However, 3DGS struggles to meet the real-time requirement of 90 frames per second (FPS) on resource-constrained mobile devices, achieving only 2 to 9 FPS.Existing accelerators focus on compute efficiency but overlook memory efficiency, leading to redundant DRAM traffic. We introduce STREAMINGGS, a fully streaming 3DGS algorithm-architecture co-design that achieves fine-grained pipelining and reduces DRAM traffic by transforming from a tile-centric rendering to a memory-centric rendering. Results show that our design achieves up to 45.7 $\times$ speedup and 62.9 $\times$ energy savings over mobile Ampere GPUs.

