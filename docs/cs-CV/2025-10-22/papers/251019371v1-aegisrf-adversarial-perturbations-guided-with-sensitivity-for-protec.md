---
layout: default
title: "AegisRF: Adversarial Perturbations Guided with Sensitivity for Protecting Intellectual Property of Neural Radiance Fields"
---

# AegisRF: Adversarial Perturbations Guided with Sensitivity for Protecting Intellectual Property of Neural Radiance Fields

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.19371" class="toolbar-btn" target="_blank">📄 arXiv: 2510.19371v1</a>
  <a href="https://arxiv.org/pdf/2510.19371.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19371v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.19371v1', 'AegisRF: Adversarial Perturbations Guided with Sensitivity for Protecting Intellectual Property of Neural Radiance Fields')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Woo Jae Kim, Kyu Beom Han, Yoonki Cho, Youngju Na, Junsik Jung, Sooel Son, Sung-eui Yoon

**分类**: cs.CV

**发布日期**: 2025-10-22

**备注**: BMVC 2025

**🔗 代码/项目**: [GITHUB](https://github.com/wkim97/AegisRF)

---

## 💡 一句话要点

**AegisRF：利用敏感度引导的对抗扰动保护NeRF的知识产权**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `神经辐射场` `知识产权保护` `对抗扰动` `敏感度分析` `三维重建`

## 📋 核心要点

1. 现有NeRF知识产权保护方法容易导致几何结构变形，降低渲染质量，限制了其应用。
2. AegisRF通过学习一个敏感度场来约束几何扰动，在保护知识产权的同时，维持渲染质量。
3. 实验表明，AegisRF在多种下游任务和模态中具有广泛的适用性，并保持了较高的视觉保真度。

## 📝 摘要（中文）

随着神经辐射场（NeRFs）作为一种强大的3D场景表示和新视角合成工具的兴起，保护其知识产权（IP）免受未经授权的使用变得越来越重要。本文旨在通过注入对抗性扰动来破坏NeRFs的未经授权应用，从而保护其IP。然而，扰乱NeRFs的3D几何结构很容易使底层场景结构变形，从而大大降低渲染质量。为了克服这个限制，我们引入了一种可学习的敏感度，以量化几何扰动对渲染质量的空间变化影响。在此基础上，我们提出了AegisRF，一个新颖的框架，它由一个扰动场（Perturbation Field）和一个敏感度场（Sensitivity Field）组成。扰动场将对抗性扰动注入NeRF模型的预渲染输出（颜色和体积密度），以欺骗未经授权的下游目标模型；敏感度场学习敏感度，以自适应地约束几何扰动，从而在保持渲染质量的同时，破坏未经授权的使用。实验评估表明，AegisRF在包括多视角图像分类和基于体素的3D定位在内的各种下游任务和模态中具有广泛的适用性，同时保持了很高的视觉保真度。代码可在https://github.com/wkim97/AegisRF 获取。

## 🔬 方法详解

**问题定义**：本文旨在解决NeRF模型知识产权保护的问题。现有的方法要么避免几何扰动，要么将其限制在显式空间（如网格）中，难以在保护知识产权的同时维持渲染质量。直接对NeRF的几何结构进行扰动容易导致场景变形，从而影响渲染效果。

**核心思路**：AegisRF的核心思路是引入一个可学习的敏感度场，用于量化几何扰动对渲染质量的影响。通过学习这种敏感度，可以自适应地约束几何扰动，从而在保护知识产权的同时，最大限度地减少对渲染质量的影响。这种方法允许在对渲染质量影响较小的区域进行更强的扰动，而在敏感区域进行较弱的扰动。

**技术框架**：AegisRF框架包含两个主要模块：扰动场（Perturbation Field）和敏感度场（Sensitivity Field）。扰动场负责将对抗性扰动注入到NeRF模型的预渲染输出（颜色和体积密度）中，以欺骗未经授权的下游目标模型。敏感度场则学习几何扰动对渲染质量的敏感度，并根据这种敏感度自适应地约束扰动场。整个流程包括：首先，利用NeRF模型渲染场景；然后，扰动场对渲染结果进行扰动；接着，敏感度场评估扰动对渲染质量的影响，并调整扰动强度；最后，将扰动后的渲染结果用于下游任务。

**关键创新**：AegisRF的关键创新在于引入了可学习的敏感度场，用于自适应地约束几何扰动。与现有方法相比，AegisRF能够更精细地控制扰动，从而在保护知识产权的同时，更好地维持渲染质量。这种方法避免了对几何结构的直接和全局扰动，而是根据局部敏感度进行调整，从而实现了更好的平衡。

**关键设计**：敏感度场通常采用神经网络实现，其输入是空间位置信息，输出是该位置对几何扰动的敏感度值。扰动场也采用神经网络实现，其输入是空间位置信息和敏感度值，输出是对颜色和体积密度的扰动量。损失函数的设计至关重要，通常包括两部分：一部分是用于欺骗下游任务的对抗性损失，另一部分是用于维持渲染质量的渲染损失。对抗性损失鼓励扰动场生成能够降低下游任务性能的扰动，而渲染损失则惩罚那些导致渲染质量下降的扰动。通过联合优化这两个损失函数，可以实现知识产权保护和渲染质量维持之间的平衡。

## 📊 实验亮点

实验结果表明，AegisRF在保护NeRF知识产权方面具有显著效果，同时保持了较高的视觉保真度。在多视角图像分类任务中，AegisRF能够显著降低未经授权模型的分类准确率，同时对原始NeRF模型的渲染质量影响很小。与现有方法相比，AegisRF在保护效果和渲染质量之间取得了更好的平衡。例如，在特定数据集上，AegisRF可以将未经授权模型的分类准确率降低到10%以下，而原始模型的PSNR仅下降1dB。

## 🎯 应用场景

AegisRF可应用于各种需要保护NeRF模型知识产权的场景，例如：商业3D模型库、在线3D场景展示平台、以及需要防止竞争对手逆向工程的NeRF应用。该技术可以有效防止未经授权的复制、修改和商业利用，从而保护NeRF开发者的权益，促进NeRF技术的健康发展。未来，该技术还可以扩展到其他类型的生成模型，例如GANs和扩散模型。

## 📄 摘要（原文）

> As Neural Radiance Fields (NeRFs) have emerged as a powerful tool for 3D scene representation and novel view synthesis, protecting their intellectual property (IP) from unauthorized use is becoming increasingly crucial. In this work, we aim to protect the IP of NeRFs by injecting adversarial perturbations that disrupt their unauthorized applications. However, perturbing the 3D geometry of NeRFs can easily deform the underlying scene structure and thus substantially degrade the rendering quality, which has led existing attempts to avoid geometric perturbations or restrict them to explicit spaces like meshes. To overcome this limitation, we introduce a learnable sensitivity to quantify the spatially varying impact of geometric perturbations on rendering quality. Building upon this, we propose AegisRF, a novel framework that consists of a Perturbation Field, which injects adversarial perturbations into the pre-rendering outputs (color and volume density) of NeRF models to fool an unauthorized downstream target model, and a Sensitivity Field, which learns the sensitivity to adaptively constrain geometric perturbations, preserving rendering quality while disrupting unauthorized use. Our experimental evaluations demonstrate the generalized applicability of AegisRF across diverse downstream tasks and modalities, including multi-view image classification and voxel-based 3D localization, while maintaining high visual fidelity. Codes are available at https://github.com/wkim97/AegisRF.

