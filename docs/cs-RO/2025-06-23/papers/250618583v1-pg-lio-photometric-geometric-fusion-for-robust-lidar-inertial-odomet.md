---
layout: default
title: "PG-LIO: Photometric-Geometric fusion for Robust LiDAR-Inertial Odometry"
---

# PG-LIO: Photometric-Geometric fusion for Robust LiDAR-Inertial Odometry

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18583" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18583v1</a>
  <a href="https://arxiv.org/pdf/2506.18583.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18583v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18583v1', 'PG-LIO: Photometric-Geometric fusion for Robust LiDAR-Inertial Odometry')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikhil Khedekar, Kostas Alexis

**分类**: cs.RO

**发布日期**: 2025-06-23

**备注**: 8 pages, 6 figures

**🔗 代码/项目**: [GITHUB](https://github.com/ntnu-arl/mimosa)

---

## 💡 一句话要点

**提出PG-LIO以解决LiDAR惯性测量中几何结构不足的问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `LiDAR惯性测量` `多模态融合` `实时优化` `因子图` `鲁棒性增强`

## 📋 核心要点

1. 现有的LIO方法在缺乏几何结构时容易出现退化，导致状态估计不准确，限制了其应用范围。
2. PG-LIO通过融合光度和几何信息，结合IMU的惯性约束，提出了一种新的实时LIO方法，增强了系统的鲁棒性。
3. 实验结果显示，PG-LIO在几何良好的场景中表现优异，并在几何退化情况下相比于其他方法有显著提升。

## 📝 摘要（中文）

LiDAR惯性测量（LIO）广泛应用于自主机器人中的状态估计和地图构建。传统的LIO方法通常依赖于LiDAR采样的几何结构来制定约束，因此在几何结构缺失时容易出现退化现象，导致失败。为了解决这一问题，本文提出了PG-LIO，一种实时的LIO方法，融合了LiDAR采样的光度和几何信息以及来自惯性测量单元（IMU）的惯性约束。该多模态信息通过滑动窗口优化的因子图进行集成。实验结果表明，PG-LIO在几何结构良好的场景中与现有最先进的LIO方法的准确性相当，同时在退化情况下显著提高了准确性。我们在几何自相似的隧道中以7.5m/s的平均速度（最大速度10.8m/s）手动驾驶1公里的轨迹，仅出现1米的漂移。

## 🔬 方法详解

**问题定义**：本文旨在解决传统LIO方法在缺乏几何结构时的退化问题，导致状态估计不准确的挑战。

**核心思路**：PG-LIO通过融合光度信息和几何信息，结合IMU的惯性数据，增强了LIO在各种环境下的鲁棒性，特别是在几何结构不足的情况下。

**技术框架**：PG-LIO采用因子图优化框架，利用滑动窗口技术实时处理多模态信息，包括LiDAR的光度和几何数据，以及IMU的惯性约束。

**关键创新**：PG-LIO的核心创新在于其多模态信息融合策略，能够在几何结构不足的情况下保持高精度的状态估计，这与传统方法单一依赖几何信息的方式有本质区别。

**关键设计**：在设计中，PG-LIO采用了优化的因子图结构，设置了适当的损失函数以平衡光度和几何信息的影响，确保在不同场景下的准确性和鲁棒性。

## 📊 实验亮点

PG-LIO在几何自相似的隧道中以7.5m/s的平均速度完成1公里的手动驾驶，仅出现1米的漂移，显示出其在退化场景中的优越性能，相比于其他融合强度信息的方法，准确性有显著提升。

## 🎯 应用场景

PG-LIO可广泛应用于自主驾驶、无人机导航和机器人定位等领域，尤其是在复杂环境中，如隧道或城市街道，具有重要的实际价值。其提升的鲁棒性和准确性将推动相关技术的进一步发展和应用。

## 📄 摘要（原文）

> LiDAR-Inertial Odometry (LIO) is widely used for accurate state estimation and mapping which is an essential requirement for autonomous robots. Conventional LIO methods typically rely on formulating constraints from the geometric structure sampled by the LiDAR. Hence, in the lack of geometric structure, these tend to become ill-conditioned (degenerate) and fail. Robustness of LIO to such conditions is a necessity for its broader deployment. To address this, we propose PG-LIO, a real-time LIO method that fuses photometric and geometric information sampled by the LiDAR along with inertial constraints from an Inertial Measurement Unit (IMU). This multi-modal information is integrated into a factor graph optimized over a sliding window for real-time operation. We evaluate PG-LIO on multiple datasets that include both geometrically well-conditioned as well as self-similar scenarios. Our method achieves accuracy on par with state-of-the-art LIO in geometrically well-structured settings while significantly improving accuracy in degenerate cases including against methods that also fuse intensity. Notably, we demonstrate only 1 m drift over a 1 km manually piloted aerial trajectory through a geometrically self-similar tunnel at an average speed of 7.5m/s (max speed 10.8 m/s). For the benefit of the community, we shall also release our source code https://github.com/ntnu-arl/mimosa

