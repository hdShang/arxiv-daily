---
layout: default
title: Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey
---

# Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12384" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12384v1</a>
  <a href="https://arxiv.org/pdf/2505.12384.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12384v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12384v1', 'Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Calvin Galagain, Martyna Poreba, François Goulette

**分类**: cs.RO

**发布日期**: 2025-05-18

---

## 💡 一句话要点

**比较不同语义SLAM方法在嵌入式系统中的适用性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `语义SLAM` `嵌入式系统` `几何SLAM` `神经辐射场` `3D高斯点云` `算法优化` `资源受限`

## 📋 核心要点

1. 现有的语义SLAM方法在嵌入式系统中面临计算资源和功耗的限制，难以实现高效的环境感知与决策。
2. 论文通过比较几何SLAM、神经辐射场和3D高斯点云等架构，提出了适合嵌入式平台的SLAM算法改进方向。
3. 实验结果显示，语义几何SLAM在计算效率和准确性上表现更佳，适合在资源受限的环境中应用。

## 📝 摘要（中文）

在嵌入式系统中，机器人需要高效感知和解读环境，以便在真实条件下可靠运行。视觉语义SLAM通过将语义信息融入地图，增强了标准SLAM的能力，从而支持更为明智的决策。然而，在资源受限的硬件上实现这些系统涉及准确性、计算效率和功耗之间的权衡。本文对近期的语义视觉SLAM方法进行了比较评审，重点关注其在嵌入式平台上的适用性。我们分析了几种主要架构，包括几何SLAM、神经辐射场（NeRF）和3D高斯点云，并评估了它们在NVIDIA Jetson AGX Orin等受限硬件上的性能。结果表明，基于NeRF和高斯点云的方法虽然语义细节丰富，但计算资源需求高，限制了其在嵌入式设备上的应用。相对而言，语义几何SLAM在计算成本和准确性之间提供了更为实用的平衡。

## 🔬 方法详解

**问题定义**：本文旨在解决语义SLAM在嵌入式系统中应用的挑战，特别是计算资源和功耗的限制。现有方法如NeRF和高斯点云虽然提供了高语义细节，但对硬件要求过高，难以在嵌入式设备上实现。

**核心思路**：论文提出通过比较不同SLAM架构，寻找在嵌入式环境中实现高效语义感知的平衡点。重点分析几何SLAM的优势，以期在保证准确性的同时降低计算负担。

**技术框架**：研究中分析了三种主要架构：几何SLAM、神经辐射场（NeRF）和3D高斯点云。每种架构在NVIDIA Jetson AGX Orin上进行性能评估，比较其准确性、分割质量、内存使用和能耗。

**关键创新**：论文的创新点在于系统性地评估了不同SLAM方法在嵌入式平台上的适用性，强调了算法与硬件协同设计的重要性，以提高效率。

**关键设计**：在实验中，针对每种架构设置了不同的参数，评估了其在内存和能耗方面的表现，特别关注了几何SLAM在资源受限环境中的优化潜力。通过这些设计，研究为未来的SLAM算法提供了改进方向。

## 📊 实验亮点

实验结果表明，基于神经辐射场和高斯点云的方法在语义细节上表现优异，但计算资源需求高，限制了其在嵌入式设备上的应用。相比之下，语义几何SLAM在计算效率和准确性上提供了更好的平衡，适合在NVIDIA Jetson AGX Orin等受限硬件上运行。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人、无人驾驶汽车和智能家居等场景，能够在资源受限的嵌入式系统中实现高效的环境感知与决策。随着技术的进步，未来可能会推动更多智能设备的普及与应用。

## 📄 摘要（原文）

> In embedded systems, robots must perceive and interpret their environment efficiently to operate reliably in real-world conditions. Visual Semantic SLAM (Simultaneous Localization and Mapping) enhances standard SLAM by incorporating semantic information into the map, enabling more informed decision-making. However, implementing such systems on resource-limited hardware involves trade-offs between accuracy, computing efficiency, and power usage.
>   This paper provides a comparative review of recent Semantic Visual SLAM methods with a focus on their applicability to embedded platforms. We analyze three main types of architectures - Geometric SLAM, Neural Radiance Fields (NeRF), and 3D Gaussian Splatting - and evaluate their performance on constrained hardware, specifically the NVIDIA Jetson AGX Orin. We compare their accuracy, segmentation quality, memory usage, and energy consumption.
>   Our results show that methods based on NeRF and Gaussian Splatting achieve high semantic detail but demand substantial computing resources, limiting their use on embedded devices. In contrast, Semantic Geometric SLAM offers a more practical balance between computational cost and accuracy. The review highlights a need for SLAM algorithms that are better adapted to embedded environments, and it discusses key directions for improving their efficiency through algorithm-hardware co-design.

