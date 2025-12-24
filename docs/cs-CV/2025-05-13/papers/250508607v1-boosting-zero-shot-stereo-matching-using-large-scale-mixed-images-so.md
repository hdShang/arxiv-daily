---
layout: default
title: Boosting Zero-shot Stereo Matching using Large-scale Mixed Images Sources in the Real World
---

# Boosting Zero-shot Stereo Matching using Large-scale Mixed Images Sources in the Real World

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08607" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08607v1</a>
  <a href="https://arxiv.org/pdf/2505.08607.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08607v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08607v1', 'Boosting Zero-shot Stereo Matching using Large-scale Mixed Images Sources in the Real World')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuran Wang, Yingping Liang, Ying Fu

**分类**: cs.CV

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出BooSTer以解决真实世界中零-shot立体匹配问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `立体匹配` `深度估计` `知识转移` `视觉基础模型` `数据生成` `伪标签` `动态损失`

## 📋 核心要点

1. 现有的立体匹配方法依赖于密集的像素级标签，获取这些标签在真实世界数据集中非常困难，导致数据稀缺和领域差距问题。
2. 本文提出的BooSTer框架结合了单目深度估计和扩散模型，能够从单视图图像生成密集的立体匹配数据，并利用伪标签增强监督。
3. 在基准数据集上的实验结果显示，BooSTer在准确性上显著优于现有方法，尤其是在标注数据有限的情况下表现突出。

## 📝 摘要（中文）

立体匹配方法依赖于密集的像素级真实标签，这在真实世界数据集中获取非常困难。缺乏标注数据以及合成与真实图像之间的领域差距也带来了显著挑战。本文提出了一种新颖的框架BooSTer，利用视觉基础模型和大规模混合图像源，包括合成图像、真实图像和单视图图像。首先，我们设计了一种数据生成策略，结合单目深度估计和扩散模型，从单视图图像生成密集的立体匹配数据。其次，为了解决真实世界数据集中稀疏标签的问题，我们从单目深度估计模型中转移知识，使用伪单目深度标签和动态尺度及位移不变损失进行额外监督。此外，我们将视觉基础模型作为编码器，以提取稳健且可迁移的特征，从而提升准确性和泛化能力。大量实验表明，我们的方法在基准数据集上显著提高了准确性，尤其是在标注数据有限和领域转移的场景中。

## 🔬 方法详解

**问题定义**：本文旨在解决立体匹配中对密集像素级真实标签的依赖问题，现有方法在真实世界数据集上面临标注稀缺和领域差距的挑战。

**核心思路**：提出BooSTer框架，通过结合单目深度估计和扩散模型，从单视图图像生成密集立体匹配数据，同时利用伪单目深度标签进行知识转移，增强监督。

**技术框架**：BooSTer框架主要包括数据生成模块、知识转移模块和特征提取模块。数据生成模块负责从单视图图像生成立体匹配数据，知识转移模块利用伪标签进行额外监督，特征提取模块则使用视觉基础模型提取特征。

**关键创新**：最重要的创新在于通过单目深度估计与扩散模型的结合，成功生成密集的立体匹配数据，并通过动态损失函数提升了模型的泛化能力。

**关键设计**：在损失函数设计上，采用动态尺度和位移不变损失，以适应不同场景下的稀疏标签问题；网络结构上，使用视觉基础模型作为编码器，确保提取的特征具有稳健性和可迁移性。

## 📊 实验亮点

实验结果表明，BooSTer在多个基准数据集上显著提高了立体匹配的准确性，尤其是在标注数据稀缺的情况下，准确性提升幅度达到XX%（具体数据未知），超越了现有的主流方法。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人视觉、虚拟现实等，能够在缺乏标注数据的情况下提升立体匹配的准确性和鲁棒性。未来，BooSTer框架有望推动更多实际应用的发展，尤其是在复杂环境下的视觉任务。

## 📄 摘要（原文）

> Stereo matching methods rely on dense pixel-wise ground truth labels, which are laborious to obtain, especially for real-world datasets. The scarcity of labeled data and domain gaps between synthetic and real-world images also pose notable challenges. In this paper, we propose a novel framework, \textbf{BooSTer}, that leverages both vision foundation models and large-scale mixed image sources, including synthetic, real, and single-view images. First, to fully unleash the potential of large-scale single-view images, we design a data generation strategy combining monocular depth estimation and diffusion models to generate dense stereo matching data from single-view images. Second, to tackle sparse labels in real-world datasets, we transfer knowledge from monocular depth estimation models, using pseudo-mono depth labels and a dynamic scale- and shift-invariant loss for additional supervision. Furthermore, we incorporate vision foundation model as an encoder to extract robust and transferable features, boosting accuracy and generalization. Extensive experiments on benchmark datasets demonstrate the effectiveness of our approach, achieving significant improvements in accuracy over existing methods, particularly in scenarios with limited labeled data and domain shifts.

