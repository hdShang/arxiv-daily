---
layout: default
title: GaussianMorphing: Mesh-Guided 3D Gaussians for Semantic-Aware Object Morphing
---

# GaussianMorphing: Mesh-Guided 3D Gaussians for Semantic-Aware Object Morphing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02034" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02034v1</a>
  <a href="https://arxiv.org/pdf/2510.02034.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02034v1" onclick="toggleFavorite(this, '2510.02034v1', 'GaussianMorphing: Mesh-Guided 3D Gaussians for Semantic-Aware Object Morphing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mengtian Li, Yunshu Bai, Yimin Chu, Yijun Shen, Zhongmei Li, Weifeng Ge, Zhifeng Xie, Chaofeng Chen

**分类**: cs.CV

**发布日期**: 2025-10-02

**备注**: Project page: https://baiyunshu.github.io/GAUSSIANMORPHING.github.io/

**🔗 代码/项目**: [PROJECT_PAGE](https://baiyunshu.github.io/GAUSSIANMORPHING.github.io/)

---

## 💡 一句话要点

**GaussianMorphing：提出网格引导的3D高斯方法，实现语义感知的物体形变。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `3D形变` `高斯溅射` `网格引导` `语义对应` `纹理保真`

## 📋 核心要点

1. 现有方法在3D形变任务中依赖点云或预定义映射，难以处理复杂纹理和拓扑结构。
2. GaussianMorphing利用网格引导的3D高斯，实现几何一致性和纹理保真度，并建立无监督语义对应。
3. 在TexMorph基准测试中，GaussianMorphing显著优于现有方法，颜色一致性误差降低22.2%，EI降低26.2%。

## 📝 摘要（中文）

GaussianMorphing 是一种新颖的框架，用于从多视角图像中实现语义感知的 3D 形状和纹理形变。先前的方法通常依赖于点云，或者需要为无纹理数据预定义的同胚映射。我们的方法通过利用网格引导的 3D 高斯溅射 (3DGS) 进行高保真几何和外观建模，克服了这些限制。该框架的核心是一种统一的变形策略，它将 3D 高斯锚定到重建的网格块，确保几何一致的变换，同时通过拓扑感知的约束保持纹理保真度。同时，我们的框架通过使用网格拓扑作为几何先验来建立无监督的语义对应关系，并通过物理上合理的点轨迹来维持结构完整性。这种集成方法在整个形变过程中保持了局部细节和全局语义连贯性，而无需标记数据。在我们提出的 TexMorph 基准测试中，GaussianMorphing 显著优于先前的 2D/3D 方法，将颜色一致性误差 ($ΔE$) 降低了 22.2%，EI 降低了 26.2%。

## 🔬 方法详解

**问题定义**：现有的3D形变方法，如基于点云的方法，难以处理具有复杂拓扑结构和纹理的对象。此外，一些方法需要预定义的同胚映射，限制了其适用性。这些方法在保持几何一致性、纹理保真度和语义连贯性方面存在挑战。

**核心思路**：GaussianMorphing的核心思路是利用网格引导的3D高斯表示，将3D高斯锚定到重建的网格块上。通过这种方式，可以实现几何一致的形变，同时利用拓扑感知的约束保持纹理的保真度。此外，利用网格拓扑作为几何先验，建立无监督的语义对应关系，从而在形变过程中保持结构的完整性。

**技术框架**：GaussianMorphing的整体框架包含以下几个主要阶段：1) 从多视角图像重建3D网格模型。2) 将3D高斯锚定到重建的网格块上。3) 利用统一的变形策略，对网格和3D高斯进行形变。4) 通过拓扑感知的约束和物理上合理的点轨迹，保持纹理保真度和结构完整性。5) 利用无监督的语义对应关系，确保形变过程中的语义连贯性。

**关键创新**：GaussianMorphing的关键创新在于：1) 提出了一种网格引导的3D高斯表示，将3D高斯与网格结构相结合，从而实现几何一致和纹理保真的形变。2) 提出了一种统一的变形策略，可以同时对网格和3D高斯进行形变。3) 利用网格拓扑作为几何先验，建立了无监督的语义对应关系，从而在形变过程中保持结构的完整性和语义连贯性。与现有方法相比，GaussianMorphing不需要预定义的同胚映射，并且能够更好地处理具有复杂拓扑结构和纹理的对象。

**关键设计**：在GaussianMorphing中，一些关键的设计包括：1) 使用基于可微渲染的优化方法，对3D高斯进行优化，以获得高质量的几何和外观模型。2) 设计了一种拓扑感知的约束，用于保持纹理的保真度。3) 使用物理上合理的点轨迹，确保形变过程中的结构完整性。4) 利用基于图神经网络的方法，建立无监督的语义对应关系。

## 📊 实验亮点

GaussianMorphing在TexMorph基准测试中取得了显著的性能提升。与现有的2D和3D形变方法相比，GaussianMorphing将颜色一致性误差($ΔE$)降低了22.2%，EI降低了26.2%。这些结果表明，GaussianMorphing能够更好地保持几何一致性、纹理保真度和语义连贯性。此外，GaussianMorphing还能够处理具有复杂拓扑结构和纹理的对象，而现有方法通常难以处理这些对象。

## 🎯 应用场景

GaussianMorphing在3D内容创作、动画制作、虚拟现实和增强现实等领域具有广泛的应用前景。它可以用于创建逼真的物体形变动画，例如人物表情变化、动物形态转换等。此外，它还可以用于3D模型的编辑和修复，例如修复损坏的网格结构、填充缺失的纹理信息等。该研究的实际价值在于提供了一种高效、高质量的3D形变方法，可以显著提高3D内容创作的效率和质量。未来，GaussianMorphing可以进一步扩展到处理更复杂的场景和对象，例如具有复杂拓扑结构和动态纹理的对象。

## 📄 摘要（原文）

> We introduce GaussianMorphing, a novel framework for semantic-aware 3D shape and texture morphing from multi-view images. Previous approaches usually rely on point clouds or require pre-defined homeomorphic mappings for untextured data. Our method overcomes these limitations by leveraging mesh-guided 3D Gaussian Splatting (3DGS) for high-fidelity geometry and appearance modeling. The core of our framework is a unified deformation strategy that anchors 3DGaussians to reconstructed mesh patches, ensuring geometrically consistent transformations while preserving texture fidelity through topology-aware constraints. In parallel, our framework establishes unsupervised semantic correspondence by using the mesh topology as a geometric prior and maintains structural integrity via physically plausible point trajectories. This integrated approach preserves both local detail and global semantic coherence throughout the morphing process with out requiring labeled data. On our proposed TexMorph benchmark, GaussianMorphing substantially outperforms prior 2D/3D methods, reducing color consistency error ($ΔE$) by 22.2% and EI by 26.2%. Project page: https://baiyunshu.github.io/GAUSSIANMORPHING.github.io/

