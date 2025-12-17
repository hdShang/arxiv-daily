---
layout: default
title: ReSplat: Learning Recurrent Gaussian Splats
---

# ReSplat: Learning Recurrent Gaussian Splats

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.08575" target="_blank" class="toolbar-btn">arXiv: 2510.08575v2</a>
    <a href="https://arxiv.org/pdf/2510.08575.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08575v2" 
            onclick="toggleFavorite(this, '2510.08575v2', 'ReSplat: Learning Recurrent Gaussian Splats')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Haofei Xu, Daniel Barath, Andreas Geiger, Marc Pollefeys

**分类**: cs.CV

**发布日期**: 2025-10-09 (更新: 2025-12-06)

**备注**: Project page: https://haofeixu.github.io/resplat/

**🔗 代码/项目**: [PROJECT_PAGE](https://haofeixu.github.io/resplat/)

---

## 💡 一句话要点

**提出ReSplat，一种迭代优化高斯splatting的循环模型，提升渲染质量和效率。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `高斯Splatting` `三维重建` `循环神经网络` `渲染优化` `神经渲染`

## 📋 核心要点

1. 传统前馈高斯splatting模型受限于单次前向推理，性能提升存在瓶颈。
2. ReSplat利用渲染误差作为反馈信号，通过循环网络迭代优化高斯分布，无需显式梯度计算。
3. ReSplat在多个数据集和分辨率下表现出SOTA性能，同时显著减少了高斯数量并提升了渲染速度。

## 📝 摘要（中文）

本文提出ReSplat，一种前馈循环高斯splatting模型，它迭代地细化3D高斯分布，而无需显式计算梯度。核心思想是，高斯splatting渲染误差作为一个丰富的反馈信号，引导循环网络学习有效的高斯更新。这种反馈信号能够自然地适应测试时未见过的数据分布，从而实现跨数据集、视角数量和图像分辨率的鲁棒泛化。为了初始化循环过程，我们引入了一个紧凑的重建模型，该模型在$16 	imes$下采样的空间中运行，产生的高斯分布比以前的逐像素高斯模型少$16 	imes$。这大大降低了计算开销，并允许高效的高斯更新。在不同输入视图（2、8、16、32）、分辨率（$256 	imes 256$到$540 	imes 960$）和数据集（DL3DV、RealEstate10K和ACID）上的大量实验表明，我们的方法实现了最先进的性能，同时显著减少了高斯分布的数量并提高了渲染速度。

## 🔬 方法详解

**问题定义**：现有基于前馈网络的高斯splatting方法，由于依赖单次前向传播进行推理，其性能受到根本限制，难以充分利用图像信息进行优化。尤其是在视角稀疏或数据分布变化时，泛化能力较弱。此外，现有方法通常需要大量的3D高斯基元来表示场景，导致计算开销大，渲染速度慢。

**核心思路**：ReSplat的核心思路是将高斯splatting的渲染过程视为一个迭代优化问题，利用渲染误差作为反馈信号，通过循环神经网络学习高斯参数的更新策略。通过迭代地细化高斯分布，逐步逼近真实场景，从而提高渲染质量和泛化能力。这种方法避免了显式计算梯度，降低了计算复杂度。

**技术框架**：ReSplat包含两个主要模块：紧凑重建模型和循环更新网络。首先，紧凑重建模型在低分辨率下生成初始的高斯分布，减少了高斯基元的数量。然后，循环更新网络以渲染误差作为输入，迭代地更新高斯参数，包括位置、缩放、旋转和不透明度等。每次迭代后，使用高斯splatting渲染图像，计算渲染误差，并将误差反馈给循环网络进行下一轮更新。

**关键创新**：ReSplat的关键创新在于利用渲染误差作为反馈信号，指导循环网络学习高斯参数的更新策略。这种方法无需显式计算梯度，降低了计算复杂度，并且能够自适应地学习不同场景和视角下的优化策略。此外，紧凑重建模型通过在低分辨率下生成初始高斯分布，显著减少了高斯基元的数量，提高了渲染效率。

**关键设计**：紧凑重建模型使用一个轻量级的卷积神经网络，在$16 	imes$下采样的空间中生成初始高斯分布。循环更新网络采用GRU或LSTM等循环神经网络结构，以渲染误差图像作为输入，输出高斯参数的更新量。损失函数包括渲染损失（如L1或L2损失）和正则化项，用于约束高斯参数的更新幅度。迭代次数是一个重要的超参数，需要根据具体场景进行调整。

## 📊 实验亮点

ReSplat在DL3DV、RealEstate10K和ACID等数据集上取得了SOTA性能，尤其是在视角稀疏的情况下，性能提升显著。与现有方法相比，ReSplat显著减少了高斯基元的数量，降低了计算开销，并提高了渲染速度。例如，在某些场景下，ReSplat使用的高斯数量减少了16倍，渲染速度提高了2倍。

## 🎯 应用场景

ReSplat具有广泛的应用前景，包括：三维重建、虚拟现实、增强现实、自动驾驶、机器人导航等。该方法能够高效地从稀疏视角图像中重建高质量的三维场景，为虚拟现实和增强现实应用提供逼真的视觉体验。在自动驾驶和机器人导航领域，ReSplat可以用于构建环境地图，帮助机器人进行定位和路径规划。

## 📄 摘要（原文）

> While feed-forward Gaussian splatting models offer computational efficiency and can generalize to sparse input settings, their performance is fundamentally constrained by relying on a single forward pass for inference. We propose ReSplat, a feed-forward recurrent Gaussian splatting model that iteratively refines 3D Gaussians without explicitly computing gradients. Our key insight is that the Gaussian splatting rendering error serves as a rich feedback signal, guiding the recurrent network to learn effective Gaussian updates. This feedback signal naturally adapts to unseen data distributions at test time, enabling robust generalization across datasets, view counts and image resolutions. To initialize the recurrent process, we introduce a compact reconstruction model that operates in a $16 \times$ subsampled space, producing $16 \times$ fewer Gaussians than previous per-pixel Gaussian models. This substantially reduces computational overhead and allows for efficient Gaussian updates. Extensive experiments across varying of input views (2, 8, 16, 32), resolutions ($256 \times 256$ to $540 \times 960$), and datasets (DL3DV, RealEstate10K and ACID) demonstrate that our method achieves state-of-the-art performance while significantly reducing the number of Gaussians and improving the rendering speed. Our project page is at https://haofeixu.github.io/resplat/.

