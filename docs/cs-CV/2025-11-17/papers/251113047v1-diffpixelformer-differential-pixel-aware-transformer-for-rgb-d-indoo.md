---
layout: default
title: DiffPixelFormer: Differential Pixel-Aware Transformer for RGB-D Indoor Scene Segmentation
---

# DiffPixelFormer: Differential Pixel-Aware Transformer for RGB-D Indoor Scene Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13047" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13047v1</a>
  <a href="https://arxiv.org/pdf/2511.13047.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13047v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.13047v1', 'DiffPixelFormer: Differential Pixel-Aware Transformer for RGB-D Indoor Scene Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yan Gong, Jianli Lu, Yongsheng Gao, Jie Zhao, Xiaojuan Zhang, Susanto Rahardja

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-17

**备注**: 11 pages, 5 figures, 5 tables

**🔗 代码/项目**: [GITHUB](https://github.com/gongyan1/DiffPixelFormer)

---

## 💡 一句话要点

**提出DiffPixelFormer，用于提升RGB-D室内场景分割的精度和效率。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `RGB-D场景分割` `Transformer` `跨模态融合` `自注意力机制` `室内场景理解` `语义分割` `深度学习`

## 📋 核心要点

1. 现有RGB-D室内场景分割方法依赖计算量大的交叉注意力，且模态内和模态间特征关系建模不足。
2. DiffPixelFormer通过差分像素感知Transformer，增强模态内表示，并使用DSIM模块解耦模态特定和共享线索。
3. 在SUN RGB-D和NYUDv2数据集上，DiffPixelFormer-L的mIoU分别提升了1.78%和2.75%。

## 📝 摘要（中文）

室内语义分割是计算机视觉和机器人学的基石，支持自主导航、增强现实和智能环境等应用。尽管RGB-D融合利用了互补的外观和几何线索，但现有方法通常依赖于计算密集型的交叉注意力机制，并且对模态内和模态间特征关系的建模不足，导致特征对齐不精确和判别表示有限。为了解决这些挑战，我们提出了一种差分像素感知Transformer，即DiffPixelFormer，用于RGB-D室内场景分割，它同时增强模态内表示并建模模态间交互。其核心是模态内-模态间交互块（IIMIB），它通过自注意力捕获模态内长程依赖关系，并使用差分-共享模态间（DSIM）模块建模模态间交互，以解耦模态特定和共享线索，从而实现细粒度的像素级跨模态对齐。此外，动态融合策略平衡了模态贡献，并根据场景特征充分利用RGB-D信息。在SUN RGB-D和NYUDv2基准上的大量实验表明，DiffPixelFormer-L实现了54.28%和59.95%的mIoU分数，分别优于DFormer-L 1.78%和2.75%。代码已在https://github.com/gongyan1/DiffPixelFormer上提供。

## 🔬 方法详解

**问题定义**：现有RGB-D室内场景分割方法在融合RGB和深度信息时，通常采用计算复杂度高的交叉注意力机制，并且对模态内部和模态之间的特征关系建模不够充分，导致特征对齐不精确，最终限制了分割的精度。这些方法难以有效区分模态特定信息和模态共享信息，从而影响了最终的分割效果。

**核心思路**：DiffPixelFormer的核心思路是通过差分像素感知Transformer，同时增强模态内表示和建模模态间交互。具体来说，它利用自注意力机制捕获模态内的长程依赖关系，并设计了差分-共享模态间（DSIM）模块来解耦模态特定和共享的线索，从而实现细粒度的像素级跨模态对齐。这种设计旨在更有效地利用RGB-D信息，提升分割精度。

**技术框架**：DiffPixelFormer的整体架构包含以下几个主要模块：首先，分别对RGB和深度图像进行特征提取。然后，通过提出的模态内-模态间交互块（IIMIB）进行特征融合，该模块包含自注意力机制和DSIM模块。自注意力机制用于捕获模态内的长程依赖关系，DSIM模块用于解耦模态特定和共享的线索。最后，通过一个动态融合策略来平衡模态贡献，并进行像素级别的语义分割。

**关键创新**：DiffPixelFormer的关键创新在于提出了差分-共享模态间（DSIM）模块。与传统的交叉注意力机制不同，DSIM模块能够显式地解耦模态特定和共享的特征，从而实现更精细的跨模态对齐。此外，动态融合策略能够根据场景特征自适应地调整RGB和深度信息的权重，进一步提升分割性能。

**关键设计**：DSIM模块的设计是关键。它通过差分学习的方式，将每个模态的特征分解为共享部分和特定部分。共享部分用于表示两个模态共有的信息，而特定部分则用于表示每个模态独有的信息。这种分解方式有助于模型更好地理解RGB-D数据，并提升分割精度。动态融合策略使用一个可学习的权重来平衡RGB和深度信息的贡献，该权重根据输入图像的特征动态调整。

## 📊 实验亮点

DiffPixelFormer在SUN RGB-D和NYUDv2数据集上取得了显著的性能提升。在SUN RGB-D数据集上，DiffPixelFormer-L达到了54.28%的mIoU，相比DFormer-L提升了1.78%。在NYUDv2数据集上，DiffPixelFormer-L达到了59.95%的mIoU，相比DFormer-L提升了2.75%。这些结果表明DiffPixelFormer在RGB-D室内场景分割任务中具有优越的性能。

## 🎯 应用场景

DiffPixelFormer在室内场景理解方面具有广泛的应用前景，例如服务机器人、增强现实、智能家居等。高精度的室内场景分割可以帮助机器人更好地理解周围环境，从而实现更智能的导航和交互。在增强现实应用中，可以提供更逼真的场景渲染和对象交互。在智能家居领域，可以实现更精细的环境感知和控制。

## 📄 摘要（原文）

> Indoor semantic segmentation is fundamental to computer vision and robotics, supporting applications such as autonomous navigation, augmented reality, and smart environments. Although RGB-D fusion leverages complementary appearance and geometric cues, existing methods often depend on computationally intensive cross-attention mechanisms and insufficiently model intra- and inter-modal feature relationships, resulting in imprecise feature alignment and limited discriminative representation. To address these challenges, we propose DiffPixelFormer, a differential pixel-aware Transformer for RGB-D indoor scene segmentation that simultaneously enhances intra-modal representations and models inter-modal interactions. At its core, the Intra-Inter Modal Interaction Block (IIMIB) captures intra-modal long-range dependencies via self-attention and models inter-modal interactions with the Differential-Shared Inter-Modal (DSIM) module to disentangle modality-specific and shared cues, enabling fine-grained, pixel-level cross-modal alignment. Furthermore, a dynamic fusion strategy balances modality contributions and fully exploits RGB-D information according to scene characteristics. Extensive experiments on the SUN RGB-D and NYUDv2 benchmarks demonstrate that DiffPixelFormer-L achieves mIoU scores of 54.28% and 59.95%, outperforming DFormer-L by 1.78% and 2.75%, respectively. Code is available at https://github.com/gongyan1/DiffPixelFormer.

