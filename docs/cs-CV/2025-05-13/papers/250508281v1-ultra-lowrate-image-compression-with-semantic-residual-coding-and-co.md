---
layout: default
title: Ultra Lowrate Image Compression with Semantic Residual Coding and Compression-aware Diffusion
---

# Ultra Lowrate Image Compression with Semantic Residual Coding and Compression-aware Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08281" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08281v1</a>
  <a href="https://arxiv.org/pdf/2505.08281.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08281v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08281v1', 'Ultra Lowrate Image Compression with Semantic Residual Coding and Compression-aware Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anle Ke, Xu Zhang, Tong Chen, Ming Lu, Chao Zhou, Jiawen Gu, Zhan Ma

**分类**: cs.CV, eess.IV

**发布日期**: 2025-05-13

**期刊**: ICML 2025

---

## 💡 一句话要点

**提出ResULIC以解决现有图像压缩效率低的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像压缩` `多模态模型` `语义残差编码` `扩散模型` `重建质量` `编码效率` `低码率`

## 📋 核心要点

1. 现有图像压缩方法在重建质量和编码效率上表现不佳，难以满足高效图像传输的需求。
2. 本文提出的ResULIC方法通过引入语义残差编码和压缩感知扩散模型，提升了图像压缩的性能。
3. 实验结果显示，ResULIC在LPIPS和FID指标上分别实现了-80.7%和-66.3%的BD-rate节省，优于现有方法。

## 📝 摘要（中文）

现有的多模态大模型图像压缩框架往往依赖于语义检索、潜在压缩和生成模型的碎片化集成，导致重建保真度和编码效率均不理想。为了解决这些挑战，本文提出了一种名为ResULIC的残差引导超低码率图像压缩方法，该方法将残差信号融入语义检索和基于扩散的生成过程中。具体而言，我们引入了语义残差编码（SRC）来捕捉原始图像与其压缩潜在表示之间的语义差异，并进一步应用感知保真度优化器以提高重建质量。此外，我们提出了压缩感知扩散模型（CDM），在比特率和扩散时间步之间建立了最佳对齐，从而改善压缩与重建的协同作用。大量实验表明，ResULIC在LPIPS和FID方面相比于最先进的基于扩散的方法实现了-80.7%和-66.3%的BD-rate节省。

## 🔬 方法详解

**问题定义**：现有的图像压缩方法在重建保真度和编码效率方面存在不足，尤其是在多模态大模型的应用中，碎片化的集成导致性能不佳。

**核心思路**：ResULIC通过引入残差信号，增强了语义检索和生成过程的有效性，旨在提高重建质量和压缩效率。

**技术框架**：该方法主要包括两个模块：语义残差编码（SRC）用于捕捉语义差异，压缩感知扩散模型（CDM）用于优化比特率与扩散时间步的对齐。

**关键创新**：最重要的创新在于将残差信号有效整合进语义检索和生成过程中，显著提升了图像压缩的重建质量和效率。

**关键设计**：在设计中，SRC模块通过特定的损失函数来优化语义差异，而CDM则通过调整扩散步骤与比特率的关系来实现更好的压缩效果。

## 📊 实验亮点

实验结果表明，ResULIC在LPIPS和FID指标上分别实现了-80.7%和-66.3%的BD-rate节省，显著优于现有的基于扩散的图像压缩方法，展示了其在重建质量和编码效率上的卓越性能。

## 🎯 应用场景

该研究的潜在应用领域包括图像传输、视频流媒体和低带宽环境下的图像存储等。通过提高图像压缩效率，ResULIC可以在移动设备、物联网设备等资源受限的场景中发挥重要作用，未来可能对图像处理和传输技术产生深远影响。

## 📄 摘要（原文）

> Existing multimodal large model-based image compression frameworks often rely on a fragmented integration of semantic retrieval, latent compression, and generative models, resulting in suboptimal performance in both reconstruction fidelity and coding efficiency. To address these challenges, we propose a residual-guided ultra lowrate image compression named ResULIC, which incorporates residual signals into both semantic retrieval and the diffusion-based generation process. Specifically, we introduce Semantic Residual Coding (SRC) to capture the semantic disparity between the original image and its compressed latent representation. A perceptual fidelity optimizer is further applied for superior reconstruction quality. Additionally, we present the Compression-aware Diffusion Model (CDM), which establishes an optimal alignment between bitrates and diffusion time steps, improving compression-reconstruction synergy. Extensive experiments demonstrate the effectiveness of ResULIC, achieving superior objective and subjective performance compared to state-of-the-art diffusion-based methods with - 80.7%, -66.3% BD-rate saving in terms of LPIPS and FID. Project page is available at https: //njuvision.github.io/ResULIC/.

