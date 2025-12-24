---
layout: default
title: "STANCE: Motion Coherent Video Generation Via Sparse-to-Dense Anchored Encoding"
---

# STANCE: Motion Coherent Video Generation Via Sparse-to-Dense Anchored Encoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14588" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14588v2</a>
  <a href="https://arxiv.org/pdf/2510.14588.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14588v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.14588v2', 'STANCE: Motion Coherent Video Generation Via Sparse-to-Dense Anchored Encoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhifei Chen, Tianshuo Xu, Leyi Wu, Luozhou Wang, Dongyu Yan, Zihan You, Wenting Luo, Guo Zhang, Yingcong Chen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-16 (更新: 2025-10-19)

**备注**: Code, model, and demos can be found at https://envision-research.github.io/STANCE/

---

## 💡 一句话要点

**STANCE：通过稀疏到稠密锚定编码实现运动连贯的视频生成**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视频生成` `运动连贯性` `稀疏到稠密编码` `旋转位置编码` `实例线索`

## 📋 核心要点

1. 现有视频生成方法难以保持物体运动和交互的连贯性，主要原因是运动提示信息在编码后损失过多，以及外观和运动优化相互干扰。
2. STANCE通过引入Instance Cues将稀疏的用户提示转化为稠密的2.5D运动场，并使用Dense RoPE保留运动信息在token空间中的显著性。
3. 该模型通过联合预测RGB和辅助地图（分割或深度），在稳定优化的同时提高了时间连贯性，无需逐帧轨迹脚本。

## 📝 摘要（中文）

视频生成技术近年来取得了显著的视觉进展，但保持连贯的物体运动和交互仍然是一个难题。我们发现了两个实际瓶颈：（i）人为提供的运动提示（例如，小的2D地图）在编码后通常会坍缩为过少的有效token，从而削弱了指导作用；（ii）在单个head中同时优化外观和运动可能会偏向纹理而非时间一致性。我们提出了STANCE，一个图像到视频的框架，通过两个简单的组件解决了这两个问题。首先，我们引入了Instance Cues——一种像素对齐的控制信号，它通过平均每个实例的流并使用单目深度增强实例掩码，将稀疏的、用户可编辑的提示转换为密集的2.5D（相机相对）运动场。与2D箭头输入相比，这减少了深度模糊，同时保持了易用性。其次，我们使用Dense RoPE保留了这些线索在token空间中的显著性，Dense RoPE用空间可寻址的旋转嵌入标记一小组运动token（锚定在第一帧上）。结合联合RGB和辅助地图预测（分割或深度），我们的模型在RGB处理外观的同时锚定结构，稳定优化并提高时间连贯性，而无需逐帧轨迹脚本。

## 🔬 方法详解

**问题定义**：现有视频生成方法在处理复杂场景时，难以生成运动连贯的视频。主要痛点在于，用户提供的稀疏运动提示在经过编码后，有效信息大幅减少，无法有效指导视频生成过程。此外，同时优化视频的外观和运动容易导致模型偏向于纹理细节，而忽略了时间一致性。

**核心思路**：STANCE的核心思路是将稀疏的用户运动提示转化为稠密的2.5D运动场，从而提供更强的运动指导信号。同时，通过解耦外观和结构信息的处理，避免两者之间的相互干扰，从而提高生成视频的时间连贯性。

**技术框架**：STANCE是一个图像到视频的生成框架，主要包含两个关键模块：Instance Cues和Dense RoPE。Instance Cues模块负责将稀疏的用户提示转化为稠密的2.5D运动场。Dense RoPE模块则负责在token空间中保留运动信息的显著性。此外，模型还采用联合预测RGB和辅助地图（分割或深度）的方式，以稳定优化并提高时间连贯性。

**关键创新**：STANCE的关键创新在于Instance Cues和Dense RoPE的引入。Instance Cues通过平均每个实例的流并使用单目深度增强实例掩码，有效地将稀疏提示转化为稠密运动场，减少了深度模糊。Dense RoPE则通过空间可寻址的旋转嵌入，保留了运动信息在token空间中的显著性，避免了信息损失。

**关键设计**：Instance Cues模块的关键设计在于使用2.5D运动场表示运动信息，这既减少了深度模糊，又保持了易用性。Dense RoPE模块的关键设计在于使用空间可寻址的旋转嵌入，这使得模型能够有效地捕捉运动信息在空间中的分布。此外，模型采用联合预测RGB和辅助地图的方式，通过辅助任务来约束模型的学习，从而提高生成视频的质量。

## 📊 实验亮点

论文提出的STANCE模型在视频生成任务上取得了显著的性能提升。通过引入Instance Cues和Dense RoPE，模型能够生成运动更加连贯、时间一致性更高的视频。实验结果表明，STANCE模型在多个指标上优于现有的视频生成方法，尤其是在处理复杂场景时，优势更加明显。具体的性能数据和对比基线信息在论文中有详细展示。

## 🎯 应用场景

STANCE具有广泛的应用前景，例如视频编辑、游戏开发、电影制作等领域。它可以用于生成具有逼真运动效果的视频内容，例如将静态图像转化为动态视频，或者根据用户提供的运动提示生成特定的视频片段。该技术还可以应用于虚拟现实和增强现实等领域，为用户提供更加沉浸式的体验。

## 📄 摘要（原文）

> Video generation has recently made striking visual progress, but maintaining coherent object motion and interactions remains difficult. We trace two practical bottlenecks: (i) human-provided motion hints (e.g., small 2D maps) often collapse to too few effective tokens after encoding, weakening guidance; and (ii) optimizing for appearance and motion in a single head can favor texture over temporal consistency. We present STANCE, an image-to-video framework that addresses both issues with two simple components. First, we introduce Instance Cues -- a pixel-aligned control signal that turns sparse, user-editable hints into a dense 2.5D (camera-relative) motion field by averaging per-instance flow and augmenting with monocular depth over the instance mask. This reduces depth ambiguity compared to 2D arrow inputs while remaining easy to use. Second, we preserve the salience of these cues in token space with Dense RoPE, which tags a small set of motion tokens (anchored on the first frame) with spatial-addressable rotary embeddings. Paired with joint RGB \(+\) auxiliary-map prediction (segmentation or depth), our model anchors structure while RGB handles appearance, stabilizing optimization and improving temporal coherence without requiring per-frame trajectory scripts.

