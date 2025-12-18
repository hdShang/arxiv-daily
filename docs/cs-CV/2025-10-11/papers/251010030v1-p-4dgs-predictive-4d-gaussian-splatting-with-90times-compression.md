---
layout: default
title: P-4DGS: Predictive 4D Gaussian Splatting with 90$\times$ Compression
---

# P-4DGS: Predictive 4D Gaussian Splatting with 90$\times$ Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10030" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10030v1</a>
  <a href="https://arxiv.org/pdf/2510.10030.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10030v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.10030v1', 'P-4DGS: Predictive 4D Gaussian Splatting with 90$\times$ Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Henan Wang, Hanxin Zhu, Xinliang Gong, Tianyu He, Xin Li, Zhibo Chen

**分类**: cs.CV

**发布日期**: 2025-10-11

---

## 💡 一句话要点

**提出P-4DGS以解决动态场景建模中的高内存消耗问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态场景重建` `3D Gaussian Splatting` `压缩技术` `空间-时间预测` `虚拟现实` `增强现实` `实时渲染`

## 📋 核心要点

1. 现有动态场景重建方法未能有效利用时间和空间冗余，导致内存消耗过高。
2. 提出P-4DGS，通过空间-时间预测模块和自适应量化策略，提升4D场景建模的压缩效率。
3. 实验表明，P-4DGS在重建质量和渲染速度上均优于现有方法，存储占用显著降低。

## 📝 摘要（中文）

3D Gaussian Splatting (3DGS)因其优越的场景表示能力和实时渲染性能而受到广泛关注，尤其是在动态3D场景重建中。然而，现有算法往往忽视动态场景中的时间和空间冗余，导致内存消耗过大。为此，本文提出了一种新颖的动态3DGS表示方法P-4DGS，利用空间-时间预测模块和自适应量化策略，显著提高了4D场景建模的压缩效率。实验结果表明，P-4DGS在合成和真实场景中均实现了最先进的重建质量和最快的渲染速度，存储占用仅约1MB，分别实现了40倍和90倍的压缩。

## 🔬 方法详解

**问题定义**：本文旨在解决动态场景建模中存在的高内存消耗问题。现有的3D Gaussian Splatting方法未能充分利用动态场景中的时间和空间冗余，导致内存使用效率低下。

**核心思路**：P-4DGS的核心思路是借鉴视频压缩中的帧内和帧间预测技术，设计一个基于3D锚点的空间-时间预测模块，以充分挖掘不同3D Gaussian原语之间的空间-时间相关性。

**技术框架**：整体架构包括空间-时间预测模块和自适应量化策略。首先，通过预测模块处理3D锚点，随后结合上下文熵编码进一步压缩数据。

**关键创新**：最重要的创新在于引入了空间-时间预测机制和上下文熵编码策略，这与现有方法的静态处理方式形成了鲜明对比，显著提高了压缩效率。

**关键设计**：在参数设置上，采用了适应性量化策略，并在损失函数中引入了对重建质量的优化目标，确保在压缩过程中尽量保留重要信息。

## 📊 实验亮点

实验结果显示，P-4DGS在合成场景中实现了最高40倍的压缩，在真实场景中更是达到了90倍的压缩，同时保持了最先进的重建质量和最快的渲染速度，存储占用仅约1MB，展现出卓越的性能。

## 🎯 应用场景

该研究在动态场景重建、虚拟现实、增强现实等领域具有广泛的应用潜力。通过降低内存消耗，P-4DGS能够支持更复杂的场景建模和实时渲染，为用户提供更流畅的体验，推动相关技术的发展。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has garnered significant attention due to its superior scene representation fidelity and real-time rendering performance, especially for dynamic 3D scene reconstruction (\textit{i.e.}, 4D reconstruction). However, despite achieving promising results, most existing algorithms overlook the substantial temporal and spatial redundancies inherent in dynamic scenes, leading to prohibitive memory consumption. To address this, we propose P-4DGS, a novel dynamic 3DGS representation for compact 4D scene modeling. Inspired by intra- and inter-frame prediction techniques commonly used in video compression, we first design a 3D anchor point-based spatial-temporal prediction module to fully exploit the spatial-temporal correlations across different 3D Gaussian primitives. Subsequently, we employ an adaptive quantization strategy combined with context-based entropy coding to further reduce the size of the 3D anchor points, thereby achieving enhanced compression efficiency. To evaluate the rate-distortion performance of our proposed P-4DGS in comparison with other dynamic 3DGS representations, we conduct extensive experiments on both synthetic and real-world datasets. Experimental results demonstrate that our approach achieves state-of-the-art reconstruction quality and the fastest rendering speed, with a remarkably low storage footprint (around \textbf{1MB} on average), achieving up to \textbf{40$\times$} and \textbf{90$\times$} compression on synthetic and real-world scenes, respectively.

