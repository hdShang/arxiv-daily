---
layout: default
title: "HGC-Avatar: Hierarchical Gaussian Compression for Streamable Dynamic 3D Avatars"
---

# HGC-Avatar: Hierarchical Gaussian Compression for Streamable Dynamic 3D Avatars

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16463" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16463v1</a>
  <a href="https://arxiv.org/pdf/2510.16463.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16463v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.16463v1', 'HGC-Avatar: Hierarchical Gaussian Compression for Streamable Dynamic 3D Avatars')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haocheng Tang, Ruoke Yan, Xinhui Yin, Qi Zhang, Xinfeng Zhang, Siwei Ma, Wen Gao, Chuanmin Jia

**分类**: cs.CV

**发布日期**: 2025-10-18

**备注**: ACM International Conference on Multimedia 2025

**DOI**: [10.1145/3746027.3755317](https://doi.org/10.1145/3746027.3755317)

---

## 💡 一句话要点

**提出HGC-Avatar，用于可流式传输的动态3D头像的高效高斯压缩。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `3D高斯溅射` `动态3D头像` `分层压缩` `SMPL-X模型` `StyleUNet` `面部注意力机制` `可流式传输` `数字人`

## 📋 核心要点

1. 现有基于通用3DGS表示的压缩方法缺乏人类先验知识，导致码率效率和解码器侧重建质量欠佳。
2. HGC-Avatar将高斯表示解耦为结构层（StyleUNet生成器）和运动层（SMPL-X模型），实现分层压缩。
3. 实验表明，HGC-Avatar在视觉质量和压缩效率上显著优于现有方法，为快速3D头像渲染提供可流式传输方案。

## 📝 摘要（中文）

本文提出HGC-Avatar，一种新颖的分层高斯压缩框架，旨在实现动态头像的高效传输和高质量渲染。该方法将高斯表示解耦为结构层和运动层。结构层通过基于StyleUNet的生成器将姿势映射到高斯分布，运动层利用SMPL-X模型紧凑且语义化地表示时间姿势变化。这种分层设计支持分层压缩、渐进式解码以及来自视频序列或文本等不同姿势输入的可控渲染。由于人们最关注面部真实感，因此在StyleUNet训练期间，我们结合了面部注意力机制，以在低比特率约束下保留身份和表情细节。实验结果表明，HGC-Avatar为快速3D头像渲染提供了一种可流式传输的解决方案，同时在视觉质量和压缩效率方面均优于现有方法。

## 🔬 方法详解

**问题定义**：现有方法在动态3D头像的编码和传输中，基于通用3D高斯溅射（3DGS）表示的压缩方法，由于缺乏对人类结构的先验知识，导致压缩效率低下，解码端重建质量不佳。这限制了它们在可流式传输的3D头像系统中的应用。

**核心思路**：HGC-Avatar的核心思路是将3D高斯表示解耦为两个层次：结构层和运动层。结构层负责捕捉头像的静态结构信息，而运动层负责捕捉头像随时间变化的姿态信息。通过这种分层解耦，可以针对每一层采用不同的压缩策略，从而提高整体的压缩效率。同时，利用SMPL-X模型对运动层进行建模，可以实现更紧凑和语义化的表示。

**技术框架**：HGC-Avatar的整体框架包括以下几个主要模块：1) 姿态编码器：将输入的姿态信息编码成低维的姿态向量。2) 结构层生成器：基于StyleUNet，将姿态向量映射到3D高斯分布的参数，生成头像的静态结构。3) 运动层编码器：利用SMPL-X模型对姿态变化进行建模，生成运动参数。4) 解码器：根据接收到的结构层和运动层信息，重建3D头像。

**关键创新**：HGC-Avatar的关键创新在于其分层高斯压缩框架，该框架将3D高斯表示解耦为结构层和运动层，并针对每一层采用不同的压缩策略。此外，该方法还引入了面部注意力机制，以在低比特率约束下保留面部细节。与现有方法相比，HGC-Avatar能够实现更高的压缩效率和更好的重建质量。

**关键设计**：在结构层生成器中，使用了基于StyleUNet的网络结构，该结构能够生成高质量的3D高斯分布参数。在训练过程中，引入了面部注意力机制，以增强网络对面部区域的关注。运动层使用了SMPL-X模型，该模型能够对人体姿态进行精确的建模。损失函数包括重建损失、正则化损失和对抗损失，以保证重建质量和生成结果的真实性。

## 📊 实验亮点

实验结果表明，HGC-Avatar在压缩效率和视觉质量方面均优于现有方法。在相同比特率下，HGC-Avatar能够实现更高的PSNR和更低的LPIPS，表明其重建的3D头像具有更高的保真度和更低的感知失真。此外，HGC-Avatar还支持可控渲染，可以根据不同的姿态输入生成相应的3D头像。

## 🎯 应用场景

HGC-Avatar在虚拟会议、远程教育、游戏、社交媒体等领域具有广泛的应用前景。它可以实现低带宽下的高质量3D头像传输，提升用户在虚拟环境中的沉浸感和交互体验。该技术还有潜力应用于数字人制作、动画生成等领域，降低相关内容的制作成本。

## 📄 摘要（原文）

> Recent advances in 3D Gaussian Splatting (3DGS) have enabled fast, photorealistic rendering of dynamic 3D scenes, showing strong potential in immersive communication. However, in digital human encoding and transmission, the compression methods based on general 3DGS representations are limited by the lack of human priors, resulting in suboptimal bitrate efficiency and reconstruction quality at the decoder side, which hinders their application in streamable 3D avatar systems. We propose HGC-Avatar, a novel Hierarchical Gaussian Compression framework designed for efficient transmission and high-quality rendering of dynamic avatars. Our method disentangles the Gaussian representation into a structural layer, which maps poses to Gaussians via a StyleUNet-based generator, and a motion layer, which leverages the SMPL-X model to represent temporal pose variations compactly and semantically. This hierarchical design supports layer-wise compression, progressive decoding, and controllable rendering from diverse pose inputs such as video sequences or text. Since people are most concerned with facial realism, we incorporate a facial attention mechanism during StyleUNet training to preserve identity and expression details under low-bitrate constraints. Experimental results demonstrate that HGC-Avatar provides a streamable solution for rapid 3D avatar rendering, while significantly outperforming prior methods in both visual quality and compression efficiency.

