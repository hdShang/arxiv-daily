---
layout: default
title: Accelerated Feature Detectors for Visual SLAM: A Comparative Study of FPGA vs GPU
---

# Accelerated Feature Detectors for Visual SLAM: A Comparative Study of FPGA vs GPU

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13546" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13546v1</a>
  <a href="https://arxiv.org/pdf/2510.13546.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13546v1" onclick="toggleFavorite(this, '2510.13546v1', 'Accelerated Feature Detectors for Visual SLAM: A Comparative Study of FPGA vs GPU')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruiqi Ye, Mikel Luján

**分类**: cs.CV, cs.ET, cs.PF, cs.RO

**发布日期**: 2025-10-15

**备注**: 12 pages, 7 figures

---

## 💡 一句话要点

**对比FPGA与GPU加速的特征检测器在视觉SLAM中的性能与能效**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉SLAM` `特征检测` `GPU加速` `FPGA加速` `硬件加速` `性能评估` `能效优化`

## 📋 核心要点

1. 视觉SLAM中的特征检测模块耗时较多，且越来越多地部署在无人机等功耗受限的平台上，需要高效的加速方案。
2. 本文对比研究了GPU和FPGA加速的FAST、Harris和SuperPoint特征检测器在视觉SLAM流水线中的性能和能效。
3. 实验结果表明，非学习型检测器GPU加速更优，学习型检测器FPGA加速更优，且硬件加速能提升V-SLAM整体性能。

## 📝 摘要（中文）

本文首次研究了硬件加速的特征检测器在视觉SLAM（V-SLAM）流水线中的应用。通过在现代SoC（Nvidia Jetson Orin和AMD Versal）上比较GPU加速的FAST、Harris和SuperPoint实现与FPGA加速的对应实现，提供了新的见解。评估表明，对于FAST和Harris等非学习型特征检测器，其GPU实现以及GPU加速的V-SLAM在运行时性能和能效方面优于FPGA实现。然而，对于SuperPoint等基于学习的检测器，其FPGA实现可以实现更好的运行时性能和能效（分别高达3.1倍和1.4倍的提升）。FPGA加速的V-SLAM在运行时性能方面与GPU加速的V-SLAM相当，在5个数据集序列中有2个实现了更好的FPS。在精度方面，GPU加速的V-SLAM通常比FPGA加速的V-SLAM更准确。最后，硬件加速特征检测的使用可以通过降低全局BA模块的调用频率来进一步提高V-SLAM流水线的性能，同时不牺牲精度。

## 🔬 方法详解

**问题定义**：视觉SLAM系统中的特征检测是计算密集型任务，尤其是在资源受限的平台（如无人机）上，需要高效的硬件加速方案。现有的研究主要集中在GPU加速上，而忽略了FPGA在能效方面的潜力。因此，本文旨在对比研究GPU和FPGA加速的特征检测器在视觉SLAM中的性能和能效，为硬件加速方案的选择提供指导。

**核心思路**：本文的核心思路是针对不同类型的特征检测器（传统算法和深度学习方法），评估GPU和FPGA加速的性能差异。通过在相同的硬件平台上运行不同的特征检测器和视觉SLAM流水线，并测量其运行时性能、能效和精度，从而确定哪种硬件加速方案更适合特定的特征检测器。

**技术框架**：本文的整体框架包括以下几个主要步骤：1) 选择三种具有代表性的特征检测器：FAST、Harris（传统算法）和SuperPoint（深度学习方法）；2) 分别在GPU（Nvidia Jetson Orin）和FPGA（AMD Versal）上实现这些特征检测器；3) 将这些特征检测器集成到视觉SLAM流水线中；4) 在多个数据集上评估不同硬件加速方案的性能、能效和精度。

**关键创新**：本文最重要的创新点在于首次对GPU和FPGA加速的特征检测器在视觉SLAM流水线中进行了全面的对比研究。以往的研究主要集中在单个特征检测器的硬件加速上，而忽略了其在实际视觉SLAM系统中的表现。此外，本文还发现，对于不同类型的特征检测器，GPU和FPGA加速的性能差异很大，这为硬件加速方案的选择提供了重要的指导。

**关键设计**：本文的关键设计包括：1) 选择了具有代表性的GPU（Nvidia Jetson Orin）和FPGA（AMD Versal）平台；2) 针对不同的硬件平台，对特征检测器进行了优化，以充分利用其硬件特性；3) 使用了多个数据集来评估不同硬件加速方案的泛化能力；4) 详细测量了运行时性能、能效和精度等指标，以全面评估不同硬件加速方案的优缺点。

## 📊 实验亮点

实验结果表明，对于非学习型特征检测器（FAST、Harris），GPU加速的V-SLAM在运行时性能和能效方面优于FPGA加速的V-SLAM。而对于学习型特征检测器（SuperPoint），FPGA实现可以实现更好的运行时性能和能效（分别高达3.1倍和1.4倍的提升）。在精度方面，GPU加速的V-SLAM通常更准确。

## 🎯 应用场景

该研究成果可应用于无人机、机器人等需要在资源受限平台上运行视觉SLAM系统的领域。通过选择合适的硬件加速方案，可以提高SLAM系统的性能和能效，从而延长无人机的续航时间或提高机器人的导航精度。此外，该研究还可以为硬件加速器的设计提供指导，促进视觉SLAM技术的进一步发展。

## 📄 摘要（原文）

> Feature detection is a common yet time-consuming module in Simultaneous Localization and Mapping (SLAM) implementations, which are increasingly deployed on power-constrained platforms, such as drones. Graphics Processing Units (GPUs) have been a popular accelerator for computer vision in general, and feature detection and SLAM in particular.
>   On the other hand, System-on-Chips (SoCs) with integrated Field Programmable Gate Array (FPGA) are also widely available. This paper presents the first study of hardware-accelerated feature detectors considering a Visual SLAM (V-SLAM) pipeline. We offer new insights by comparing the best GPU-accelerated FAST, Harris, and SuperPoint implementations against the FPGA-accelerated counterparts on modern SoCs (Nvidia Jetson Orin and AMD Versal).
>   The evaluation shows that when using a non-learning-based feature detector such as FAST and Harris, their GPU implementations, and the GPU-accelerated V-SLAM can achieve better run-time performance and energy efficiency than the FAST and Harris FPGA implementations as well as the FPGA-accelerated V-SLAM. However, when considering a learning-based detector such as SuperPoint, its FPGA implementation can achieve better run-time performance and energy efficiency (up to 3.1$\times$ and 1.4$\times$ improvements, respectively) than the GPU implementation. The FPGA-accelerated V-SLAM can also achieve comparable run-time performance compared to the GPU-accelerated V-SLAM, with better FPS in 2 out of 5 dataset sequences. When considering the accuracy, the results show that the GPU-accelerated V-SLAM is more accurate than the FPGA-accelerated V-SLAM in general. Last but not least, the use of hardware acceleration for feature detection could further improve the performance of the V-SLAM pipeline by having the global bundle adjustment module invoked less frequently without sacrificing accuracy.

