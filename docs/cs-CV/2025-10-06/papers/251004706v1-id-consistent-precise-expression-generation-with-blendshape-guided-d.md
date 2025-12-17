---
layout: default
title: ID-Consistent, Precise Expression Generation with Blendshape-Guided Diffusion
---

# ID-Consistent, Precise Expression Generation with Blendshape-Guided Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04706" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04706v1</a>
  <a href="https://arxiv.org/pdf/2510.04706.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04706v1" onclick="toggleFavorite(this, '2510.04706v1', 'ID-Consistent, Precise Expression Generation with Blendshape-Guided Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Foivos Paraperas Papantoniou, Stefanos Zafeiriou

**分类**: cs.CV

**发布日期**: 2025-10-06

**备注**: ICCVW 2025, Code: https://github.com/foivospar/Arc2Face

**🔗 代码/项目**: [GITHUB](https://github.com/foivospar/Arc2Face)

---

## 💡 一句话要点

**提出Blendshape引导的扩散模型，实现身份保持和精准表情生成。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `面部表情生成` `身份保持` `FLAME模型` `Blendshape参数`

## 📋 核心要点

1. 现有AI驱动的生成模型在精细表情控制和身份保持方面存在挑战，难以兼顾两者。
2. 论文提出一种基于扩散模型的框架，利用FLAME blendshape参数引导表情生成，实现精准控制。
3. 实验表明，该模型在表情生成和身份保持方面优于现有方法，并能处理微表情和表情过渡。

## 📝 摘要（中文）

本文提出了一种基于扩散模型的框架，旨在逼真地重塑任何主体在任何特定面部表情下的形象。该框架建立在身份一致的面部基础模型之上，采用了一种组合式设计，其特点是使用由FLAME blendshape参数引导的表情交叉注意力模块，以实现显式控制。该模型在包含丰富表情变化的图像和视频数据的混合数据集上进行训练，能够泛化到细微的微表情和表情过渡，这些是先前工作所忽略的。此外，一个可插拔的参考适配器通过在合成过程中从参考帧转移外观，从而实现在真实图像中的表情编辑。大量的定量和定性评估表明，我们的模型在定制和身份一致的表情生成方面优于现有方法。

## 🔬 方法详解

**问题定义**：现有的人脸生成模型，尤其是在AI驱动的叙事应用中，难以在保持个体身份的同时，实现对面部表情的精确控制。虽然基于扩散模型的方法在身份保持方面取得了显著进展，但在不损害身份的情况下实现细粒度的表情控制仍然是一个挑战。

**核心思路**：本文的核心思路是利用FLAME blendshape参数作为显式的表情控制信号，通过一个表情交叉注意力模块来引导扩散模型的生成过程。这种方法将表情控制与底层身份信息解耦，从而允许在不改变身份的情况下精确地控制面部表情。

**技术框架**：该框架建立在一个身份一致的面部基础模型之上。主要包含以下几个模块：1) 基础扩散模型，负责生成人脸图像；2) FLAME blendshape参数提取模块，用于提取输入图像或视频中的表情参数；3) 表情交叉注意力模块，该模块将提取的blendshape参数作为条件，通过交叉注意力机制来调节扩散模型的生成过程，从而控制生成的面部表情；4) 可选的参考适配器，用于在真实图像中进行表情编辑，通过从参考帧转移外观来实现。

**关键创新**：该方法的主要创新在于使用blendshape参数作为显式的表情控制信号，并将其融入到扩散模型的生成过程中。与以往方法相比，这种方法能够实现更精确的表情控制，并且能够更好地保持个体身份。此外，该模型能够泛化到微表情和表情过渡，这是以往方法所忽略的。

**关键设计**：表情交叉注意力模块是关键设计之一，它允许模型根据blendshape参数来调节生成过程。训练数据包含图像和视频的混合数据，以增加模型的泛化能力。损失函数包括重建损失和对抗损失，以保证生成图像的质量和真实感。参考适配器通过学习参考图像和目标图像之间的映射关系，实现外观的转移。

## 📊 实验亮点

实验结果表明，该模型在身份一致性和表情控制方面均优于现有方法。定性结果展示了模型生成微表情和表情过渡的能力。定量评估指标显示，该模型在表情准确性和身份保持方面取得了显著提升。代码和模型已开源。

## 🎯 应用场景

该研究成果可应用于AI驱动的叙事、虚拟化身生成、人机交互、动画制作、以及面部表情分析等领域。通过精确控制面部表情，可以创造更逼真、更具表现力的虚拟角色，提升用户体验，并为心理学研究提供新的工具。

## 📄 摘要（原文）

> Human-centric generative models designed for AI-driven storytelling must bring together two core capabilities: identity consistency and precise control over human performance. While recent diffusion-based approaches have made significant progress in maintaining facial identity, achieving fine-grained expression control without compromising identity remains challenging. In this work, we present a diffusion-based framework that faithfully reimagines any subject under any particular facial expression. Building on an ID-consistent face foundation model, we adopt a compositional design featuring an expression cross-attention module guided by FLAME blendshape parameters for explicit control. Trained on a diverse mixture of image and video data rich in expressive variation, our adapter generalizes beyond basic emotions to subtle micro-expressions and expressive transitions, overlooked by prior works. In addition, a pluggable Reference Adapter enables expression editing in real images by transferring the appearance from a reference frame during synthesis. Extensive quantitative and qualitative evaluations show that our model outperforms existing methods in tailored and identity-consistent expression generation. Code and models can be found at https://github.com/foivospar/Arc2Face.

