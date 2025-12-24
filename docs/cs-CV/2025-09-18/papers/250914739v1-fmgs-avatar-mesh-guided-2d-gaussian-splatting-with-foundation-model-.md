---
layout: default
title: "FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction"
---

# FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14739" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14739v1</a>
  <a href="https://arxiv.org/pdf/2509.14739.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14739v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14739v1', 'FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinlong Fan, Bingyu Hu, Xingguang Li, Yuxiang Yang, Jing Zhang

**分类**: cs.CV

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**FMGS-Avatar：利用基础模型先验的网格引导2D高斯溅射单目3D人像重建**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D人像重建` `单目视频` `高斯溅射` `基础模型` `网格引导`

## 📋 核心要点

1. 单目视频三维人像重建面临几何信息不足的挑战，现有3D高斯溅射方法难以保持表面细节。
2. 提出FMGS-Avatar，通过网格引导2D高斯溅射增强表面对齐和细节保持，并利用基础模型先验知识。
3. 实验表明，该方法在几何精度和外观保真度方面优于现有方法，并实现了时空一致的渲染。

## 📝 摘要（中文）

从单目视频重建高保真可动画的人体化身仍然具有挑战性，因为单视角观测中缺乏足够的几何信息。虽然最近的3D高斯溅射方法显示出潜力，但由于3D高斯原语的自由形式性质，它们在表面细节保持方面存在困难。为了解决表示限制和信息稀缺问题，我们提出了一种新方法FMGS-Avatar，该方法集成了两项关键创新。首先，我们引入了网格引导的2D高斯溅射，其中2D高斯原语直接附加到具有约束的位置、旋转和运动的模板网格面上，从而实现卓越的表面对齐和几何细节保持。其次，我们利用在大型数据集（如Sapiens）上训练的基础模型来补充来自单目视频的有限视觉线索。然而，当从基础模型中提取多模态先验知识时，由于不同的模态表现出不同的参数敏感性，可能会出现冲突的优化目标。我们通过选择性梯度隔离的协调训练策略来解决这个问题，使每个损失分量能够优化其相关参数而不受干扰。通过增强的表示和协调的信息提取的结合，我们的方法显着推进了3D单目人体化身重建。实验评估表明，与现有方法相比，重建质量更高，在几何精度和外观保真度方面有显着提高，同时提供丰富的语义信息。此外，在共享规范空间中提取的先验知识自然地实现了新视角和姿势下空间和时间上一致的渲染。

## 🔬 方法详解

**问题定义**：论文旨在解决从单目视频中重建高保真、可动画的3D人体化身的问题。现有方法，特别是基于3D高斯溅射的方法，虽然在神经渲染方面取得了进展，但由于单目视频缺乏足够的几何信息，以及3D高斯原语的自由形式特性，难以保持重建人像的表面细节和几何精度。

**核心思路**：论文的核心思路是结合模板网格的几何约束和基础模型提供的先验知识，来指导2D高斯溅射过程。通过将2D高斯原语附加到模板网格面上，可以更好地对齐表面并保留几何细节。同时，利用在大型数据集上训练的基础模型，可以补充单目视频中缺失的视觉信息，从而提高重建质量。

**技术框架**：FMGS-Avatar的整体框架包括以下几个主要模块：1) **模板网格初始化**：使用预训练的3D人体模型作为模板网格。2) **网格引导的2D高斯溅射**：将2D高斯原语附加到模板网格的每个面上，并约束其位置、旋转和运动。3) **基础模型先验**：利用在大型数据集上训练的基础模型，提取多模态先验知识，例如形状、纹理和语义信息。4) **协调训练**：设计一种协调训练策略，通过选择性梯度隔离，解决不同模态之间的优化冲突。5) **渲染**：使用渲染模块将2D高斯原语渲染成图像。

**关键创新**：该方法的主要创新点在于：1) **网格引导的2D高斯溅射**：通过将2D高斯原语附加到模板网格面上，实现了更好的表面对齐和几何细节保持。2) **基础模型先验的利用**：利用在大型数据集上训练的基础模型，补充了单目视频中缺失的视觉信息。3) **协调训练策略**：通过选择性梯度隔离，解决了不同模态之间的优化冲突，提高了训练效率和重建质量。

**关键设计**：在网格引导的2D高斯溅射中，论文设计了约束2D高斯原语位置、旋转和运动的损失函数。在基础模型先验的利用中，论文使用了Sapiens数据集训练的基础模型，并设计了多模态损失函数，例如形状损失、纹理损失和语义损失。为了解决不同模态之间的优化冲突，论文设计了一种选择性梯度隔离的协调训练策略，即在训练过程中，只允许每个损失分量优化其相关的参数，从而避免了不同模态之间的干扰。

## 📊 实验亮点

实验结果表明，FMGS-Avatar在几何精度和外观保真度方面均优于现有方法。与基线方法相比，该方法在重建人像的表面细节和几何结构方面有显著提升，并且能够生成时空一致的渲染结果。此外，该方法还能够提供丰富的语义信息，例如人脸表情和身体姿态。

## 🎯 应用场景

该研究成果可应用于虚拟现实、增强现实、游戏、电影制作等领域，实现高质量的3D人体化身重建和动画。例如，用户可以通过单目摄像头创建自己的虚拟形象，并将其应用于虚拟社交、在线会议等场景。未来，该技术有望进一步发展，实现更加逼真和个性化的3D人像重建。

## 📄 摘要（原文）

> Reconstructing high-fidelity animatable human avatars from monocular videos remains challenging due to insufficient geometric information in single-view observations. While recent 3D Gaussian Splatting methods have shown promise, they struggle with surface detail preservation due to the free-form nature of 3D Gaussian primitives. To address both the representation limitations and information scarcity, we propose a novel method, \textbf{FMGS-Avatar}, that integrates two key innovations. First, we introduce Mesh-Guided 2D Gaussian Splatting, where 2D Gaussian primitives are attached directly to template mesh faces with constrained position, rotation, and movement, enabling superior surface alignment and geometric detail preservation. Second, we leverage foundation models trained on large-scale datasets, such as Sapiens, to complement the limited visual cues from monocular videos. However, when distilling multi-modal prior knowledge from foundation models, conflicting optimization objectives can emerge as different modalities exhibit distinct parameter sensitivities. We address this through a coordinated training strategy with selective gradient isolation, enabling each loss component to optimize its relevant parameters without interference. Through this combination of enhanced representation and coordinated information distillation, our approach significantly advances 3D monocular human avatar reconstruction. Experimental evaluation demonstrates superior reconstruction quality compared to existing methods, with notable gains in geometric accuracy and appearance fidelity while providing rich semantic information. Additionally, the distilled prior knowledge within a shared canonical space naturally enables spatially and temporally consistent rendering under novel views and poses.

