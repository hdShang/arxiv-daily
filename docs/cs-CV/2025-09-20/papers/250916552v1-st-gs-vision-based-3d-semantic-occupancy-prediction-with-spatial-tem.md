---
layout: default
title: "ST-GS: Vision-Based 3D Semantic Occupancy Prediction with Spatial-Temporal Gaussian Splatting"
---

# ST-GS: Vision-Based 3D Semantic Occupancy Prediction with Spatial-Temporal Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16552" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16552v1</a>
  <a href="https://arxiv.org/pdf/2509.16552.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16552v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16552v1', 'ST-GS: Vision-Based 3D Semantic Occupancy Prediction with Spatial-Temporal Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoyang Yan, Muleilan Pei, Shaojie Shen

**分类**: cs.CV, cs.RO

**发布日期**: 2025-09-20

---

## 💡 一句话要点

**提出ST-GS框架，通过时空高斯溅射提升视觉中心自动驾驶中的3D语义占据预测**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D语义占据预测` `高斯溅射` `时空建模` `自动驾驶` `多视角融合` `时间一致性` `空间聚合`

## 📋 核心要点

1. 现有基于高斯模型的占据预测方法在多视角空间交互和多帧时间一致性方面存在不足，限制了性能。
2. ST-GS框架通过指导信息空间聚合策略和几何感知的时间融合方案，增强空间交互和时间连续性。
3. 在nuScenes数据集上，ST-GS取得了SOTA性能，并显著提升了时间一致性，验证了方法的有效性。

## 📝 摘要（中文）

本文提出了一种新颖的时空高斯溅射（ST-GS）框架，旨在增强基于高斯模型的3D语义占据预测中的空间和时间建模能力。现有方法在多视角空间交互和多帧时间一致性方面存在不足。为了解决这些问题，我们设计了一种指导信息空间聚合策略，在双模态注意力机制中加强高斯表示的空间交互。此外，我们引入了一种几何感知的时间融合方案，有效地利用历史上下文来提高场景补全的时间连续性。在大型nuScenes占据预测基准上的大量实验表明，我们提出的方法不仅实现了最先进的性能，而且与现有的基于高斯的方法相比，提供了明显更好的时间一致性。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉中心自动驾驶中3D语义占据预测问题。现有基于高斯模型的方法，虽然降低了计算开销，但缺乏充分的多视角空间交互和多帧时间一致性，导致预测精度和稳定性受限。

**核心思路**：论文的核心思路是利用时空高斯溅射（ST-GS）框架，显式地建模高斯表示的空间关系和时间演变。通过增强空间交互和时间连续性，提升3D语义占据预测的准确性和鲁棒性。

**技术框架**：ST-GS框架主要包含两个关键模块：1) 指导信息空间聚合模块：利用双模态注意力机制，增强高斯表示之间的空间交互，从而更好地理解场景的几何结构。2) 几何感知的时间融合模块：利用历史上下文信息，通过几何约束来融合不同时间帧的高斯表示，从而提高时间连续性。整体流程是从多视角图像提取特征，然后通过空间聚合和时间融合，最终预测3D语义占据。

**关键创新**：论文的关键创新在于：1) 提出了指导信息空间聚合策略，利用双模态注意力机制，有效增强了高斯表示的空间交互。2) 提出了几何感知的时间融合方案，利用历史上下文信息，提高了场景补全的时间连续性。与现有方法相比，ST-GS能够更好地建模场景的时空关系。

**关键设计**：在空间聚合模块中，双模态注意力机制同时考虑了高斯特征和空间位置信息。在时间融合模块中，几何约束用于筛选可靠的历史信息，避免噪声干扰。具体的损失函数包括占据预测损失和语义分割损失，用于优化高斯表示的参数。

## 📊 实验亮点

在nuScenes占据预测基准测试中，ST-GS取得了state-of-the-art的性能，显著优于现有的基于高斯的方法。尤其在时间一致性方面，ST-GS取得了明显的提升，表明其能够更好地建模场景的时间演变。具体性能数据（如IoU等指标）在论文中有详细展示。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、增强现实等领域。通过准确预测周围环境的3D语义占据情况，自动驾驶系统可以做出更安全、更合理的决策。机器人可以更好地理解和操作周围环境。增强现实应用可以更真实地将虚拟物体融入现实场景。

## 📄 摘要（原文）

> 3D occupancy prediction is critical for comprehensive scene understanding in vision-centric autonomous driving. Recent advances have explored utilizing 3D semantic Gaussians to model occupancy while reducing computational overhead, but they remain constrained by insufficient multi-view spatial interaction and limited multi-frame temporal consistency. To overcome these issues, in this paper, we propose a novel Spatial-Temporal Gaussian Splatting (ST-GS) framework to enhance both spatial and temporal modeling in existing Gaussian-based pipelines. Specifically, we develop a guidance-informed spatial aggregation strategy within a dual-mode attention mechanism to strengthen spatial interaction in Gaussian representations. Furthermore, we introduce a geometry-aware temporal fusion scheme that effectively leverages historical context to improve temporal continuity in scene completion. Extensive experiments on the large-scale nuScenes occupancy prediction benchmark showcase that our proposed approach not only achieves state-of-the-art performance but also delivers markedly better temporal consistency compared to existing Gaussian-based methods.

