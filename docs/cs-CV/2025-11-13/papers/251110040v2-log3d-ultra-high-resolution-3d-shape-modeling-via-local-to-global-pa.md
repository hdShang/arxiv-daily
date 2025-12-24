---
layout: default
title: "LoG3D: Ultra-High-Resolution 3D Shape Modeling via Local-to-Global Partitioning"
---

# LoG3D: Ultra-High-Resolution 3D Shape Modeling via Local-to-Global Partitioning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10040" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10040v2</a>
  <a href="https://arxiv.org/pdf/2511.10040.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10040v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.10040v2', 'LoG3D: Ultra-High-Resolution 3D Shape Modeling via Local-to-Global Partitioning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinran Yang, Shuichang Lai, Jiangjing Lyu, Hongjie Li, Bowen Pan, Yuanqi Li, Jie Guo, Zhengkang Zhou, Yanwen Guo

**分类**: cs.CV

**发布日期**: 2025-11-13 (更新: 2025-11-18)

**备注**: 11 pages, 6 figures

---

## 💡 一句话要点

**LoG3D：通过局部到全局分割实现超高分辨率3D形状建模**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D建模` `变分自动编码器` `无符号距离场` `局部到全局` `超高分辨率`

## 📋 核心要点

1. 现有3D建模方法在处理复杂拓扑结构和保持几何细节方面存在挑战，SDF方法预处理代价高，点云方法易产生伪影。
2. LoG3D提出一种基于无符号距离场（UDF）的VAE框架，通过局部到全局的架构处理UDF，实现高分辨率建模。
3. 实验结果表明，LoG3D在重建精度和生成质量方面均达到SOTA，并能生成更平滑、几何灵活性更高的表面。

## 📝 摘要（中文）

生成高保真3D内容仍然是一个根本性的挑战，因为需要表示任意拓扑结构（例如开放表面和复杂的内部结构），同时保留几何细节。基于有符号距离场（SDF）的现有方法受到代价高昂的watertight预处理的阻碍，并且难以处理非流形几何体，而点云表示通常会受到采样伪影和表面不连续性的影响。为了克服这些限制，我们提出了一种新颖的3D变分自动编码器（VAE）框架，该框架建立在无符号距离场（UDF）之上——这是一种更鲁棒且计算效率更高的表示，可以自然地处理复杂和不完整的形状。我们的核心创新是一种局部到全局（LoG）架构，该架构通过将UDF划分为均匀的子体积（称为UBlock）来处理UDF。该架构将3D卷积用于捕获局部细节，并将稀疏Transformer用于增强全局一致性。Pad-Average策略进一步确保了重建期间子体积边界处的平滑过渡。这种模块化设计能够无缝扩展到高达2048^3的超高分辨率——这是3D VAE以前无法达到的范围。实验表明，在重建精度和生成质量方面均达到了最先进的性能，从而产生了卓越的表面平滑度和几何灵活性。

## 🔬 方法详解

**问题定义**：论文旨在解决现有3D建模方法在高分辨率和复杂几何形状建模方面的局限性。具体来说，基于SDF的方法需要耗时的watertight预处理，并且难以处理非流形几何体，而基于点云的方法容易出现采样伪影和表面不连续性。这些问题限制了3D模型的分辨率和质量。

**核心思路**：论文的核心思路是使用无符号距离场（UDF）作为3D形状的表示，并设计一种局部到全局（LoG）的架构来处理UDF。UDF比SDF更鲁棒，且计算效率更高，能够自然地处理复杂和不完整的形状。LoG架构通过将UDF划分为均匀的子体积（UBlock），并结合3D卷积和稀疏Transformer来捕获局部细节和全局一致性。

**技术框架**：LoG3D框架主要包含以下几个模块：1) UDF表示：使用UDF表示3D形状。2) UBlock划分：将UDF划分为均匀的子体积UBlock。3) 局部特征提取：使用3D卷积从每个UBlock中提取局部特征。4) 全局关系建模：使用稀疏Transformer建模UBlock之间的全局关系。5) 重建：将局部特征和全局关系结合起来，重建3D形状。Pad-Average策略用于确保子体积边界处的平滑过渡。

**关键创新**：LoG3D的关键创新在于其局部到全局的架构，该架构能够有效地处理高分辨率的UDF，并捕获3D形状的局部细节和全局一致性。与现有方法相比，LoG3D不需要watertight预处理，并且能够处理非流形几何体。此外，LoG3D的模块化设计使其能够无缝扩展到超高分辨率（高达2048^3）。

**关键设计**：1) UBlock大小：论文中UBlock的大小是一个重要的参数，它决定了局部特征提取的范围和计算复杂度。2) 稀疏Transformer：使用稀疏Transformer来降低计算复杂度，并提高全局关系建模的效率。3) Pad-Average策略：使用Pad-Average策略来确保子体积边界处的平滑过渡，从而提高重建质量。4) 损失函数：使用重建损失和KL散度损失来训练VAE模型。

## 📊 实验亮点

实验结果表明，LoG3D在重建精度和生成质量方面均达到了最先进的性能。与现有方法相比，LoG3D能够生成更平滑、几何灵活性更高的表面。此外，LoG3D还能够处理高达2048^3分辨率的3D模型，这是现有3D VAE无法达到的。

## 🎯 应用场景

LoG3D在游戏开发、电影制作、工业设计、医学成像等领域具有广泛的应用前景。它可以用于生成高保真、高分辨率的3D模型，从而提高视觉效果和用户体验。此外，LoG3D还可以用于3D形状的生成和编辑，从而加速设计流程和降低成本。未来，LoG3D有望成为3D内容创作的重要工具。

## 📄 摘要（原文）

> Generating high-fidelity 3D contents remains a fundamental challenge due to the complexity of representing arbitrary topologies-such as open surfaces and intricate internal structures-while preserving geometric details. Prevailing methods based on signed distance fields (SDFs) are hampered by costly watertight preprocessing and struggle with non-manifold geometries, while point-cloud representations often suffer from sampling artifacts and surface discontinuities. To overcome these limitations, we propose a novel 3D variational autoencoder (VAE) framework built upon unsigned distance fields (UDFs)-a more robust and computationally efficient representation that naturally handles complex and incomplete shapes. Our core innovation is a local-to-global (LoG) architecture that processes the UDF by partitioning it into uniform subvolumes, termed UBlocks. This architecture couples 3D convolutions for capturing local detail with sparse transformers for enforcing global coherence. A Pad-Average strategy further ensures smooth transitions at subvolume boundaries during reconstruction. This modular design enables seamless scaling to ultra-high resolutions up to $2048^3$-a regime previously unattainable for 3D VAEs. Experiments demonstrate state-of-the-art performance in both reconstruction accuracy and generative quality, yielding superior surface smoothness and geometric flexibility.

