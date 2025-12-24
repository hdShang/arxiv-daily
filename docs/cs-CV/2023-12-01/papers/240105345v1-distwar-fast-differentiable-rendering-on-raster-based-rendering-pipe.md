---
layout: default
title: "DISTWAR: Fast Differentiable Rendering on Raster-based Rendering Pipelines"
---

# DISTWAR: Fast Differentiable Rendering on Raster-based Rendering Pipelines

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2401.05345" class="toolbar-btn" target="_blank">📄 arXiv: 2401.05345v1</a>
  <a href="https://arxiv.org/pdf/2401.05345.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2401.05345v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2401.05345v1', 'DISTWAR: Fast Differentiable Rendering on Raster-based Rendering Pipelines')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sankeerth Durvasula, Adrian Zhao, Fan Chen, Ruofan Liang, Pawan Kumar Sanjaya, Nandita Vijaykumar

**分类**: cs.CV, cs.GR, cs.PF

**发布日期**: 2023-12-01

---

## 💡 一句话要点

**提出DISTWAR以加速光栅化渲染中的原子操作**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `可微渲染` `光栅化` `原子操作` `GPU加速` `计算机视觉` `3D场景重建` `性能优化`

## 📋 核心要点

1. 现有的可微渲染方法在训练过程中，梯度计算阶段由于大量原子操作导致GPU性能瓶颈，影响整体效率。
2. 本文提出DISTWAR，通过在SM子核心实现线程的warp级别归约和在L2原子单元之间分配计算，优化原子操作的执行。
3. 实验结果显示，DISTWAR在光栅化可微渲染任务中实现了平均2.44倍的加速，最高可达5.7倍，显著提升了渲染速度。

## 📝 摘要（中文）

可微渲染是一种重要的视觉计算技术，通过使用梯度下降从2D图像训练3D场景模型。尽管现有方法（如3D高斯点云）在高速度下提供高质量的图像，但训练模型仍然耗时。本文提出DISTWAR，旨在解决GPU上梯度计算阶段的瓶颈，主要通过优化原子操作来提高效率。实验表明，DISTWAR在常用的光栅化可微渲染任务中平均加速2.44倍，最高可达5.7倍。

## 🔬 方法详解

**问题定义**：本文要解决的问题是GPU在可微渲染训练过程中，梯度计算阶段由于大量原子操作导致的性能瓶颈。现有方法在处理这些原子操作时，容易造成L2分区的原子单元过载，从而导致性能下降。

**核心思路**：论文的核心思路是通过优化原子操作的执行方式，减少对GPU资源的占用。具体而言，利用warp级别的线程归约和L2原子单元的分配来提高原子操作的吞吐量。

**技术框架**：DISTWAR的整体架构包括两个主要模块：首先，在SM子核心中进行warp级别的线程归约，以利用线程之间的局部性；其次，将原子计算分配到SM的warp级别归约和L2原子单元之间，以提高计算效率。

**关键创新**：DISTWAR的关键创新在于通过调度具有相同内存更新的线程到SM，同时将其他线程使用L2原子单元，从而有效提升了原子操作的处理速度。这一设计与现有方法的主要区别在于优化了原子操作的调度策略。

**关键设计**：在实现DISTWAR时，采用了现有的warp级别原语，确保了设计的兼容性和高效性。关键参数设置包括线程归约的粒度和原子操作的调度策略，这些设计细节直接影响了性能提升的幅度。

## 📊 实验亮点

实验结果表明，DISTWAR在广泛使用的光栅化可微渲染任务中实现了显著的性能提升，平均加速达到2.44倍，最高可达5.7倍。这一成果展示了DISTWAR在优化GPU原子操作方面的有效性，为可微渲染技术的进一步发展奠定了基础。

## 🎯 应用场景

DISTWAR的研究成果在计算机视觉、机器人以及虚拟现实等领域具有广泛的应用潜力。通过加速可微渲染过程，能够更快速地生成高质量的3D场景，提升图像合成、场景重建等任务的效率，进而推动相关技术的发展和应用。未来，DISTWAR可能为实时渲染和交互式应用提供更强大的支持。

## 📄 摘要（原文）

> Differentiable rendering is a technique used in an important emerging class of visual computing applications that involves representing a 3D scene as a model that is trained from 2D images using gradient descent. Recent works (e.g. 3D Gaussian Splatting) use a rasterization pipeline to enable rendering high quality photo-realistic imagery at high speeds from these learned 3D models. These methods have been demonstrated to be very promising, providing state-of-art quality for many important tasks. However, training a model to represent a scene is still a time-consuming task even when using powerful GPUs. In this work, we observe that the gradient computation phase during training is a significant bottleneck on GPUs due to the large number of atomic operations that need to be processed. These atomic operations overwhelm atomic units in the L2 partitions causing stalls. To address this challenge, we leverage the observations that during the gradient computation: (1) for most warps, all threads atomically update the same memory locations; and (2) warps generate varying amounts of atomic traffic (since some threads may be inactive). We propose DISTWAR, a software-approach to accelerate atomic operations based on two key ideas: First, we enable warp-level reduction of threads at the SM sub-cores using registers to leverage the locality in intra-warp atomic updates. Second, we distribute the atomic computation between the warp-level reduction at the SM and the L2 atomic units to increase the throughput of atomic computation. Warps with many threads performing atomic updates to the same memory locations are scheduled at the SM, and the rest using L2 atomic units. We implement DISTWAR using existing warp-level primitives. We evaluate DISTWAR on widely used raster-based differentiable rendering workloads. We demonstrate significant speedups of 2.44x on average (up to 5.7x).

