---
layout: default
title: Did you just see that? Arbitrary view synthesis for egocentric replay of operating room workflows from ambient sensors
---

# Did you just see that? Arbitrary view synthesis for egocentric replay of operating room workflows from ambient sensors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04802" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04802v1</a>
  <a href="https://arxiv.org/pdf/2510.04802.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04802v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.04802v1', 'Did you just see that? Arbitrary view synthesis for egocentric replay of operating room workflows from ambient sensors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Han Zhang, Lalithkumar Seenivasan, Jose L. Porras, Roger D. Soberanis-Mukul, Hao Ding, Hongchao Shu, Benjamin D. Killeen, Ankita Ghosh, Lonny Yarmus, Masaru Ishii, Angela Christine Argento, Mathias Unberath

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-06

---

## 💡 一句话要点

**EgoSurg：基于环境传感器，为手术室工作流程重建任意视角的自我中心回放。**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `神经渲染` `扩散模型` `自我中心视角` `手术室` `视图合成`

## 📋 核心要点

1. 现有手术观察依赖固定视角或回忆，缺乏记录临床决策的自我中心视角，限制了对手术安全、培训和流程优化的深入理解。
2. EgoSurg通过结合几何驱动的神经渲染和扩散模型增强，从固定摄像头视频重建手术人员的动态自我中心视角。
3. 实验结果表明，EgoSurg能够以高视觉质量和保真度重建个体的手术视野和任意视角，为手术数据分析提供新途径。

## 📝 摘要（中文）

本研究提出EgoSurg，一个从墙壁安装的固定摄像头视频中，为手术室(OR)工作人员重建动态的、自我中心回放的框架，无需干预临床工作流程。EgoSurg结合了几何驱动的神经渲染和基于扩散的视图增强，从而能够以高视觉保真度合成任意和自我中心的视角。在跨多地点手术案例和对照研究的评估中，EgoSurg以高视觉质量和保真度重建了特定人员的视野和任意视角。通过将现有的OR摄像头基础设施转变为可导航的动态3D记录，EgoSurg为沉浸式手术数据科学奠定了新的基础，使手术实践能够从各个角度进行可视化、体验和分析。

## 🔬 方法详解

**问题定义**：现有手术室观察方法主要依赖于固定摄像头或术后回忆，无法准确捕捉手术人员在手术过程中的真实视野，这对于理解手术决策过程、优化手术流程以及进行有效的手术培训构成了挑战。现有方法难以提供沉浸式、个性化的手术视角体验。

**核心思路**：EgoSurg的核心思路是利用手术室中已有的固定摄像头视频，通过神经渲染技术重建手术人员的自我中心视角。通过几何信息引导的神经渲染，初步生成视角图像，然后利用扩散模型进行图像增强，提高视觉质量和保真度。这样可以在不干扰手术流程的前提下，获得高质量的自我中心视角视频。

**技术框架**：EgoSurg框架主要包含两个阶段：几何驱动的神经渲染和基于扩散的视图增强。首先，利用多视角几何信息，估计手术室场景的3D结构和人员姿态。然后，基于估计的几何信息和人员姿态，使用神经渲染技术生成目标视角的图像。最后，使用基于扩散模型的图像增强模块，提高生成图像的视觉质量和真实感。

**关键创新**：EgoSurg的关键创新在于将几何驱动的神经渲染与扩散模型相结合，用于重建手术人员的自我中心视角。与传统的基于图像的渲染方法相比，EgoSurg利用几何信息提高了渲染的准确性和一致性。同时，扩散模型的使用显著提高了生成图像的视觉质量，使其更接近真实的手术场景。

**关键设计**：EgoSurg在几何驱动的神经渲染阶段，采用了可微分渲染技术，使得整个框架可以进行端到端的训练。在扩散模型增强阶段，使用了预训练的扩散模型，并针对手术场景进行了微调，以提高生成图像的真实感。损失函数包括渲染损失、几何一致性损失和对抗损失，以保证生成图像的质量和几何准确性。

## 📊 实验亮点

EgoSurg在多地点手术案例和对照研究中进行了评估，结果表明其能够以高视觉质量和保真度重建个体的手术视野和任意视角。具体而言，EgoSurg在主观视觉质量评估中显著优于传统方法，并且在几何准确性方面也取得了显著提升。实验结果证明了EgoSurg在重建自我中心视角方面的有效性和优越性。

## 🎯 应用场景

EgoSurg可应用于手术培训、手术流程优化、手术安全分析等领域。通过提供沉浸式的自我中心视角，EgoSurg可以帮助医生和护士更好地理解手术过程，提高手术技能。此外，EgoSurg还可以用于分析手术流程中的潜在风险，从而提高手术安全性。未来，EgoSurg有望成为手术数据科学的重要组成部分。

## 📄 摘要（原文）

> Observing surgical practice has historically relied on fixed vantage points or recollections, leaving the egocentric visual perspectives that guide clinical decisions undocumented. Fixed-camera video can capture surgical workflows at the room-scale, but cannot reconstruct what each team member actually saw. Thus, these videos only provide limited insights into how decisions that affect surgical safety, training, and workflow optimization are made. Here we introduce EgoSurg, the first framework to reconstruct the dynamic, egocentric replays for any operating room (OR) staff directly from wall-mounted fixed-camera video, and thus, without intervention to clinical workflow. EgoSurg couples geometry-driven neural rendering with diffusion-based view enhancement, enabling high-visual fidelity synthesis of arbitrary and egocentric viewpoints at any moment. In evaluation across multi-site surgical cases and controlled studies, EgoSurg reconstructs person-specific visual fields and arbitrary viewpoints with high visual quality and fidelity. By transforming existing OR camera infrastructure into a navigable dynamic 3D record, EgoSurg establishes a new foundation for immersive surgical data science, enabling surgical practice to be visualized, experienced, and analyzed from every angle.

