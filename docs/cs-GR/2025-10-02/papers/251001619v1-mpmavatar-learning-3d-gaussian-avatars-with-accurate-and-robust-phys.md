---
layout: default
title: MPMAvatar: Learning 3D Gaussian Avatars with Accurate and Robust Physics-Based Dynamics
---

# MPMAvatar: Learning 3D Gaussian Avatars with Accurate and Robust Physics-Based Dynamics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01619" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01619v1</a>
  <a href="https://arxiv.org/pdf/2510.01619.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01619v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01619v1', 'MPMAvatar: Learning 3D Gaussian Avatars with Accurate and Robust Physics-Based Dynamics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changmin Lee, Jihyun Lee, Tae-Kyun Kim

**分类**: cs.GR, cs.CV

**发布日期**: 2025-10-02

**备注**: Accepted to NeurIPS 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://KAISTChangmin.github.io/MPMAvatar/)

---

## 💡 一句话要点

**MPMAvatar：提出基于物理的精确鲁棒3D高斯Avatar学习框架**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `3D Avatar` `物理模拟` `Material Point Method` `高斯溅射` `服装动态` `多视角重建` `虚拟现实`

## 📋 核心要点

1. 现有方法在模拟人体及其宽松服装的物理动态方面存在精度和鲁棒性不足的挑战。
2. MPMAvatar利用Material Point Method模拟器，结合各向异性模型和碰撞处理，实现精确的服装动态模拟。
3. 实验证明MPMAvatar在动力学和渲染精度、鲁棒性及效率上优于现有技术，并能零样本泛化到新的交互。

## 📝 摘要（中文）

本文提出MPMAvatar，一个从多视角视频创建3D人体Avatar的框架，它支持高度真实、鲁棒的动画，以及自由视角的照片级渲染。为了实现精确和鲁棒的动力学建模，核心思想是使用基于Material Point Method (MPM) 的模拟器，通过结合各向异性本构模型和新颖的碰撞处理算法，精心定制该模拟器以模拟具有复杂变形的服装以及与底层身体的接触。将此动力学建模方案与使用具有准阴影的3D高斯溅射渲染的规范Avatar相结合，从而为物理上逼真的动画实现高保真渲染。实验表明，MPMAvatar在动力学建模精度、渲染精度以及鲁棒性和效率方面显著优于现有的最先进的基于物理的Avatar。此外，本文还展示了一个新颖的应用，Avatar可以以零样本方式推广到未见过的交互，这对于以前基于学习的方法来说是无法实现的，因为它们具有有限的模拟泛化能力。

## 🔬 方法详解

**问题定义**：现有基于视觉观测的3D Avatar创建方法在模拟具有宽松服装的人体物理动态方面存在困难，精度和鲁棒性不足，难以泛化到新的动画输入。

**核心思路**：利用Material Point Method (MPM) 模拟器来精确建模服装的物理动态。MPM能够有效处理复杂形变和碰撞，通过定制化的MPM模拟器，可以更真实地模拟服装与人体之间的交互。结合高斯溅射渲染，实现逼真的渲染效果。

**技术框架**：MPMAvatar框架包含以下几个主要模块：1) 多视角视频输入；2) 基于MPM的物理模拟器，用于模拟服装的动态；3) 3D高斯溅射渲染器，用于生成逼真的渲染图像；4) 规范Avatar模型，作为物理模拟的基础。整体流程是从多视角视频中重建规范Avatar，然后使用MPM模拟器模拟服装的动态，最后使用高斯溅射渲染器渲染最终的Avatar动画。

**关键创新**：1) 将Material Point Method引入到3D Avatar的服装动态模拟中，能够更精确地处理服装的复杂形变和碰撞。2) 结合各向异性本构模型和新颖的碰撞处理算法，进一步提升了物理模拟的精度和鲁棒性。3) 使用3D高斯溅射渲染，实现了高保真度的渲染效果。与现有方法相比，MPMAvatar在动力学建模和渲染方面都取得了显著的提升。

**关键设计**：在MPM模拟器中，使用了各向异性本构模型来更准确地描述服装材料的特性。设计了一种新的碰撞处理算法，以避免模拟过程中出现穿透现象。在渲染方面，使用了准阴影技术来增强渲染的真实感。损失函数的设计目标是最小化重建误差、物理模拟误差和渲染误差。

## 📊 实验亮点

MPMAvatar在动力学建模精度、渲染精度以及鲁棒性和效率方面显著优于现有技术。实验结果表明，MPMAvatar能够生成更真实的服装动态效果，并且能够以零样本方式泛化到未见过的交互，这对于以前基于学习的方法来说是无法实现的。具体性能数据未知，但摘要强调了显著的性能提升。

## 🎯 应用场景

MPMAvatar可应用于虚拟现实、增强现实、游戏、电影制作等领域，创建逼真且可交互的虚拟角色。该技术能够模拟服装的真实物理行为，提升用户体验，并为服装设计和虚拟试穿提供新的工具。未来，该技术有望应用于远程协作、虚拟化身等更广泛的场景。

## 📄 摘要（原文）

> While there has been significant progress in the field of 3D avatar creation from visual observations, modeling physically plausible dynamics of humans with loose garments remains a challenging problem. Although a few existing works address this problem by leveraging physical simulation, they suffer from limited accuracy or robustness to novel animation inputs. In this work, we present MPMAvatar, a framework for creating 3D human avatars from multi-view videos that supports highly realistic, robust animation, as well as photorealistic rendering from free viewpoints. For accurate and robust dynamics modeling, our key idea is to use a Material Point Method-based simulator, which we carefully tailor to model garments with complex deformations and contact with the underlying body by incorporating an anisotropic constitutive model and a novel collision handling algorithm. We combine this dynamics modeling scheme with our canonical avatar that can be rendered using 3D Gaussian Splatting with quasi-shadowing, enabling high-fidelity rendering for physically realistic animations. In our experiments, we demonstrate that MPMAvatar significantly outperforms the existing state-of-the-art physics-based avatar in terms of (1) dynamics modeling accuracy, (2) rendering accuracy, and (3) robustness and efficiency. Additionally, we present a novel application in which our avatar generalizes to unseen interactions in a zero-shot manner-which was not achievable with previous learning-based methods due to their limited simulation generalizability. Our project page is at: https://KAISTChangmin.github.io/MPMAvatar/

