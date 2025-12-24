---
layout: default
title: "HOTFLoc++: End-to-End Hierarchical LiDAR Place Recognition, Re-Ranking, and 6-DoF Metric Localisation in Forests"
---

# HOTFLoc++: End-to-End Hierarchical LiDAR Place Recognition, Re-Ranking, and 6-DoF Metric Localisation in Forests

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.09170" class="toolbar-btn" target="_blank">📄 arXiv: 2511.09170v1</a>
  <a href="https://arxiv.org/pdf/2511.09170.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09170v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.09170v1', 'HOTFLoc++: End-to-End Hierarchical LiDAR Place Recognition, Re-Ranking, and 6-DoF Metric Localisation in Forests')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ethan Griffiths, Maryam Haghighat, Simon Denman, Clinton Fookes, Milad Ramezani

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-12

**备注**: 9 pages, 2 figures. Submitted to RA-L

---

## 💡 一句话要点

**HOTFLoc++：森林环境下端到端分层LiDAR定位与重排序**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `LiDAR定位` `地点识别` `点云配准` `Transformer网络` `分层特征` `多尺度几何验证` `森林环境` `机器人导航`

## 📋 核心要点

1. 现有LiDAR定位方法在森林等复杂环境中，易受杂波、自相似性和视角变化的影响，导致定位精度下降。
2. HOTFLoc++利用八叉树Transformer提取分层局部描述符，并提出可学习的多尺度几何验证模块，提升定位鲁棒性。
3. 实验表明，HOTFLoc++在多个数据集上优于现有方法，尤其在CS-Wild-Places数据集上Recall@1提升显著。

## 📝 摘要（中文）

本文提出HOTFLoc++，一个用于森林环境中LiDAR地点识别、重排序和6自由度(6-DoF)度量定位的端到端框架。该方法利用基于八叉树的Transformer提取多粒度的分层局部描述符，增强了在复杂场景中对杂波、自相似性和视角变化的鲁棒性，包括森林和城市环境中的地对地和地对空场景。我们提出了一个可学习的多尺度几何验证模块，以减少在单尺度对应关系退化情况下的重排序失败。我们的由粗到精的配准方法实现了与基线方法相当或更低的定位误差，并且对于密集点云，运行时间比RANSAC提高了两个数量级。在公共数据集上的实验结果表明，与最先进的方法相比，我们的方法具有优越性，在CS-Wild-Places上实现了90.7%的平均Recall@1，比基线方法提高了29.6个百分点，同时在单源基准测试中保持了高性能，在Wild-Places和MulRan上分别实现了91.7%和96.0%的平均Recall@1。我们的方法在97.2%的6-DoF配准尝试中实现了低于2米和5度的误差，我们的多尺度重排序模块平均减少了约2倍的定位误差。代码将在接收后提供。

## 🔬 方法详解

**问题定义**：论文旨在解决森林等复杂环境中，LiDAR点云定位精度低的问题。现有方法难以有效应对杂波、自相似性和视角变化，导致地点识别和位姿估计的准确性下降，尤其是在地对地和地对空场景中表现不佳。

**核心思路**：论文的核心思路是利用分层局部描述符和多尺度几何验证，增强对复杂环境的感知能力。通过八叉树Transformer提取不同粒度的特征，捕捉场景的全局和局部信息，从而提高地点识别的准确性。多尺度几何验证模块则用于过滤错误的对应关系，提升位姿估计的精度。

**技术框架**：HOTFLoc++框架包含以下主要模块：1) 基于八叉树的Transformer：用于提取多粒度的分层局部描述符。2) 地点识别：利用提取的描述符进行地点匹配。3) 多尺度几何验证：通过可学习的模块验证匹配的几何一致性，减少错误匹配。4) 由粗到精的配准：利用地点识别的结果进行初始位姿估计，然后通过迭代优化进行精细配准。

**关键创新**：该方法最重要的创新点在于分层局部描述符的提取和多尺度几何验证模块的设计。分层描述符能够捕捉不同尺度的场景信息，提高对视角变化的鲁棒性。多尺度几何验证模块则能够有效过滤错误的对应关系，提升位姿估计的精度，尤其是在单尺度信息退化的情况下。

**关键设计**：八叉树Transformer的具体结构未知，但其关键在于利用八叉树结构对点云进行分层划分，并在每个层级上应用Transformer进行特征提取。多尺度几何验证模块的具体实现未知，但推测其利用多个尺度的几何信息（例如点云的局部形状、法向量等）来判断对应关系的正确性。损失函数的设计也未知，但可能包含地点识别的损失和位姿估计的损失。

## 📊 实验亮点

HOTFLoc++在CS-Wild-Places数据集上取得了显著的性能提升，Recall@1达到90.7%，相比基线方法提高了29.6个百分点。同时，在Wild-Places和MulRan等单源基准测试中也保持了较高的性能，Recall@1分别达到91.7%和96.0%。该方法在6-DoF配准中，97.2%的尝试实现了低于2米和5度的误差，多尺度重排序模块平均减少了约2倍的定位误差。

## 🎯 应用场景

该研究成果可应用于森林勘探、自动驾驶、机器人导航、三维地图重建等领域。尤其是在需要高精度定位的复杂环境中，例如森林、矿区、城市峡谷等，该方法具有重要的应用价值。未来，该技术有望进一步提升无人系统的自主导航能力，并促进相关产业的发展。

## 📄 摘要（原文）

> This article presents HOTFLoc++, an end-to-end framework for LiDAR place recognition, re-ranking, and 6-DoF metric localisation in forests. Leveraging an octree-based transformer, our approach extracts hierarchical local descriptors at multiple granularities to increase robustness to clutter, self-similarity, and viewpoint changes in challenging scenarios, including ground-to-ground and ground-to-aerial in forest and urban environments. We propose a learnable multi-scale geometric verification module to reduce re-ranking failures in the presence of degraded single-scale correspondences. Our coarse-to-fine registration approach achieves comparable or lower localisation errors to baselines, with runtime improvements of two orders of magnitude over RANSAC for dense point clouds. Experimental results on public datasets show the superiority of our approach compared to state-of-the-art methods, achieving an average Recall@1 of 90.7% on CS-Wild-Places: an improvement of 29.6 percentage points over baselines, while maintaining high performance on single-source benchmarks with an average Recall@1 of 91.7% and 96.0% on Wild-Places and MulRan, respectively. Our method achieves under 2 m and 5 degrees error for 97.2% of 6-DoF registration attempts, with our multi-scale re-ranking module reducing localisation errors by ~2$\times$ on average. The code will be available upon acceptance.

