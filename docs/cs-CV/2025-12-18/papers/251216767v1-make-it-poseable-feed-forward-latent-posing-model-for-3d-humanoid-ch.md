---
layout: default
title: "Make-It-Poseable: Feed-forward Latent Posing Model for 3D Humanoid Character Animation"
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

**提出Make-It-Poseable，解决3D人形角色动画中姿态控制难题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `3D角色动画` `姿态控制` `潜在空间变换` `Transformer网络` `自适应补全`

## 📋 核心要点

1. 现有3D角色姿态控制方法在蒙皮权重预测、拓扑结构和姿态一致性方面存在不足，影响了其鲁棒性和泛化性。
2. Make-It-Poseable将姿态控制问题转化为潜在空间中的变换，通过操纵潜在表示来重建角色姿态，避免了直接变形网格。
3. 该方法通过潜在姿态Transformer、密集姿态表示、潜在空间监督和自适应补全模块，实现了高质量的姿态控制，并可扩展到3D编辑应用。

## 📝 摘要（中文）

本文提出了一种名为Make-It-Poseable的新型前馈框架，用于3D人形角色动画的姿态控制。现有方法如自动绑定和姿态条件生成，在蒙皮权重预测不准确、拓扑结构缺陷和姿态一致性差等方面存在挑战，限制了其鲁棒性和泛化能力。Make-It-Poseable将角色姿态控制重新定义为潜在空间转换问题。该方法不直接变形网格顶点，而是通过操纵角色的潜在表示来重建新的姿态。核心是一个潜在姿态Transformer，它根据骨骼运动来操纵形状token。密集姿态表示用于实现精确控制。为了确保高保真几何形状并适应拓扑变化，还引入了潜在空间监督策略和自适应补全模块。实验表明，该方法在姿态质量方面表现出色，并且可以自然地扩展到3D编辑应用，如部件替换和优化。

## 🔬 方法详解

**问题定义**：论文旨在解决3D人形角色动画中，现有姿态控制方法存在的不足。现有方法，如自动绑定和姿态条件生成，在蒙皮权重预测的准确性、拓扑结构的完整性以及姿态一致性方面表现不佳，导致生成的人物模型质量不高，难以满足实际应用需求。这些问题限制了模型的鲁棒性和泛化能力。

**核心思路**：论文的核心思路是将3D角色姿态控制问题转化为潜在空间中的变换问题。不同于传统方法直接对网格顶点进行变形，该方法通过学习一个潜在空间，并将角色表示为该空间中的一个点。然后，通过操纵这个潜在表示，可以重建出具有不同姿态的角色模型。这种方法避免了直接处理复杂的网格变形，从而提高了模型的鲁棒性和生成质量。

**技术框架**：Make-It-Poseable框架主要包含以下几个模块：1) 编码器：将3D角色网格编码到潜在空间中。2) 潜在姿态Transformer：根据输入的骨骼运动信息，对潜在空间中的角色表示进行变换，从而得到新的姿态。3) 解码器：将变换后的潜在表示解码回3D角色网格。4) 自适应补全模块：用于处理拓扑结构变化，确保生成高质量的网格模型。框架采用前馈结构，可以高效地生成各种姿态的角色模型。

**关键创新**：该方法最重要的技术创新在于将姿态控制问题转化为潜在空间变换。与现有方法直接操作网格顶点不同，该方法通过学习一个潜在空间，并将角色表示为该空间中的一个点。然后，通过操纵这个潜在表示，可以重建出具有不同姿态的角色模型。这种方法避免了直接处理复杂的网格变形，从而提高了模型的鲁棒性和生成质量。此外，自适应补全模块也是一个重要的创新，它可以处理拓扑结构变化，确保生成高质量的网格模型。

**关键设计**：潜在姿态Transformer是基于Transformer架构设计的，用于根据输入的骨骼运动信息，对潜在空间中的角色表示进行变换。论文使用了密集姿态表示，以实现对姿态的精确控制。为了确保高保真几何形状，论文还引入了潜在空间监督策略，即在潜在空间中对生成的角色表示进行约束，使其与真实的角色表示尽可能接近。此外，自适应补全模块采用了一种基于学习的方法，可以根据输入的角色网格和目标姿态，自动生成缺失的网格部分。

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

实验结果表明，Make-It-Poseable在姿态质量方面优于现有方法。该方法能够生成具有高保真几何形状和准确姿态的3D角色模型。与基线方法相比，Make-It-Poseable在姿态一致性方面取得了显著提升。此外，该方法还能够自然地扩展到3D编辑应用，例如部件替换和优化，展示了其强大的泛化能力。

## 🎯 应用场景

该研究成果可广泛应用于3D游戏开发、动画制作、虚拟现实和增强现实等领域。通过Make-It-Poseable，可以快速生成具有各种姿态的3D角色模型，从而提高内容创作效率。此外，该方法还可以用于3D角色编辑，例如部件替换和优化，为用户提供更加灵活和便捷的创作工具。未来，该技术有望应用于个性化虚拟形象定制、人机交互等领域。

## 📄 摘要（原文）

> Posing 3D characters is a fundamental task in computer graphics and vision. However, existing methods like auto-rigging and pose-conditioned generation often struggle with challenges such as inaccurate skinning weight prediction, topological imperfections, and poor pose conformance, limiting their robustness and generalizability. To overcome these limitations, we introduce Make-It-Poseable, a novel feed-forward framework that reformulates character posing as a latent-space transformation problem. Instead of deforming mesh vertices as in traditional pipelines, our method reconstructs the character in new poses by directly manipulating its latent representation. At the core of our method is a latent posing transformer that manipulates shape tokens based on skeletal motion. This process is facilitated by a dense pose representation for precise control. To ensure high-fidelity geometry and accommodate topological changes, we also introduce a latent-space supervision strategy and an adaptive completion module. Our method demonstrates superior performance in posing quality. It also naturally extends to 3D editing applications like part replacement and refinement.

