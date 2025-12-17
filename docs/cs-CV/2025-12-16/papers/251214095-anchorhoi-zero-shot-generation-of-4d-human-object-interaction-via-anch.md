---
layout: default
title: AnchorHOI: Zero-shot Generation of 4D Human-Object Interaction via Anchor-based Prior Distillation
---

# AnchorHOI: Zero-shot Generation of 4D Human-Object Interaction via Anchor-based Prior Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14095" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14095</a>
  <a href="https://arxiv.org/pdf/2512.14095.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14095" onclick="toggleFavorite(this, '2512.14095', 'AnchorHOI: Zero-shot Generation of 4D Human-Object Interaction via Anchor-based Prior Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sisi Dai, Kai Xu

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**AnchorHOI：基于锚点的先验知识蒸馏实现零样本4D人-物交互生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `4D人-物交互` `零样本生成` `扩散模型` `先验知识蒸馏` `锚点` `神经辐射场` `运动合成`

## 📋 核心要点

1. 现有文本驱动4D HOI生成方法受限于大规模数据集的稀缺，泛化能力不足。
2. AnchorHOI利用锚点先验蒸馏策略，通过交互感知的锚点引导生成，降低优化难度。
3. 实验表明，AnchorHOI在生成多样性和泛化性上优于现有方法，提升了4D HOI生成效果。

## 📝 摘要（中文）

本文提出AnchorHOI框架，旨在解决大规模4D人-物交互(HOI)数据集稀缺导致的文本驱动4D HOI生成可扩展性受限问题。AnchorHOI通过结合视频扩散模型和图像扩散模型，充分利用混合先验知识，从而推进4D HOI生成。该方法引入基于锚点的先验知识蒸馏策略，构建交互感知的锚点，并利用这些锚点指导生成过程，从而解决直接优化高维4D HOI带来的挑战，特别是对于人体姿态和组合运动。具体而言，AnchorHOI为4D HOI生成设计了两个定制锚点：用于表达交互组合的锚点神经辐射场(NeRFs)和用于逼真运动合成的锚点关键点。实验结果表明，AnchorHOI在多样性和泛化性方面优于现有方法。

## 🔬 方法详解

**问题定义**：现有文本驱动的4D人-物交互（HOI）生成方法依赖于大规模的4D HOI数据集进行训练，但此类数据集的获取成本高昂，导致模型泛化能力受限，难以应用于各种复杂的交互场景。直接利用预训练的图像扩散模型进行零样本生成时，交互信息的有效利用不足，影响了生成结果的质量和多样性。

**核心思路**：AnchorHOI的核心思路是利用预训练的图像和视频扩散模型中的先验知识，通过锚点（anchors）作为桥梁，将这些先验知识有效地蒸馏到4D HOI生成过程中。通过构建交互感知的锚点，降低了直接优化高维4D HOI的难度，从而实现高质量、多样化的零样本4D HOI生成。

**技术框架**：AnchorHOI框架包含两个主要阶段：锚点构建阶段和生成阶段。在锚点构建阶段，首先根据文本描述生成初始的3D人体姿态和物体形状。然后，利用预训练的图像和视频扩散模型，分别生成锚点NeRFs（用于表达交互组合）和锚点关键点（用于逼真运动合成）。在生成阶段，利用锚点NeRFs和锚点关键点作为引导，通过扩散模型逐步生成最终的4D HOI结果。

**关键创新**：AnchorHOI的关键创新在于提出了基于锚点的先验知识蒸馏策略。与直接优化4D HOI不同，AnchorHOI通过构建交互感知的锚点，将复杂的4D HOI生成过程分解为两个更易于处理的子问题：交互组合和运动合成。这种分解方式使得模型能够更好地利用预训练模型中的先验知识，从而提高生成结果的质量和多样性。

**关键设计**：AnchorHOI的关键设计包括：1) 锚点NeRFs的设计，用于表达人体和物体之间的交互关系，通过NeRFs可以生成高质量的3D形状和纹理；2) 锚点关键点的设计，用于捕捉人体运动的动态信息，通过关键点可以生成逼真的运动序列；3) 损失函数的设计，用于约束生成结果与锚点之间的相似性，确保生成结果符合预期的交互模式和运动轨迹。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14095/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14095/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14095/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，AnchorHOI在4D HOI生成任务上取得了显著的性能提升。相较于现有方法，AnchorHOI在生成结果的多样性和泛化性方面均有明显优势。具体而言，AnchorHOI能够生成更加逼真、自然的交互动画，并且能够处理各种复杂的交互场景。

## 🎯 应用场景

AnchorHOI在虚拟现实、游戏开发、人机交互等领域具有广泛的应用前景。它可以用于生成逼真的人-物交互动画，提升虚拟环境的沉浸感和交互性。此外，AnchorHOI还可以用于机器人控制和行为规划，帮助机器人更好地理解和执行复杂的任务。

## 📄 摘要（原文）

> Despite significant progress in text-driven 4D human-object interaction (HOI) generation with supervised methods, the scalability remains limited by the scarcity of large-scale 4D HOI datasets. To overcome this, recent approaches attempt zero-shot 4D HOI generation with pre-trained image diffusion models. However, interaction cues are minimally distilled during the generation process, restricting their applicability across diverse scenarios. In this paper, we propose AnchorHOI, a novel framework that thoroughly exploits hybrid priors by incorporating video diffusion models beyond image diffusion models, advancing 4D HOI generation. Nevertheless, directly optimizing high-dimensional 4D HOI with such priors remains challenging, particularly for human pose and compositional motion. To address this challenge, AnchorHOI introduces an anchor-based prior distillation strategy, which constructs interaction-aware anchors and then leverages them to guide generation in a tractable two-step process. Specifically, two tailored anchors are designed for 4D HOI generation: anchor Neural Radiance Fields (NeRFs) for expressive interaction composition, and anchor keypoints for realistic motion synthesis. Extensive experiments demonstrate that AnchorHOI outperforms previous methods with superior diversity and generalization.

