---
layout: default
title: "GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading"
---

# GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15645" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15645v1</a>
  <a href="https://arxiv.org/pdf/2509.15645.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15645v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15645v1', 'GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Donghyun Lee, Dawoon Jeong, Jae W. Lee, Hongil Yoon

**分类**: cs.CV

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**GS-Scale：通过主机卸载解锁大规模3D高斯溅射训练**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `大规模场景` `主机卸载` `GPU内存优化` `渲染` `优化器更新` `视锥剔除`

## 📋 核心要点

1. 现有3D高斯溅射方法在训练大规模场景时，面临着GPU内存需求过高的挑战，限制了模型质量和场景复杂度。
2. GS-Scale通过将高斯分布存储在主机内存中，并仅在需要时将子集传输到GPU，显著降低了GPU内存占用。
3. 实验表明，GS-Scale在降低GPU内存需求的同时，保持了与GPU训练相当的速度，并显著提升了LPIPS指标。

## 📝 摘要（中文）

3D高斯溅射通过提供高质量的视觉效果和快速的渲染速度，彻底改变了图形渲染。然而，由于存储参数、梯度和优化器状态需要大量的内存，快速耗尽GPU内存，因此高质量地训练大规模场景仍然具有挑战性。为了解决这些限制，我们提出了GS-Scale，一个快速且内存高效的3D高斯溅射训练系统。GS-Scale将所有高斯分布存储在主机内存中，仅在每次前向和后向传递时按需将子集传输到GPU。虽然这显著降低了GPU内存使用量，但需要CPU执行视锥剔除和优化器更新，由于CPU有限的计算和内存带宽，导致速度减慢。为了缓解这个问题，GS-Scale采用了三个系统级优化：（1）选择性卸载几何参数以实现快速视锥剔除，（2）参数转发以流水线化CPU优化器更新与GPU计算，以及（3）延迟优化器更新以最小化对零梯度高斯分布的不必要内存访问。我们对大规模数据集的广泛评估表明，GS-Scale显著降低了3.3-5.6倍的GPU内存需求，同时实现了与没有主机卸载的GPU相当的训练速度。这使得在消费级GPU上进行大规模3D高斯溅射训练成为可能；例如，GS-Scale可以在RTX 4070 Mobile GPU上将高斯分布的数量从400万扩展到1800万，从而提高23-35%的LPIPS（学习的感知图像块相似度）。

## 🔬 方法详解

**问题定义**：现有3D高斯溅射方法在处理大规模场景时，由于需要存储大量的参数、梯度和优化器状态，GPU内存消耗巨大，导致无法在高配置下训练，限制了场景的规模和渲染质量。现有方法难以在消费级GPU上训练大规模高斯模型。

**核心思路**：GS-Scale的核心思路是将所有高斯参数存储在主机（CPU）内存中，仅在每次前向和后向传播时，将当前需要的参数子集传输到GPU。这样可以显著降低GPU内存占用，从而支持更大规模的场景和更高质量的渲染。为了弥补CPU计算能力较弱的缺点，论文提出了多种系统级优化。

**技术框架**：GS-Scale的整体框架包括以下几个主要阶段：
1.  **数据准备**：将所有高斯参数存储在主机内存中。
2.  **视锥剔除**：在CPU上进行视锥剔除，确定需要参与当前渲染的高斯分布子集。为了加速视锥剔除，论文提出了选择性卸载几何参数的优化。
3.  **数据传输**：将选定的高斯参数从主机内存传输到GPU内存。
4.  **前向传播和后向传播**：在GPU上进行前向和后向传播计算。
5.  **优化器更新**：在CPU上进行优化器更新。为了加速优化器更新，论文提出了参数转发和延迟优化器更新的优化。

**关键创新**：GS-Scale的关键创新在于：
1.  **主机卸载**：将高斯参数存储在主机内存中，显著降低GPU内存占用。
2.  **选择性卸载几何参数**：加速CPU上的视锥剔除。
3.  **参数转发**：流水线化CPU优化器更新与GPU计算。
4.  **延迟优化器更新**：减少不必要的内存访问。

**关键设计**：
1.  **选择性卸载几何参数**：仅将位置和缩放等几何参数卸载到CPU，用于快速视锥剔除。
2.  **参数转发**：在GPU计算的同时，将梯度信息转发到CPU，以便CPU可以并行地进行优化器更新。
3.  **延迟优化器更新**：仅对梯度不为零的高斯分布进行优化器更新，减少不必要的内存访问。

## 📊 实验亮点

GS-Scale在大型数据集上进行了广泛的评估，结果表明，GS-Scale可以将GPU内存需求降低3.3-5.6倍，同时保持与GPU训练相当的速度。例如，在RTX 4070 Mobile GPU上，GS-Scale可以将高斯分布的数量从400万扩展到1800万，从而提高23-35%的LPIPS。

## 🎯 应用场景

GS-Scale的潜在应用领域包括：大规模城市建模、虚拟现实/增强现实、游戏开发、自动驾驶等。该研究降低了3D高斯溅射训练的硬件门槛，使得在消费级GPU上训练大规模场景成为可能，从而加速了相关技术的普及和应用。未来，该技术可以进一步扩展到动态场景和实时渲染等领域。

## 📄 摘要（原文）

> The advent of 3D Gaussian Splatting has revolutionized graphics rendering by delivering high visual quality and fast rendering speeds. However, training large-scale scenes at high quality remains challenging due to the substantial memory demands required to store parameters, gradients, and optimizer states, which can quickly overwhelm GPU memory. To address these limitations, we propose GS-Scale, a fast and memory-efficient training system for 3D Gaussian Splatting. GS-Scale stores all Gaussians in host memory, transferring only a subset to the GPU on demand for each forward and backward pass. While this dramatically reduces GPU memory usage, it requires frustum culling and optimizer updates to be executed on the CPU, introducing slowdowns due to CPU's limited compute and memory bandwidth. To mitigate this, GS-Scale employs three system-level optimizations: (1) selective offloading of geometric parameters for fast frustum culling, (2) parameter forwarding to pipeline CPU optimizer updates with GPU computation, and (3) deferred optimizer update to minimize unnecessary memory accesses for Gaussians with zero gradients. Our extensive evaluations on large-scale datasets demonstrate that GS-Scale significantly lowers GPU memory demands by 3.3-5.6x, while achieving training speeds comparable to GPU without host offloading. This enables large-scale 3D Gaussian Splatting training on consumer-grade GPUs; for instance, GS-Scale can scale the number of Gaussians from 4 million to 18 million on an RTX 4070 Mobile GPU, leading to 23-35% LPIPS (learned perceptual image patch similarity) improvement.

