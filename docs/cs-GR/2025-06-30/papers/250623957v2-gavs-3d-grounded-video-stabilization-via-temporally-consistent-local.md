---
layout: default
title: "GaVS: 3D-Grounded Video Stabilization via Temporally-Consistent Local Reconstruction and Rendering"
---

# GaVS: 3D-Grounded Video Stabilization via Temporally-Consistent Local Reconstruction and Rendering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23957" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23957v2</a>
  <a href="https://arxiv.org/pdf/2506.23957.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23957v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23957v2', 'GaVS: 3D-Grounded Video Stabilization via Temporally-Consistent Local Reconstruction and Rendering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zinuo You, Stamatios Georgoulis, Anpei Chen, Siyu Tang, Dengxin Dai

**分类**: cs.GR, cs.CV

**发布日期**: 2025-06-30 (更新: 2025-07-18)

**备注**: siggraph 2025, project website: https://sinoyou.github.io/gavs. version 2, update discussion

**DOI**: [10.1145/3721238.3730757](https://doi.org/10.1145/3721238.3730757)

---

## 💡 一句话要点

**提出GaVS以解决视频稳定化中的几何失真和裁剪问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视频稳定化` `3D重建` `局部重建` `时间一致性` `高斯点云` `多视角监督` `几何一致性`

## 📋 核心要点

1. 现有视频稳定化方法存在几何失真、过度裁剪和泛化能力差等问题，影响用户体验。
2. 本文提出GaVS方法，通过3D相机姿态进行局部重建与渲染，确保时间一致性，避免裁剪。
3. 实验结果表明，GaVS在传统指标和几何一致性方面优于现有的2D和2.5D方法，用户反馈也显示出明显的改善。

## 📝 摘要（中文）

视频稳定化在视频处理领域至关重要，它能够消除不必要的抖动，同时保留用户的原始运动意图。现有方法在不同领域中存在几种问题，如几何失真、过度裁剪和较差的泛化能力，这些问题降低了用户体验。为了解决这些问题，本文提出了一种新颖的3D基础方法GaVS，将视频稳定化重新定义为一个时间一致的局部重建和渲染范式。通过3D相机姿态，增强重建模型以预测高斯点云原语，并在测试时进行微调，利用多视角动态感知的光度监督和跨帧正则化，生成时间一致的局部重建。该模型随后用于渲染每一帧稳定的视频。我们利用场景外推模块避免了帧裁剪。通过在一个重新设计的数据集上进行评估，结果显示我们的方法在传统任务指标和几何一致性方面与最先进的2D和2.5D方法具有竞争力或优越性。

## 🔬 方法详解

**问题定义**：本文旨在解决视频稳定化过程中常见的几何失真、过度裁剪和泛化能力不足的问题。这些问题导致用户体验下降，影响视频质量。

**核心思路**：GaVS通过将视频稳定化视为时间一致的局部重建和渲染过程，利用3D相机姿态增强重建模型，确保生成的稳定视频保持用户的运动意图。

**技术框架**：整体架构包括重建模型、时间一致性优化模块和渲染模块。重建模型负责生成高斯点云原语，时间一致性优化模块通过多视角动态感知的光度监督和跨帧正则化进行微调，最后渲染模块生成稳定的输出帧。

**关键创新**：GaVS的主要创新在于其将视频稳定化问题重新定义为局部重建与渲染的结合，利用3D信息增强了时间一致性，避免了传统方法中的裁剪问题。

**关键设计**：在模型设计中，采用了多视角动态感知的光度监督和跨帧正则化作为损失函数，确保了生成结果的时间一致性和几何准确性。

## 📊 实验亮点

实验结果显示，GaVS在传统视频稳定化任务中表现优越，尤其在几何一致性方面，相较于最先进的2D和2.5D方法，性能提升显著。用户研究验证了该方法在视觉质量上的明显改善，用户满意度高于其他对比方法。

## 🎯 应用场景

GaVS方法在视频处理、虚拟现实和增强现实等领域具有广泛的应用潜力。通过提高视频稳定化的质量，可以显著提升用户体验，尤其是在动态场景下的实时视频处理。此外，该方法的3D基础设计为未来的多媒体内容创作提供了新的思路和工具。

## 📄 摘要（原文）

> Video stabilization is pivotal for video processing, as it removes unwanted shakiness while preserving the original user motion intent. Existing approaches, depending on the domain they operate, suffer from several issues (e.g. geometric distortions, excessive cropping, poor generalization) that degrade the user experience. To address these issues, we introduce \textbf{GaVS}, a novel 3D-grounded approach that reformulates video stabilization as a temporally-consistent `local reconstruction and rendering' paradigm. Given 3D camera poses, we augment a reconstruction model to predict Gaussian Splatting primitives, and finetune it at test-time, with multi-view dynamics-aware photometric supervision and cross-frame regularization, to produce temporally-consistent local reconstructions. The model are then used to render each stabilized frame. We utilize a scene extrapolation module to avoid frame cropping. Our method is evaluated on a repurposed dataset, instilled with 3D-grounded information, covering samples with diverse camera motions and scene dynamics. Quantitatively, our method is competitive with or superior to state-of-the-art 2D and 2.5D approaches in terms of conventional task metrics and new geometry consistency. Qualitatively, our method produces noticeably better results compared to alternatives, validated by the user study.

