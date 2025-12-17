---
layout: default
title: VGD: Visual Geometry Gaussian Splatting for Feed-Forward Surround-view Driving Reconstruction
---

# VGD: Visual Geometry Gaussian Splatting for Feed-Forward Surround-view Driving Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.19578" class="toolbar-btn" target="_blank">📄 arXiv: 2510.19578v1</a>
  <a href="https://arxiv.org/pdf/2510.19578.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19578v1" onclick="toggleFavorite(this, '2510.19578v1', 'VGD: Visual Geometry Gaussian Splatting for Feed-Forward Surround-view Driving Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junhong Lin, Kangli Wang, Shunzhou Wang, Songlin Fan, Ge Li, Wei Gao

**分类**: cs.CV

**发布日期**: 2025-10-22

**备注**: 10 pages, 7 figures

---

## 💡 一句话要点

**VGD：用于前馈环视驾驶场景重建的视觉几何高斯溅射**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `环视重建` `自动驾驶` `高斯溅射` `几何学习` `新视角合成`

## 📋 核心要点

1. 现有环视自动驾驶场景重建方法难以在新视角下保证几何一致性和重建质量，尤其是在重叠区域较小的情况下。
2. VGD通过显式学习几何信息，并利用这些特征指导新视角语义质量的提升，从而解决上述问题。
3. 实验结果表明，VGD在nuScenes数据集上显著优于现有方法，验证了其可扩展性和高保真重建能力。

## 📝 摘要（中文）

本文提出了一种前馈环视自动驾驶场景重建方法，旨在实现快速且泛化性强的推理，其核心挑战在于保证泛化性的同时提升新视角的重建质量。针对环视图像重叠区域小的问题，现有方法难以保证新视角的几何一致性和重建质量。为此，我们认为必须显式地学习几何信息，并利用这些特征来指导新视角语义质量的提升。我们提出了视觉高斯驾驶（VGD），一种新颖的前馈端到端学习框架来解决这一挑战。为了实现可泛化的几何估计，我们设计了一个轻量级的VGGT变体，以有效地将预训练VGGT的几何先验知识提炼到几何分支中。此外，我们设计了一个高斯头，融合多尺度几何tokens来预测新视角渲染的高斯参数，该高斯头与几何分支共享相同的patch backbone。最后，我们整合来自几何分支和高斯头分支的多尺度特征，共同监督语义细化模型，通过特征一致性学习优化渲染质量。在nuScenes上的实验表明，我们的方法在各种设置下，在客观指标和主观质量方面均显著优于最先进的方法，验证了VGD的可扩展性和高保真环视重建能力。

## 🔬 方法详解

**问题定义**：论文旨在解决前馈环视自动驾驶场景重建中，如何在保证泛化性的前提下，提升新视角的重建质量和几何一致性的问题。现有方法由于环视图像的重叠区域小，难以在新视角下维持几何一致性，导致重建质量下降。

**核心思路**：论文的核心思路是显式地学习几何信息，并将这些几何信息作为先验知识，指导新视角的语义质量提升。通过学习几何信息，可以更好地理解场景结构，从而提高新视角的重建质量和几何一致性。

**技术框架**：VGD框架包含三个主要模块：几何分支、高斯头和语义细化模型。几何分支负责提取几何特征，高斯头利用几何特征预测高斯参数，语义细化模型则整合几何和高斯头的信息，优化最终的渲染质量。整个框架采用端到端的前馈方式进行训练。

**关键创新**：论文的关键创新在于显式地学习几何信息，并将其融入到新视角的渲染过程中。具体来说，通过轻量级的VGGT变体提取几何特征，并设计高斯头预测高斯参数，从而实现高质量的新视角渲染。此外，特征一致性学习也进一步提升了渲染质量。

**关键设计**：几何分支采用轻量级的VGGT变体，从预训练的VGGT中蒸馏几何先验知识。高斯头融合多尺度几何tokens，预测高斯参数。语义细化模型整合几何分支和高斯头的多尺度特征，通过特征一致性学习优化渲染质量。损失函数包括几何损失、渲染损失和特征一致性损失。

## 📊 实验亮点

VGD在nuScenes数据集上取得了显著的性能提升，在客观指标和主观质量上均优于现有方法。实验结果表明，VGD能够生成更清晰、更逼真的新视角图像，并且具有更好的几何一致性。具体提升幅度在论文中进行了详细的量化。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、虚拟现实等领域。通过高质量的环视场景重建，可以提升自动驾驶系统的环境感知能力，提高导航的准确性和安全性。在虚拟现实领域，可以创建更逼真、更沉浸式的虚拟环境。

## 📄 摘要（原文）

> Feed-forward surround-view autonomous driving scene reconstruction offers fast, generalizable inference ability, which faces the core challenge of ensuring generalization while elevating novel view quality. Due to the surround-view with minimal overlap regions, existing methods typically fail to ensure geometric consistency and reconstruction quality for novel views. To tackle this tension, we claim that geometric information must be learned explicitly, and the resulting features should be leveraged to guide the elevating of semantic quality in novel views. In this paper, we introduce \textbf{Visual Gaussian Driving (VGD)}, a novel feed-forward end-to-end learning framework designed to address this challenge. To achieve generalizable geometric estimation, we design a lightweight variant of the VGGT architecture to efficiently distill its geometric priors from the pre-trained VGGT to the geometry branch. Furthermore, we design a Gaussian Head that fuses multi-scale geometry tokens to predict Gaussian parameters for novel view rendering, which shares the same patch backbone as the geometry branch. Finally, we integrate multi-scale features from both geometry and Gaussian head branches to jointly supervise a semantic refinement model, optimizing rendering quality through feature-consistent learning. Experiments on nuScenes demonstrate that our approach significantly outperforms state-of-the-art methods in both objective metrics and subjective quality under various settings, which validates VGD's scalability and high-fidelity surround-view reconstruction.

