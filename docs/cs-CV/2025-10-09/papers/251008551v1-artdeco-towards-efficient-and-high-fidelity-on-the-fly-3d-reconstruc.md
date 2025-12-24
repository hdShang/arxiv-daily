---
layout: default
title: "ARTDECO: Towards Efficient and High-Fidelity On-the-Fly 3D Reconstruction with Structured Scene Representation"
---

# ARTDECO: Towards Efficient and High-Fidelity On-the-Fly 3D Reconstruction with Structured Scene Representation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08551" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08551v1</a>
  <a href="https://arxiv.org/pdf/2510.08551.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08551v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.08551v1', 'ARTDECO: Towards Efficient and High-Fidelity On-the-Fly 3D Reconstruction with Structured Scene Representation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guanghao Li, Kerui Ren, Linning Xu, Zhewen Zheng, Changjian Jiang, Xin Gao, Bo Dai, Jian Pu, Mulin Yu, Jiangmiao Pang

**分类**: cs.CV

**发布日期**: 2025-10-09

**🔗 代码/项目**: [PROJECT_PAGE](https://city-super.github.io/artdeco/)

---

## 💡 一句话要点

**ARTDECO：基于结构化场景表示的高效高保真即时3D重建**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `即时3D重建` `单目视觉` `高斯表示` `分层渲染` `SLAM` `3D基础模型` `场景数字化`

## 📋 核心要点

1. 现有即时3D重建方法面临保真度和计算效率的权衡：逐场景优化保真度高但计算成本高昂，前馈模型速度快但精度和鲁棒性不足。
2. ARTDECO的核心思想是结合前馈模型的效率和SLAM的可靠性，利用3D基础模型进行位姿估计和点预测，并采用结构化高斯表示进行场景重建。
3. 实验结果表明，ARTDECO在交互性能、鲁棒性和重建质量方面均表现出色，在多个数据集上取得了与现有技术相当或更好的结果。

## 📝 摘要（中文）

本文提出ARTDECO，一个统一的框架，旨在结合前馈模型的效率和基于SLAM流程的可靠性，实现单目图像序列的即时3D重建。ARTDECO利用3D基础模型进行位姿估计和点预测，并结合高斯解码器将多尺度特征转换为结构化的3D高斯表示。为了在规模化场景下保持保真度和效率，设计了一种分层高斯表示，并采用LoD感知的渲染策略，从而提高渲染保真度并减少冗余。在八个不同的室内和室外基准测试中，实验结果表明ARTDECO实现了与SLAM相当的交互性能，与前馈系统相似的鲁棒性，以及接近于单场景优化的重建质量，为以精确的几何形状和高视觉保真度对真实世界环境进行即时数字化提供了一条可行的途径。

## 🔬 方法详解

**问题定义**：论文旨在解决单目图像序列的即时3D重建问题。现有方法要么依赖于计算量大的逐场景优化，要么依赖于精度和鲁棒性不足的前馈模型。因此，如何在保证重建质量的同时，实现高效的即时重建是一个关键挑战。

**核心思路**：ARTDECO的核心思路是结合前馈模型的效率和SLAM的可靠性。具体来说，利用3D基础模型进行位姿估计和初始点云预测，然后通过高斯解码器将多尺度特征转换为结构化的3D高斯表示，从而实现高效且高质量的场景重建。

**技术框架**：ARTDECO的整体框架包含以下几个主要模块：1) 位姿估计模块，利用3D基础模型估计相机位姿；2) 点云预测模块，利用3D基础模型预测初始点云；3) 高斯解码器，将多尺度特征解码为3D高斯参数；4) 分层高斯表示，用于存储和管理3D高斯；5) LoD感知渲染模块，根据视点距离选择合适的细节层次进行渲染。

**关键创新**：ARTDECO的关键创新在于以下几个方面：1) 结合了前馈模型和SLAM的优点，实现了高效且高质量的即时重建；2) 提出了分层高斯表示，有效管理大规模场景；3) 提出了LoD感知渲染策略，提高了渲染效率和质量。

**关键设计**：ARTDECO的关键设计包括：1) 使用预训练的3D基础模型进行位姿估计和点云预测，避免了从头开始训练；2) 设计了高斯解码器，将多尺度特征转换为3D高斯参数，包括位置、协方差和颜色等；3) 采用分层高斯表示，将场景划分为不同层级的细节，并根据视点距离选择合适的层级进行渲染；4) 设计了LoD感知的渲染损失函数，鼓励模型学习更有效的细节层次表示。

## 📊 实验亮点

ARTDECO在八个不同的室内和室外基准测试中进行了评估，实验结果表明，ARTDECO实现了与SLAM相当的交互性能，与前馈系统相似的鲁棒性，以及接近于单场景优化的重建质量。例如，在重建质量方面，ARTDECO在多个数据集上取得了与现有技术相当或更好的结果，同时保持了较高的运行效率。

## 🎯 应用场景

ARTDECO在诸多领域具有广泛的应用前景，包括：实时三维重建、增强现实/虚拟现实（AR/VR）、机器人导航与环境感知、以及快速构建数字孪生等。该技术能够帮助机器人更好地理解周围环境，为AR/VR应用提供更逼真的场景，并加速现实世界到虚拟世界的数字化进程。

## 📄 摘要（原文）

> On-the-fly 3D reconstruction from monocular image sequences is a long-standing challenge in computer vision, critical for applications such as real-to-sim, AR/VR, and robotics. Existing methods face a major tradeoff: per-scene optimization yields high fidelity but is computationally expensive, whereas feed-forward foundation models enable real-time inference but struggle with accuracy and robustness. In this work, we propose ARTDECO, a unified framework that combines the efficiency of feed-forward models with the reliability of SLAM-based pipelines. ARTDECO uses 3D foundation models for pose estimation and point prediction, coupled with a Gaussian decoder that transforms multi-scale features into structured 3D Gaussians. To sustain both fidelity and efficiency at scale, we design a hierarchical Gaussian representation with a LoD-aware rendering strategy, which improves rendering fidelity while reducing redundancy. Experiments on eight diverse indoor and outdoor benchmarks show that ARTDECO delivers interactive performance comparable to SLAM, robustness similar to feed-forward systems, and reconstruction quality close to per-scene optimization, providing a practical path toward on-the-fly digitization of real-world environments with both accurate geometry and high visual fidelity. Explore more demos on our project page: https://city-super.github.io/artdeco/.

