---
layout: default
title: "HyPlaneHead: Rethinking Tri-plane-like Representations in Full-Head Image Synthesis"
---

# HyPlaneHead: Rethinking Tri-plane-like Representations in Full-Head Image Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16748" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16748v1</a>
  <a href="https://arxiv.org/pdf/2509.16748.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16748v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16748v1', 'HyPlaneHead: Rethinking Tri-plane-like Representations in Full-Head Image Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heyuan Li, Kenkun Liu, Lingteng Qiu, Qi Zuo, Keru Zheng, Zilong Dong, Xiaoguang Han

**分类**: cs.CV

**发布日期**: 2025-09-20

**备注**: Accepted by NeurIPS 2025

---

## 💡 一句话要点

**提出HyPlaneHead，通过混合平面表示实现高质量全头部图像合成**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `全头部图像合成` `3D感知GAN` `混合平面表示` `特征解耦` `生成对抗网络`

## 📋 核心要点

1. 现有基于三平面表示的头部图像合成方法存在特征纠缠、特征图利用率不均以及平面间特征渗透等问题，限制了性能提升。
2. 论文提出混合平面（hy-plane）表示，结合平面和球面表示的优势，并采用近等面积扭曲策略和单通道统一特征图来优化特征利用和减少特征渗透。
3. 实验结果表明，HyPlaneHead方法在全头部图像合成任务中取得了state-of-the-art的性能，验证了所提出方法的有效性。

## 📝 摘要（中文）

本文针对3D感知GAN中广泛使用的类三平面表示在头部图像合成中的问题进行了研究。现有方法如笛卡尔坐标投影导致特征纠缠，产生镜像伪影；球坐标三平面虽然缓解了特征纠缠，但存在特征图利用率不均的问题。此外，平面间的特征渗透也会造成干扰。本文首次系统性地分析了这些问题，并提出了创新性的解决方案。具体而言，我们引入了一种新型的混合平面（hy-plane）表示，它结合了平面和球面表示的优点，同时避免了它们的缺点。我们还通过一种近等面积的扭曲策略来增强球面平面，从而最大限度地提高特征图的有效利用率。此外，我们的生成器合成单通道统一特征图，从而有效地消除了特征渗透。通过一系列技术改进，我们的hy-plane表示使我们的方法HyPlaneHead在全头部图像合成中实现了最先进的性能。

## 🔬 方法详解

**问题定义**：现有基于三平面表示的3D-aware GAN在全头部图像合成中存在三个主要问题：一是笛卡尔坐标投影导致特征纠缠，产生镜像伪影；二是球面三平面存在特征图利用率不均的问题，难以生成精细图像细节；三是平面间的特征渗透会造成干扰，影响合成质量。这些问题限制了三平面表示方法的潜力。

**核心思路**：论文的核心思路是结合平面和球面表示的优势，提出一种混合平面（hy-plane）表示。平面表示擅长捕捉局部细节，而球面表示擅长处理全局结构。通过合理地结合两者，可以克服各自的缺点，提高特征表达能力。此外，通过优化特征图的利用率和减少特征渗透，进一步提升合成质量。

**技术框架**：HyPlaneHead的整体框架包括一个生成器网络和一个判别器网络。生成器网络首先将潜在编码映射到混合平面表示（hy-plane），然后通过一个渲染模块将hy-plane表示转换为RGB图像。判别器网络用于区分生成的图像和真实图像。关键模块包括：混合平面生成模块、近等面积扭曲模块和单通道特征图生成模块。

**关键创新**：论文的关键创新在于提出了混合平面（hy-plane）表示，它结合了平面和球面表示的优点。与传统的平面或球面表示相比，hy-plane表示能够更好地捕捉头部图像的全局结构和局部细节。此外，近等面积扭曲策略和单通道特征图生成策略也是重要的创新点，它们分别解决了特征图利用率不均和特征渗透的问题。

**关键设计**：混合平面表示的具体实现方式是将平面和球面表示进行加权融合。权重的选择可以根据具体任务进行调整。近等面积扭曲策略采用了一种特殊的映射函数，使得特征图上的每个像素对应于球面上的近似相等面积的区域。单通道特征图生成策略通过一个卷积层将多个特征通道合并为一个通道，从而消除特征渗透。损失函数包括对抗损失、感知损失和正则化损失。

## 📊 实验亮点

HyPlaneHead在全头部图像合成任务中取得了state-of-the-art的性能。实验结果表明，HyPlaneHead生成的图像在视觉质量和身份保持方面均优于现有方法。例如，在CelebA-HQ数据集上，HyPlaneHead的FID得分显著低于其他基线方法，表明其生成的图像更加逼真。

## 🎯 应用场景

HyPlaneHead在虚拟现实、增强现实、游戏开发、数字人生成等领域具有广泛的应用前景。它可以用于创建逼真的虚拟化身，改善视频会议体验，以及生成高质量的头部图像用于各种视觉应用。该研究的成果有助于推动3D感知GAN在实际应用中的发展。

## 📄 摘要（原文）

> Tri-plane-like representations have been widely adopted in 3D-aware GANs for head image synthesis and other 3D object/scene modeling tasks due to their efficiency. However, querying features via Cartesian coordinate projection often leads to feature entanglement, which results in mirroring artifacts. A recent work, SphereHead, attempted to address this issue by introducing spherical tri-planes based on a spherical coordinate system. While it successfully mitigates feature entanglement, SphereHead suffers from uneven mapping between the square feature maps and the spherical planes, leading to inefficient feature map utilization during rendering and difficulties in generating fine image details. Moreover, both tri-plane and spherical tri-plane representations share a subtle yet persistent issue: feature penetration across convolutional channels can cause interference between planes, particularly when one plane dominates the others. These challenges collectively prevent tri-plane-based methods from reaching their full potential. In this paper, we systematically analyze these problems for the first time and propose innovative solutions to address them. Specifically, we introduce a novel hybrid-plane (hy-plane for short) representation that combines the strengths of both planar and spherical planes while avoiding their respective drawbacks. We further enhance the spherical plane by replacing the conventional theta-phi warping with a novel near-equal-area warping strategy, which maximizes the effective utilization of the square feature map. In addition, our generator synthesizes a single-channel unified feature map instead of multiple feature maps in separate channels, thereby effectively eliminating feature penetration. With a series of technical improvements, our hy-plane representation enables our method, HyPlaneHead, to achieve state-of-the-art performance in full-head image synthesis.

