---
layout: default
title: Splatent: Splatting Diffusion Latents for Novel View Synthesis
---

# Splatent: Splatting Diffusion Latents for Novel View Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09923" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09923v1</a>
  <a href="https://arxiv.org/pdf/2512.09923.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09923v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.09923v1', 'Splatent: Splatting Diffusion Latents for Novel View Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz

**分类**: cs.CV

**发布日期**: 2025-12-10

---

## 💡 一句话要点

**Splatent：通过Splatting扩散模型潜在空间提升新视角合成质量**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `新视角合成` `扩散模型` `VAE` `3D高斯Splatting` `多视角注意力`

## 📋 核心要点

1. 现有基于VAE潜在空间的辐射场方法在新视角合成中存在多视角一致性问题，导致纹理模糊和细节丢失。
2. Splatent通过在2D图像空间中利用多视角注意力机制恢复细节，避免了在3D空间中直接重建，从而保留了预训练VAE的重建质量。
3. 实验结果表明，Splatent在多个基准测试中达到了VAE潜在辐射场重建的最先进水平，并能提升现有前馈框架的细节保留能力。

## 📝 摘要（中文）

辐射场表示最近在VAE的潜在空间中得到了探索，这些VAE通常被扩散模型使用。这种方法提供了高效的渲染和与基于扩散的流程的无缝集成。然而，这些方法面临一个根本的限制：VAE潜在空间缺乏多视角一致性，导致3D重建期间纹理模糊和细节丢失。现有方法试图通过微调VAE来解决这个问题，但以牺牲重建质量为代价，或者依赖于预训练的扩散模型来恢复细粒度细节，但存在产生幻觉的风险。我们提出了Splatent，一个基于扩散的增强框架，旨在在VAE的潜在空间中运行在3D高斯Splatting (3DGS)之上。我们的关键见解偏离了传统的以3D为中心的视角：我们不是在3D空间中重建细粒度细节，而是通过多视角注意力机制从输入视图中在2D中恢复它们。这种方法保留了预训练VAE的重建质量，同时实现了忠实的细节恢复。在多个基准测试中进行评估，Splatent为VAE潜在辐射场重建建立了新的最先进水平。我们进一步证明，将我们的方法与现有的前馈框架集成，可以持续提高细节保留，为高质量的稀疏视图3D重建开辟新的可能性。

## 🔬 方法详解

**问题定义**：论文旨在解决基于VAE潜在空间的辐射场方法在新视角合成中存在的细节缺失和纹理模糊问题。现有方法要么通过微调VAE来改善多视角一致性，但牺牲了重建质量；要么依赖预训练扩散模型，但容易产生幻觉。这些方法无法在保持重建质量的同时，有效地恢复细粒度细节。

**核心思路**：Splatent的核心思路是将细节恢复过程从3D空间转移到2D图像空间。通过利用多视角注意力机制，从输入视图中提取并恢复细节，避免了直接在VAE潜在空间中进行3D重建可能导致的不一致性问题。这种2D-centric的方法能够更好地利用输入图像的细节信息，同时保持预训练VAE的重建质量。

**技术框架**：Splatent框架主要包含以下几个阶段：1）使用预训练的VAE将输入图像编码到潜在空间；2）使用3D高斯Splatting (3DGS) 在潜在空间中进行场景表示；3）使用多视角注意力机制，从原始输入图像中提取细节信息；4）将提取的细节信息融合到3DGS表示中，从而增强新视角合成的细节；5）使用VAE解码器将增强后的潜在表示解码为最终的图像。

**关键创新**：Splatent的关键创新在于其2D-centric的细节恢复方法。与传统的3D-centric方法不同，Splatent不是直接在3D空间中重建细节，而是利用多视角注意力机制从2D输入图像中提取细节，并将其融合到3DGS表示中。这种方法能够更好地利用输入图像的细节信息，避免了3D重建可能导致的不一致性问题。

**关键设计**：Splatent的关键设计包括：1）使用预训练的VAE，以保证重建质量；2）使用3DGS作为场景表示，以实现高效的渲染；3）设计多视角注意力机制，用于从输入图像中提取细节信息。具体来说，多视角注意力机制可能包含多个注意力层，用于学习不同视角之间的对应关系，并提取相关的细节特征。损失函数可能包含重建损失、正则化损失等，用于优化3DGS表示和注意力机制的参数。具体的网络结构和参数设置在论文中应该有详细描述，此处未知。

## 📊 实验亮点

Splatent在多个基准测试中取得了最先进的结果，显著提升了VAE潜在辐射场重建的质量。具体性能数据和对比基线在论文中应该有详细描述，此处未知。该方法不仅能够生成更清晰、更逼真的新视角图像，还能有效提升现有前馈框架的细节保留能力，为高质量的稀疏视图3D重建开辟了新的可能性。

## 🎯 应用场景

Splatent可应用于新视角合成、三维重建、虚拟现实、增强现实等领域。该技术能够提升稀疏视图三维重建的质量，尤其是在需要高质量纹理和细节的应用场景中，例如虚拟旅游、游戏开发、电影制作等。未来，Splatent有望推动相关领域的发展，并为用户带来更逼真、更沉浸式的体验。

## 📄 摘要（原文）

> Radiance field representations have recently been explored in the latent space of VAEs that are commonly used by diffusion models. This direction offers efficient rendering and seamless integration with diffusion-based pipelines. However, these methods face a fundamental limitation: The VAE latent space lacks multi-view consistency, leading to blurred textures and missing details during 3D reconstruction. Existing approaches attempt to address this by fine-tuning the VAE, at the cost of reconstruction quality, or by relying on pre-trained diffusion models to recover fine-grained details, at the risk of some hallucinations. We present Splatent, a diffusion-based enhancement framework designed to operate on top of 3D Gaussian Splatting (3DGS) in the latent space of VAEs. Our key insight departs from the conventional 3D-centric view: rather than reconstructing fine-grained details in 3D space, we recover them in 2D from input views through multi-view attention mechanisms. This approach preserves the reconstruction quality of pretrained VAEs while achieving faithful detail recovery. Evaluated across multiple benchmarks, Splatent establishes a new state-of-the-art for VAE latent radiance field reconstruction. We further demonstrate that integrating our method with existing feed-forward frameworks, consistently improves detail preservation, opening new possibilities for high-quality sparse-view 3D reconstruction.

