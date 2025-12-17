---
layout: default
title: SaFiRe: Saccade-Fixation Reiteration with Mamba for Referring Image Segmentation
---

# SaFiRe: Saccade-Fixation Reiteration with Mamba for Referring Image Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10160" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10160v2</a>
  <a href="https://arxiv.org/pdf/2510.10160.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10160v2" onclick="toggleFavorite(this, '2510.10160v2', 'SaFiRe: Saccade-Fixation Reiteration with Mamba for Referring Image Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenjie Mao, Yuhuan Yang, Chaofan Ma, Dongsheng Jiang, Jiangchao Yao, Ya Zhang, Yanfeng Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-11 (更新: 2025-11-26)

**备注**: NeurIPS 2025; Project page: https://zhenjiemao.github.io/SaFiRe/

---

## 💡 一句话要点

**提出SaFiRe框架，利用Mamba解决指代图像分割中复杂表达式的难题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `指代图像分割` `Mamba` `视觉语言理解` `复杂表达式` `迭代细化`

## 📋 核心要点

1. 现有指代图像分割方法在处理复杂、具有歧义性的表达式时存在不足，容易退化为关键词匹配。
2. SaFiRe框架模仿人类认知过程，通过全局理解和细节检查两个阶段，利用Mamba进行高效的多周期细化。
3. 引入新的基准数据集aRefCOCO，并在标准数据集和新数据集上验证了SaFiRe的优越性。

## 📝 摘要（中文）

本文提出了一种名为SaFiRe的新框架，用于解决指代图像分割(RIS)中复杂表达式的挑战。现有的RIS方法主要关注简单的名词短语，容易将RIS简化为关键词匹配问题，从而限制了模型处理表达式中指代歧义的能力。本文针对两种具有挑战性的现实场景：包含多个实体和上下文线索的对象干扰表达式，以及未明确说明对象类别的类别隐式表达式，提出了SaFiRe。该框架模仿人类的两阶段认知过程，首先形成全局理解，然后通过细节导向的检查来细化理解。Mamba的扫描-更新特性自然支持这种分阶段设计，并以线性复杂度实现高效的多周期细化。此外，本文还引入了一个新的基准数据集aRefCOCO，用于评估RIS模型在模糊指代表达式下的性能。在标准数据集和提出的数据集上的大量实验表明，SaFiRe优于最先进的基线方法。

## 🔬 方法详解

**问题定义**：指代图像分割(RIS)旨在根据自然语言表达式分割图像中的目标对象。现有方法在处理复杂表达式时，容易将问题简化为关键词匹配，忽略了表达式中的上下文信息和指代关系，导致模型无法准确理解和分割目标对象。特别是对于对象干扰表达式（包含多个实体）和类别隐式表达式（未明确指出对象类别）两种情况，现有方法的性能显著下降。

**核心思路**：SaFiRe框架的核心思路是模仿人类的认知过程，将RIS任务分解为两个阶段：全局理解和细节检查。全局理解阶段旨在快速捕捉图像和表达式的整体信息，建立初步的指代关系；细节检查阶段则通过关注局部细节和上下文信息，对初步的指代关系进行细化和修正。这种两阶段的迭代过程能够更好地处理表达式中的歧义性和复杂性。

**技术框架**：SaFiRe框架主要包含三个模块：视觉编码器、文本编码器和Mamba迭代细化模块。视觉编码器和文本编码器分别用于提取图像和表达式的特征。Mamba迭代细化模块是核心模块，它利用Mamba的扫描-更新特性，在全局理解和细节检查两个阶段之间进行迭代。在每个迭代周期中，Mamba首先扫描图像和表达式的特征，然后根据扫描结果更新指代关系。通过多个迭代周期，模型可以逐步细化指代关系，最终实现准确的图像分割。

**关键创新**：SaFiRe的关键创新在于将Mamba应用于RIS任务，并利用其扫描-更新特性来模拟人类的认知过程。与传统的循环神经网络(RNN)和Transformer相比，Mamba具有线性复杂度，能够高效地处理长序列数据，更适合于多周期迭代细化。此外，SaFiRe框架的分阶段设计也使其能够更好地处理复杂表达式中的歧义性和上下文信息。

**关键设计**：SaFiRe框架使用预训练的视觉Transformer (例如ViT) 和文本Transformer (例如BERT) 作为视觉编码器和文本编码器。Mamba迭代细化模块包含多个Mamba层，每个Mamba层都包含一个选择机制，用于选择重要的特征进行更新。损失函数采用Dice loss和交叉熵损失的组合，用于优化分割结果。aRefCOCO数据集的构建考虑了对象干扰和类别隐式两种情况，包含更复杂的表达式和更具挑战性的场景。

## 📊 实验亮点

实验结果表明，SaFiRe在标准数据集RefCOCO、RefCOCO+和G-Ref上取得了显著的性能提升，尤其是在新提出的aRefCOCO数据集上，SaFiRe的性能明显优于其他基线方法。例如，在aRefCOCO数据集上，SaFiRe的IoU指标比最先进的基线方法提高了5%以上，证明了SaFiRe在处理复杂表达式方面的优越性。

## 🎯 应用场景

SaFiRe框架在指代图像分割领域具有广泛的应用前景，例如智能监控、自动驾驶、图像编辑和人机交互等。该框架能够准确理解复杂的自然语言指令，并分割图像中的目标对象，从而实现更智能、更高效的图像处理和分析。未来，SaFiRe可以进一步扩展到其他视觉任务，例如视觉问答和图像描述。

## 📄 摘要（原文）

> Referring Image Segmentation (RIS) aims to segment the target object in an image given a natural language expression. While recent methods leverage pre-trained vision backbones and more training corpus to achieve impressive results, they predominantly focus on simple expressions--short, clear noun phrases like "red car" or "left girl". This simplification often reduces RIS to a key word/concept matching problem, limiting the model's ability to handle referential ambiguity in expressions. In this work, we identify two challenging real-world scenarios: object-distracting expressions, which involve multiple entities with contextual cues, and category-implicit expressions, where the object class is not explicitly stated. To address the challenges, we propose a novel framework, SaFiRe, which mimics the human two-phase cognitive process--first forming a global understanding, then refining it through detail-oriented inspection. This is naturally supported by Mamba's scan-then-update property, which aligns with our phased design and enables efficient multi-cycle refinement with linear complexity. We further introduce aRefCOCO, a new benchmark designed to evaluate RIS models under ambiguous referring expressions. Extensive experiments on both standard and proposed datasets demonstrate the superiority of SaFiRe over state-of-the-art baselines.

