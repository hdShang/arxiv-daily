---
layout: default
title: MAFNet:Multi-frequency Adaptive Fusion Network for Real-time Stereo Matching
---

# MAFNet:Multi-frequency Adaptive Fusion Network for Real-time Stereo Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04358" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04358v1</a>
  <a href="https://arxiv.org/pdf/2512.04358.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04358v1" onclick="toggleFavorite(this, '2512.04358v1', 'MAFNet:Multi-frequency Adaptive Fusion Network for Real-time Stereo Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ao Xu, Rujin Zhao, Xiong Xu, Boceng Huang, Yujia Jia, Hongfeng Long, Fuxuan Chen, Zilong Cao, Fangyuan Chen

**分类**: cs.CV

**发布日期**: 2025-12-04

---

## 💡 一句话要点

**提出MAFNet，通过多频自适应融合网络实现实时高精度立体匹配**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `立体匹配` `深度估计` `实时性` `频域分析` `注意力机制`

## 📋 核心要点

1. 现有立体匹配方法在计算代价体或建模非局部上下文信息方面存在不足，难以在移动设备上实现实时应用。
2. MAFNet通过自适应频域滤波注意力模块分解代价体，并利用Linformer低秩注意力机制融合高低频信息，实现高效视差估计。
3. 实验表明，MAFNet在Scene Flow和KITTI 2015数据集上优于现有实时方法，实现了精度和实时性的平衡。

## 📝 摘要（中文）

现有的立体匹配网络通常依赖于基于3D卷积的代价体构建或基于迭代优化的形变方法。前者在代价聚合过程中产生显著的计算开销，而后者通常缺乏建模非局部上下文信息的能力。这些方法在资源受限的移动设备上的兼容性较差，限制了它们在实时应用中的部署。为了解决这个问题，我们提出了一种多频自适应融合网络(MAFNet)，它仅使用高效的2D卷积即可生成高质量的视差图。具体来说，我们设计了一个自适应频域滤波注意力模块，将完整的代价体分解为高频和低频体，分别执行频率感知的特征聚合。随后，我们引入了一种基于Linformer的低秩注意力机制，自适应地融合高频和低频信息，从而产生更鲁棒的视差估计。大量的实验表明，所提出的MAFNet在Scene Flow和KITTI 2015等公共数据集上显著优于现有的实时方法，在精度和实时性能之间取得了良好的平衡。

## 🔬 方法详解

**问题定义**：现有立体匹配网络，如基于3D卷积代价体的方法，计算量大，难以实时；基于形变优化的方法，缺乏非局部上下文建模能力。这些问题限制了它们在移动设备等资源受限平台上的应用。

**核心思路**：将代价体分解为高频和低频部分，分别进行处理，然后自适应地融合它们。这种方法旨在降低计算复杂度，同时保留重要的频率信息，从而提高精度和效率。

**技术框架**：MAFNet包含以下主要模块：1) 特征提取网络（未明确说明具体网络结构，但推测为常见的卷积神经网络）；2) 自适应频域滤波注意力模块，用于将代价体分解为高频和低频部分，并进行频率感知的特征聚合；3) 基于Linformer的低秩注意力机制，用于自适应融合高频和低频信息；4) 视差回归层，用于预测最终的视差图。

**关键创新**：主要创新点在于：1) 提出自适应频域滤波注意力模块，将代价体分解为高频和低频部分，分别处理；2) 使用Linformer低秩注意力机制，降低计算复杂度，同时实现高低频信息的有效融合。

**关键设计**：1) 自适应频域滤波注意力模块的具体实现细节（例如，如何进行频率分解，如何设计频率感知的特征聚合方式）未知；2) Linformer低秩注意力机制的具体参数设置未知；3) 损失函数的设计未知；4) 特征提取网络的具体结构未知。

## 📊 实验亮点

实验结果表明，MAFNet在Scene Flow和KITTI 2015数据集上显著优于现有的实时立体匹配方法。具体性能数据和对比基线未在摘要中明确给出，但强调了该方法在精度和实时性之间取得了良好的平衡，表明其在实际应用中具有优势。

## 🎯 应用场景

MAFNet具有广泛的应用前景，包括自动驾驶、机器人导航、三维重建、虚拟现实和增强现实等领域。其高效的计算性能使其能够部署在资源受限的移动设备上，为这些应用提供实时的深度感知能力。该研究的未来影响在于推动立体匹配技术在嵌入式系统和移动平台上的普及。

## 📄 摘要（原文）

> Existing stereo matching networks typically rely on either cost-volume construction based on 3D convolutions or deformation methods based on iterative optimization. The former incurs significant computational overhead during cost aggregation, whereas the latter often lacks the ability to model non-local contextual information. These methods exhibit poor compatibility on resource-constrained mobile devices, limiting their deployment in real-time applications. To address this, we propose a Multi-frequency Adaptive Fusion Network (MAFNet), which can produce high-quality disparity maps using only efficient 2D convolutions. Specifically, we design an adaptive frequency-domain filtering attention module that decomposes the full cost volume into high-frequency and low-frequency volumes, performing frequency-aware feature aggregation separately. Subsequently, we introduce a Linformer-based low-rank attention mechanism to adaptively fuse high- and low-frequency information, yielding more robust disparity estimation. Extensive experiments demonstrate that the proposed MAFNet significantly outperforms existing real-time methods on public datasets such as Scene Flow and KITTI 2015, showing a favorable balance between accuracy and real-time performance.

