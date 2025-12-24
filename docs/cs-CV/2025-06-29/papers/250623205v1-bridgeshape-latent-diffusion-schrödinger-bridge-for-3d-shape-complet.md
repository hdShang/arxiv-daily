---
layout: default
title: "BridgeShape: Latent Diffusion Schrödinger Bridge for 3D Shape Completion"
---

# BridgeShape: Latent Diffusion Schrödinger Bridge for 3D Shape Completion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23205" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23205v1</a>
  <a href="https://arxiv.org/pdf/2506.23205.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23205v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23205v1', 'BridgeShape: Latent Diffusion Schrödinger Bridge for 3D Shape Completion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dequan Kong, Zhe Zhu, Honghua Chen, Mingqiang Wei

**分类**: cs.CV

**发布日期**: 2025-06-29

---

## 💡 一句话要点

**提出BridgeShape以解决3D形状补全中的全局传输路径建模问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `3D形状补全` `潜在扩散` `最优传输` `向量量化变分自编码器` `几何结构感知` `计算机图形学` `虚拟现实` `增强现实`

## 📋 核心要点

1. 现有的3D形状补全方法未能有效建模全局传输路径，导致补全效果不佳。
2. BridgeShape将形状补全视为最优传输问题，并通过潜在扩散薛定谔桥进行建模。
3. 在大规模3D形状补全基准上，BridgeShape实现了最先进的性能，特别是在高分辨率和未见物体类别上表现优异。

## 📝 摘要（中文）

现有的基于扩散的3D形状补全方法通常采用条件范式，通过深度特征交互将不完整形状信息注入去噪网络，以引导采样生成完整形状。然而，这些方法未能明确建模最佳的全局传输路径，导致补全效果不佳。此外，直接在体素空间中进行扩散会限制分辨率，限制了细致几何细节的生成。为了解决这些挑战，本文提出了BridgeShape，一个通过潜在扩散薛定谔桥进行3D形状补全的新框架。关键创新在于将形状补全形式化为一个最优传输问题，并引入深度增强的向量量化变分自编码器（VQ-VAE），以编码3D形状到紧凑的潜在空间，从而有效缓解分辨率限制并实现高保真度的3D形状补全。

## 🔬 方法详解

**问题定义**：本文旨在解决现有3D形状补全方法在全局传输路径建模上的不足，导致补全效果不理想。现有方法在体素空间中直接进行扩散，限制了生成的几何细节。

**核心思路**：BridgeShape通过将形状补全问题形式化为最优传输问题，明确建模不完整形状与完整形状之间的转换，以确保全局一致的变换。

**技术框架**：该框架主要包括两个模块：首先是深度增强的向量量化变分自编码器（VQ-VAE），用于将3D形状编码到紧凑的潜在空间；其次是潜在扩散薛定谔桥，用于在潜在空间中进行形状补全。

**关键创新**：BridgeShape的核心创新在于将形状补全视为最优传输问题，并在潜在空间中进行操作，从而有效缓解了分辨率限制，与传统方法形成了本质区别。

**关键设计**：在设计中，采用了自投影的多视角深度信息，并结合强大的DINOv2特征，以增强几何结构感知。此外，损失函数的设计也考虑了全局一致性，以优化补全效果。

## 📊 实验亮点

BridgeShape在大规模3D形状补全基准上取得了最先进的性能，特别是在高分辨率下，补全效果显著优于现有方法，尤其是在未见物体类别上，展现出更高的保真度和细节表现。

## 🎯 应用场景

该研究的潜在应用领域包括计算机图形学、虚拟现实、增强现实以及机器人视觉等。通过高效的3D形状补全，BridgeShape能够为设计、模拟和交互提供更为真实的三维模型，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Existing diffusion-based 3D shape completion methods typically use a conditional paradigm, injecting incomplete shape information into the denoising network via deep feature interactions (e.g., concatenation, cross-attention) to guide sampling toward complete shapes, often represented by voxel-based distance functions. However, these approaches fail to explicitly model the optimal global transport path, leading to suboptimal completions. Moreover, performing diffusion directly in voxel space imposes resolution constraints, limiting the generation of fine-grained geometric details. To address these challenges, we propose BridgeShape, a novel framework for 3D shape completion via latent diffusion Schrödinger bridge. The key innovations lie in two aspects: (i) BridgeShape formulates shape completion as an optimal transport problem, explicitly modeling the transition between incomplete and complete shapes to ensure a globally coherent transformation. (ii) We introduce a Depth-Enhanced Vector Quantized Variational Autoencoder (VQ-VAE) to encode 3D shapes into a compact latent space, leveraging self-projected multi-view depth information enriched with strong DINOv2 features to enhance geometric structural perception. By operating in a compact yet structurally informative latent space, BridgeShape effectively mitigates resolution constraints and enables more efficient and high-fidelity 3D shape completion. BridgeShape achieves state-of-the-art performance on large-scale 3D shape completion benchmarks, demonstrating superior fidelity at higher resolutions and for unseen object classes.

