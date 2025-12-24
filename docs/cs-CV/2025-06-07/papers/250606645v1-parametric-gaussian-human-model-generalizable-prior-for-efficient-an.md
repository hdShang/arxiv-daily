---
layout: default
title: "Parametric Gaussian Human Model: Generalizable Prior for Efficient and Realistic Human Avatar Modeling"
---

# Parametric Gaussian Human Model: Generalizable Prior for Efficient and Realistic Human Avatar Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06645" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06645v1</a>
  <a href="https://arxiv.org/pdf/2506.06645.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06645v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06645v1', 'Parametric Gaussian Human Model: Generalizable Prior for Efficient and Realistic Human Avatar Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cheng Peng, Jingxiang Sun, Yushuo Chen, Zhaoqi Su, Zhuo Su, Yebin Liu

**分类**: cs.CV

**发布日期**: 2025-06-07

**备注**: Project Page: https://pengc02.github.io/pghm/

---

## 💡 一句话要点

**提出参数化高斯人模型以解决单目视频头像重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `高斯模型` `人类头像` `单目视频` `虚拟现实` `增强现实` `头像重建` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有方法在个体优化上耗时较长，并且在稀疏单目输入下泛化能力不足。
2. 提出的PGHM框架通过引入人类先验知识，实现了高效的单目视频头像重建。
3. 实验结果显示，PGHM在效率上显著优于传统方法，每个主体仅需约20分钟即可生成高质量头像。

## 📝 摘要（中文）

逼真且可动画的人类头像是虚拟现实、增强现实、远程呈现和数字娱乐的关键。尽管3D高斯点云技术在渲染质量和效率上取得了显著进展，但现有方法仍面临个体优化耗时和在稀疏单目输入下泛化能力差等挑战。本文提出了参数化高斯人模型（PGHM），该框架将人类先验知识整合到3D高斯点云中，实现了从单目视频快速高保真头像重建。PGHM引入了两个核心组件：UV对齐的潜在身份图和解耦的多头U-Net，能够在复杂姿态和视角下保持渲染质量，同时无需多视角捕捉或长时间优化。实验表明，PGHM的效率显著高于从头优化的方法，每个主体仅需约20分钟即可生成视觉质量相当的头像，展示了其在现实单目头像创建中的实际应用潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决从单目视频中高效重建逼真头像的问题。现有方法在个体优化上耗时较长，并且在稀疏单目输入下的泛化能力较差，限制了其实际应用。

**核心思路**：PGHM框架通过引入UV对齐的潜在身份图和解耦的多头U-Net，整合人类先验知识，从而实现快速且高保真的头像重建。这样的设计使得在复杂姿态和视角下仍能保持良好的渲染质量。

**技术框架**：PGHM的整体架构包括两个主要模块：UV对齐的潜在身份图用于编码个体几何和外观信息，解耦的多头U-Net用于预测高斯属性。该框架通过条件解码器分解静态、姿态依赖和视角依赖的组件。

**关键创新**：PGHM的核心创新在于其将人类先验知识与3D高斯点云技术结合，显著提高了头像重建的效率和质量。这与传统方法相比，减少了对多视角捕捉和长时间优化的依赖。

**关键设计**：在设计中，UV对齐的潜在身份图被用作可学习的特征张量，解耦的多头U-Net通过条件解码器来预测高斯属性，确保在不同姿态和视角下的渲染质量。

## 📊 实验亮点

实验结果表明，PGHM在头像生成效率上显著优于传统的从头优化方法，每个主体仅需约20分钟即可生成视觉质量相当的头像，展示了其在实际应用中的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实、远程呈现和数字娱乐等。通过提供高效且高保真的人类头像重建，PGHM可以在游戏、影视制作和在线社交等多个场景中发挥重要作用，提升用户体验和交互质量。

## 📄 摘要（原文）

> Photorealistic and animatable human avatars are a key enabler for virtual/augmented reality, telepresence, and digital entertainment. While recent advances in 3D Gaussian Splatting (3DGS) have greatly improved rendering quality and efficiency, existing methods still face fundamental challenges, including time-consuming per-subject optimization and poor generalization under sparse monocular inputs. In this work, we present the Parametric Gaussian Human Model (PGHM), a generalizable and efficient framework that integrates human priors into 3DGS for fast and high-fidelity avatar reconstruction from monocular videos. PGHM introduces two core components: (1) a UV-aligned latent identity map that compactly encodes subject-specific geometry and appearance into a learnable feature tensor; and (2) a disentangled Multi-Head U-Net that predicts Gaussian attributes by decomposing static, pose-dependent, and view-dependent components via conditioned decoders. This design enables robust rendering quality under challenging poses and viewpoints, while allowing efficient subject adaptation without requiring multi-view capture or long optimization time. Experiments show that PGHM is significantly more efficient than optimization-from-scratch methods, requiring only approximately 20 minutes per subject to produce avatars with comparable visual quality, thereby demonstrating its practical applicability for real-world monocular avatar creation.

