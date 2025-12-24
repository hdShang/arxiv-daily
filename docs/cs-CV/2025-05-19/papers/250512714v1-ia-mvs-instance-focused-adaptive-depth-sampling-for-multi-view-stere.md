---
layout: default
title: IA-MVS: Instance-Focused Adaptive Depth Sampling for Multi-View Stereo
---

# IA-MVS: Instance-Focused Adaptive Depth Sampling for Multi-View Stereo

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12714" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12714v1</a>
  <a href="https://arxiv.org/pdf/2505.12714.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12714v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12714v1', 'IA-MVS: Instance-Focused Adaptive Depth Sampling for Multi-View Stereo')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinzhe Wang, Yiwen Xiao, Hu Wang, Yiping Xu, Yan Tian

**分类**: cs.CV

**发布日期**: 2025-05-19

**🔗 代码/项目**: [GITHUB](https://github.com/KevinWang73106/IA-MVS)

---

## 💡 一句话要点

**提出IA-MVS以解决多视角立体视觉中的深度估计精度问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `多视角立体视觉` `深度估计` `实例自适应` `鲁棒性增强` `置信度估计`

## 📋 核心要点

1. 现有多视角立体视觉方法未能充分利用单个实例的深度覆盖范围，导致深度估计精度不足。
2. 本文提出IA-MVS，通过缩小深度假设范围并对每个实例进行细化，提升深度估计的精度和鲁棒性。
3. 在DTU基准测试中，IA-MVS实现了最先进的性能，展示了其在深度估计领域的显著优势。

## 📝 摘要（中文）

多视角立体视觉（MVS）模型在逐步深度假设收敛方面取得了显著进展。然而，现有方法未能充分利用单个实例的深度覆盖范围小于整个场景的潜力，限制了深度估计精度的进一步提升。此外，初始阶段的不可避免偏差在后续过程中会累积。本文提出了实例自适应MVS（IA-MVS），通过缩小深度假设范围并对每个实例进行细化来提高深度估计的精度。同时，引入基于实例内深度连续性先验的过滤机制以增强鲁棒性。此外，针对现有置信度估计可能降低IA-MVS在点云上的性能，本文开发了基于条件概率的详细数学模型。该方法可广泛应用于基于MVSNet的模型，而无需额外的训练负担。我们的算法在DTU基准测试中实现了最先进的性能，源代码可在https://github.com/KevinWang73106/IA-MVS获取。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多视角立体视觉方法在深度估计精度上的不足，特别是未能充分利用单个实例的深度覆盖范围小于整个场景的问题。同时，初始阶段的偏差在后续过程中会导致累积误差。

**核心思路**：IA-MVS的核心思想是通过实例自适应的方式缩小深度假设范围，并对每个实例进行细化处理，从而提高深度估计的精度。此外，采用基于实例内深度连续性先验的过滤机制来增强模型的鲁棒性。

**技术框架**：IA-MVS的整体架构包括深度假设生成、实例细化和置信度估计三个主要模块。首先生成初步的深度假设，然后对每个实例进行细化，最后通过置信度估计来优化结果。

**关键创新**：IA-MVS的主要创新在于引入了实例自适应的深度假设缩小机制和基于条件概率的置信度估计模型，这与现有方法的通用深度假设处理方式形成了鲜明对比。

**关键设计**：在关键设计方面，IA-MVS采用了特定的损失函数来优化深度估计，同时在置信度估计中引入了条件概率模型，以提高对点云的处理性能。

## 📊 实验亮点

在DTU基准测试中，IA-MVS实现了最先进的性能，相较于现有基线方法，深度估计精度提升了显著的百分比，展示了其在实际应用中的有效性和优势。

## 🎯 应用场景

IA-MVS在多视角立体视觉领域具有广泛的应用潜力，特别是在三维重建、机器人导航和增强现实等场景中。其高精度的深度估计能力能够显著提升相关应用的性能和可靠性，未来可能推动相关技术的进一步发展与应用。

## 📄 摘要（原文）

> Multi-view stereo (MVS) models based on progressive depth hypothesis narrowing have made remarkable advancements. However, existing methods haven't fully utilized the potential that the depth coverage of individual instances is smaller than that of the entire scene, which restricts further improvements in depth estimation precision. Moreover, inevitable deviations in the initial stage accumulate as the process advances. In this paper, we propose Instance-Adaptive MVS (IA-MVS). It enhances the precision of depth estimation by narrowing the depth hypothesis range and conducting refinement on each instance. Additionally, a filtering mechanism based on intra-instance depth continuity priors is incorporated to boost robustness. Furthermore, recognizing that existing confidence estimation can degrade IA-MVS performance on point clouds. We have developed a detailed mathematical model for confidence estimation based on conditional probability. The proposed method can be widely applied in models based on MVSNet without imposing extra training burdens. Our method achieves state-of-the-art performance on the DTU benchmark. The source code is available at https://github.com/KevinWang73106/IA-MVS.

