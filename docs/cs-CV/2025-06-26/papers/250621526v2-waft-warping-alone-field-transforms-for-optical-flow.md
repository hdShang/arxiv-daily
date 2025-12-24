---
layout: default
title: "WAFT: Warping-Alone Field Transforms for Optical Flow"
---

# WAFT: Warping-Alone Field Transforms for Optical Flow

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21526" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21526v2</a>
  <a href="https://arxiv.org/pdf/2506.21526.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21526v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21526v2', 'WAFT: Warping-Alone Field Transforms for Optical Flow')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yihan Wang, Jia Deng

**分类**: cs.CV

**发布日期**: 2025-06-26 (更新: 2025-10-07)

**🔗 代码/项目**: [GITHUB](https://github.com/princeton-vl/WAFT)

---

## 💡 一句话要点

**提出WAFT以解决光流估计中的高内存消耗问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `光流估计` `高分辨率变形` `成本体积` `实时处理` `自动驾驶` `机器人导航` `性能优化`

## 📋 核心要点

1. 现有光流估计方法通常依赖于成本体积，导致内存消耗高且计算复杂。
2. WAFT通过高分辨率变形替代成本体积，提供了一种简单有效的光流估计新方法。
3. WAFT在多个基准测试中表现优异，尤其在KITTI上实现了最佳的零-shot泛化，速度显著提升。

## 📝 摘要（中文）

我们介绍了Warping-Alone Field Transforms（WAFT），这是一种简单而有效的光流估计方法。WAFT与RAFT相似，但用高分辨率的变形替代了成本体积，从而在降低内存消耗的同时提高了准确性。这一设计挑战了传统观念，即构建成本体积是实现强大性能的必要条件。WAFT是一种简单灵活的元架构，具有最小的归纳偏置和对自定义设计的依赖。与现有方法相比，WAFT在Spring、Sintel和KITTI基准测试中排名第一，并在KITTI上实现了最佳的零-shot泛化，同时速度比性能相似的方法快多达4.1倍。代码和模型权重可在https://github.com/princeton-vl/WAFT获取。

## 🔬 方法详解

**问题定义**：论文旨在解决光流估计中高内存消耗和计算复杂度的问题。现有方法如RAFT依赖于成本体积，导致性能受限。

**核心思路**：WAFT的核心思路是用高分辨率的变形替代传统的成本体积，从而在保持高准确度的同时，显著降低内存需求。这样的设计使得模型更加灵活且易于实现。

**技术框架**：WAFT的整体架构包括输入图像的高分辨率变形模块，随后通过简单的卷积网络进行光流估计。该框架避免了复杂的成本体积构建过程，简化了计算流程。

**关键创新**：WAFT的主要创新在于其不依赖于成本体积的设计理念，这与传统方法本质上不同。通过高效的变形处理，WAFT在性能和资源消耗上实现了良好的平衡。

**关键设计**：在关键设计上，WAFT采用了高分辨率的变形策略，结合了简单的卷积网络结构，损失函数设计上也进行了优化，以确保模型在训练过程中的稳定性和准确性。整体设计强调了简洁性和高效性。

## 📊 实验亮点

WAFT在Spring、Sintel和KITTI基准测试中均排名第一，特别是在KITTI上实现了最佳的零-shot泛化能力。同时，WAFT的速度比性能相似的其他方法快多达4.1倍，展示了其在效率和准确性上的显著优势。

## 🎯 应用场景

WAFT在光流估计领域具有广泛的应用潜力，尤其适用于实时视频处理、自动驾驶、机器人导航等场景。其高效的内存使用和快速的计算速度使得在资源受限的环境中也能实现高性能的光流估计，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce Warping-Alone Field Transforms (WAFT), a simple and effective method for optical flow. WAFT is similar to RAFT but replaces cost volume with high-resolution warping, achieving better accuracy with lower memory cost. This design challenges the conventional wisdom that constructing cost volumes is necessary for strong performance. WAFT is a simple and flexible meta-architecture with minimal inductive biases and reliance on custom designs. Compared with existing methods, WAFT ranks 1st on Spring, Sintel, and KITTI benchmarks, achieves the best zero-shot generalization on KITTI, while being up to 4.1x faster than methods with similar performance. Code and model weights are available at https://github.com/princeton-vl/WAFT.

