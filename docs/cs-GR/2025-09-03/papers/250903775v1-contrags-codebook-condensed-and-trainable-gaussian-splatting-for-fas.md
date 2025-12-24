---
layout: default
title: "ContraGS: Codebook-Condensed and Trainable Gaussian Splatting for Fast, Memory-Efficient Reconstruction"
---

# ContraGS: Codebook-Condensed and Trainable Gaussian Splatting for Fast, Memory-Efficient Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03775" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03775v1</a>
  <a href="https://arxiv.org/pdf/2509.03775.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03775v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03775v1', 'ContraGS: Codebook-Condensed and Trainable Gaussian Splatting for Fast, Memory-Efficient Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sankeerth Durvasula, Sharanshangar Muhunthan, Zain Moustafa, Richard Chen, Ruofan Liang, Yushi Guan, Nilesh Ahuja, Nilesh Jain, Selvakumar Panneer, Nandita Vijaykumar

**分类**: cs.GR, cs.CV

**发布日期**: 2025-09-03

---

## 💡 一句话要点

**ContraGS：提出基于码本压缩和可训练高斯溅射方法，实现快速、内存高效的3D重建。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `码本压缩` `贝叶斯推断` `MCMC采样` `内存优化` `快速重建` `实时渲染`

## 📋 核心要点

1. 现有3D高斯溅射方法在高质量重建时需要大量高斯参数，导致GPU内存消耗过高，训练和渲染速度慢。
2. ContraGS通过引入码本压缩高斯参数，并在训练过程中直接在压缩表示上进行优化，从而降低内存占用。
3. 实验表明，ContraGS在显著降低内存消耗的同时，加速了训练和渲染过程，并保持了接近SOTA的重建质量。

## 📝 摘要（中文）

3D高斯溅射(3DGS)是一种先进的技术，可以高质量和实时渲染地对真实场景进行建模。通常，可以通过使用大量的3D高斯来实现更高质量的表示。然而，使用大量的3D高斯会显著增加GPU设备内存，用于存储模型参数。因此，大型模型需要具有高内存容量的强大GPU进行训练，并且由于内存访问和数据移动的效率低下，训练/渲染延迟会更慢。在这项工作中，我们介绍ContraGS，一种可以直接在压缩的3DGS表示上进行训练的方法，而无需减少高斯计数，从而在模型质量上损失很小。ContraGS利用码本在整个训练过程中紧凑地存储一组高斯参数向量，从而显著减少内存消耗。虽然码本已被证明在压缩完全训练的3DGS模型方面非常有效，但直接使用码本表示进行训练是一个尚未解决的挑战。ContraGS通过将参数估计表示为一个贝叶斯推断问题，解决了在码本压缩表示中学习不可微参数的问题。为此，ContraGS提供了一个框架，该框架有效地使用MCMC采样来对这些压缩表示的后验分布进行采样。通过ContraGS，我们证明ContraGS显著降低了训练期间的峰值内存（平均3.49倍），并加速了训练和渲染（平均分别为1.36倍和1.88倍），同时重新训练接近最先进的质量。

## 🔬 方法详解

**问题定义**：论文旨在解决3D高斯溅射（3DGS）模型训练过程中GPU内存消耗过高的问题。现有方法为了达到高质量的重建效果，需要使用大量的3D高斯基元，导致模型参数量巨大，训练和渲染速度受限，并且需要昂贵的高性能GPU。

**核心思路**：论文的核心思路是利用码本（codebook）压缩3D高斯模型的参数，并在压缩域中直接进行训练。通过将高斯参数量化到码本中的有限个向量，可以显著降低内存占用。同时，论文提出了一种基于贝叶斯推断的方法，解决在码本压缩表示下训练时遇到的不可微问题。

**技术框架**：ContraGS的整体框架包括以下几个主要步骤：1）初始化3D高斯模型；2）使用码本对高斯参数进行压缩；3）利用MCMC采样在压缩域中进行参数优化，解决不可微问题；4）更新高斯参数和码本；5）重复步骤2-4直到训练收敛。该框架的关键在于MCMC采样过程，它允许在离散的码本空间中进行有效的参数搜索。

**关键创新**：ContraGS的关键创新在于：1）提出了一种在码本压缩的3DGS表示上直接进行训练的方法，避免了先训练再压缩的流程；2）利用贝叶斯推断和MCMC采样解决了码本压缩带来的不可微问题，使得可以在离散空间中优化高斯参数；3）通过码本压缩，显著降低了训练过程中的内存消耗，并加速了训练和渲染速度。

**关键设计**：ContraGS的关键设计包括：1）码本的大小和初始化方式；2）MCMC采样的具体实现，包括提议分布的选择和接受率的控制；3）损失函数的设计，需要考虑重建质量和码本使用的平衡；4）高斯参数的量化和反量化过程，需要保证梯度信息的有效传递。

## 📊 实验亮点

ContraGS在多个数据集上进行了实验，结果表明，与现有方法相比，ContraGS在训练过程中平均降低了3.49倍的峰值内存消耗，并加速了训练和渲染速度，平均分别提升了1.36倍和1.88倍。同时，ContraGS在重建质量上保持了接近SOTA的水平，证明了其在内存效率和性能方面的优势。

## 🎯 应用场景

ContraGS具有广泛的应用前景，包括：1）移动设备上的3D场景重建和渲染；2）大规模场景的快速建模和可视化；3）虚拟现实和增强现实应用；4）机器人导航和环境感知。通过降低内存需求和提高训练效率，ContraGS使得3DGS技术可以在资源受限的平台上部署，并加速了3D内容的生成和应用。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) is a state-of-art technique to model real-world scenes with high quality and real-time rendering. Typically, a higher quality representation can be achieved by using a large number of 3D Gaussians. However, using large 3D Gaussian counts significantly increases the GPU device memory for storing model parameters. A large model thus requires powerful GPUs with high memory capacities for training and has slower training/rendering latencies due to the inefficiencies of memory access and data movement. In this work, we introduce ContraGS, a method to enable training directly on compressed 3DGS representations without reducing the Gaussian Counts, and thus with a little loss in model quality. ContraGS leverages codebooks to compactly store a set of Gaussian parameter vectors throughout the training process, thereby significantly reducing memory consumption. While codebooks have been demonstrated to be highly effective at compressing fully trained 3DGS models, directly training using codebook representations is an unsolved challenge. ContraGS solves the problem of learning non-differentiable parameters in codebook-compressed representations by posing parameter estimation as a Bayesian inference problem. To this end, ContraGS provides a framework that effectively uses MCMC sampling to sample over a posterior distribution of these compressed representations. With ContraGS, we demonstrate that ContraGS significantly reduces the peak memory during training (on average 3.49X) and accelerated training and rendering (1.36X and 1.88X on average, respectively), while retraining close to state-of-art quality.

