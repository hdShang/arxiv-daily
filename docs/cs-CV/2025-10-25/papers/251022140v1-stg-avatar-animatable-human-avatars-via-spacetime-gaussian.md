---
layout: default
title: "STG-Avatar: Animatable Human Avatars via Spacetime Gaussian"
---

# STG-Avatar: Animatable Human Avatars via Spacetime Gaussian

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22140" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22140v1</a>
  <a href="https://arxiv.org/pdf/2510.22140.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22140v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.22140v1', 'STG-Avatar: Animatable Human Avatars via Spacetime Gaussian')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangan Jiang, Tianzi Zhang, Dong Li, Zhenjun Zhao, Haoang Li, Mingrui Li, Hongyu Wang

**分类**: cs.CV

**发布日期**: 2025-10-25

**备注**: Accepted by the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 2025

**🔗 代码/项目**: [GITHUB](https://github.com/jiangguangan/STG-Avatar)

---

## 💡 一句话要点

**提出STG-Avatar，通过时空高斯优化实现高保真可动画人体化身重建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `人体化身` `3D高斯` `时空高斯` `线性混合蒙皮` `非刚性形变` `光流` `实时渲染`

## 📋 核心要点

1. 现有3DGS人体化身方法难以准确捕捉服装形变和快速运动肢体等细节。
2. STG-Avatar结合LBS的实时控制和STG的时空自适应优化，实现高保真重建。
3. 利用光流引导高动态区域的3D高斯密集化，提升动态区域的重建质量。

## 📝 摘要（中文）

本文提出STG-Avatar，一个基于3D高斯（3DGS）框架，用于高保真可动画人体化身重建。现有基于3DGS的人体化身方法难以准确表示非刚性物体（如服装形变）和动态区域（如快速移动的肢体）的细节特征。为了解决这些挑战，STG-Avatar引入了一种刚性-非刚性耦合的形变框架，将时空高斯（STG）与线性混合蒙皮（LBS）相结合。在该混合设计中，LBS通过驱动全局姿态变换实现实时骨骼控制，而STG通过时空自适应优化3D高斯来补充LBS的不足。此外，我们利用光流来识别高动态区域，并指导这些区域中3D高斯的自适应密集化。实验结果表明，我们的方法在重建质量和运算效率方面始终优于最先进的基线方法，在保持实时渲染能力的同时，实现了卓越的定量指标。

## 🔬 方法详解

**问题定义**：现有基于3D高斯的人体化身重建方法在处理非刚性形变（例如服装的褶皱和摆动）以及快速运动区域（例如快速挥动的手臂）时，难以捕捉到精细的细节。这些方法通常无法在重建质量和计算效率之间取得良好的平衡，难以实现高质量的实时渲染。

**核心思路**：STG-Avatar的核心思路是将传统的线性混合蒙皮（LBS）方法与时空高斯（STG）表示相结合，形成一种刚性-非刚性耦合的形变框架。LBS负责处理全局的、刚性的姿态变换，而STG则负责捕捉局部的、非刚性的形变细节。通过这种混合表示，可以充分利用LBS的实时性和STG的表达能力，从而实现高质量的实时人体化身重建。

**技术框架**：STG-Avatar的整体框架包含以下几个主要模块：1) 基于单目视频的人体姿态估计；2) 基于LBS的骨骼驱动；3) 基于STG的非刚性形变建模；4) 基于光流的动态区域检测与高斯密集化；5) 渲染模块。首先，从单目视频中估计人体姿态，并利用LBS驱动骨骼运动。然后，利用STG对非刚性形变进行建模，并根据光流检测到的动态区域进行高斯密集化。最后，通过渲染模块生成最终的人体化身图像。

**关键创新**：STG-Avatar的关键创新在于刚性-非刚性耦合的形变框架，以及基于光流的动态区域自适应高斯密集化策略。与传统的仅使用LBS或仅使用神经隐式表示的方法相比，STG-Avatar能够更好地平衡重建质量和计算效率。基于光流的动态区域自适应高斯密集化策略能够有效地提升动态区域的重建质量，从而避免了过度密集化带来的计算负担。

**关键设计**：在STG-Avatar中，关键的设计包括：1) STG的参数化方式，例如高斯分布的均值、方差、颜色等；2) LBS与STG的融合方式，例如如何将LBS的形变信息传递给STG；3) 光流的计算方式和动态区域的判断阈值；4) 高斯密集化的策略，例如何时进行高斯分裂、合并等。损失函数的设计也至关重要，通常包括重建损失、正则化损失等。

## 📊 实验亮点

实验结果表明，STG-Avatar在重建质量和运算效率方面均优于现有方法。在定量指标上，STG-Avatar在多个数据集上取得了state-of-the-art的结果。在定性结果上，STG-Avatar能够重建出更加精细的服装细节和动态区域，并且能够实现实时的渲染。

## 🎯 应用场景

STG-Avatar在人机交互、虚拟现实、增强现实、数字内容创作等领域具有广泛的应用前景。它可以用于创建逼真的虚拟化身，从而提升用户在虚拟环境中的沉浸感和交互体验。此外，STG-Avatar还可以用于远程呈现、虚拟会议、游戏开发等场景，为用户提供更加自然和高效的交流方式。

## 📄 摘要（原文）

> Realistic animatable human avatars from monocular videos are crucial for advancing human-robot interaction and enhancing immersive virtual experiences. While recent research on 3DGS-based human avatars has made progress, it still struggles with accurately representing detailed features of non-rigid objects (e.g., clothing deformations) and dynamic regions (e.g., rapidly moving limbs). To address these challenges, we present STG-Avatar, a 3DGS-based framework for high-fidelity animatable human avatar reconstruction. Specifically, our framework introduces a rigid-nonrigid coupled deformation framework that synergistically integrates Spacetime Gaussians (STG) with linear blend skinning (LBS). In this hybrid design, LBS enables real-time skeletal control by driving global pose transformations, while STG complements it through spacetime adaptive optimization of 3D Gaussians. Furthermore, we employ optical flow to identify high-dynamic regions and guide the adaptive densification of 3D Gaussians in these regions. Experimental results demonstrate that our method consistently outperforms state-of-the-art baselines in both reconstruction quality and operational efficiency, achieving superior quantitative metrics while retaining real-time rendering capabilities. Our code is available at https://github.com/jiangguangan/STG-Avatar

