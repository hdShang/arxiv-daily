---
layout: default
title: "Proxy-GS: Efficient 3D Gaussian Splatting via Proxy Mesh"
---

# Proxy-GS: Efficient 3D Gaussian Splatting via Proxy Mesh

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24421" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24421v2</a>
  <a href="https://arxiv.org/pdf/2509.24421.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24421v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24421v2', 'Proxy-GS: Efficient 3D Gaussian Splatting via Proxy Mesh')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanyuan Gao, Yuning Gong, Yifei Liu, Li Jingfeng, Zhihang Zhong, Dingwen Zhang, Yanci Zhang, Dan Xu, Xiao Sun

**分类**: cs.CV

**发布日期**: 2025-09-29 (更新: 2025-10-01)

---

## 💡 一句话要点

**Proxy-GS：利用代理网格实现高效的3D高斯溅射，提升渲染速度与质量**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `遮挡感知` `代理网格` `高效渲染` `大规模场景`

## 📋 核心要点

1. 现有3D高斯溅射方法在高遮挡场景中存在大量冗余计算，缺乏有效的遮挡感知机制。
2. Proxy-GS通过引入快速代理系统生成精确的遮挡深度图，实现高斯原语的遮挡感知剔除和训练指导。
3. 实验表明，Proxy-GS在高遮挡场景下显著提升了渲染速度和质量，加速比超过Octree-GS 2.5倍。

## 📝 摘要（中文）

本文提出了一种名为Proxy-GS的新型3D高斯溅射（3DGS）渲染管线，旨在解决现有方法在高遮挡场景下存在的冗余计算问题。Proxy-GS利用一个快速代理系统，在1毫秒内生成分辨率为1000x1000的精确遮挡深度图，从而实现高斯原语的遮挡感知。该代理系统有两个作用：一是指导锚点和高斯原语的剔除，加速渲染；二是指导训练过程中的稠密化，避免遮挡区域的不一致性，提高渲染质量。在MatrixCity Streets等高遮挡场景中，Proxy-GS不仅增强了基于MLP的高斯溅射的渲染能力，还显著提高了渲染速度，相比Octree-GS实现了超过2.5倍的加速，并持续提供更高的渲染质量。代码将在接收后公开。

## 🔬 方法详解

**问题定义**：现有基于3D高斯溅射的方法，尤其是在大规模和高遮挡场景中，存在大量的冗余高斯原语，导致渲染效率低下。虽然一些剪枝和LOD技术被提出，但由于缺乏有效的遮挡感知，仍然存在显著的冗余计算，限制了渲染速度和质量。

**核心思路**：Proxy-GS的核心思路是利用一个快速生成的代理网格来提供遮挡信息，从而指导高斯原语的剔除和训练过程中的稠密化。通过遮挡感知，可以避免在被遮挡区域生成不必要的高斯原语，并加速渲染过程。

**技术框架**：Proxy-GS包含以下主要模块：1) 快速代理系统：用于生成精确的遮挡深度图。2) 遮挡感知剔除：利用代理网格的深度信息剔除被遮挡的高斯原语。3) 遮挡感知稠密化：在训练过程中，利用代理网格的深度信息指导高斯原语的稠密化，避免在遮挡区域产生不一致性。整体流程是先使用代理网格进行遮挡剔除，然后进行渲染，并在训练过程中利用代理网格指导稠密化。

**关键创新**：Proxy-GS的关键创新在于引入了一个快速且精确的代理系统，能够实时生成遮挡深度图，从而实现对高斯原语的遮挡感知。与现有方法相比，Proxy-GS能够更有效地减少冗余计算，提高渲染速度和质量。

**关键设计**：代理系统能够以低于1毫秒的速度生成1000x1000分辨率的深度图。具体实现细节（如代理网格的构建方式、深度图的生成算法、以及遮挡剔除和稠密化的具体策略）在论文中应该有更详细的描述，但摘要中未提供。损失函数和网络结构等细节也需要在论文中查找。

## 📊 实验亮点

Proxy-GS在MatrixCity Streets数据集上取得了显著的性能提升，渲染速度比Octree-GS快2.5倍以上，并且渲染质量也得到了大幅提升。这些结果表明，Proxy-GS在高遮挡场景下具有强大的渲染能力和效率优势。具体的量化指标（如PSNR、SSIM等）需要在论文中查找。

## 🎯 应用场景

Proxy-GS在需要高效渲染大规模、高遮挡三维场景的应用中具有广泛的应用前景，例如城市建模、自动驾驶仿真、游戏开发、虚拟现实和增强现实等。通过提高渲染速度和质量，Proxy-GS可以为用户提供更流畅、更逼真的视觉体验，并降低计算资源的需求，从而促进这些技术的普及和应用。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as an efficient approach for achieving photorealistic rendering. Recent MLP-based variants further improve visual fidelity but introduce substantial decoding overhead during rendering. To alleviate computation cost, several pruning strategies and level-of-detail (LOD) techniques have been introduced, aiming to effectively reduce the number of Gaussian primitives in large-scale scenes. However, our analysis reveals that significant redundancy still remains due to the lack of occlusion awareness. In this work, we propose Proxy-GS, a novel pipeline that exploits a proxy to introduce Gaussian occlusion awareness from any view. At the core of our approach is a fast proxy system capable of producing precise occlusion depth maps at a resolution of 1000x1000 under 1ms. This proxy serves two roles: first, it guides the culling of anchors and Gaussians to accelerate rendering speed. Second, it guides the densification towards surfaces during training, avoiding inconsistencies in occluded regions, and improving the rendering quality. In heavily occluded scenarios, such as the MatrixCity Streets dataset, Proxy-GS not only equips MLP-based Gaussian splatting with stronger rendering capability but also achieves faster rendering speed. Specifically, it achieves more than 2.5x speedup over Octree-GS, and consistently delivers substantially higher rendering quality. Code will be public upon acceptance.

