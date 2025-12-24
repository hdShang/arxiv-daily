---
layout: default
title: VGGT-SLAM: Dense RGB SLAM Optimized on the SL(4) Manifold
---

# VGGT-SLAM: Dense RGB SLAM Optimized on the SL(4) Manifold

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12549" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12549v2</a>
  <a href="https://arxiv.org/pdf/2505.12549.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12549v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12549v2', 'VGGT-SLAM: Dense RGB SLAM Optimized on the SL(4) Manifold')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dominic Maggio, Hyungtae Lim, Luca Carlone

**分类**: cs.CV

**发布日期**: 2025-05-18 (更新: 2025-05-23)

---

## 💡 一句话要点

**提出VGGT-SLAM以解决无标定单目相机的稠密RGB SLAM问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `稠密RGB SLAM` `无标定相机` `SL(4)流形` `场景重建` `单应性变换` `环闭约束` `机器人导航` `增强现实`

## 📋 核心要点

1. 现有的SLAM方法在处理无标定相机时，通常依赖于相似性变换，导致重建精度不足。
2. VGGT-SLAM通过在SL(4)流形上优化，解决了无标定相机的重建模糊性问题，实现了更一致的场景重建。
3. 实验结果表明，VGGT-SLAM在长视频序列下的地图质量显著提高，克服了VGGT的高GPU需求限制。

## 📝 摘要（中文）

我们提出了VGGT-SLAM，这是一个稠密RGB SLAM系统，通过增量和全局对齐从前馈场景重建方法VGGT创建的子地图，仅使用无标定单目相机。相关工作通常使用相似性变换（即平移、旋转和缩放）对齐子地图，但我们表明这种方法在无标定相机的情况下是不够的。特别是，我们重新审视了重建模糊性的概念，在没有对相机运动或场景结构的假设下，给定一组无标定相机，场景只能重建到真实几何的15自由度投影变换。这激励我们通过在SL(4)流形上优化来恢复跨子地图的一致场景重建，从而在考虑潜在环闭约束的情况下估计顺序子地图之间的15自由度单应性变换。通过大量实验验证，我们展示了VGGT-SLAM在使用长视频序列时实现了更好的地图质量，这对于VGGT由于其高GPU需求而不可行。

## 🔬 方法详解

**问题定义**：本论文旨在解决无标定单目相机在稠密RGB SLAM中的重建精度不足问题。现有方法依赖于相似性变换，无法有效处理相机运动和场景结构的不确定性。

**核心思路**：我们提出通过在SL(4)流形上进行优化，来恢复跨子地图的一致场景重建。该方法能够估计15自由度的单应性变换，克服了重建模糊性。

**技术框架**：VGGT-SLAM的整体架构包括子地图的增量创建、全局对齐和优化过程。首先，通过前馈场景重建生成子地图，然后在SL(4)流形上进行优化以实现一致性。

**关键创新**：最重要的创新在于引入SL(4)流形优化方法，能够有效处理无标定相机的重建模糊性，与传统的相似性变换方法本质上不同。

**关键设计**：在设计中，我们设置了适当的损失函数以优化单应性变换，并考虑了环闭约束以提高重建的一致性和精度。

## 📊 实验亮点

实验结果显示，VGGT-SLAM在处理长视频序列时，地图质量显著提高，相较于VGGT，性能提升幅度达到XX%（具体数据未知），有效克服了高GPU需求的限制。

## 🎯 应用场景

VGGT-SLAM的研究具有广泛的应用潜力，尤其在机器人导航、增强现实和自动驾驶等领域。其能够在不依赖高精度相机标定的情况下，实现高质量的场景重建，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We present VGGT-SLAM, a dense RGB SLAM system constructed by incrementally and globally aligning submaps created from the feed-forward scene reconstruction approach VGGT using only uncalibrated monocular cameras. While related works align submaps using similarity transforms (i.e., translation, rotation, and scale), we show that such approaches are inadequate in the case of uncalibrated cameras. In particular, we revisit the idea of reconstruction ambiguity, where given a set of uncalibrated cameras with no assumption on the camera motion or scene structure, the scene can only be reconstructed up to a 15-degrees-of-freedom projective transformation of the true geometry. This inspires us to recover a consistent scene reconstruction across submaps by optimizing over the SL(4) manifold, thus estimating 15-degrees-of-freedom homography transforms between sequential submaps while accounting for potential loop closure constraints. As verified by extensive experiments, we demonstrate that VGGT-SLAM achieves improved map quality using long video sequences that are infeasible for VGGT due to its high GPU requirements.

