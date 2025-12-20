---
layout: default
title: Make-It-Poseable: Feed-forward Latent Posing Model for 3D Humanoid Character Animation
---

# Make-It-Poseable: Feed-forward Latent Posing Model for 3D Humanoid Character Animation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16767" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16767v1</a>
  <a href="https://arxiv.org/pdf/2512.16767.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16767v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16767v1', 'Make-It-Poseable: Feed-forward Latent Posing Model for 3D Humanoid Character Animation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyang Guo, Ori Zhang, Jax Xiang, Alan Zhao, Wengang Zhou, Houqiang Li

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project page: https://jasongzy.github.io/Make-It-Poseable/

---

## 💡 一句话要点

**提出Make-It-Poseable，用于解决3D人形角色动画中姿态控制难题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `3D角色动画` `姿态控制` `潜在空间变换` `Transformer` `人形建模`

## 📋 核心要点

1. 现有3D角色姿态控制方法在蒙皮权重预测、拓扑结构和姿态一致性方面存在不足，影响了鲁棒性和泛化性。
2. Make-It-Poseable将姿态控制视为潜在空间变换问题，通过操纵潜在表示而非直接变形顶点来重建角色。
3. 该方法通过潜在姿态Transformer、密集姿态表示、潜在空间监督和自适应补全模块，实现了高质量的姿态控制。

## 📝 摘要（中文）

本文提出了一种名为Make-It-Poseable的新型前馈框架，用于3D人形角色动画的姿态控制。现有方法如自动绑定和姿态条件生成，在蒙皮权重预测不准确、拓扑结构缺陷和姿态一致性差等方面存在挑战，限制了它们的鲁棒性和泛化能力。为了克服这些限制，Make-It-Poseable将角色姿态控制重新定义为一个潜在空间变换问题。该方法不直接变形网格顶点，而是通过操纵角色的潜在表示来重建新的姿态。核心是一个潜在姿态Transformer，它基于骨骼运动来操纵形状token。密集姿态表示用于实现精确控制。为了确保高保真几何形状并适应拓扑变化，还引入了潜在空间监督策略和自适应补全模块。该方法在姿态质量方面表现出卓越的性能，并且自然地扩展到3D编辑应用，如部件替换和优化。

## 🔬 方法详解

**问题定义**：论文旨在解决3D人形角色动画中姿态控制的问题。现有方法，如自动绑定和姿态条件生成，在蒙皮权重预测、拓扑结构以及姿态一致性方面存在不足，导致生成结果不准确，鲁棒性和泛化能力较差。这些问题限制了3D角色动画在各种应用中的使用。

**核心思路**：论文的核心思路是将角色姿态控制问题转化为潜在空间中的变换问题。不再直接操作3D模型的顶点，而是学习一个潜在空间，并在该空间中通过变换来改变角色的姿态。这种方法可以更好地处理拓扑变化，并提高姿态控制的精度和鲁棒性。通过在潜在空间进行操作，可以避免传统方法中复杂的蒙皮和变形计算。

**技术框架**：Make-It-Poseable框架主要包含以下几个模块：1) 编码器：将3D角色模型编码到潜在空间中。2) 潜在姿态Transformer：根据输入的骨骼运动信息，在潜在空间中对形状token进行变换，从而改变角色的姿态。3) 解码器：将变换后的潜在表示解码回3D模型。4) 自适应补全模块：用于处理拓扑变化，并补全缺失的几何细节。整个流程是前馈的，可以高效地生成新的姿态。

**关键创新**：该方法最重要的创新点在于将姿态控制问题转化为潜在空间变换问题。与直接操作3D模型顶点的方法不同，该方法通过操纵潜在表示来重建角色，从而更好地处理拓扑变化，并提高姿态控制的精度和鲁棒性。此外，潜在姿态Transformer的设计也使得可以有效地利用骨骼运动信息来控制角色的姿态。

**关键设计**：论文中使用了密集姿态表示来精确控制角色的姿态。潜在姿态Transformer采用Transformer架构，用于学习骨骼运动与潜在空间表示之间的映射关系。为了确保高保真几何形状，引入了潜在空间监督策略，通过在潜在空间中进行监督，可以更好地约束模型的学习。自适应补全模块的设计也考虑了拓扑变化，可以有效地补全缺失的几何细节。损失函数的设计也至关重要，需要综合考虑姿态一致性、几何形状和拓扑结构等因素。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16767v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16767v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16767v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文提出的Make-It-Poseable方法在姿态质量方面表现出卓越的性能。实验结果表明，该方法能够生成高质量的3D角色姿态，并且能够有效地处理拓扑变化。与现有方法相比，该方法在姿态一致性和几何细节方面都有显著提升。此外，该方法还能够自然地扩展到3D编辑应用，例如部件替换和优化。

## 🎯 应用场景

该研究成果可广泛应用于3D游戏开发、虚拟现实、动画制作等领域。通过Make-It-Poseable，可以更高效、更精确地控制3D角色的姿态，从而提升用户体验和创作效率。此外，该方法还可以应用于3D角色编辑，例如部件替换和优化，为3D内容创作提供更多可能性。未来，该技术有望进一步推动虚拟角色的智能化和自动化。

## 📄 摘要（原文）

> Posing 3D characters is a fundamental task in computer graphics and vision. However, existing methods like auto-rigging and pose-conditioned generation often struggle with challenges such as inaccurate skinning weight prediction, topological imperfections, and poor pose conformance, limiting their robustness and generalizability. To overcome these limitations, we introduce Make-It-Poseable, a novel feed-forward framework that reformulates character posing as a latent-space transformation problem. Instead of deforming mesh vertices as in traditional pipelines, our method reconstructs the character in new poses by directly manipulating its latent representation. At the core of our method is a latent posing transformer that manipulates shape tokens based on skeletal motion. This process is facilitated by a dense pose representation for precise control. To ensure high-fidelity geometry and accommodate topological changes, we also introduce a latent-space supervision strategy and an adaptive completion module. Our method demonstrates superior performance in posing quality. It also naturally extends to 3D editing applications like part replacement and refinement.

