---
layout: default
title: MRD: Using Physically Based Differentiable Rendering to Probe Vision Models for 3D Scene Understanding
---

# MRD: Using Physically Based Differentiable Rendering to Probe Vision Models for 3D Scene Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.12307" class="toolbar-btn" target="_blank">📄 arXiv: 2512.12307v1</a>
  <a href="https://arxiv.org/pdf/2512.12307.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.12307v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.12307v1', 'MRD: Using Physically Based Differentiable Rendering to Probe Vision Models for 3D Scene Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Benjamin Beilharz, Thomas S. A. Wallis

**分类**: cs.CV, cs.GR

**发布日期**: 2025-12-13

**备注**: 18 pages, 6 figures. Supplementary material and code will be provided at the end of January

---

## 💡 一句话要点

**提出MRD，利用可微渲染探究视觉模型对3D场景的理解能力**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `可微渲染` `模型可解释性` `3D场景理解` `视觉模型` `物理渲染`

## 📋 核心要点

1. 现有视觉模型难以解释其对3D场景的隐式理解，缺乏有效的探究方法。
2. MRD利用可微渲染，寻找物理上不同但模型激活相同的3D场景参数，从而探究模型对场景属性的敏感性。
3. 实验表明，MRD能有效重建场景参数，揭示模型对形状和材质等属性的关注点。

## 📝 摘要（中文）

深度学习方法在许多视觉基准测试中取得了显著成功，但理解和解释这些模型的表征和决策仍然很困难。虽然视觉模型通常在2D输入上训练，但人们常常假设它们发展了对底层3D场景的隐式表征（例如，对部分遮挡的容忍度，或推理相对深度的能力）。本文介绍MRD（metamers rendered differentiably），该方法利用基于物理的可微渲染来探究视觉模型对生成式3D场景属性的隐式理解，通过寻找在物理上不同但产生相同模型激活的3D场景参数（即模型同度异构体）。与之前基于像素的评估模型表征的方法不同，这些重建结果始终基于物理场景描述。这意味着我们可以探究模型对物体形状的敏感性，同时保持材质和光照不变。作为概念验证，我们评估了多个模型恢复几何形状（形状）和双向反射分布函数（材质）等场景参数的能力。结果表明，目标场景和优化场景之间的模型激活具有高度相似性，但视觉结果各不相同。定性地，这些重建有助于研究模型敏感或不变的物理场景属性。MRD有望通过分析物理场景参数如何驱动模型响应的变化，从而促进我们对计算机和人类视觉的理解。

## 🔬 方法详解

**问题定义**：现有深度学习视觉模型在2D图像上训练，虽然被认为学习了对3D场景的隐式理解，但缺乏有效的方法来探究和解释这种理解。之前的像素级方法无法保证重建结果的物理合理性，难以控制场景属性，例如独立地改变形状或材质。

**核心思路**：MRD的核心思路是利用可微渲染技术，将视觉模型的输出与3D场景参数联系起来。通过优化3D场景参数，使得渲染出的图像在视觉模型中产生与目标图像相似的激活，从而反推出模型所“看到”的3D场景。这种方法保证了重建结果的物理一致性，并允许研究者控制和操纵场景属性。

**技术框架**：MRD的整体框架包含以下几个主要步骤：1) 选择一个目标图像，输入到预训练的视觉模型中，提取特定层的激活作为目标激活。2) 初始化一个3D场景，包含几何形状、材质和光照等参数。3) 使用可微渲染器将3D场景渲染成2D图像。4) 将渲染的图像输入到相同的视觉模型中，提取对应层的激活。5) 计算渲染图像的激活与目标激活之间的损失函数。6) 使用梯度下降等优化算法，调整3D场景参数，最小化损失函数。7) 重复步骤3-6，直到损失函数收敛。

**关键创新**：MRD的关键创新在于将可微渲染技术与视觉模型的表征学习联系起来，提供了一种基于物理的、可解释的模型探究方法。与传统的基于像素的优化方法相比，MRD的重建结果具有物理合理性，并且可以控制场景属性，例如独立地改变形状或材质。

**关键设计**：MRD的关键设计包括：1) 使用基于物理的渲染器，保证渲染结果的真实感和物理一致性。2) 选择合适的视觉模型层，以提取具有代表性的激活。3) 设计合适的损失函数，例如L2损失或余弦相似度，以衡量激活之间的相似性。4) 选择合适的优化算法，例如Adam或LBFGS，以有效地优化3D场景参数。5) 对3D场景参数进行合理的初始化和约束，以避免优化过程中的奇异值和不合理的场景配置。

## 📊 实验亮点

实验结果表明，MRD能够有效地重建3D场景参数，使得重建场景在视觉模型中产生与目标场景相似的激活。虽然视觉效果上可能存在差异，但模型激活的相似度很高，表明模型对某些物理属性具有不变性。通过分析重建结果，可以揭示模型对形状、材质和光照等属性的敏感程度。

## 🎯 应用场景

MRD可用于分析和理解计算机视觉模型的内部表征，揭示模型对不同场景属性的敏感性。此外，该方法还可应用于对抗样本生成，通过操纵3D场景参数生成难以被模型识别的图像。未来，MRD有望促进计算机视觉和人类视觉的交叉研究，帮助我们更好地理解人类视觉感知机制。

## 📄 摘要（原文）

> While deep learning methods have achieved impressive success in many vision benchmarks, it remains difficult to understand and explain the representations and decisions of these models. Though vision models are typically trained on 2D inputs, they are often assumed to develop an implicit representation of the underlying 3D scene (for example, showing tolerance to partial occlusion, or the ability to reason about relative depth). Here, we introduce MRD (metamers rendered differentiably), an approach that uses physically based differentiable rendering to probe vision models' implicit understanding of generative 3D scene properties, by finding 3D scene parameters that are physically different but produce the same model activation (i.e. are model metamers). Unlike previous pixel-based methods for evaluating model representations, these reconstruction results are always grounded in physical scene descriptions. This means we can, for example, probe a model's sensitivity to object shape while holding material and lighting constant. As a proof-of-principle, we assess multiple models in their ability to recover scene parameters of geometry (shape) and bidirectional reflectance distribution function (material). The results show high similarity in model activation between target and optimized scenes, with varying visual results. Qualitatively, these reconstructions help investigate the physical scene attributes to which models are sensitive or invariant. MRD holds promise for advancing our understanding of both computer and human vision by enabling analysis of how physical scene parameters drive changes in model responses.

