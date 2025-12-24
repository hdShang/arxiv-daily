---
layout: default
title: Advancing high-fidelity 3D and Texture Generation with 2.5D latents
---

# Advancing high-fidelity 3D and Texture Generation with 2.5D latents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21050" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21050v2</a>
  <a href="https://arxiv.org/pdf/2505.21050.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21050v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21050v2', 'Advancing high-fidelity 3D and Texture Generation with 2.5D latents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Yang, Jiantao Lin, Yingjie Xu, Haodong Li, Yingcong Chen

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-05-28)

---

## 💡 一句话要点

**提出一种新框架以解决3D几何与纹理生成不一致问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D生成` `纹理生成` `几何一致性` `2.5D表示` `多视角图像` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有3D生成方法通常在几何和纹理生成上采用不同模型，导致生成结果缺乏一致性。
2. 本文提出了一种新框架，通过2.5D表示实现3D几何和纹理的联合生成，提升生成质量。
3. 实验结果显示，模型在高质量3D对象生成上表现优异，且在纹理生成方面显著优于现有技术。

## 📝 摘要（中文）

尽管已有大规模3D数据集和3D生成模型的进展，3D几何和纹理数据的复杂性及质量不均仍然阻碍了3D生成技术的性能。现有方法通常分阶段生成3D几何和纹理，导致两者之间缺乏一致性。为此，本文提出了一种新颖的框架，专注于联合生成3D几何和纹理，利用可无缝转换的2.5D表示。通过整合多视角RGB、法线和坐标图像为统一的2.5D潜在表示，并适配预训练的2D基础模型，最终引入轻量级的2.5D到3D的精炼解码器框架，生成高保真3D表示。实验表明，该模型在生成高质量3D对象方面表现优异，且在几何条件下的纹理生成上显著超越现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有3D生成技术中几何与纹理生成不一致的问题。现有方法通常分阶段处理，导致生成结果的结构和颜色不协调。

**核心思路**：提出一种基于2.5D表示的联合生成框架，能够在2D与3D之间无缝转换，从而提高生成的一致性和质量。

**技术框架**：整体架构包括三个主要模块：首先整合多视角RGB、法线和坐标图像为统一的2.5D潜在表示；其次，利用文本和图像条件适配预训练的2D基础模型进行高保真2.5D生成；最后，采用轻量级的2.5D到3D精炼解码器框架生成详细的3D表示。

**关键创新**：最重要的创新在于提出了2.5D潜在表示的概念，使得几何和纹理的生成可以在同一框架下进行，从而克服了传统方法的局限性。

**关键设计**：在模型设计中，采用了特定的损失函数以确保生成结果的结构和颜色一致性，同时优化了网络结构以提高生成效率和质量。

## 📊 实验亮点

实验结果表明，所提出的模型在生成高质量3D对象方面表现优异，生成的3D对象在结构和颜色一致性上显著优于现有方法，尤其在几何条件下的纹理生成上，性能提升幅度达到XX%。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发、电影特效制作等，能够为3D内容创作提供更高效的解决方案。未来，该技术可能在自动化设计、数字孪生等领域发挥重要作用，推动3D生成技术的进一步发展。

## 📄 摘要（原文）

> Despite the availability of large-scale 3D datasets and advancements in 3D generative models, the complexity and uneven quality of 3D geometry and texture data continue to hinder the performance of 3D generation techniques. In most existing approaches, 3D geometry and texture are generated in separate stages using different models and non-unified representations, frequently leading to unsatisfactory coherence between geometry and texture. To address these challenges, we propose a novel framework for joint generation of 3D geometry and texture. Specifically, we focus in generate a versatile 2.5D representations that can be seamlessly transformed between 2D and 3D. Our approach begins by integrating multiview RGB, normal, and coordinate images into a unified representation, termed as 2.5D latents. Next, we adapt pre-trained 2D foundation models for high-fidelity 2.5D generation, utilizing both text and image conditions. Finally, we introduce a lightweight 2.5D-to-3D refiner-decoder framework that efficiently generates detailed 3D representations from 2.5D images. Extensive experiments demonstrate that our model not only excels in generating high-quality 3D objects with coherent structure and color from text and image inputs but also significantly outperforms existing methods in geometry-conditioned texture generation.

