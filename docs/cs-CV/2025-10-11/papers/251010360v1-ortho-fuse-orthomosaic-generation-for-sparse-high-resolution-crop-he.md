---
layout: default
title: Ortho-Fuse: Orthomosaic Generation for Sparse High-Resolution Crop Health Maps Through Intermediate Optical Flow Estimation
---

# Ortho-Fuse: Orthomosaic Generation for Sparse High-Resolution Crop Health Maps Through Intermediate Optical Flow Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10360" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10360v1</a>
  <a href="https://arxiv.org/pdf/2510.10360.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10360v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.10360v1', 'Ortho-Fuse: Orthomosaic Generation for Sparse High-Resolution Crop Health Maps Through Intermediate Optical Flow Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rugved Katole, Christopher Stewart

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-11

**备注**: 6 Figures, 9 pages

**期刊**: Harvest Workshop -- International Conference on Parallel Processing (ICPP), 2025

**DOI**: [10.1145/3750720.3758083](https://doi.org/10.1145/3750720.3758083)

---

## 💡 一句话要点

**Ortho-Fuse：通过光流估计为稀疏高分辨率作物健康地图生成正射影像**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `正射影像生成` `光流估计` `精准农业` `作物健康监测` `低重叠率图像` `摄影测量` `图像合成`

## 📋 核心要点

1. 传统摄影测量重建依赖高图像重叠率，这限制了AI驱动作物健康监测系统在资源受限环境下的应用。
2. Ortho-Fuse通过光流估计合成中间过渡图像，有效增加特征对应，降低了对图像重叠率的要求。
3. 实验结果表明，Ortho-Fuse能够将最低图像重叠率要求降低20%，提升正射影像生成质量。

## 📝 摘要（中文）

基于人工智能的作物健康地图系统通过加速数据采集和降低成本，相比传统监测方法具有显著优势。然而，由于从稀疏航拍图像数据集中生成正射影像的技术限制，该系统在农民中的广泛应用仍然受到限制。传统摄影测量重建需要70-80%的图像重叠率，以建立足够的特征对应关系来实现精确的几何配准。在资源受限条件下运行的AI驱动系统无法始终如一地达到这些重叠阈值，导致重建质量下降，从而降低了用户对自主监测技术的信心。本文提出Ortho-Fuse，一个基于光流的框架，能够以较低的重叠率生成可靠的正射影像。我们的方法采用中间光流估计来合成连续航拍帧之间的过渡图像，人为地增加特征对应关系，从而改善几何重建。实验验证表明，最低重叠率要求降低了20%。我们进一步分析了精准农业中的应用障碍，以确定增强AI驱动监测系统集成的方法。

## 🔬 方法详解

**问题定义**：现有基于航拍图像的作物健康监测系统，在生成正射影像时，依赖于高重叠率的图像数据。在实际应用中，由于成本、飞行条件等限制，难以保证70-80%的图像重叠率，导致正射影像质量下降，影响后续分析的准确性。因此，需要一种方法能够在低重叠率图像条件下，生成高质量的正射影像。

**核心思路**：Ortho-Fuse的核心思路是通过光流估计，在原始的稀疏航拍图像之间合成中间过渡图像。这些合成图像可以有效地增加相邻图像之间的特征对应关系，从而改善后续的几何重建过程，即使在低重叠率的情况下也能生成高质量的正射影像。

**技术框架**：Ortho-Fuse框架主要包含以下几个阶段：1) 图像采集：获取低重叠率的航拍图像序列。2) 光流估计：使用光流算法估计相邻图像之间的像素运动。3) 中间图像合成：基于光流估计的结果，合成原始图像之间的过渡图像。4) 几何重建：利用原始图像和合成图像，进行几何重建，生成点云或网格模型。5) 正射影像生成：基于重建结果，生成正射影像。

**关键创新**：Ortho-Fuse的关键创新在于利用光流估计来合成中间图像，从而人为地增加特征对应关系。这种方法避免了对高重叠率图像的依赖，使得在资源受限的条件下也能生成高质量的正射影像。与传统的摄影测量方法相比，Ortho-Fuse能够在低重叠率下实现更好的重建效果。

**关键设计**：在光流估计方面，可以选择各种现有的光流算法，如RAFT、FlowNet等。中间图像合成可以通过线性插值或其他更复杂的插值方法实现。几何重建可以使用Structure from Motion (SfM) 或 Simultaneous Localization and Mapping (SLAM) 等算法。关键参数包括光流算法的选择、中间图像的数量、以及SfM/SLAM算法的参数设置。

## 📊 实验亮点

实验结果表明，Ortho-Fuse能够显著降低对图像重叠率的要求。具体来说，在相同的重建质量下，Ortho-Fuse可以将最低图像重叠率要求降低20%。这意味着在相同的飞行条件下，可以采集更少的图像，从而降低数据采集成本和时间。此外，Ortho-Fuse生成的正射影像具有更高的几何精度，能够更准确地反映地物信息。

## 🎯 应用场景

Ortho-Fuse技术可广泛应用于精准农业领域，例如作物长势监测、病虫害识别、产量预测等。通过降低对图像重叠率的要求，可以降低数据采集成本，提高监测效率，从而帮助农民更好地管理农田，提高农业生产效率和可持续性。该技术还可应用于其他需要低成本、高效率正射影像生成的场景，如灾害评估、环境监测等。

## 📄 摘要（原文）

> AI-driven crop health mapping systems offer substantial advantages over conventional monitoring approaches through accelerated data acquisition and cost reduction. However, widespread farmer adoption remains constrained by technical limitations in orthomosaic generation from sparse aerial imagery datasets. Traditional photogrammetric reconstruction requires 70-80\% inter-image overlap to establish sufficient feature correspondences for accurate geometric registration. AI-driven systems operating under resource-constrained conditions cannot consistently achieve these overlap thresholds, resulting in degraded reconstruction quality that undermines user confidence in autonomous monitoring technologies. In this paper, we present Ortho-Fuse, an optical flow-based framework that enables the generation of a reliable orthomosaic with reduced overlap requirements. Our approach employs intermediate flow estimation to synthesize transitional imagery between consecutive aerial frames, artificially augmenting feature correspondences for improved geometric reconstruction. Experimental validation demonstrates a 20\% reduction in minimum overlap requirements. We further analyze adoption barriers in precision agriculture to identify pathways for enhanced integration of AI-driven monitoring systems.

