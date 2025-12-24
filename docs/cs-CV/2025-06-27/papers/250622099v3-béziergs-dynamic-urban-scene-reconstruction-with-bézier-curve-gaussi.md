---
layout: default
title: "BézierGS: Dynamic Urban Scene Reconstruction with Bézier Curve Gaussian Splatting"
---

# BézierGS: Dynamic Urban Scene Reconstruction with Bézier Curve Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22099" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22099v3</a>
  <a href="https://arxiv.org/pdf/2506.22099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22099v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22099v3', 'BézierGS: Dynamic Urban Scene Reconstruction with Bézier Curve Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zipei Ma, Junzhe Jiang, Yurui Chen, Li Zhang

**分类**: cs.CV

**发布日期**: 2025-06-27 (更新: 2025-07-08)

**备注**: Accepted at ICCV 2025, Project Page: https://github.com/fudan-zvg/BezierGS

---

## 💡 一句话要点

**提出BézierGS以解决动态城市场景重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态场景重建` `Bézier曲线` `高斯喷溅` `自动驾驶` `虚拟现实` `城市规划` `机器学习`

## 📋 核心要点

1. 现有方法依赖高精度的物体姿态注释，限制了动态物体的重建和渲染过程，难以实现大规模场景重建。
2. 本文提出BézierGS，通过可学习的Bézier曲线表示动态物体的运动轨迹，自动纠正姿态误差，充分利用时间信息。
3. 在Waymo开放数据集和nuPlan基准上，BézierGS在动态和静态场景重建及新视角合成方面表现优异，超越了现有方法。

## 📝 摘要（中文）

街景的真实重建对于开发自动驾驶的现实模拟器至关重要。现有方法依赖于物体姿态注释，这限制了大规模场景重建的能力。为了解决这一挑战，本文提出了Bézier曲线高斯喷溅（BézierGS），通过可学习的Bézier曲线表示动态物体的运动轨迹，充分利用动态物体的时间信息，并自动纠正姿态误差。通过对动态物体渲染的额外监督和曲线间一致性约束，我们实现了场景元素的合理分离和重建。在Waymo开放数据集和nuPlan基准上的大量实验表明，BézierGS在动态和静态场景组件重建及新视角合成方面优于现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决动态城市场景重建中的物体姿态注释依赖问题，现有方法在大规模场景重建中存在局限性。

**核心思路**：提出BézierGS，通过可学习的Bézier曲线来表示动态物体的运动轨迹，利用时间信息来自动纠正姿态误差，从而提高重建精度。

**技术框架**：整体架构包括动态物体的运动轨迹建模、姿态误差纠正、动态物体渲染和曲线间一致性约束等模块，形成一个闭环的重建流程。

**关键创新**：最重要的创新在于引入可学习的Bézier曲线来表示动态物体的运动轨迹，区别于传统方法对物体姿态的依赖，增强了重建的灵活性和准确性。

**关键设计**：设计中采用了额外的监督信号来指导动态物体的渲染，并设置了曲线间的一致性约束，确保了重建结果的合理性和准确性。具体的损失函数和网络结构细节在实验中进行了优化。

## 📊 实验亮点

实验结果显示，BézierGS在动态和静态场景组件重建方面的性能显著优于现有最先进的方法。在Waymo开放数据集上，BézierGS的重建精度提升了XX%，在nuPlan基准上也取得了YY%的性能提升，验证了其有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、虚拟现实和城市规划等。通过提高动态场景的重建精度，能够为自动驾驶系统提供更真实的环境模拟，进而提升安全性和可靠性。此外，该方法也可用于生成高质量的城市场景模型，推动相关领域的发展。

## 📄 摘要（原文）

> The realistic reconstruction of street scenes is critical for developing real-world simulators in autonomous driving. Most existing methods rely on object pose annotations, using these poses to reconstruct dynamic objects and move them during the rendering process. This dependence on high-precision object annotations limits large-scale and extensive scene reconstruction. To address this challenge, we propose Bézier curve Gaussian splatting (BézierGS), which represents the motion trajectories of dynamic objects using learnable Bézier curves. This approach fully leverages the temporal information of dynamic objects and, through learnable curve modeling, automatically corrects pose errors. By introducing additional supervision on dynamic object rendering and inter-curve consistency constraints, we achieve reasonable and accurate separation and reconstruction of scene elements. Extensive experiments on the Waymo Open Dataset and the nuPlan benchmark demonstrate that BézierGS outperforms state-of-the-art alternatives in both dynamic and static scene components reconstruction and novel view synthesis.

