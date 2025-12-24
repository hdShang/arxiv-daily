---
layout: default
title: "GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale Multi-Agent Gaussian SLAM"
---

# GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale Multi-Agent Gaussian SLAM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18885" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18885v1</a>
  <a href="https://arxiv.org/pdf/2506.18885.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18885v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18885v1', 'GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale Multi-Agent Gaussian SLAM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How

**分类**: cs.RO, cs.CV

**发布日期**: 2025-06-23

---

## 💡 一句话要点

**提出GRAND-SLAM以解决大规模多智能体高斯SLAM问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `高斯SLAM` `多智能体系统` `局部优化` `回环闭合` `环境重建` `机器人协作` `计算机视觉`

## 📋 核心要点

1. 现有的多智能体高斯SLAM方法主要局限于小规模的室内环境，无法有效处理大规模户外场景。
2. GRAND-SLAM通过引入局部优化的隐式跟踪模块和回环闭合机制，提升了多智能体协作的环境重建能力。
3. 实验结果显示，GRAND-SLAM在多个数据集上均表现出色，显著提高了跟踪精度和渲染质量。

## 📝 摘要（中文）

3D高斯点云已成为RGB-D视觉SLAM的有效场景表示，但其在大规模多智能体户外环境中的应用尚未被探索。多智能体高斯SLAM是快速探索和重建环境的有前景的方法，提供可扩展的环境表示，但现有方法仅限于小规模室内环境。为此，本文提出了基于多智能体密集SLAM的高斯重建方法GRAND-SLAM，集成了基于局部优化的隐式跟踪模块和集成于姿态图优化框架的机器人间和机器人内回环闭合方法。实验表明，GRAND-SLAM在Replica室内数据集上提供了最先进的跟踪性能，PSNR比现有方法高出28%，在大规模户外Kimera-Multi数据集上，多个智能体的跟踪误差降低了91%，渲染效果也有所改善。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多智能体高斯SLAM方法在大规模户外环境中的应用不足，现有方法无法有效处理复杂的场景和多智能体协作问题。

**核心思路**：GRAND-SLAM的核心思路是通过局部优化和回环闭合机制，提升多智能体在大规模环境中的跟踪和重建能力，确保全局一致性。

**技术框架**：GRAND-SLAM的整体架构包括隐式跟踪模块、姿态图优化框架以及回环闭合机制。隐式跟踪模块通过局部优化处理子图，姿态图优化则整合多智能体的位姿信息。

**关键创新**：GRAND-SLAM的主要创新在于将局部优化与多智能体协作相结合，显著提高了跟踪精度和环境重建的效率，与现有方法相比，能够处理更大规模的场景。

**关键设计**：在设计中，GRAND-SLAM采用了特定的损失函数来优化跟踪精度，并在网络结构上进行了调整，以适应多智能体的协作需求。

## 📊 实验亮点

在实验中，GRAND-SLAM在Replica室内数据集上实现了28%的PSNR提升，并在大规模户外Kimera-Multi数据集上降低了91%的多智能体跟踪误差，显示出显著的性能优势和渲染质量的提升。

## 🎯 应用场景

GRAND-SLAM的研究成果具有广泛的应用潜力，尤其在无人驾驶、机器人探索和环境监测等领域。通过提升多智能体在复杂环境中的协作能力，该方法能够有效支持大规模场景的实时重建与导航，推动相关技术的发展与应用。

## 📄 摘要（原文）

> 3D Gaussian splatting has emerged as an expressive scene representation for RGB-D visual SLAM, but its application to large-scale, multi-agent outdoor environments remains unexplored. Multi-agent Gaussian SLAM is a promising approach to rapid exploration and reconstruction of environments, offering scalable environment representations, but existing approaches are limited to small-scale, indoor environments. To that end, we propose Gaussian Reconstruction via Multi-Agent Dense SLAM, or GRAND-SLAM, a collaborative Gaussian splatting SLAM method that integrates i) an implicit tracking module based on local optimization over submaps and ii) an approach to inter- and intra-robot loop closure integrated into a pose-graph optimization framework. Experiments show that GRAND-SLAM provides state-of-the-art tracking performance and 28% higher PSNR than existing methods on the Replica indoor dataset, as well as 91% lower multi-agent tracking error and improved rendering over existing multi-agent methods on the large-scale, outdoor Kimera-Multi dataset.

