---
layout: default
title: Blending 3D Geometry and Machine Learning for Multi-View Stereopsis
---

# Blending 3D Geometry and Machine Learning for Multi-View Stereopsis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03470" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03470v4</a>
  <a href="https://arxiv.org/pdf/2505.03470.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03470v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03470v4', 'Blending 3D Geometry and Machine Learning for Multi-View Stereopsis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vibhas Vats, Md. Alimoor Reza, David Crandall, Soon-heung Jung

**分类**: cs.CV, cs.AI, cs.CG, cs.LG

**发布日期**: 2025-05-06 (更新: 2025-09-14)

**备注**: A pre-print -- accepted at Neurocomputing. arXiv admin note: substantial text overlap with arXiv:2310.19583

**期刊**: Neurocomputing, 2025

---

## 💡 一句话要点

**提出GC MVSNet++以解决多视图立体视觉中的几何一致性问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `多视图立体视觉` `几何一致性` `深度学习` `3D重建` `计算机视觉` `代价正则化网络` `模型优化`

## 📋 核心要点

1. 现有的多视图立体视觉方法在几何一致性方面存在不足，导致学习效率低下。
2. GC MVSNet++通过在学习阶段强制执行几何一致性，显著提高了训练速度和效果。
3. 该方法在多个数据集上表现优异，达到了新的性能标杆，展示了其有效性。

## 📝 摘要（中文）

传统的多视图立体视觉（MVS）方法主要依赖于光度和几何一致性约束，而现代基于学习的算法通常在推断3D几何时依赖于平面扫描算法，仅在后处理阶段应用显式的几何一致性检查。本文提出GC MVSNet++，在学习阶段主动强制参考视图深度图在多个源视图和不同尺度下的几何一致性。通过直接惩罚几何不一致的像素，该方法显著加速了学习过程，训练迭代次数减少了一半。此外，论文还引入了一种密集连接的代价正则化网络，优化了特征连接以增强正则化效果。实验结果表明，该方法在DTU和BlendedMVS数据集上达到了新的最优状态，并在Tanks and Temples基准测试中获得第二名。

## 🔬 方法详解

**问题定义**：本文旨在解决传统多视图立体视觉方法在几何一致性方面的不足，现有方法往往在学习过程中未能有效利用几何一致性信息，导致训练效率低下。

**核心思路**：GC MVSNet++的核心思想是在学习阶段主动强制执行几何一致性，通过直接惩罚几何不一致的像素，来加速学习过程并提高模型的准确性。

**技术框架**：该方法的整体架构包括多个模块，首先是深度图的生成模块，然后是几何一致性检查模块，最后是代价正则化网络。通过这些模块的协同工作，实现了多视图、多尺度的几何一致性学习。

**关键创新**：GC MVSNet++是首个在学习过程中强制执行多视图、多尺度的几何一致性的方法，这一创新显著区别于以往仅在后处理阶段进行几何一致性检查的算法。

**关键设计**：在网络设计上，采用了密集连接的代价正则化网络，包含简单和特征密集的两种模块设计，以优化特征连接。此外，损失函数设计上引入了几何一致性惩罚项，进一步提升了模型的学习效果。

## 📊 实验亮点

实验结果表明，GC MVSNet++在DTU和BlendedMVS数据集上达到了新的最优性能，训练迭代次数减少了50%。在Tanks and Temples基准测试中，该方法获得第二名，显示出其在多视图立体视觉任务中的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、机器人导航、虚拟现实和增强现实等。通过提高多视图立体视觉的精度和效率，该方法能够在实际场景中提供更高质量的3D重建，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Traditional multi-view stereo (MVS) methods primarily depend on photometric and geometric consistency constraints. In contrast, modern learning-based algorithms often rely on the plane sweep algorithm to infer 3D geometry, applying explicit geometric consistency (GC) checks only as a post-processing step, with no impact on the learning process itself. In this work, we introduce GC MVSNet plus plus, a novel approach that actively enforces geometric consistency of reference view depth maps across multiple source views (multi view) and at various scales (multi scale) during the learning phase (see Fig. 1). This integrated GC check significantly accelerates the learning process by directly penalizing geometrically inconsistent pixels, effectively halving the number of training iterations compared to other MVS methods. Furthermore, we introduce a densely connected cost regularization network with two distinct block designs simple and feature dense optimized to harness dense feature connections for enhanced regularization. Extensive experiments demonstrate that our approach achieves a new state of the art on the DTU and BlendedMVS datasets and secures second place on the Tanks and Temples benchmark. To our knowledge, GC MVSNet plus plus is the first method to enforce multi-view, multi-scale supervised geometric consistency during learning. Our code is available.

