---
layout: default
title: ADC-GS: Anchor-Driven Deformable and Compressed Gaussian Splatting for Dynamic Scene Reconstruction
---

# ADC-GS: Anchor-Driven Deformable and Compressed Gaussian Splatting for Dynamic Scene Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08196" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08196v1</a>
  <a href="https://arxiv.org/pdf/2505.08196.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08196v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08196v1', 'ADC-GS: Anchor-Driven Deformable and Compressed Gaussian Splatting for Dynamic Scene Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: He Huang, Qi Yang, Mufan Liu, Yiling Xu, Zhu Li

**分类**: cs.CV

**发布日期**: 2025-05-13

**🔗 代码/项目**: [GITHUB](https://github.com/H-Huang774/ADC-GS.git)

---

## 💡 一句话要点

**提出ADC-GS以解决动态场景重建中的冗余问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态场景重建` `高斯点云` `锚点结构` `运动捕捉` `率失真优化` `渲染效率` `存储效率`

## 📋 核心要点

1. 现有的4D高斯点云方法在动态场景重建中存在冗余变形问题，导致性能不佳。
2. 本文提出ADC-GS，通过锚点结构和时间重要性优化策略来提高高斯原语的表示效率。
3. 实验结果显示，ADC-GS在渲染速度上提升300%-800%，并在存储效率上达到最先进水平。

## 📝 摘要（中文）

现有的4D高斯点云方法依赖于从标准空间到目标帧的每个高斯的变形，这忽视了相邻高斯原语之间的冗余，导致性能不佳。为了解决这一局限性，本文提出了基于锚点的可变形和压缩高斯点云（ADC-GS），为动态场景重建提供了一种紧凑高效的表示。具体而言，ADC-GS在标准空间中将高斯原语组织成基于锚点的结构，并通过基于时间重要性的锚点优化策略进行增强。为了减少变形冗余，ADC-GS引入了分层的粗到细的管道，以捕捉不同粒度的运动。此外，采用率失真优化以实现比特率消耗与表示保真度之间的最佳平衡。实验结果表明，ADC-GS在渲染速度上比每个高斯变形方法提高了300%-800%，同时在不妥协渲染质量的情况下实现了最先进的存储效率。

## 🔬 方法详解

**问题定义**：现有的4D高斯点云方法在动态场景重建中存在冗余变形问题，尤其是相邻高斯原语之间的冗余未被有效利用，导致性能不佳。

**核心思路**：本文提出的ADC-GS通过引入锚点结构和基于时间的重要性优化策略，旨在减少冗余变形并提高表示效率。这样的设计可以更好地捕捉动态场景中的运动特征。

**技术框架**：ADC-GS的整体架构包括高斯原语的锚点组织、时间重要性锚点优化、分层粗到细的运动捕捉管道，以及率失真优化模块。各个模块协同工作，以实现高效的动态场景重建。

**关键创新**：ADC-GS的主要创新在于其锚点驱动的结构和分层运动捕捉策略，这与传统的每个高斯变形方法有本质区别，显著减少了冗余并提高了效率。

**关键设计**：在设计中，ADC-GS采用了分层的运动捕捉策略，结合了多种粒度的运动信息，并通过率失真优化来平衡比特率和表示质量，确保了高效的存储和渲染性能。

## 📊 实验亮点

实验结果表明，ADC-GS在渲染速度上比传统的每个高斯变形方法提升了300%-800%，同时在存储效率上达到了最先进水平，且渲染质量未受到影响。这一成果展示了ADC-GS在动态场景重建中的显著优势。

## 🎯 应用场景

该研究在动态场景重建领域具有广泛的应用潜力，特别是在虚拟现实、增强现实和计算机动画等领域。通过提高渲染速度和存储效率，ADC-GS能够为实时应用提供更好的用户体验，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Existing 4D Gaussian Splatting methods rely on per-Gaussian deformation from a canonical space to target frames, which overlooks redundancy among adjacent Gaussian primitives and results in suboptimal performance. To address this limitation, we propose Anchor-Driven Deformable and Compressed Gaussian Splatting (ADC-GS), a compact and efficient representation for dynamic scene reconstruction. Specifically, ADC-GS organizes Gaussian primitives into an anchor-based structure within the canonical space, enhanced by a temporal significance-based anchor refinement strategy. To reduce deformation redundancy, ADC-GS introduces a hierarchical coarse-to-fine pipeline that captures motions at varying granularities. Moreover, a rate-distortion optimization is adopted to achieve an optimal balance between bitrate consumption and representation fidelity. Experimental results demonstrate that ADC-GS outperforms the per-Gaussian deformation approaches in rendering speed by 300%-800% while achieving state-of-the-art storage efficiency without compromising rendering quality. The code is released at https://github.com/H-Huang774/ADC-GS.git.

