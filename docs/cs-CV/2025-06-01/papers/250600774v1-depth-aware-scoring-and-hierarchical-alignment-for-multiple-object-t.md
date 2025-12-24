---
layout: default
title: Depth-Aware Scoring and Hierarchical Alignment for Multiple Object Tracking
---

# Depth-Aware Scoring and Hierarchical Alignment for Multiple Object Tracking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00774" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00774v1</a>
  <a href="https://arxiv.org/pdf/2506.00774.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00774v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00774v1', 'Depth-Aware Scoring and Hierarchical Alignment for Multiple Object Tracking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Milad Khanchi, Maria Amer, Charalambos Poullis

**分类**: cs.CV

**发布日期**: 2025-06-01

**备注**: ICIP 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Milad-Khanchi/DepthMOT)

---

## 💡 一句话要点

**提出深度感知评分与分层对齐以解决多目标跟踪问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `多目标跟踪` `深度感知` `分层对齐` `视觉相似对象` `遮挡处理` `无监督学习` `计算机视觉`

## 📋 核心要点

1. 现有的多目标跟踪方法在处理遮挡和视觉相似对象时，依赖交并比（IoU）导致效果不佳。
2. 本文提出了一种深度感知框架，通过零样本估计深度并将其作为独立特征用于对象关联。
3. 该框架在多个挑战性基准上取得了最先进的结果，且无需额外的训练或微调。

## 📝 摘要（中文）

当前基于运动的多目标跟踪（MOT）方法在对象关联上过于依赖交并比（IoU），在遮挡或视觉相似对象的场景中效果不佳。为此，本文提出了一种新颖的深度感知框架，通过零样本方法估计深度，并将其作为独立特征融入关联过程中。此外，我们引入了分层对齐评分，通过整合粗略边界框重叠和细粒度（像素级）对齐来改进关联准确性，而无需额外的可学习参数。我们的方法是首个在关联步骤中将3D特征（单目深度）作为独立决策矩阵的MOT框架。我们的框架在具有挑战性的基准测试中实现了最先进的结果，无需任何训练或微调。代码可在https://github.com/Milad-Khanchi/DepthMOT获取。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多目标跟踪方法在遮挡和视觉相似对象场景下的关联准确性不足的问题。现有方法过于依赖交并比（IoU），导致在复杂场景中的性能下降。

**核心思路**：我们提出了一种深度感知框架，通过零样本方法估计深度，并将其作为独立特征融入到对象关联过程中，以提高跟踪的准确性和鲁棒性。

**技术框架**：该框架主要包括深度估计模块和分层对齐评分模块。深度估计模块负责生成每个对象的深度信息，而分层对齐评分模块则结合粗略的边界框重叠和细粒度的像素级对齐来优化对象关联。

**关键创新**：本文的主要创新在于首次将3D特征（单目深度）作为独立决策矩阵引入到多目标跟踪的关联步骤中，这一设计显著提高了在复杂场景下的跟踪性能。

**关键设计**：我们在设计中没有引入额外的可学习参数，而是通过分层对齐评分来优化IoU，确保了方法的简洁性和高效性。

## 📊 实验亮点

在多个挑战性基准测试中，我们的方法实现了最先进的性能，显著优于传统的基于IoU的跟踪方法，具体提升幅度未知，且无需任何训练或微调，展示了其在实际应用中的高效性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、自动驾驶、机器人导航等场景，能够有效提升在复杂环境下的目标跟踪能力。未来，该框架可能推动更多基于深度信息的跟踪技术的发展，提升多目标跟踪的实用性和准确性。

## 📄 摘要（原文）

> Current motion-based multiple object tracking (MOT) approaches rely heavily on Intersection-over-Union (IoU) for object association. Without using 3D features, they are ineffective in scenarios with occlusions or visually similar objects. To address this, our paper presents a novel depth-aware framework for MOT. We estimate depth using a zero-shot approach and incorporate it as an independent feature in the association process. Additionally, we introduce a Hierarchical Alignment Score that refines IoU by integrating both coarse bounding box overlap and fine-grained (pixel-level) alignment to improve association accuracy without requiring additional learnable parameters. To our knowledge, this is the first MOT framework to incorporate 3D features (monocular depth) as an independent decision matrix in the association step. Our framework achieves state-of-the-art results on challenging benchmarks without any training nor fine-tuning. The code is available at https://github.com/Milad-Khanchi/DepthMOT

