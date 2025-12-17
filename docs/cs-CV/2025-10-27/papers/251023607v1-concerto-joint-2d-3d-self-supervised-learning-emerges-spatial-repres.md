---
layout: default
title: Concerto: Joint 2D-3D Self-Supervised Learning Emerges Spatial Representations
---

# Concerto: Joint 2D-3D Self-Supervised Learning Emerges Spatial Representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23607" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23607v1</a>
  <a href="https://arxiv.org/pdf/2510.23607.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23607v1" onclick="toggleFavorite(this, '2510.23607v1', 'Concerto: Joint 2D-3D Self-Supervised Learning Emerges Spatial Representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yujia Zhang, Xiaoyang Wu, Yixing Lao, Chengyao Wang, Zhuotao Tian, Naiyan Wang, Hengshuang Zhao

**分类**: cs.CV

**发布日期**: 2025-10-27

**备注**: NeurIPS 2025, produced by Pointcept, project page: https://pointcept.github.io/Concerto

**期刊**: Neural Information Processing Systems 2025

---

## 💡 一句话要点

**Concerto：融合2D-3D自监督学习，涌现空间表征**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `自监督学习` `跨模态学习` `3D场景理解` `空间表征` `点云处理`

## 📋 核心要点

1. 现有2D和3D自监督学习方法在空间表征学习方面存在局限性，未能充分利用跨模态信息。
2. Concerto通过模拟人类多感官协同学习机制，结合3D自蒸馏和2D-3D跨模态联合嵌入，学习更连贯的空间特征。
3. 实验表明，Concerto在多个场景理解任务中超越了SOTA模型，并在ScanNet上取得了80.7%的mIoU。

## 📝 摘要（中文）

本文提出Concerto，一个模拟人类空间认知概念学习的极简框架，它结合了3D模内自蒸馏和2D-3D跨模态联合嵌入。Concerto学习到更连贯和信息丰富的空间特征，这通过零样本可视化得到验证。在3D场景感知的线性探测任务中，Concerto优于独立的SOTA 2D和3D自监督模型，分别提升了14.2%和4.8%，也优于它们的特征拼接。通过完全微调，Concerto在多个场景理解基准测试中取得了新的SOTA结果（例如，在ScanNet上达到80.7%的mIoU）。此外，本文还提出了Concerto的一个变体，专门用于视频提升点云的空间理解，以及一个将Concerto表征线性投影到CLIP语言空间的转换器，从而实现开放世界的感知。这些结果表明，Concerto涌现的空间表征具有卓越的细粒度几何和语义一致性。

## 🔬 方法详解

**问题定义**：现有方法在学习空间表征时，通常独立地处理2D图像和3D点云数据，忽略了它们之间的互补信息。这导致学习到的表征缺乏几何和语义一致性，限制了模型在复杂场景理解任务中的性能。此外，如何有效地利用无标签数据进行自监督学习仍然是一个挑战。

**核心思路**：Concerto的核心思路是模拟人类通过多感官协同学习抽象概念的过程。通过将2D图像和3D点云数据进行联合嵌入，并利用3D模内自蒸馏，模型可以学习到更丰富、更连贯的空间表征。这种跨模态学习方式能够弥补单一模态的不足，提高表征的泛化能力。

**技术框架**：Concerto包含两个主要模块：3D自蒸馏模块和2D-3D跨模态联合嵌入模块。3D自蒸馏模块利用3D数据本身的信息进行学习，提高3D表征的质量。2D-3D跨模态联合嵌入模块将2D图像和3D点云数据映射到同一个特征空间，使得模型能够学习到它们之间的对应关系。整体流程是先进行3D自蒸馏，然后进行2D-3D联合嵌入，最后通过线性探测或微调进行评估。

**关键创新**：Concerto的关键创新在于其跨模态联合学习框架，它能够有效地融合2D图像和3D点云数据的信息，学习到更具几何和语义一致性的空间表征。此外，3D自蒸馏模块进一步提高了3D表征的质量，使得模型能够更好地理解3D场景。与现有方法相比，Concerto能够更好地利用无标签数据，提高模型的泛化能力。

**关键设计**：在3D自蒸馏模块中，使用了教师-学生网络结构，教师网络生成的目标用于指导学生网络的学习。在2D-3D跨模态联合嵌入模块中，使用了对比学习损失函数，使得相似的2D和3D特征在特征空间中更接近，不相似的特征更远离。具体的网络结构和损失函数选择需要根据具体的任务和数据集进行调整。对于视频提升点云的空间理解，Concerto采用时序信息建模，增强了对动态场景的理解能力。线性投影到CLIP空间，利用CLIP强大的语义理解能力，实现开放世界感知。

## 📊 实验亮点

Concerto在3D场景感知的线性探测任务中，优于SOTA 2D和3D自监督模型分别14.2%和4.8%。在ScanNet数据集上，通过完全微调，Concerto取得了80.7%的mIoU，刷新了SOTA记录。这些结果表明，Concerto能够学习到更具几何和语义一致性的空间表征，并在多个场景理解任务中取得了显著的性能提升。

## 🎯 应用场景

Concerto在机器人导航、自动驾驶、增强现实等领域具有广泛的应用前景。它可以帮助机器人更好地理解周围环境，从而实现更安全、更高效的导航。在自动驾驶领域，Concerto可以提高车辆对复杂场景的感知能力，从而提高驾驶安全性。在增强现实领域，Concerto可以实现更逼真的虚拟现实融合，提升用户体验。未来，Concerto有望成为构建智能空间的关键技术。

## 📄 摘要（原文）

> Humans learn abstract concepts through multisensory synergy, and once formed, such representations can often be recalled from a single modality. Inspired by this principle, we introduce Concerto, a minimalist simulation of human concept learning for spatial cognition, combining 3D intra-modal self-distillation with 2D-3D cross-modal joint embedding. Despite its simplicity, Concerto learns more coherent and informative spatial features, as demonstrated by zero-shot visualizations. It outperforms both standalone SOTA 2D and 3D self-supervised models by 14.2% and 4.8%, respectively, as well as their feature concatenation, in linear probing for 3D scene perception. With full fine-tuning, Concerto sets new SOTA results across multiple scene understanding benchmarks (e.g., 80.7% mIoU on ScanNet). We further present a variant of Concerto tailored for video-lifted point cloud spatial understanding, and a translator that linearly projects Concerto representations into CLIP's language space, enabling open-world perception. These results highlight that Concerto emerges spatial representations with superior fine-grained geometric and semantic consistency.

