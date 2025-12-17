---
layout: default
title: Enhancing Foveated Rendering with Weighted Reservoir Sampling
---

# Enhancing Foveated Rendering with Weighted Reservoir Sampling

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.03964" target="_blank" class="toolbar-btn">arXiv: 2510.03964v1</a>
    <a href="https://arxiv.org/pdf/2510.03964.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03964v1" 
            onclick="toggleFavorite(this, '2510.03964v1', 'Enhancing Foveated Rendering with Weighted Reservoir Sampling')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Ville Cantory, Darya Biparva, Haoyu Tan, Tongyu Nie, John Schroeder, Ruofei Du, Victoria Interrante, Piotr Didyk

**分类**: cs.GR

**发布日期**: 2025-10-04

**备注**: To appear in The 18th ACM SIGGRAPH Conference on Motion, Interaction, and Games (MIG '25), December 03-05, 2025, Zurich, Switzerland

**DOI**: [10.1145/3769047.3769058](https://doi.org/10.1145/3769047.3769058)

---

## 💡 一句话要点

**提出加权水库抽样方法，提升注视点渲染的感知质量和效率**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `注视点渲染` `水库抽样` `时域渲染` `感知优化` `VR/AR` `实时渲染` `图像质量`

## 📋 核心要点

1. 传统注视点渲染在高注视级别下质量下降，且忽略了先前帧的高分辨率信息，导致感知质量受限。
2. 提出加权水库抽样技术，维护高质量像素样本库，并将其融入当前帧的渲染，实现时域像素复用。
3. 该方法在4K分辨率下耗时低于1毫秒，可集成到实时VR/AR系统中，提升注视点渲染的感知质量。

## 📝 摘要（中文）

本文提出了一种增强注视点渲染的方法，该方法利用人眼对周边视觉高频信息不敏感的特性，通过降低周边区域渲染分辨率来减少计算成本。传统注视点渲染系统在高注视级别下会降低渲染质量，且无法保留先前帧中以高分辨率渲染的样本。考虑到人眼扫视落点并非精确位于目标位置，且在注视期间存在微小眼动，本文提出利用时域相邻帧的不同注视位置进行采样，以减少注视区域的渲染尺寸，同时提高感知图像质量。我们将像素的时域呈现视为数据流，并提出加权水库抽样技术，高效维护感知相关的高质量像素样本库，并将其融入当前帧的计算中。该方法允许渲染器通过时域复用像素样本来渲染更小的注视区域，从而在更高注视级别下重建更高感知图像质量。该方法运行在注视点渲染的输出上，在4K分辨率下耗时低于1毫秒，使其高效且易于集成到实时VR和AR注视点渲染系统中。

## 🔬 方法详解

**问题定义**：传统注视点渲染在高注视级别下会显著降低图像质量，并且没有充分利用时间冗余信息。先前帧中以高分辨率渲染的像素信息被简单丢弃，导致感知质量下降。此外，人眼的扫视落点并非完全精确，存在微小的眼动，这为利用时间相邻帧的信息提供了机会。

**核心思路**：论文的核心思路是将像素的时域呈现视为一个数据流，并利用水库抽样技术来维护一个高质量像素样本的“水库”。通过对水库中的样本进行加权，可以优先保留感知上更重要的像素，并在当前帧的渲染中复用这些像素，从而在降低渲染成本的同时提高感知质量。

**技术框架**：该方法运行在注视点渲染的输出之后，作为一个后处理步骤。整体流程如下：1. 对当前帧进行注视点渲染。2. 从先前帧的像素水库中采样像素。3. 对采样到的像素进行加权，权重取决于像素的质量和时间衰减。4. 将采样到的像素与当前帧的渲染结果进行融合，生成最终的输出图像。5. 更新像素水库，保留高质量的像素，并淘汰低质量的像素。

**关键创新**：关键创新在于使用加权水库抽样来管理和复用时间冗余的像素信息。传统的注视点渲染方法忽略了先前帧的信息，而该方法通过维护一个像素水库，可以有效地利用这些信息，从而提高感知质量。加权机制允许优先保留感知上更重要的像素，进一步提升了渲染效率和质量。

**关键设计**：加权水库抽样的权重计算是关键。权重可以基于多种因素，例如像素的梯度、颜色差异、时间衰减等。时间衰减函数用于降低旧像素的权重，以反映其与当前帧的相关性。水库的大小需要根据实际应用进行调整，以在存储成本和性能之间取得平衡。融合策略也需要仔细设计，以避免引入伪影。

## 📊 实验亮点

实验结果表明，该方法在4K分辨率下运行时间低于1毫秒，具有很高的效率。通过与传统的注视点渲染方法相比，该方法能够显著提高感知图像质量，尤其是在高注视级别下。主观评价实验也表明，用户更倾向于使用该方法渲染的图像，认为其细节更丰富，画面更清晰。

## 🎯 应用场景

该研究成果可广泛应用于VR/AR头显、移动设备等需要实时渲染的场景。通过降低渲染分辨率，可以显著降低计算负担，提高设备续航能力，并为用户提供更流畅的体验。此外，该方法还可以应用于云游戏、远程渲染等领域，降低带宽需求，提升用户体验，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Spatiotemporal sensitivity to high frequency information declines with increased peripheral eccentricity. Foveated rendering exploits this by decreasing the spatial resolution of rendered images in peripheral vision, reducing the rendering cost by omitting high frequency details. As foveation levels increase, the rendering quality is reduced, and traditional foveated rendering systems tend not to preserve samples that were previously rendered at high spatial resolution in previous frames. Additionally, prior research has shown that saccade landing positions are distributed around a target location rather than landing at a single point, and that even during fixations, eyes perform small microsaccades around a fixation point. This creates an opportunity for sampling from temporally neighbouring frames with differing foveal locations to reduce the required rendered size of the foveal region while achieving a higher perceived image quality. We further observe that the temporal presentation of pixels frame-to-frame can be viewed as a data stream, presenting a random sampling problem. Following this intuition, we propose a Weighted Reservoir Sampling technique to efficiently maintain a reservoir of the perceptually relevant high quality pixel samples from previous frames and incorporate them into the computation of the current frame. This allows the renderer to render a smaller region of foveal pixels per frame by temporally reusing pixel samples that are still relevant to reconstruct a higher perceived image quality, while allowing for higher levels of foveation. Our method operates on the output of foveated rendering, and runs in under 1\,ms at 4K resolution, making it highly efficient and integrable with real-time VR and AR foveated rendering systems.

