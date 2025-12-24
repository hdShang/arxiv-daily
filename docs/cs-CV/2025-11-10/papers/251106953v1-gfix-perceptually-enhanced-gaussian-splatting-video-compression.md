---
layout: default
title: "GFix: Perceptually Enhanced Gaussian Splatting Video Compression"
---

# GFix: Perceptually Enhanced Gaussian Splatting Video Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06953" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06953v1</a>
  <a href="https://arxiv.org/pdf/2511.06953.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06953v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.06953v1', 'GFix: Perceptually Enhanced Gaussian Splatting Video Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyue Teng, Ge Gao, Duolikun Danier, Yuxuan Jiang, Fan Zhang, Thomas Davis, Zoe Liu, David Bull

**分类**: cs.CV

**发布日期**: 2025-11-10

---

## 💡 一句话要点

**GFix：提出感知增强的高斯溅射视频压缩方法，提升视觉质量和压缩率。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `视频压缩` `感知增强` `扩散模型` `LoRA`

## 📋 核心要点

1. 现有基于3DGS的视频压缩方法存在视觉伪影明显、压缩率相对较低的问题，限制了其应用。
2. GFix提出了一种内容自适应框架，利用单步扩散模型作为神经增强器，提升感知质量。
3. GFix采用调制LoRA方案，通过冻结低秩分解和调制中间隐藏状态，实现了高效的扩散骨干自适应和高压缩率。

## 📝 摘要（中文）

3D高斯溅射(3DGS)通过显式表示和快速渲染增强了3D场景重建，展现了在包括视频压缩在内的各种底层视觉任务中的潜在优势。然而，现有的基于3DGS的视频编解码器通常表现出更明显的视觉伪影和相对较低的压缩率。本文基于3DGS渲染和量化产生的伪影类似于扩散训练期间采样的噪声潜在变量的假设，专门针对3DGS视频压缩的感知增强。在此前提下，我们提出了一个内容自适应框架GFix，它包含一个简化的单步扩散模型，作为现成的神经增强器。此外，为了提高压缩效率，我们提出了一种调制LoRA方案，该方案冻结低秩分解并调制中间隐藏状态，从而通过高度可压缩的更新来实现扩散骨干的高效自适应。实验结果表明，GFix提供了强大的感知质量增强，在LPIPS中优于GSVC高达72.1%的BD-rate节省，在FID中优于21.4%。

## 🔬 方法详解

**问题定义**：现有的基于3DGS的视频压缩方法在压缩过程中引入了明显的视觉伪影，导致感知质量下降。同时，这些方法的压缩效率相对较低，限制了其在实际应用中的推广。因此，需要一种能够在保证高压缩率的同时，显著提升感知质量的3DGS视频压缩方法。

**核心思路**：GFix的核心思路是将3DGS渲染和量化过程中产生的伪影视为扩散训练中采样的噪声潜在变量。基于此，利用扩散模型强大的去噪能力，对压缩后的3DGS视频进行感知增强，从而提升视觉质量。同时，为了提高压缩效率，采用调制LoRA方案，实现扩散骨干的高效自适应。

**技术框架**：GFix框架主要包含两个阶段：首先，使用现有的3DGS视频编码器对视频进行压缩；然后，将压缩后的视频输入到GFix神经增强器中进行感知质量提升。GFix神经增强器是一个简化的单步扩散模型，它以压缩后的3DGS视频作为输入，输出增强后的视频。为了提高压缩效率，GFix采用了调制LoRA方案，对扩散骨干进行高效自适应。

**关键创新**：GFix的关键创新在于以下两点：1) 将扩散模型应用于3DGS视频压缩的感知增强，利用其强大的去噪能力提升视觉质量；2) 提出了一种调制LoRA方案，通过冻结低秩分解和调制中间隐藏状态，实现了扩散骨干的高效自适应，从而提高了压缩效率。

**关键设计**：GFix的关键设计包括：1) 采用简化的单步扩散模型，降低计算复杂度；2) 使用内容自适应的方式，根据不同的视频内容调整增强策略；3) 采用调制LoRA方案，冻结低秩分解，仅对中间隐藏状态进行调制，从而减少需要更新的参数量，提高压缩效率。损失函数的设计目标是最小化增强后的视频与原始视频之间的感知差异，例如使用LPIPS或FID等感知指标。

## 📊 实验亮点

实验结果表明，GFix在感知质量方面取得了显著提升，在LPIPS指标上，相比于GSVC，BD-rate节省高达72.1%；在FID指标上，BD-rate节省高达21.4%。这些数据表明，GFix能够有效地去除3DGS视频压缩带来的视觉伪影，显著提升用户体验。

## 🎯 应用场景

GFix技术可应用于各种需要高质量、高压缩率3D视频传输和存储的场景，例如：VR/AR应用、远程会议、在线游戏、3D内容创作等。该技术能够显著提升用户体验，降低带宽需求，并促进3D视频内容的普及。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) enhances 3D scene reconstruction through explicit representation and fast rendering, demonstrating potential benefits for various low-level vision tasks, including video compression. However, existing 3DGS-based video codecs generally exhibit more noticeable visual artifacts and relatively low compression ratios. In this paper, we specifically target the perceptual enhancement of 3DGS-based video compression, based on the assumption that artifacts from 3DGS rendering and quantization resemble noisy latents sampled during diffusion training. Building on this premise, we propose a content-adaptive framework, GFix, comprising a streamlined, single-step diffusion model that serves as an off-the-shelf neural enhancer. Moreover, to increase compression efficiency, We propose a modulated LoRA scheme that freezes the low-rank decompositions and modulates the intermediate hidden states, thereby achieving efficient adaptation of the diffusion backbone with highly compressible updates. Experimental results show that GFix delivers strong perceptual quality enhancement, outperforming GSVC with up to 72.1% BD-rate savings in LPIPS and 21.4% in FID.

