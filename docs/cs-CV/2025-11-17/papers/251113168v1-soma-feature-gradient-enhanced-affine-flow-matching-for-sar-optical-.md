---
layout: default
title: SOMA: Feature Gradient Enhanced Affine-Flow Matching for SAR-Optical Registration
---

# SOMA: Feature Gradient Enhanced Affine-Flow Matching for SAR-Optical Registration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13168" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13168v1</a>
  <a href="https://arxiv.org/pdf/2511.13168.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13168v1" onclick="toggleFavorite(this, '2511.13168v1', 'SOMA: Feature Gradient Enhanced Affine-Flow Matching for SAR-Optical Registration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haodong Wang, Tao Zhuo, Xiuwei Zhang, Hanlin Yin, Wencong Wu, Yanning Zhang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-17

---

## 💡 一句话要点

**SOMA：通过特征梯度增强的仿射流匹配实现SAR-光学图像配准**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `SAR-光学图像配准` `深度学习` `特征梯度增强` `仿射流匹配` `跨模态图像配准`

## 📋 核心要点

1. SAR与光学图像配准因成像差异大而困难，现有深度学习方法效果不佳，未能有效利用梯度信息。
2. SOMA框架将结构梯度先验融入深度特征，并结合全局-局部仿射流匹配，提升配准精度。
3. 实验表明，SOMA在SEN1-2和GFGE_SO数据集上显著提升了配准精度，并具有良好的鲁棒性和泛化能力。

## 📝 摘要（中文）

由于成像机制和视觉特征的根本差异，SAR和光学图像之间实现像素级配准仍然是一项具有挑战性的任务。尽管深度学习在许多跨模态任务中取得了巨大成功，但其在SAR-光学图像配准任务中的性能仍然不尽如人意。传统上，基于梯度的信息通过突出结构差异在手工设计的描述符中发挥了关键作用。然而，这种梯度线索尚未在用于SAR-光学图像匹配的深度学习框架中得到有效利用。为了解决这一差距，我们提出了一种密集配准框架SOMA，该框架将结构梯度先验集成到深度特征中，并通过混合匹配策略来优化对齐。具体来说，我们引入了特征梯度增强器（FGE），它使用注意力和重建机制将多尺度、多方向梯度滤波器嵌入到特征空间中，以提高特征的区分性。此外，我们提出了全局-局部仿射流匹配器（GLAM），它在粗到细的架构中结合了仿射变换和基于流的细化，以确保结构一致性和局部精度。实验结果表明，SOMA显著提高了配准精度，在SEN1-2数据集上将CMR@1px提高了12.29%，在GFGE_SO数据集上提高了18.50%。此外，SOMA表现出强大的鲁棒性，并且可以在不同的场景和分辨率中很好地泛化。

## 🔬 方法详解

**问题定义**：SAR（合成孔径雷达）图像和光学图像由于成像原理不同，导致其视觉特征差异很大，这使得它们之间的精确配准成为一个难题。现有的深度学习方法在处理这种跨模态图像配准时，往往无法充分利用图像的结构信息，特别是梯度信息，导致配准精度不高。

**核心思路**：SOMA的核心思路是将图像的结构梯度信息融入到深度学习特征中，从而增强特征的区分性，提高配准的准确性。同时，采用一种混合匹配策略，结合全局的仿射变换和局部的光流细化，以保证配准的结构一致性和局部精度。

**技术框架**：SOMA框架主要包含两个核心模块：特征梯度增强器（FGE）和全局-局部仿射流匹配器（GLAM）。首先，FGE模块通过多尺度、多方向的梯度滤波器提取图像的结构信息，并将其嵌入到深度特征中。然后，GLAM模块利用仿射变换进行粗略的全局配准，再通过光流方法进行精细的局部调整，最终实现精确的图像配准。整个过程采用粗到细的架构，逐步提高配准精度。

**关键创新**：SOMA的关键创新在于将传统的梯度信息有效地融入到深度学习框架中。FGE模块通过注意力机制和重建机制，自适应地选择重要的梯度信息，并将其与深度特征融合，从而增强了特征的表达能力。GLAM模块则结合了全局和局部的配准策略，克服了单一方法的局限性。

**关键设计**：FGE模块采用了多尺度、多方向的梯度滤波器，以捕捉不同尺度的结构信息。注意力机制用于自适应地选择重要的梯度信息，重建机制则用于保证特征的完整性。GLAM模块中的仿射变换采用RANSAC算法进行鲁棒估计，光流方法则采用迭代优化算法进行精确匹配。损失函数包括配准误差和结构一致性约束，以保证配准的准确性和稳定性。

## 📊 实验亮点

SOMA在SEN1-2数据集和GFGE_SO数据集上取得了显著的性能提升。在SEN1-2数据集上，CMR@1px指标提高了12.29%，在GFGE_SO数据集上提高了18.50%。这些结果表明，SOMA能够有效地提高SAR-光学图像的配准精度，并且具有良好的泛化能力和鲁棒性。与其他基线方法相比，SOMA在各种场景和分辨率下均表现出更优越的性能。

## 🎯 应用场景

SOMA在遥感图像处理领域具有广泛的应用前景，例如城市规划、灾害监测、环境评估等。通过精确配准SAR和光学图像，可以获取更全面的地物信息，为决策提供更可靠的依据。该研究成果还有助于推动跨模态图像配准技术的发展，并可应用于其他领域，如医学图像分析、自动驾驶等。

## 📄 摘要（原文）

> Achieving pixel-level registration between SAR and optical images remains a challenging task due to their fundamentally different imaging mechanisms and visual characteristics. Although deep learning has achieved great success in many cross-modal tasks, its performance on SAR-Optical registration tasks is still unsatisfactory. Gradient-based information has traditionally played a crucial role in handcrafted descriptors by highlighting structural differences. However, such gradient cues have not been effectively leveraged in deep learning frameworks for SAR-Optical image matching. To address this gap, we propose SOMA, a dense registration framework that integrates structural gradient priors into deep features and refines alignment through a hybrid matching strategy. Specifically, we introduce the Feature Gradient Enhancer (FGE), which embeds multi-scale, multi-directional gradient filters into the feature space using attention and reconstruction mechanisms to boost feature distinctiveness. Furthermore, we propose the Global-Local Affine-Flow Matcher (GLAM), which combines affine transformation and flow-based refinement within a coarse-to-fine architecture to ensure both structural consistency and local accuracy. Experimental results demonstrate that SOMA significantly improves registration precision, increasing the CMR@1px by 12.29% on the SEN1-2 dataset and 18.50% on the GFGE_SO dataset. In addition, SOMA exhibits strong robustness and generalizes well across diverse scenes and resolutions.

