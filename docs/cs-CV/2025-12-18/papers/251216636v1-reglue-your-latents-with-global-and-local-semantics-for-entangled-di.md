---
layout: default
title: REGLUE Your Latents with Global and Local Semantics for Entangled Diffusion
---

# REGLUE Your Latents with Global and Local Semantics for Entangled Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16636" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16636v1</a>
  <a href="https://arxiv.org/pdf/2512.16636.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16636v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16636v1', 'REGLUE Your Latents with Global and Local Semantics for Entangled Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Giorgos Petsangourakis, Christos Sgouropoulos, Bill Psomas, Theodoros Giannakopoulos, Giorgos Sfikas, Ioannis Kakogeorgiou

**分类**: cs.CV

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/giorgospets/reglue)

---

## 💡 一句话要点

**REGLUE：融合全局与局部语义的解耦扩散模型，提升图像合成质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `潜在扩散模型` `图像合成` `视觉基础模型` `语义融合` `全局局部语义`

## 📋 核心要点

1. 现有潜在扩散模型语义监督不足，导致训练缓慢且样本质量受限，未能充分利用视觉基础模型(VFM)的丰富语义信息。
2. REGLUE通过联合建模VAE潜在变量、局部VFM语义和全局[CLS] token，在扩散过程中融合全局和局部语义信息，实现更有效的语义监督。
3. 实验表明，REGLUE在ImageNet 256x256上显著提升了FID，并加速了收敛速度，优于现有方法。

## 📝 摘要（中文）

潜在扩散模型(LDMs)在图像合成方面取得了最先进的成果，但其重建式去噪目标仅提供了间接的语义监督：高层语义出现缓慢，需要更长的训练时间，并限制了样本质量。最近的研究通过表征对齐从视觉基础模型(VFMs)外部注入语义，或者通过在扩散过程中联合建模VFM特征的一小部分来内部注入语义，未能充分利用可用的丰富、非线性、多层空间语义。我们提出了REGLUE（Representation Entanglement with Global-Local Unified Encoding），一个统一的潜在扩散框架，它在单个SiT骨干网络中联合建模(i)VAE图像潜在变量，(ii)紧凑的局部(patch级别)VFM语义，以及(iii)全局(图像级别)[CLS] token。一个轻量级的卷积语义压缩器将多层VFM特征非线性地聚合为低维、空间结构化的表示，并在扩散过程中与VAE潜在变量纠缠。外部对齐损失进一步将内部表示正则化到冻结的VFM目标。在ImageNet 256x256上，REGLUE始终如一地提高了FID，并加速了SiT-B/2和SiT-XL/2基线以及REPA、ReDi和REG的收敛速度。大量实验表明，(a)空间VFM语义至关重要，(b)非线性压缩是充分发挥其优势的关键，以及(c)全局token和外部对齐在我们全局-局部-潜在联合建模框架中充当互补的、轻量级的增强。

## 🔬 方法详解

**问题定义**：现有的潜在扩散模型在图像生成任务中，虽然取得了不错的效果，但是其训练过程依赖于重建式的去噪目标，这种方式提供的语义监督是间接的，导致高层语义的学习较为缓慢，需要更长的训练时间，并且最终生成的图像质量也受到限制。此外，现有方法在利用视觉基础模型（VFMs）的语义信息时，要么只利用了VFM特征的一小部分，要么没有充分利用VFM提供的多层空间语义信息。

**核心思路**：REGLUE的核心思路是通过联合建模VAE图像潜在变量、局部（patch级别）VFM语义以及全局（图像级别）[CLS] token，从而在扩散过程中更有效地融合全局和局部语义信息。通过这种方式，模型可以更好地理解图像的整体结构和局部细节，从而生成更高质量的图像。

**技术框架**：REGLUE的整体框架包含以下几个主要模块：1) VAE编码器：将输入图像编码为潜在变量。2) 视觉基础模型（VFM）：提取图像的多层语义特征。3) 卷积语义压缩器：将VFM特征非线性地压缩为低维、空间结构化的表示。4) SiT骨干网络：作为扩散模型的去噪器，联合建模VAE潜在变量、压缩后的VFM语义和全局[CLS] token。5) 外部对齐损失：正则化内部表示，使其与冻结的VFM目标对齐。

**关键创新**：REGLUE的关键创新在于其全局-局部-潜在联合建模框架，该框架能够有效地融合来自VAE潜在变量、局部VFM语义和全局[CLS] token的信息。此外，使用非线性卷积语义压缩器来处理VFM特征也是一个重要的创新点，它可以更好地提取和利用VFM提供的丰富语义信息。

**关键设计**：REGLUE的关键设计包括：1) 使用轻量级的卷积语义压缩器，以减少计算量并保留关键的语义信息。2) 在SiT骨干网络中同时建模VAE潜在变量、局部VFM语义和全局[CLS] token，实现全局和局部语义的有效融合。3) 使用外部对齐损失，以确保内部表示与VFM目标对齐，从而提高生成图像的质量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16636v1/figs/training_steps_photos/50k_steps/000343.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16636v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16636v1/figs/cfg/golden_retriever_207/000444.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

REGLUE在ImageNet 256x256数据集上进行了实验，结果表明，REGLUE能够显著提高FID，并加速收敛速度。具体来说，REGLUE优于SiT-B/2和SiT-XL/2基线，以及REPA、ReDi和REG等现有方法。实验还表明，空间VFM语义至关重要，非线性压缩是充分发挥其优势的关键，全局token和外部对齐可以作为互补的增强手段。

## 🎯 应用场景

REGLUE具有广泛的应用前景，包括图像生成、图像编辑、图像修复等。该方法可以用于生成逼真度更高、语义更丰富的图像，例如，可以用于生成高质量的艺术作品、游戏素材、虚拟现实内容等。此外，REGLUE还可以应用于医学图像分析、遥感图像分析等领域，帮助医生和研究人员更好地理解和分析图像数据。

## 📄 摘要（原文）

> Latent diffusion models (LDMs) achieve state-of-the-art image synthesis, yet their reconstruction-style denoising objective provides only indirect semantic supervision: high-level semantics emerge slowly, requiring longer training and limiting sample quality. Recent works inject semantics from Vision Foundation Models (VFMs) either externally via representation alignment or internally by jointly modeling only a narrow slice of VFM features inside the diffusion process, under-utilizing the rich, nonlinear, multi-layer spatial semantics available. We introduce REGLUE (Representation Entanglement with Global-Local Unified Encoding), a unified latent diffusion framework that jointly models (i) VAE image latents, (ii) compact local (patch-level) VFM semantics, and (iii) a global (image-level) [CLS] token within a single SiT backbone. A lightweight convolutional semantic compressor nonlinearly aggregates multi-layer VFM features into a low-dimensional, spatially structured representation, which is entangled with the VAE latents in the diffusion process. An external alignment loss further regularizes internal representations toward frozen VFM targets. On ImageNet 256x256, REGLUE consistently improves FID and accelerates convergence over SiT-B/2 and SiT-XL/2 baselines, as well as over REPA, ReDi, and REG. Extensive experiments show that (a) spatial VFM semantics are crucial, (b) non-linear compression is key to unlocking their full benefit, and (c) global tokens and external alignment act as complementary, lightweight enhancements within our global-local-latent joint modeling framework. The code is available at https://github.com/giorgospets/reglue .

