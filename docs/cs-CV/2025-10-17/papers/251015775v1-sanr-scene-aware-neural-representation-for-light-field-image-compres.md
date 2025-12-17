---
layout: default
title: SANR: Scene-Aware Neural Representation for Light Field Image Compression with Rate-Distortion Optimization
---

# SANR: Scene-Aware Neural Representation for Light Field Image Compression with Rate-Distortion Optimization

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.15775" target="_blank" class="toolbar-btn">arXiv: 2510.15775v1</a>
    <a href="https://arxiv.org/pdf/2510.15775.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15775v1" 
            onclick="toggleFavorite(this, '2510.15775v1', 'SANR: Scene-Aware Neural Representation for Light Field Image Compression with Rate-Distortion Optimization')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Gai Zhang, Xinfeng Zhang, Lv Tang, Hongyu An, Li Zhang, Qingming Huang

**分类**: eess.IV, cs.CV, cs.MM

**发布日期**: 2025-10-17

---

## 💡 一句话要点

**提出SANR：一种场景感知神经表示光场图像压缩框架，实现率失真优化。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `光场图像压缩` `神经表示` `场景感知` `率失真优化` `量化感知训练`

## 📋 核心要点

1. 现有光场图像压缩方法忽略了场景结构的显式建模，且缺乏端到端的率失真优化，导致压缩效率受限。
2. SANR通过分层场景建模块捕获场景内在结构，并首次将熵约束量化感知训练（QAT）引入神经表示光场图像压缩。
3. 实验结果表明，SANR在率失真性能上显著优于现有技术，相对于HEVC节省了65.62%的BD-rate。

## 📝 摘要（中文）

光场图像捕捉多视点场景信息，在3D场景重建中起着关键作用。然而，其高维特性导致数据量巨大，给实际存储和传输场景中的高效压缩带来了重大挑战。虽然基于神经表示的方法在光场图像压缩中显示出前景，但大多数方法依赖于通过隐式神经表示（INR）的直接坐标到像素的映射，通常忽略了场景结构的显式建模。此外，它们通常缺乏端到端的率失真优化，限制了其压缩效率。为了解决这些限制，我们提出了SANR，一个用于光场图像压缩的场景感知神经表示框架，具有端到端的率失真优化。对于场景感知，SANR引入了一个分层场景建模块，该块利用多尺度潜在代码来捕获内在的场景结构，从而减少了INR输入坐标和目标光场图像之间的信息差距。从压缩的角度来看，SANR是第一个将熵约束量化感知训练（QAT）纳入基于神经表示的光场图像压缩中的方法，从而实现了端到端的率失真优化。大量的实验结果表明，SANR在率失真性能方面显著优于最先进的技术，相对于HEVC节省了65.62%的BD-rate。

## 🔬 方法详解

**问题定义**：光场图像数据量巨大，高效压缩是关键挑战。现有基于隐式神经表示(INR)的光场图像压缩方法，通常忽略场景结构的显式建模，且缺乏端到端的率失真优化，导致压缩效率不高。

**核心思路**：SANR的核心思路是利用场景感知的分层神经表示，显式地建模场景结构，从而减少INR输入坐标和目标光场图像之间的信息差距。同时，引入熵约束量化感知训练（QAT），实现端到端的率失真优化。

**技术框架**：SANR框架主要包含两个核心模块：分层场景建模块和熵约束量化感知训练。首先，分层场景建模块利用多尺度潜在代码捕获场景结构。然后，通过INR将坐标映射到像素值。最后，使用QAT进行端到端的率失真优化。

**关键创新**：SANR的关键创新在于：1) 引入分层场景建模块，显式建模场景结构，增强场景感知能力；2) 首次将熵约束量化感知训练（QAT）应用于基于神经表示的光场图像压缩，实现端到端的率失真优化。

**关键设计**：分层场景建模块采用多尺度卷积神经网络提取潜在代码，并通过注意力机制融合不同尺度的特征。熵约束量化感知训练使用拉格朗日乘子平衡率和失真，损失函数包括率损失和失真损失。网络结构采用MLP，并针对光场图像的特性进行了优化。

## 📊 实验亮点

SANR在率失真性能方面显著优于现有技术，实验结果表明，相对于HEVC，SANR实现了65.62%的BD-rate节省。这表明SANR在光场图像压缩方面具有显著的优势，能够有效降低存储和传输成本。

## 🎯 应用场景

该研究成果可应用于3D场景重建、虚拟现实、增强现实、自由视点视频等领域。通过高效压缩光场图像，可以降低存储和传输成本，提升用户体验，加速相关技术的普及和应用。未来，该方法有望扩展到其他高维数据的压缩任务中。

## 📄 摘要（原文）

> Light field images capture multi-view scene information and play a crucial role in 3D scene reconstruction. However, their high-dimensional nature results in enormous data volumes, posing a significant challenge for efficient compression in practical storage and transmission scenarios. Although neural representation-based methods have shown promise in light field image compression, most approaches rely on direct coordinate-to-pixel mapping through implicit neural representation (INR), often neglecting the explicit modeling of scene structure. Moreover, they typically lack end-to-end rate-distortion optimization, limiting their compression efficiency. To address these limitations, we propose SANR, a Scene-Aware Neural Representation framework for light field image compression with end-to-end rate-distortion optimization. For scene awareness, SANR introduces a hierarchical scene modeling block that leverages multi-scale latent codes to capture intrinsic scene structures, thereby reducing the information gap between INR input coordinates and the target light field image. From a compression perspective, SANR is the first to incorporate entropy-constrained quantization-aware training (QAT) into neural representation-based light field image compression, enabling end-to-end rate-distortion optimization. Extensive experiment results demonstrate that SANR significantly outperforms state-of-the-art techniques regarding rate-distortion performance with a 65.62\% BD-rate saving against HEVC.

