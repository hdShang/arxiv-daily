---
layout: default
title: "TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric Constraints"
---

# TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23207" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23207v1</a>
  <a href="https://arxiv.org/pdf/2506.23207.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23207v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23207v1', 'TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu

**分类**: cs.CV

**发布日期**: 2025-06-29

---

## 💡 一句话要点

**提出TVG-SLAM以解决RGB-only SLAM系统的鲁棒性问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `RGB-only SLAM` `三视几何约束` `高斯点云` `鲁棒性` `相机跟踪` `光度损失` `动态衰减机制` `户外环境`

## 📋 核心要点

1. 现有RGB-only SLAM系统在光照和视角变化剧烈的环境中鲁棒性不足，导致跟踪不稳定。
2. TVG-SLAM通过引入三视几何约束和混合几何约束，增强了相机跟踪的稳定性和映射质量。
3. 实验结果显示，TVG-SLAM在多个数据集上表现优异，特别是在最具挑战性的数据集中，跟踪误差显著降低。

## 📝 摘要（中文）

近年来，3D高斯点云技术的进步使得RGB-only SLAM系统能够实现高保真场景表示。然而，现有系统过度依赖光度渲染损失进行相机跟踪，导致在视角和光照变化剧烈的户外环境中鲁棒性不足。为了解决这些挑战，本文提出了TVG-SLAM，一个鲁棒的RGB-only 3DGS SLAM系统，利用新颖的三视几何范式确保一致的跟踪和高质量的映射。我们引入了密集的三视匹配模块，将可靠的成对对应关系聚合为一致的三视匹配，形成跨帧的鲁棒几何约束。实验结果表明，TVG-SLAM在多个公共户外数据集上优于之前的RGB-only 3DGS SLAM系统，尤其在最具挑战性的数据集中，跟踪鲁棒性提高，平均绝对轨迹误差降低了69.0%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有RGB-only SLAM系统在户外环境中因光照和视角变化导致的跟踪不稳定性问题。现有方法过度依赖光度渲染损失，缺乏鲁棒性。

**核心思路**：TVG-SLAM通过引入三视几何约束来增强跟踪的稳定性，同时结合光度损失，确保在极端条件下的准确姿态估计。

**技术框架**：TVG-SLAM的整体架构包括密集三视匹配模块、混合几何约束和新的概率初始化策略，形成一个完整的SLAM流程。

**关键创新**：最重要的创新在于引入了三视几何范式和动态渲染信任衰减机制，这与现有方法的单一光度损失依赖形成了本质区别。

**关键设计**：在参数设置上，采用了新的概率初始化策略来编码三视对应关系的几何不确定性，并设计了动态衰减机制以减少因映射延迟引起的跟踪漂移。

## 📊 实验亮点

在多个公共户外数据集上的实验结果表明，TVG-SLAM显著优于之前的RGB-only 3DGS SLAM系统。在最具挑战性的数据集中，跟踪鲁棒性提高，平均绝对轨迹误差降低了69.0%，同时实现了最先进的渲染质量。

## 🎯 应用场景

TVG-SLAM的研究成果可广泛应用于无人驾驶、增强现实和机器人导航等领域。其鲁棒的跟踪能力和高质量的映射性能将极大提升这些应用的可靠性和实用性，推动相关技术的发展与应用。未来，随着算法的进一步优化，TVG-SLAM有望在更复杂的环境中发挥作用。

## 📄 摘要（原文）

> Recent advances in 3D Gaussian Splatting (3DGS) have enabled RGB-only SLAM systems to achieve high-fidelity scene representation. However, the heavy reliance of existing systems on photometric rendering loss for camera tracking undermines their robustness, especially in unbounded outdoor environments with severe viewpoint and illumination changes. To address these challenges, we propose TVG-SLAM, a robust RGB-only 3DGS SLAM system that leverages a novel tri-view geometry paradigm to ensure consistent tracking and high-quality mapping. We introduce a dense tri-view matching module that aggregates reliable pairwise correspondences into consistent tri-view matches, forming robust geometric constraints across frames. For tracking, we propose Hybrid Geometric Constraints, which leverage tri-view matches to construct complementary geometric cues alongside photometric loss, ensuring accurate and stable pose estimation even under drastic viewpoint shifts and lighting variations. For mapping, we propose a new probabilistic initialization strategy that encodes geometric uncertainty from tri-view correspondences into newly initialized Gaussians. Additionally, we design a Dynamic Attenuation of Rendering Trust mechanism to mitigate tracking drift caused by mapping latency. Experiments on multiple public outdoor datasets show that our TVG-SLAM outperforms prior RGB-only 3DGS-based SLAM systems. Notably, in the most challenging dataset, our method improves tracking robustness, reducing the average Absolute Trajectory Error (ATE) by 69.0\% while achieving state-of-the-art rendering quality. The implementation of our method will be released as open-source.

