---
layout: default
title: "GoLF-NRT: Integrating Global Context and Local Geometry for Few-Shot View Synthesis"
---

# GoLF-NRT: Integrating Global Context and Local Geometry for Few-Shot View Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19813" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19813v1</a>
  <a href="https://arxiv.org/pdf/2505.19813.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19813v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19813v1', 'GoLF-NRT: Integrating Global Context and Local Geometry for Few-Shot View Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: You Wang, Li Fang, Hao Zhu, Fei Hu, Long Ye, Zhan Ma

**分类**: cs.CV

**发布日期**: 2025-05-26

**备注**: CVPR 2025

**🔗 代码/项目**: [GITHUB](https://github.com/KLMAV-CUC/GoLF-NRT)

---

## 💡 一句话要点

**提出GoLF-NRT以解决少量视图合成质量下降问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `神经辐射场` `视图合成` `全局特征` `局部几何` `自适应采样` `3D变换器` `稀疏注意力` `计算机视觉`

## 📋 核心要点

1. 现有的NeRF模型在输入视图数量有限时，渲染质量显著下降，无法满足高质量新视图合成的需求。
2. GoLF-NRT通过结合全局场景上下文和局部几何特征，利用3D变换器和稀疏注意力机制，提升少量输入视图下的渲染效果。
3. 在公共数据集上的实验结果显示，GoLF-NRT在不同输入视图数量下均表现出色，超越了现有的最先进方法。

## 📝 摘要（中文）

神经辐射场（NeRF）通过直接从图像建模场景特定的体积表示，改变了新视图合成。然而，现有的可泛化NeRF模型在输入视图数量有限时，渲染质量显著下降。为了解决这一问题，本文提出了GoLF-NRT：一种基于全局和局部特征融合的神经渲染变换器。GoLF-NRT通过高效稀疏注意力机制捕捉全局场景上下文，并结合沿极线提取的局部几何特征，从1到3个输入视图中实现高质量场景重建。此外，基于注意力权重和核回归的自适应采样策略提高了变换器神经渲染的准确性。大量实验表明，GoLF-NRT在不同输入视图数量下均实现了最先进的性能，展示了其方法的有效性和优越性。

## 🔬 方法详解

**问题定义**：本文旨在解决在输入视图数量有限时，NeRF模型渲染质量显著下降的问题。现有方法依赖大量多视图观察，导致在少量视图下性能下降。

**核心思路**：GoLF-NRT的核心思路是通过全局和局部特征的融合，利用3D变换器的稀疏注意力机制来捕捉场景的全局上下文，同时提取局部几何特征，从而在少量输入视图下实现高质量的场景重建。

**技术框架**：GoLF-NRT的整体架构包括全局特征提取模块、局部几何特征提取模块和自适应采样策略。全局特征通过3D变换器获取，而局部几何特征则沿极线提取。自适应采样策略则基于注意力权重进行优化。

**关键创新**：GoLF-NRT的主要创新在于结合全局上下文和局部几何信息的特征融合方法，以及引入的自适应采样策略，这在现有NeRF模型中尚未实现。

**关键设计**：在设计中，采用了高效的稀疏注意力机制以降低计算复杂度，并通过核回归方法优化采样策略，从而提高了渲染的准确性和质量。具体的损失函数和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

在公共数据集上的实验结果表明，GoLF-NRT在输入视图数量为1至3时，渲染质量显著提升，超越了现有最先进的NeRF模型，展示了其在少量视图合成中的有效性。具体性能数据未提供，但实验结果表明该方法在多种场景下均表现优异。

## 🎯 应用场景

GoLF-NRT的研究成果在虚拟现实、增强现实和计算机图形学等领域具有广泛的应用潜力。通过提升少量视图下的渲染质量，该方法可以为实时场景重建和交互式应用提供更高的视觉体验，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Neural Radiance Fields (NeRF) have transformed novel view synthesis by modeling scene-specific volumetric representations directly from images. While generalizable NeRF models can generate novel views across unknown scenes by learning latent ray representations, their performance heavily depends on a large number of multi-view observations. However, with limited input views, these methods experience significant degradation in rendering quality. To address this limitation, we propose GoLF-NRT: a Global and Local feature Fusion-based Neural Rendering Transformer. GoLF-NRT enhances generalizable neural rendering from few input views by leveraging a 3D transformer with efficient sparse attention to capture global scene context. In parallel, it integrates local geometric features extracted along the epipolar line, enabling high-quality scene reconstruction from as few as 1 to 3 input views. Furthermore, we introduce an adaptive sampling strategy based on attention weights and kernel regression, improving the accuracy of transformer-based neural rendering. Extensive experiments on public datasets show that GoLF-NRT achieves state-of-the-art performance across varying numbers of input views, highlighting the effectiveness and superiority of our approach. Code is available at https://github.com/KLMAV-CUC/GoLF-NRT.

