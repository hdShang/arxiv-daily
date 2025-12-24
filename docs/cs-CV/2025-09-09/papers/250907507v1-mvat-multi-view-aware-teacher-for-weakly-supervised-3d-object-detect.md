---
layout: default
title: "MVAT: Multi-View Aware Teacher for Weakly Supervised 3D Object Detection"
---

# MVAT: Multi-View Aware Teacher for Weakly Supervised 3D Object Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07507" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07507v1</a>
  <a href="https://arxiv.org/pdf/2509.07507.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07507v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07507v1', 'MVAT: Multi-View Aware Teacher for Weakly Supervised 3D Object Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saad Lahlali, Alexandre Fournier Montgieux, Nicolas Granger, Hervé Le Borgne, Quoc Cuong Pham

**分类**: cs.CV

**发布日期**: 2025-09-09

**备注**: Accepted at WACV 2026

**🔗 代码/项目**: [GITHUB](https://github.com/CEA-LIST/MVAT)

---

## 💡 一句话要点

**MVAT：多视角感知教师网络用于弱监督3D目标检测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `弱监督学习` `3D目标检测` `多视角学习` `Teacher-Student模型` `点云聚合`

## 📋 核心要点

1. 现有弱监督3D目标检测方法依赖2D框，存在投影歧义和单视角遮挡问题，导致3D框估计不准确。
2. MVAT利用时序多视角信息，聚合对象中心点云构建完整3D表示，并采用Teacher-Student蒸馏框架。
3. 实验表明，MVAT在nuScenes和Waymo Open数据集上取得了SOTA性能，显著缩小了与全监督方法的差距。

## 📝 摘要（中文）

3D目标检测中，3D数据标注成本高昂，因此本文提出一种弱监督标注方法MVAT，该方法依赖于更容易获取的2D框标注。仅依赖2D框会引入投影歧义，因为单个2D框可能对应多个有效的3D姿态。此外，单视角下的部分遮挡使得准确的3D框估计变得困难。MVAT利用序列数据中的时序多视角信息来解决这些问题。该方法随时间聚合以对象为中心的点云，以构建尽可能密集和完整的3D对象表示。采用Teacher-Student蒸馏范式：Teacher网络从单个视角学习，但目标来自时序聚合的静态对象。然后，Teacher生成高质量的伪标签，Student学习从单个视角预测静态和移动对象。整个框架包含一个多视角2D投影损失，以强制预测的3D框与所有可用的2D标注之间的一致性。在nuScenes和Waymo Open数据集上的实验表明，MVAT在弱监督3D目标检测方面实现了最先进的性能，显著缩小了与全监督方法的差距，而无需任何3D框标注。

## 🔬 方法详解

**问题定义**：论文旨在解决弱监督3D目标检测中，仅使用2D框标注带来的3D姿态估计不准确问题。现有方法受限于2D到3D的投影歧义，以及单视角下目标的部分遮挡，难以获得高质量的3D目标检测结果。

**核心思路**：论文的核心思路是利用时序多视角信息，通过聚合多个视角下的点云数据，构建更完整、更鲁棒的3D目标表示。同时，采用Teacher-Student蒸馏框架，利用聚合后的3D信息生成伪标签，指导Student网络学习单视角下的3D目标检测。

**技术框架**：MVAT框架主要包含以下几个模块：1) 对象中心点云聚合模块：将同一对象的点云在不同时间步进行聚合，形成更完整的3D表示。2) Teacher网络：基于聚合后的点云学习3D目标检测，生成高质量的伪标签。3) Student网络：学习从单视角点云预测3D目标，并接受Teacher网络生成的伪标签的指导。4) 多视角2D投影损失：强制3D预测结果与所有可用的2D标注保持一致性。

**关键创新**：该方法最重要的创新点在于利用时序多视角信息进行点云聚合，从而克服了单视角下目标遮挡和2D-3D投影歧义的问题。此外，Teacher-Student蒸馏框架能够有效地将聚合后的3D信息传递给单视角Student网络，提升了弱监督学习的性能。与现有方法相比，MVAT能够更有效地利用弱监督信息，生成更准确的3D目标检测结果。

**关键设计**：在点云聚合方面，论文采用对象中心的对齐方式，以确保不同视角下的点云能够正确地融合。在Teacher网络中，使用了更强的网络结构和更长的训练时间，以保证其能够生成高质量的伪标签。多视角2D投影损失的设计，则保证了3D预测结果与2D标注的一致性，进一步提升了检测的准确性。

## 📊 实验亮点

MVAT在nuScenes和Waymo Open数据集上取得了显著的性能提升，在弱监督3D目标检测任务上达到了SOTA水平。实验结果表明，MVAT能够显著缩小与全监督方法的性能差距，证明了其有效性。具体性能数据需要在论文中查找。

## 🎯 应用场景

MVAT在自动驾驶、机器人导航、智能监控等领域具有广泛的应用前景。通过利用更容易获取的2D标注，降低了3D目标检测的标注成本，加速了3D目标检测技术在实际场景中的部署。该研究的成果有助于推动自动驾驶等领域的发展，提高系统的感知能力和安全性。

## 📄 摘要（原文）

> Annotating 3D data remains a costly bottleneck for 3D object detection, motivating the development of weakly supervised annotation methods that rely on more accessible 2D box annotations. However, relying solely on 2D boxes introduces projection ambiguities since a single 2D box can correspond to multiple valid 3D poses. Furthermore, partial object visibility under a single viewpoint setting makes accurate 3D box estimation difficult. We propose MVAT, a novel framework that leverages temporal multi-view present in sequential data to address these challenges. Our approach aggregates object-centric point clouds across time to build 3D object representations as dense and complete as possible. A Teacher-Student distillation paradigm is employed: The Teacher network learns from single viewpoints but targets are derived from temporally aggregated static objects. Then the Teacher generates high quality pseudo-labels that the Student learns to predict from a single viewpoint for both static and moving objects. The whole framework incorporates a multi-view 2D projection loss to enforce consistency between predicted 3D boxes and all available 2D annotations. Experiments on the nuScenes and Waymo Open datasets demonstrate that MVAT achieves state-of-the-art performance for weakly supervised 3D object detection, significantly narrowing the gap with fully supervised methods without requiring any 3D box annotations. % \footnote{Code available upon acceptance} Our code is available in our public repository (\href{https://github.com/CEA-LIST/MVAT}{code}).

