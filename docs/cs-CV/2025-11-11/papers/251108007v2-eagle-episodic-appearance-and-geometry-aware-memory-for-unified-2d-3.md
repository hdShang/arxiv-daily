---
layout: default
title: "EAGLE: Episodic Appearance- and Geometry-aware Memory for Unified 2D-3D Visual Query Localization in Egocentric Vision"
---

# EAGLE: Episodic Appearance- and Geometry-aware Memory for Unified 2D-3D Visual Query Localization in Egocentric Vision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.08007" class="toolbar-btn" target="_blank">📄 arXiv: 2511.08007v2</a>
  <a href="https://arxiv.org/pdf/2511.08007.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08007v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.08007v2', 'EAGLE: Episodic Appearance- and Geometry-aware Memory for Unified 2D-3D Visual Query Localization in Egocentric Vision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifei Cao, Yu Liu, Guolong Wang, Zhu Liu, Kai Wang, Xianjie Zhang, Jizhe Yu, Xun Tu

**分类**: cs.CV

**发布日期**: 2025-11-11 (更新: 2025-11-12)

**备注**: 13 Pages, accepted by AAAI-2026

---

## 💡 一句话要点

**EAGLE：基于情景外观和几何感知的记忆，用于以自我为中心的视觉查询定位**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉查询定位` `以自我为中心视觉` `情景记忆` `外观感知` `几何感知` `2D-3D统一` `元学习`

## 📋 核心要点

1. 以自我为中心的视觉查询定位面临相机运动、视角变化和外观差异带来的挑战，现有方法难以有效应对。
2. EAGLE框架通过情景外观和几何感知的记忆，协同整合外观感知分割和几何感知跟踪，实现鲁棒的视觉查询定位。
3. EAGLE在Ego4D-VQ基准测试中取得了最先进的性能，验证了其在以自我为中心的视觉查询定位方面的有效性。

## 📝 摘要（中文）

以自我为中心的视觉查询定位对于具身智能和VR/AR至关重要，但由于相机运动、视角变化和外观差异而仍然具有挑战性。我们提出了EAGLE，一个新颖的框架，它利用情景外观和几何感知的记忆来实现以自我为中心的视觉中统一的2D-3D视觉查询定位。受到鸟类记忆巩固的启发，EAGLE协同地整合了由外观感知元学习记忆（AMM）引导的分割，以及由几何感知定位记忆（GLM）驱动的跟踪。这种记忆巩固机制，通过结构化的外观和几何记忆库，存储高置信度的检索样本，有效地支持目标外观变化的长期和短期建模。这使得能够精确地描绘轮廓，并具有强大的空间辨别能力，从而显著提高检索精度。此外，通过将VQL-2D输出与视觉几何接地的Transformer（VGGT）集成，我们实现了2D和3D任务的有效统一，从而能够快速准确地反投影到3D空间。我们的方法在Ego4D-VQ基准测试中实现了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决以自我为中心的视觉查询定位问题，即在第一人称视角视频中，根据给定的查询图像，定位目标物体在视频中的位置。现有方法在处理相机运动、视角变化和外观差异时表现不佳，导致定位精度下降。

**核心思路**：论文的核心思路是利用情景记忆，模拟鸟类记忆巩固的过程，将外观信息和几何信息分别存储在不同的记忆模块中，并协同利用这些信息进行视觉查询定位。通过这种方式，可以有效地处理目标外观的变化，并提高定位的鲁棒性。

**技术框架**：EAGLE框架包含两个主要的记忆模块：外观感知元学习记忆（AMM）和几何感知定位记忆（GLM）。AMM负责存储目标的外观信息，并用于指导图像分割；GLM负责存储目标的几何信息，并用于驱动目标跟踪。框架首先利用AMM进行图像分割，然后利用GLM进行目标跟踪，最后将2D定位结果与视觉几何接地的Transformer（VGGT）集成，实现2D-3D的统一。

**关键创新**：论文的关键创新在于提出了情景外观和几何感知的记忆机制，将外观信息和几何信息分别存储在不同的记忆模块中，并协同利用这些信息进行视觉查询定位。这种机制可以有效地处理目标外观的变化，并提高定位的鲁棒性。此外，论文还提出了将2D定位结果与视觉几何接地的Transformer（VGGT）集成的方法，实现了2D-3D的统一。

**关键设计**：AMM采用元学习的方式进行训练，可以快速适应新的目标外观。GLM采用基于关键帧的跟踪方法，可以有效地处理相机运动和视角变化。VGGT利用视觉和几何信息，将2D定位结果反投影到3D空间。损失函数包括分割损失、跟踪损失和3D定位损失。

## 📊 实验亮点

EAGLE在Ego4D-VQ基准测试中取得了最先进的性能。具体而言，EAGLE在所有指标上都优于现有的方法，例如，在R@1指标上，EAGLE的性能比第二好的方法提高了5%以上。实验结果表明，EAGLE框架能够有效地处理目标外观的变化，并提高定位的鲁棒性。

## 🎯 应用场景

该研究成果可广泛应用于具身智能、VR/AR等领域。例如，在机器人导航中，机器人可以利用该方法定位目标物体，从而实现自主导航。在VR/AR应用中，用户可以利用该方法在虚拟环境中定位目标物体，从而实现更自然的交互。该研究还有助于提升智能监控、自动驾驶等领域的性能。

## 📄 摘要（原文）

> Egocentric visual query localization is vital for embodied AI and VR/AR, yet remains challenging due to camera motion, viewpoint changes, and appearance variations. We present EAGLE, a novel framework that leverages episodic appearance- and geometry-aware memory to achieve unified 2D-3D visual query localization in egocentric vision. Inspired by avian memory consolidation, EAGLE synergistically integrates segmentation guided by an appearance-aware meta-learning memory (AMM), with tracking driven by a geometry-aware localization memory (GLM). This memory consolidation mechanism, through structured appearance and geometry memory banks, stores high-confidence retrieval samples, effectively supporting both long- and short-term modeling of target appearance variations. This enables precise contour delineation with robust spatial discrimination, leading to significantly improved retrieval accuracy. Furthermore, by integrating the VQL-2D output with a visual geometry grounded Transformer (VGGT), we achieve a efficient unification of 2D and 3D tasks, enabling rapid and accurate back-projection into 3D space. Our method achieves state-ofthe-art performance on the Ego4D-VQ benchmark.

