---
layout: default
title: "LaMoGen: Laban Movement-Guided Diffusion for Text-to-Motion Generation"
---

# LaMoGen: Laban Movement-Guided Diffusion for Text-to-Motion Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24469" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24469v2</a>
  <a href="https://arxiv.org/pdf/2509.24469.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24469v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24469v2', 'LaMoGen: Laban Movement-Guided Diffusion for Text-to-Motion Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heechang Kim, Gwanghyun Kim, Se Young Chun

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-29 (更新: 2025-10-13)

---

## 💡 一句话要点

**提出LaMoGen以解决文本到运动生成中的表达控制问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `文本到运动生成` `扩散模型` `Laban运动分析` `人类运动生成` `可解释性` `表现控制` `多样性`

## 📋 核心要点

1. 现有的文本到运动生成方法在细粒度表现控制上存在显著挑战，主要由于数据集缺乏运动风格多样性。
2. 本文提出了一种将Laban运动分析的量化方法集成到文本引导运动生成模型中的新方法，旨在实现更好的运动控制。
3. 实验结果表明，该方法在多样化表现运动质量和保持运动身份方面表现优异，成功操控运动属性。

## 📝 摘要（中文）

多样化的人类运动生成在计算机视觉、人机交互和动画等领域越来越重要。尽管基于扩散模型的文本到运动合成在生成高质量运动方面取得了成功，但实现细粒度的表现控制仍然是一个重大挑战。这主要源于数据集中运动风格多样性的缺乏以及用自然语言表达定量特征的困难。Laban运动分析被舞蹈专家广泛使用，以尽可能一致地表达运动的细节和质量。受此启发，本文旨在通过将Laban Effort和Shape组件的量化方法无缝集成到文本引导的运动生成模型中，实现人类运动生成的可解释和表现控制。我们提出的零-shot推理优化方法在采样步骤中更新预训练扩散模型的文本嵌入，从而指导运动生成模型获得所需的Laban Effort和Shape组件，而无需额外的运动数据。我们的研究表明，该方法在成功操控运动属性的同时，能够生成多样化的表现运动质量，保持运动身份。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到运动生成中的细粒度表现控制问题，现有方法在运动风格多样性和自然语言表达定量特征方面存在不足。

**核心思路**：通过将Laban Effort和Shape组件的量化方法集成到文本引导的运动生成模型中，本文实现了对人类运动生成的可解释和表现控制。该方法在推理时优化文本嵌入，避免了对额外运动数据的需求。

**技术框架**：整体架构包括预训练的扩散模型和优化过程。在采样步骤中，更新文本嵌入以引导运动生成，确保生成的运动符合目标Laban标签。

**关键创新**：最重要的创新在于提出了一种零-shot推理优化方法，使得模型能够在没有额外运动数据的情况下，灵活生成符合Laban Effort和Shape要求的运动。

**关键设计**：关键设计包括对文本嵌入的动态更新策略，以及如何在生成过程中有效地操控运动属性，确保生成的运动既多样又具有表现力。具体的损失函数和网络结构设计在论文中进行了详细讨论。

## 📊 实验亮点

实验结果显示，LaMoGen在生成运动质量方面表现出色，相较于基线模型，运动表现的多样性和表达能力显著提升，具体提升幅度未知，且成功操控运动属性的能力得到了验证。

## 🎯 应用场景

该研究的潜在应用领域包括动画制作、游戏开发和虚拟现实等。通过实现对人类运动生成的精确控制，能够提升人机交互的自然性和表现力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Diverse human motion generation is an increasingly important task, having various applications in computer vision, human-computer interaction and animation. While text-to-motion synthesis using diffusion models has shown success in generating high-quality motions, achieving fine-grained expressive motion control remains a significant challenge. This is due to the lack of motion style diversity in datasets and the difficulty of expressing quantitative characteristics in natural language. Laban movement analysis has been widely used by dance experts to express the details of motion including motion quality as consistent as possible. Inspired by that, this work aims for interpretable and expressive control of human motion generation by seamlessly integrating the quantification methods of Laban Effort and Shape components into the text-guided motion generation models. Our proposed zero-shot, inference-time optimization method guides the motion generation model to have desired Laban Effort and Shape components without any additional motion data by updating the text embedding of pretrained diffusion models during the sampling step. We demonstrate that our approach yields diverse expressive motion qualities while preserving motion identity by successfully manipulating motion attributes according to target Laban tags.

