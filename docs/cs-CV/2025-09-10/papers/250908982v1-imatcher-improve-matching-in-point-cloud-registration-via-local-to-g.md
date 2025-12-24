---
layout: default
title: "iMatcher: Improve matching in point cloud registration via local-to-global geometric consistency learning"
---

# iMatcher: Improve matching in point cloud registration via local-to-global geometric consistency learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08982" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08982v1</a>
  <a href="https://arxiv.org/pdf/2509.08982.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08982v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08982v1', 'iMatcher: Improve matching in point cloud registration via local-to-global geometric consistency learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Karim Slimani, Catherine Achard, Brahim Tamadazte

**分类**: cs.CV

**发布日期**: 2025-09-10

---

## 💡 一句话要点

**iMatcher：通过局部到全局几何一致性学习改进点云配准中的特征匹配**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `点云配准` `特征匹配` `几何一致性` `深度学习` `图神经网络`

## 📋 核心要点

1. 现有方法在点云配准中，难以有效利用局部和全局几何一致性信息，导致特征匹配精度不高。
2. iMatcher通过学习局部到全局的几何一致性，预测置信度矩阵，从而提升特征匹配的准确性。
3. 实验表明，iMatcher在多个数据集上显著提高了刚性配准性能，内点率达到state-of-the-art水平。

## 📝 摘要（中文）

本文提出iMatcher，一个完全可微的点云配准特征匹配框架。该方法利用学习到的特征来预测几何一致的置信度矩阵，融合了局部和全局一致性。首先，局部图嵌入模块初始化得分矩阵。然后，通过在3D空间中进行双向源到目标和目标到源的最近邻搜索，进行重定位步骤以细化该矩阵。配对的点特征被堆叠在一起，通过全局几何一致性学习进行细化，以预测点级的匹配概率。在真实世界的室外（KITTI、KITTI-360）和室内（3DMatch）数据集，以及6自由度姿态估计（TUD-L）和部分到部分匹配（MVP-RG）上的大量实验表明，iMatcher显著提高了刚性配准性能。该方法实现了最先进的内点率，在KITTI上达到95%-97%，在KITTI-360上达到94%-97%，在3DMatch上高达81.1%，突显了其在不同环境下的鲁棒性。

## 🔬 方法详解

**问题定义**：点云配准旨在找到两个点云之间的变换关系，而特征匹配是其中的关键步骤。现有方法通常难以充分利用局部和全局的几何约束信息，导致匹配错误率较高，尤其是在噪声、遮挡和低重叠率等情况下。因此，如何有效地利用几何一致性信息来提高特征匹配的准确性是亟待解决的问题。

**核心思路**：iMatcher的核心思路是学习一个几何一致的置信度矩阵，该矩阵能够反映点对之间匹配的概率。通过融合局部和全局的几何信息，iMatcher能够更准确地评估点对之间的匹配关系。这种方法的设计基于以下考虑：局部几何信息可以提供初始的匹配线索，而全局几何信息可以用于消除歧义和提高匹配的鲁棒性。

**技术框架**：iMatcher的整体框架包括以下几个主要模块：1) 局部图嵌入模块：用于初始化得分矩阵，捕捉局部几何信息。2) 重定位步骤：通过双向最近邻搜索，细化得分矩阵。3) 全局几何一致性学习模块：通过学习到的特征，预测点级的匹配概率。整个流程是端到端可微的，可以进行联合优化。

**关键创新**：iMatcher的关键创新在于其全局几何一致性学习模块，该模块能够有效地融合局部和全局的几何信息，从而提高特征匹配的准确性。与现有方法相比，iMatcher不仅考虑了点对之间的局部关系，还考虑了点云整体的几何结构，从而能够更好地处理噪声、遮挡和低重叠率等情况。

**关键设计**：在局部图嵌入模块中，使用了图神经网络来学习点云的局部特征。在全局几何一致性学习模块中，使用了多层感知机（MLP）来预测点级的匹配概率。损失函数的设计考虑了匹配的准确性和一致性，使用了交叉熵损失和对比损失等。

## 📊 实验亮点

iMatcher在KITTI、KITTI-360和3DMatch等多个数据集上取得了state-of-the-art的性能。在KITTI数据集上，iMatcher的内点率达到了95%-97%，在KITTI-360数据集上达到了94%-97%，在3DMatch数据集上高达81.1%。这些结果表明，iMatcher在不同场景下都具有很强的鲁棒性和泛化能力。

## 🎯 应用场景

iMatcher在机器人导航、三维重建、自动驾驶等领域具有广泛的应用前景。高精度的点云配准是这些应用的基础，iMatcher的改进可以显著提升这些应用的性能和鲁棒性。例如，在自动驾驶中，iMatcher可以用于精确地定位车辆，从而提高驾驶安全性。

## 📄 摘要（原文）

> This paper presents iMatcher, a fully differentiable framework for feature matching in point cloud registration. The proposed method leverages learned features to predict a geometrically consistent confidence matrix, incorporating both local and global consistency. First, a local graph embedding module leads to an initialization of the score matrix. A subsequent repositioning step refines this matrix by considering bilateral source-to-target and target-to-source matching via nearest neighbor search in 3D space. The paired point features are then stacked together to be refined through global geometric consistency learning to predict a point-wise matching probability. Extensive experiments on real-world outdoor (KITTI, KITTI-360) and indoor (3DMatch) datasets, as well as on 6-DoF pose estimation (TUD-L) and partial-to-partial matching (MVP-RG), demonstrate that iMatcher significantly improves rigid registration performance. The method achieves state-of-the-art inlier ratios, scoring 95% - 97% on KITTI, 94% - 97% on KITTI-360, and up to 81.1% on 3DMatch, highlighting its robustness across diverse settings.

