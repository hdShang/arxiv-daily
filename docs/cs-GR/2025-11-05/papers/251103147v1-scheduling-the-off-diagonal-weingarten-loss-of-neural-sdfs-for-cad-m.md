---
layout: default
title: Scheduling the Off-Diagonal Weingarten Loss of Neural SDFs for CAD Models
---

# Scheduling the Off-Diagonal Weingarten Loss of Neural SDFs for CAD Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.03147" class="toolbar-btn" target="_blank">📄 arXiv: 2511.03147v1</a>
  <a href="https://arxiv.org/pdf/2511.03147.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03147v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.03147v1', 'Scheduling the Off-Diagonal Weingarten Loss of Neural SDFs for CAD Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haotian Yin, Przemyslaw Musialski

**分类**: cs.GR, cs.CV, cs.LG

**发布日期**: 2025-11-05

**备注**: Lecture Notes in Computer Science (LNCS), 20th International Symposium on Visual Computing 2025, 12 pages, 4 figures, preprint

---

## 💡 一句话要点

**针对CAD模型神经SDF，提出ODW损失调度策略，提升重建精度。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `神经SDF` `CAD模型` `曲率正则化` `ODW损失` `损失调度`

## 📋 核心要点

1. 神经SDF重建CAD模型时，固定权重的曲率正则化在优化稳定性和细节恢复间存在矛盾。
2. 提出ODW损失的调度策略，通过时变权重平衡优化稳定性和细节恢复，提升重建效果。
3. 实验表明，时变调度策略优于固定权重，Chamfer距离指标最高提升35%。

## 📝 摘要（中文）

神经符号距离函数(SDFs)已成为从点云进行几何重建的强大表示方法，但通常需要基于梯度和曲率的正则化来抑制虚假扭曲并保持结构保真度。FlatCAD引入了Off-Diagonal Weingarten (ODW)损失，作为CAD表面的有效二阶先验，以大约一半的计算成本逼近完整的Hessian正则化。然而，FlatCAD在整个训练过程中应用固定的ODW权重，这是次优的：强正则化稳定了早期优化，但抑制了后期阶段的细节恢复。我们提出了ODW损失的调度策略，该策略分配一个高的初始权重来稳定优化，并逐步衰减它以允许精细的细化。我们研究了常数、线性、五次和步进插值调度，以及增加的预热变体。在ABC CAD数据集上的实验表明，时变调度始终优于固定权重。我们的方法在Chamfer距离上实现了高达35%的改进，证明了调度是曲率正则化的一个简单而有效的扩展，用于鲁棒的CAD重建。

## 🔬 方法详解

**问题定义**：神经SDF用于CAD模型重建时，需要曲率正则化来保证形状的结构保真度。FlatCAD使用Off-Diagonal Weingarten (ODW)损失作为二阶先验，但其固定权重在训练初期稳定优化，后期抑制细节恢复，导致重建精度受限。

**核心思路**：核心在于设计一种ODW损失的调度策略，即在训练的不同阶段动态调整ODW损失的权重。初期使用较大的权重以稳定优化过程，后期逐渐减小权重，允许网络恢复更多的细节信息。通过这种方式，平衡了优化稳定性和细节恢复之间的矛盾。

**技术框架**：该方法主要是在FlatCAD的基础上，修改了ODW损失的使用方式。整体流程与FlatCAD类似，包括：1. 使用神经SDF表示CAD模型；2. 从点云数据中学习SDF；3. 使用ODW损失进行曲率正则化。关键区别在于，ODW损失的权重不再是固定的，而是根据预设的调度策略随时间变化。

**关键创新**：关键创新在于提出了ODW损失的调度策略。与FlatCAD的固定权重相比，该策略能够根据训练阶段动态调整ODW损失的权重，从而更好地平衡优化稳定性和细节恢复。这种时变权重的思想可以应用于其他类似的正则化方法中。

**关键设计**：论文研究了多种调度策略，包括常数、线性、五次和步进插值调度，以及增加的预热变体。这些策略定义了ODW损失权重随时间变化的函数。具体实现时，只需要在训练循环中，根据当前的训练步数或epoch，计算出对应的ODW损失权重，并将其应用于损失函数中即可。

## 📊 实验亮点

实验结果表明，提出的ODW损失调度策略在ABC CAD数据集上显著优于FlatCAD的固定权重方法。在Chamfer距离指标上，最佳调度策略实现了高达35%的性能提升，证明了时变权重对于曲率正则化的有效性。

## 🎯 应用场景

该研究成果可应用于CAD模型的自动重建、逆向工程、三维模型编辑等领域。通过提高CAD模型重建的精度和鲁棒性，可以减少人工干预，提高设计效率，并为后续的分析、仿真和制造提供更准确的模型。

## 📄 摘要（原文）

> Neural signed distance functions (SDFs) have become a powerful representation for geometric reconstruction from point clouds, yet they often require both gradient- and curvature-based regularization to suppress spurious warp and preserve structural fidelity. FlatCAD introduced the Off-Diagonal Weingarten (ODW) loss as an efficient second-order prior for CAD surfaces, approximating full-Hessian regularization at roughly half the computational cost. However, FlatCAD applies a fixed ODW weight throughout training, which is suboptimal: strong regularization stabilizes early optimization but suppresses detail recovery in later stages. We present scheduling strategies for the ODW loss that assign a high initial weight to stabilize optimization and progressively decay it to permit fine-scale refinement. We investigate constant, linear, quintic, and step interpolation schedules, as well as an increasing warm-up variant. Experiments on the ABC CAD dataset demonstrate that time-varying schedules consistently outperform fixed weights. Our method achieves up to a 35% improvement in Chamfer Distance over the FlatCAD baseline, establishing scheduling as a simple yet effective extension of curvature regularization for robust CAD reconstruction.

