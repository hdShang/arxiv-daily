---
layout: default
title: "SGS-3D: High-Fidelity 3D Instance Segmentation via Reliable Semantic Mask Splitting and Growing"
---

# SGS-3D: High-Fidelity 3D Instance Segmentation via Reliable Semantic Mask Splitting and Growing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05144" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05144v1</a>
  <a href="https://arxiv.org/pdf/2509.05144.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05144v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05144v1', 'SGS-3D: High-Fidelity 3D Instance Segmentation via Reliable Semantic Mask Splitting and Growing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chaolei Wang, Yang Luo, Jing Du, Siyu Chen, Yiping Chen, Ting Han

**分类**: cs.CV

**发布日期**: 2025-09-05

---

## 💡 一句话要点

**SGS-3D：通过可靠语义掩码分割与生长实现高保真3D实例分割**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D实例分割` `语义分割` `几何基元` `场景理解` `2D-to-3D lifting`

## 📋 核心要点

1. 现有的基于2D-to-3D lifting的实例分割方法，由于语义模糊和深度约束不足，导致分割精度不高。
2. SGS-3D提出了一种“分割-然后-生长”的框架，利用几何基元提纯分割掩码，并结合语义和几何信息进行实例生长。
3. SGS-3D在ScanNet200等数据集上显著提升了分割精度和鲁棒性，展现了良好的泛化能力。

## 📝 摘要（中文）

精确的3D实例分割对于3D视觉领域的高质量场景理解至关重要。然而，基于2D到3D lifting方法的3D实例分割难以产生精确的实例级分割，这是由于从模糊的语义引导和不足的深度约束中lifting过程引入的累积误差所致。为了应对这些挑战，我们提出了一种用于高保真3D实例分割的可靠语义掩码分割与生长方法（SGS-3D），这是一种新颖的“分割-然后-生长”框架，它首先使用几何基元来提纯和分割模糊的lifted掩码，然后在场景中将它们生长为完整的实例。与直接依赖原始lifted掩码并牺牲分割精度的现有方法不同，SGS-3D作为一种免训练的细化方法，共同融合了语义和几何信息，从而实现了两个级别表示之间的有效协作。具体来说，对于语义引导，我们引入了一种掩码过滤策略，该策略利用3D几何基元的共现来识别和删除模糊的掩码，从而确保与3D对象实例更可靠的语义一致性。对于几何细化，我们通过利用空间连续性和高级特征来构建细粒度的对象实例，尤其是在不同对象之间存在语义模糊的情况下。在ScanNet200、ScanNet++和KITTI-360上的实验结果表明，SGS-3D显着提高了分割精度和对来自预训练模型的不准确掩码的鲁棒性，从而在保持跨各种室内和室外环境的强大泛化能力的同时，产生高保真的对象实例。代码可在补充材料中找到。

## 🔬 方法详解

**问题定义**：现有基于2D-to-3D lifting的3D实例分割方法，在将2D信息提升到3D空间时，会累积误差，导致分割结果不精确，尤其是在语义信息模糊或深度信息不足的情况下。这些方法通常直接依赖于原始的lifted掩码，无法有效区分和处理错误或不完整的分割结果，从而牺牲了分割精度。

**核心思路**：SGS-3D的核心思路是首先对lifted的语义掩码进行提纯和分割，去除模糊和不准确的部分，然后利用几何信息将分割后的掩码生长为完整的实例。这种“分割-然后-生长”的策略，旨在通过几何约束来纠正语义信息的不足，并利用语义信息引导几何信息的应用，从而实现更精确的3D实例分割。

**技术框架**：SGS-3D框架主要包含两个阶段：语义掩码分割和实例生长。首先，利用几何基元（如平面、球体等）对lifted的语义掩码进行过滤，去除与几何信息不一致的模糊掩码。然后，利用空间连续性和高级特征，将分割后的掩码生长为完整的实例。该框架是一个免训练的后处理步骤，可以应用于各种基于2D-to-3D lifting的实例分割方法。

**关键创新**：SGS-3D的关键创新在于其“分割-然后-生长”的框架，以及将语义和几何信息有效融合的策略。与现有方法直接依赖原始lifted掩码不同，SGS-3D首先对掩码进行提纯，从而提高了分割的可靠性。此外，SGS-3D利用几何基元进行掩码过滤，并利用空间连续性和高级特征进行实例生长，从而实现了更精确的实例分割。

**关键设计**：掩码过滤策略利用3D几何基元的共现性来识别和移除模糊的掩码，确保语义一致性。实例生长过程则利用空间连续性和高层特征，尤其是在不同对象之间存在语义模糊的情况下。具体的参数设置和损失函数等细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

SGS-3D在ScanNet200、ScanNet++和KITTI-360等数据集上取得了显著的性能提升。实验结果表明，SGS-3D能够有效提高分割精度和鲁棒性，尤其是在处理不准确的lifted掩码时。具体性能数据和对比基线在论文中给出，但此处无法详细列出。

## 🎯 应用场景

SGS-3D技术可广泛应用于机器人导航、自动驾驶、增强现实等领域。精确的3D场景理解是这些应用的关键，而高保真的3D实例分割能够提供更准确的场景信息，从而提高系统的性能和可靠性。未来，该技术有望在智能家居、工业自动化等领域发挥重要作用。

## 📄 摘要（原文）

> Accurate 3D instance segmentation is crucial for high-quality scene understanding in the 3D vision domain. However, 3D instance segmentation based on 2D-to-3D lifting approaches struggle to produce precise instance-level segmentation, due to accumulated errors introduced during the lifting process from ambiguous semantic guidance and insufficient depth constraints. To tackle these challenges, we propose splitting and growing reliable semantic mask for high-fidelity 3D instance segmentation (SGS-3D), a novel "split-then-grow" framework that first purifies and splits ambiguous lifted masks using geometric primitives, and then grows them into complete instances within the scene. Unlike existing approaches that directly rely on raw lifted masks and sacrifice segmentation accuracy, SGS-3D serves as a training-free refinement method that jointly fuses semantic and geometric information, enabling effective cooperation between the two levels of representation. Specifically, for semantic guidance, we introduce a mask filtering strategy that leverages the co-occurrence of 3D geometry primitives to identify and remove ambiguous masks, thereby ensuring more reliable semantic consistency with the 3D object instances. For the geometric refinement, we construct fine-grained object instances by exploiting both spatial continuity and high-level features, particularly in the case of semantic ambiguity between distinct objects. Experimental results on ScanNet200, ScanNet++, and KITTI-360 demonstrate that SGS-3D substantially improves segmentation accuracy and robustness against inaccurate masks from pre-trained models, yielding high-fidelity object instances while maintaining strong generalization across diverse indoor and outdoor environments. Code is available in the supplementary materials.

