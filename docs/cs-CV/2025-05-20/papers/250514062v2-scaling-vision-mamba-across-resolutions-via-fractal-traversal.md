---
layout: default
title: Scaling Vision Mamba Across Resolutions via Fractal Traversal
---

# Scaling Vision Mamba Across Resolutions via Fractal Traversal

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14062" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14062v2</a>
  <a href="https://arxiv.org/pdf/2505.14062.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14062v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14062v2', 'Scaling Vision Mamba Across Resolutions via Fractal Traversal')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bo Li, Haoke Xiao, Lv Tang

**分类**: cs.CV

**发布日期**: 2025-05-20 (更新: 2025-08-13)

---

## 💡 一句话要点

**提出FractalMamba++以解决视觉输入分辨率适应性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉模型` `补丁序列化` `高分辨率适应性` `分形技术` `全局上下文传播` `局部邻接性恢复` `计算机视觉` `深度学习`

## 📋 核心要点

1. 现有的Vision Mamba模型在视觉输入的2D到1D补丁序列化过程中存在局部空间连续性破坏的问题，导致跨尺度泛化能力不足。
2. 本文提出FractalMamba++，通过希尔伯特曲线实现基于分形的补丁序列化，保持空间局部性，并引入CSR机制和PRC模块以增强全局上下文传播和恢复局部邻接性。
3. 实验结果显示，FractalMamba++在多项下游任务中表现优异，尤其在高分辨率输入下，相较于之前的Mamba基础模型有显著提升。

## 📝 摘要（中文）

Vision Mamba作为一种新兴的视觉模型，虽然在序列长度上具有线性复杂度和强大的建模能力，但在适应视觉输入时面临2D到1D补丁序列化的挑战，以及在不同输入分辨率下的可扩展性不足。现有的序列化策略如光栅扫描破坏了局部空间连续性，限制了模型的跨尺度泛化能力。为此，本文提出FractalMamba++，利用基于分形的补丁序列化方法，通过希尔伯特曲线保持空间局部性，并实现无缝的分辨率适应性。此外，论文引入了跨状态路由（CSR）机制，以增强高分辨率输入中的全局上下文传播，并提出了位置关系捕获（PRC）模块，以恢复因曲线拐点而中断的局部邻接性。实验结果表明，FractalMamba++在图像分类、语义分割和目标检测等多项下游任务中，均显著优于之前的Mamba基础模型，尤其在高分辨率设置下表现尤为突出。

## 🔬 方法详解

**问题定义**：本文旨在解决Vision Mamba在视觉输入适应性方面的不足，特别是2D到1D补丁序列化导致的局部空间连续性破坏和跨尺度泛化能力不足的问题。

**核心思路**：FractalMamba++通过引入基于希尔伯特曲线的分形补丁序列化方法，保持了空间局部性，并通过CSR机制增强了高分辨率输入中的全局上下文传播，此外，PRC模块则恢复了因曲线拐点而中断的局部邻接性。

**技术框架**：整体架构包括三个主要模块：分形补丁序列化模块、跨状态路由（CSR）模块和位置关系捕获（PRC）模块。分形补丁序列化模块负责将输入图像转换为补丁，CSR模块则在高分辨率输入中增强全局上下文的传播，而PRC模块则修复局部邻接性。

**关键创新**：最重要的创新在于引入了基于希尔伯特曲线的补丁序列化方法和CSR机制，这与现有的光栅扫描方法本质上不同，能够更好地保持空间局部性和全局上下文。

**关键设计**：在设计中，补丁的大小、CSR机制中的状态选择策略以及PRC模块的具体实现细节都是关键参数，这些设计确保了模型在高分辨率输入下的有效性和鲁棒性。

## 📊 实验亮点

在多项下游任务的实验中，FractalMamba++在图像分类、语义分割和目标检测等任务上均表现出色，尤其在高分辨率设置下，相较于之前的Mamba基础模型，性能提升幅度显著，具体数据未提供，但实验结果表明其具有明显优势。

## 🎯 应用场景

FractalMamba++的研究成果在多个领域具有广泛的应用潜力，包括计算机视觉中的图像分类、语义分割和目标检测等任务。其高效的分辨率适应性和强大的建模能力使其在处理高分辨率图像时表现出色，未来可望在自动驾驶、医疗影像分析和智能监控等实际场景中发挥重要作用。

## 📄 摘要（原文）

> Vision Mamba has recently emerged as a promising alternative to Transformer-based architectures, offering linear complexity in sequence length while maintaining strong modeling capacity. However, its adaptation to visual inputs is hindered by challenges in 2D-to-1D patch serialization and weak scalability across input resolutions. Existing serialization strategies such as raster scanning disrupt local spatial continuity and limit the model's ability to generalize across scales. In this paper, we propose FractalMamba++, a robust vision backbone that leverages fractal-based patch serialization via Hilbert curves to preserve spatial locality and enable seamless resolution adaptability. To address long-range dependency fading in high-resolution inputs, we further introduce a Cross-State Routing (CSR) mechanism that enhances global context propagation through selective state reuse. Additionally, we propose a Positional-Relation Capture (PRC) module to recover local adjacency disrupted by curve inflection points. Extensive experiments across diverse downstream tasks, including image classification, semantic segmentation and object detection, demonstrate that FractalMamba++ consistently outperforms previous Mamba-based backbones, with particularly notable gains under high-resolution settings.

