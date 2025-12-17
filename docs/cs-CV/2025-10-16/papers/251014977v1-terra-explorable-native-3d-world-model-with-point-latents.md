---
layout: default
title: Terra: Explorable Native 3D World Model with Point Latents
---

# Terra: Explorable Native 3D World Model with Point Latents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14977" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14977v1</a>
  <a href="https://arxiv.org/pdf/2510.14977.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14977v1" onclick="toggleFavorite(this, '2510.14977v1', 'Terra: Explorable Native 3D World Model with Point Latents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanhui Huang, Weiliang Chen, Wenzhao Zheng, Xin Tao, Pengfei Wan, Jie Zhou, Jiwen Lu

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-10-16

**备注**: Project Page: https://huang-yh.github.io/terra/

---

## 💡 一句话要点

**Terra：基于点潜变量的可探索原生3D世界模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `3D世界模型` `点云` `变分自编码器` `生成模型` `场景重建` `可探索环境` `3D一致性`

## 📋 核心要点

1. 现有世界模型依赖像素对齐表示，忽略了真实世界的3D特性，导致3D一致性差和建模效率低。
2. Terra提出了一种原生3D世界模型，使用点潜变量在3D潜在空间中表示和生成可探索环境。
3. 实验表明，Terra在ScanNet v2数据集上实现了最先进的重建和生成性能，并具有高3D一致性。

## 📝 摘要（中文）

世界模型在真实世界建模中日益受到关注。然而，现有方法大多依赖于像素对齐的表示进行世界演化，忽略了物理世界固有的3D特性，这会损害3D一致性并降低世界模型的建模效率。本文提出了Terra，一种原生的3D世界模型，它在固有的3D潜在空间中表示和生成可探索的环境。具体来说，我们提出了一种新颖的点到高斯变分自编码器(P2G-VAE)，将3D输入编码为潜在点表示，然后将其解码为3D高斯基元，以联合建模几何和外观。我们还引入了一个稀疏点流匹配网络(SPFlow)来生成潜在点表示，该网络同时对点潜变量的位置和特征进行去噪。Terra通过原生3D表示和架构实现精确的多视角一致性，并支持仅通过单个生成过程从任何视点进行灵活渲染。此外，Terra通过在点潜在空间中进行渐进式生成来实现可探索的世界建模。我们在具有挑战性的ScanNet v2室内场景上进行了大量实验。Terra在重建和生成方面都取得了最先进的性能，并具有很高的3D一致性。

## 🔬 方法详解

**问题定义**：现有世界模型主要基于2D像素对齐的表示，无法充分利用3D世界的固有结构信息，导致建模效率低下，且难以保证多视角下3D一致性。因此，如何构建一个能够原生处理和生成3D环境，并保持良好3D一致性的世界模型是一个关键问题。

**核心思路**：Terra的核心思路是将3D场景编码到由点表示的潜在空间中，每个点携带几何和外观信息。通过在这个潜在空间中进行操作（如生成、演化），可以实现对3D世界的建模和探索。使用点作为基本表示单元，能够更好地捕捉3D场景的结构信息，并方便进行后续的生成和操作。

**技术框架**：Terra主要包含两个核心模块：P2G-VAE（Point-to-Gaussian Variational Autoencoder）和SPFlow（Sparse Point Flow Matching Network）。P2G-VAE负责将3D输入编码为点潜变量，并将其解码为3D高斯基元，从而实现几何和外观的联合建模。SPFlow则负责在点潜变量空间中进行生成，通过对点的位置和特征进行去噪，逐步生成新的3D场景。整体流程为：3D场景 -> P2G-VAE编码 -> 点潜变量 -> SPFlow生成/演化 -> P2G-VAE解码 -> 3D场景。

**关键创新**：Terra的关键创新在于：1) 提出了基于点潜变量的原生3D世界模型，避免了传统方法中2D表示的局限性；2) 设计了P2G-VAE，能够有效地将3D场景编码为点潜变量，并解码为具有几何和外观信息的3D高斯基元；3) 引入了SPFlow，实现了在点潜变量空间中的生成和演化，从而支持可探索的世界建模。与现有方法相比，Terra能够更好地保持3D一致性，并支持灵活的视角渲染。

**关键设计**：P2G-VAE使用变分自编码器框架，包含编码器和解码器。编码器将3D输入编码为点潜变量，解码器则将点潜变量解码为3D高斯基元。SPFlow采用流匹配网络结构，通过学习点的位置和特征的流动，实现对点潜变量的生成和去噪。损失函数包括重建损失、KL散度损失和流匹配损失。具体参数设置（如网络层数、学习率等）在论文中有详细描述。

## 📊 实验亮点

Terra在ScanNet v2数据集上进行了实验，结果表明，在3D场景重建和生成方面，Terra取得了state-of-the-art的性能。相较于现有方法，Terra在3D一致性方面有显著提升，能够生成更逼真、更连贯的3D场景。具体性能数据（如重建误差、生成质量等）在论文中有详细展示。

## 🎯 应用场景

Terra具有广泛的应用前景，例如：机器人导航与环境理解，可以帮助机器人在未知环境中进行探索和规划；虚拟现实与增强现实，可以生成逼真的3D环境，提升用户体验；游戏开发，可以快速生成各种游戏场景；3D内容创作，可以辅助设计师进行3D建模和编辑。该研究有望推动3D世界建模技术的发展，并为相关领域带来新的可能性。

## 📄 摘要（原文）

> World models have garnered increasing attention for comprehensive modeling of the real world. However, most existing methods still rely on pixel-aligned representations as the basis for world evolution, neglecting the inherent 3D nature of the physical world. This could undermine the 3D consistency and diminish the modeling efficiency of world models. In this paper, we present Terra, a native 3D world model that represents and generates explorable environments in an intrinsic 3D latent space. Specifically, we propose a novel point-to-Gaussian variational autoencoder (P2G-VAE) that encodes 3D inputs into a latent point representation, which is subsequently decoded as 3D Gaussian primitives to jointly model geometry and appearance. We then introduce a sparse point flow matching network (SPFlow) for generating the latent point representation, which simultaneously denoises the positions and features of the point latents. Our Terra enables exact multi-view consistency with native 3D representation and architecture, and supports flexible rendering from any viewpoint with only a single generation process. Furthermore, Terra achieves explorable world modeling through progressive generation in the point latent space. We conduct extensive experiments on the challenging indoor scenes from ScanNet v2. Terra achieves state-of-the-art performance in both reconstruction and generation with high 3D consistency.

