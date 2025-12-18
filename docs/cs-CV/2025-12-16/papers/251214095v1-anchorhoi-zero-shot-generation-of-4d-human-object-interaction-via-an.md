---
layout: default
title: AnchorHOI: Zero-shot Generation of 4D Human-Object Interaction via Anchor-based Prior Distillation
---

# AnchorHOI: Zero-shot Generation of 4D Human-Object Interaction via Anchor-based Prior Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14095" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14095v1</a>
  <a href="https://arxiv.org/pdf/2512.14095.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14095v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14095v1', 'AnchorHOI: Zero-shot Generation of 4D Human-Object Interaction via Anchor-based Prior Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sisi Dai, Kai Xu

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: AAAI 2026

---

## 💡 一句话要点

**AnchorHOI：基于锚点的先验知识蒸馏实现零样本4D人-物交互生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `4D人-物交互生成` `零样本学习` `扩散模型` `先验知识蒸馏` `神经辐射场` `锚点` `运动合成`

## 📋 核心要点

1. 现有文本驱动4D HOI生成方法受限于大规模数据集的稀缺，泛化能力不足。
2. AnchorHOI利用图像和视频扩散模型，通过锚点先验蒸馏策略，指导4D HOI生成。
3. 实验表明，AnchorHOI在多样性和泛化性上优于现有方法，提升了生成质量。

## 📝 摘要（中文）

本文提出AnchorHOI框架，旨在解决大规模4D人-物交互(HOI)数据集稀缺导致的文本驱动4D HOI生成可扩展性受限问题。AnchorHOI通过结合视频扩散模型和图像扩散模型，充分利用混合先验知识，从而推进4D HOI生成。针对直接优化高维4D HOI带来的挑战，特别是人体姿态和组合运动方面，AnchorHOI引入了一种基于锚点的先验知识蒸馏策略。该策略构建交互感知的锚点，并利用这些锚点在可处理的两步过程中指导生成。具体而言，为4D HOI生成设计了两个定制锚点：用于表达交互组合的锚点神经辐射场(NeRFs)和用于真实运动合成的锚点关键点。大量实验表明，AnchorHOI优于以往方法，具有更好的多样性和泛化性。

## 🔬 方法详解

**问题定义**：现有文本驱动的4D人-物交互生成方法依赖于大规模的4D HOI数据集进行训练，但此类数据集的获取成本高昂且规模有限，导致模型在面对新的交互场景时泛化能力不足。此外，直接从文本生成复杂的4D HOI数据，特别是人体姿态和物体运动的组合，是一个极具挑战性的问题。

**核心思路**：AnchorHOI的核心思路是利用预训练的图像和视频扩散模型作为先验知识，通过锚点（anchors）来引导4D HOI的生成过程。这种方法避免了直接在高维空间中优化复杂的4D HOI数据，而是通过锚点将生成过程分解为更易于处理的步骤。锚点的设计需要能够捕捉交互的关键信息，并指导生成过程朝着更真实、更多样化的方向发展。

**技术框架**：AnchorHOI框架包含两个主要阶段：锚点生成阶段和基于锚点的生成阶段。在锚点生成阶段，首先根据文本描述构建交互感知的锚点，包括锚点NeRFs用于表达交互组合，以及锚点关键点用于真实运动合成。然后，在基于锚点的生成阶段，利用这些锚点作为先验知识，指导扩散模型生成最终的4D HOI数据。整个框架利用了图像和视频扩散模型的优势，并结合了锚点先验蒸馏策略，从而实现了零样本的4D HOI生成。

**关键创新**：AnchorHOI的关键创新在于提出了基于锚点的先验知识蒸馏策略。与以往直接利用扩散模型生成4D HOI数据的方法不同，AnchorHOI通过引入锚点，将复杂的生成过程分解为更易于控制的步骤。这种方法不仅降低了优化难度，还能够更好地利用预训练模型的先验知识，从而生成更真实、更多样化的4D HOI数据。此外，针对4D HOI生成，定制化设计了锚点NeRFs和锚点关键点，分别用于表达交互组合和真实运动合成。

**关键设计**：AnchorHOI的关键设计包括：1) 锚点NeRFs的设计，用于表达人与物体之间的交互关系，例如手握物体的方式、物体与身体的相对位置等。2) 锚点关键点的设计，用于捕捉人体运动的关键信息，例如关节的位置、运动轨迹等。3) 先验知识蒸馏策略，通过锚点将预训练扩散模型的先验知识传递到4D HOI生成过程中。4) 损失函数的设计，用于约束生成结果与锚点之间的关系，保证生成结果的真实性和一致性。具体的参数设置和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14095v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14095v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14095v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，AnchorHOI在零样本4D HOI生成任务中取得了显著的性能提升。与现有方法相比，AnchorHOI生成的4D HOI数据具有更高的真实性和多样性。通过定量评估和定性比较，证明了AnchorHOI在交互组合和运动合成方面的优势。具体的性能数据和对比基线在论文中有详细展示。

## 🎯 应用场景

AnchorHOI在虚拟现实、增强现实、游戏开发、机器人控制等领域具有广泛的应用前景。它可以用于生成逼真的人机交互场景，例如虚拟人物与虚拟物体的互动，从而提升用户体验。此外，AnchorHOI还可以用于训练机器人，使其能够更好地理解和执行人机交互任务。未来，该技术有望应用于更广泛的领域，例如智能家居、自动驾驶等。

## 📄 摘要（原文）

> Despite significant progress in text-driven 4D human-object interaction (HOI) generation with supervised methods, the scalability remains limited by the scarcity of large-scale 4D HOI datasets. To overcome this, recent approaches attempt zero-shot 4D HOI generation with pre-trained image diffusion models. However, interaction cues are minimally distilled during the generation process, restricting their applicability across diverse scenarios. In this paper, we propose AnchorHOI, a novel framework that thoroughly exploits hybrid priors by incorporating video diffusion models beyond image diffusion models, advancing 4D HOI generation. Nevertheless, directly optimizing high-dimensional 4D HOI with such priors remains challenging, particularly for human pose and compositional motion. To address this challenge, AnchorHOI introduces an anchor-based prior distillation strategy, which constructs interaction-aware anchors and then leverages them to guide generation in a tractable two-step process. Specifically, two tailored anchors are designed for 4D HOI generation: anchor Neural Radiance Fields (NeRFs) for expressive interaction composition, and anchor keypoints for realistic motion synthesis. Extensive experiments demonstrate that AnchorHOI outperforms previous methods with superior diversity and generalization.

