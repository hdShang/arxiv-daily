---
layout: default
title: Progressive Gaussian Transformer with Anisotropy-aware Sampling for Open Vocabulary Occupancy Prediction
---

# Progressive Gaussian Transformer with Anisotropy-aware Sampling for Open Vocabulary Occupancy Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04759" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04759v2</a>
  <a href="https://arxiv.org/pdf/2510.04759.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04759v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.04759v2', 'Progressive Gaussian Transformer with Anisotropy-aware Sampling for Open Vocabulary Occupancy Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chi Yan, Dan Xu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-06 (更新: 2025-10-08)

**备注**: Project Page: https://yanchi-3dv.github.io/PG-Occ

**🔗 代码/项目**: [PROJECT_PAGE](https://yanchi-3dv.github.io/PG-Occ)

---

## 💡 一句话要点

**提出PG-Occ框架，通过渐进式高斯Transformer实现开放词汇三维 occupancy 预测。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `三维 occupancy 预测` `开放词汇` `高斯表示` `Transformer` `自动驾驶`

## 📋 核心要点

1. 现有三维 occupancy 预测方法在开放词汇场景中存在稀疏表示难以捕捉小物体，密集表示计算开销大的问题。
2. PG-Occ框架采用渐进式在线密集化策略，逐步增强高斯表示，以捕捉精细场景细节，实现更精确的场景理解。
3. 引入各向异性感知采样策略，自适应地为不同尺度高斯分配感受野，实现更有效的特征聚合，mIoU相对提升14.3%。

## 📝 摘要（中文）

近年来，三维 occupancy 预测任务取得了显著进展，在基于视觉的自动驾驶系统中发挥着关键作用。传统方法局限于固定的语义类别，而最近的方法转向预测文本对齐的特征，以支持真实场景中的开放词汇文本查询。然而，文本对齐的场景建模存在一个权衡：稀疏高斯表示难以捕捉场景中的小物体，而密集表示会产生巨大的计算开销。为了解决这些限制，我们提出了PG-Occ，一种创新的渐进式高斯Transformer框架，用于实现开放词汇三维 occupancy 预测。我们的框架采用渐进式在线密集化，这是一种前馈策略，逐步增强三维高斯表示，以捕捉精细的场景细节。通过迭代增强表示，该框架实现了越来越精确和详细的场景理解。另一个关键贡献是引入了具有时空融合的各向异性感知采样策略，该策略自适应地为不同尺度和阶段的高斯分配感受野，从而实现更有效的特征聚合和更丰富的场景信息捕获。通过广泛的评估，我们证明了PG-Occ实现了最先进的性能，相对于之前表现最佳的方法，mIoU相对提高了14.3%。代码和预训练模型将在项目页面上发布。

## 🔬 方法详解

**问题定义**：论文旨在解决开放词汇三维 occupancy 预测问题。现有方法在处理开放词汇场景时，面临着稀疏高斯表示难以捕捉小物体，而密集表示计算开销过大的难题。这限制了三维场景理解的精度和效率。

**核心思路**：论文的核心思路是通过渐进式的高斯表示来平衡精度和效率。从稀疏的高斯表示开始，逐步进行在线密集化，从而在计算资源可控的前提下，逐步提升场景表示的精细程度。同时，通过各向异性感知采样，自适应地调整感受野，以更好地聚合特征。

**技术框架**：PG-Occ框架主要包含以下几个阶段：1) 初始稀疏高斯表示：使用少量高斯分布来初步表示场景。2) 渐进式在线密集化：通过前馈策略，逐步增加高斯分布的数量，从而增强场景表示的细节。3) 各向异性感知采样：根据高斯分布的尺度和阶段，自适应地分配感受野，进行时空特征融合。4) Occupancy 预测：基于增强的高斯表示，预测三维空间的 occupancy 状态。

**关键创新**：论文的关键创新在于以下两点：1) 渐进式在线密集化：这种策略能够在计算资源有限的情况下，逐步提升场景表示的精度。2) 各向异性感知采样：这种采样策略能够根据高斯分布的特性，自适应地调整感受野，从而更有效地聚合特征。与现有方法相比，PG-Occ能够在精度和效率之间取得更好的平衡。

**关键设计**：在渐进式在线密集化过程中，论文采用了一种前馈策略，避免了复杂的优化过程。在各向异性感知采样中，论文设计了一种基于高斯分布尺度和阶段的自适应感受野分配方法。具体的损失函数和网络结构细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

PG-Occ在开放词汇三维 occupancy 预测任务上取得了state-of-the-art的性能，相对于之前表现最佳的方法，mIoU相对提高了14.3%。这表明PG-Occ在精度和效率方面都具有显著优势，能够更好地处理复杂的真实场景。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、虚拟现实等领域。通过实现开放词汇的三维场景理解，可以使自动驾驶系统更好地识别和理解复杂的交通环境，提高驾驶安全性。在机器人导航中，可以帮助机器人更好地感知周围环境，实现更智能的路径规划。在虚拟现实中，可以创建更逼真的三维场景，提升用户体验。

## 📄 摘要（原文）

> The 3D occupancy prediction task has witnessed remarkable progress in recent years, playing a crucial role in vision-based autonomous driving systems. While traditional methods are limited to fixed semantic categories, recent approaches have moved towards predicting text-aligned features to enable open-vocabulary text queries in real-world scenes. However, there exists a trade-off in text-aligned scene modeling: sparse Gaussian representation struggles to capture small objects in the scene, while dense representation incurs significant computational overhead. To address these limitations, we present PG-Occ, an innovative Progressive Gaussian Transformer Framework that enables open-vocabulary 3D occupancy prediction. Our framework employs progressive online densification, a feed-forward strategy that gradually enhances the 3D Gaussian representation to capture fine-grained scene details. By iteratively enhancing the representation, the framework achieves increasingly precise and detailed scene understanding. Another key contribution is the introduction of an anisotropy-aware sampling strategy with spatio-temporal fusion, which adaptively assigns receptive fields to Gaussians at different scales and stages, enabling more effective feature aggregation and richer scene information capture. Through extensive evaluations, we demonstrate that PG-Occ achieves state-of-the-art performance with a relative 14.3% mIoU improvement over the previous best performing method. Code and pretrained models will be released upon publication on our project page: https://yanchi-3dv.github.io/PG-Occ

