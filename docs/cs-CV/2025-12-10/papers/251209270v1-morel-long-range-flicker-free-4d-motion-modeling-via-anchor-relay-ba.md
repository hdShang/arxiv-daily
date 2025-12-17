---
layout: default
title: MoRel: Long-Range Flicker-Free 4D Motion Modeling via Anchor Relay-based Bidirectional Blending with Hierarchical Densification
---

# MoRel: Long-Range Flicker-Free 4D Motion Modeling via Anchor Relay-based Bidirectional Blending with Hierarchical Densification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09270" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09270v1</a>
  <a href="https://arxiv.org/pdf/2512.09270.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09270v1" onclick="toggleFavorite(this, '2512.09270v1', 'MoRel: Long-Range Flicker-Free 4D Motion Modeling via Anchor Relay-based Bidirectional Blending with Hierarchical Densification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sangwoon Kwak, Weeyoung Kwon, Jun Young Jeong, Geonho Kim, Won-Sik Cheong, Jihyong Oh

**分类**: cs.CV

**发布日期**: 2025-12-10

**备注**: Please visit our project page at https://cmlab-korea.github.io/MoRel/

---

## 💡 一句话要点

**MoRel：基于锚点中继双向融合和分层稠密化的长程无闪烁4D运动建模**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `4D高斯溅射` `动态场景重建` `长程运动建模` `时间一致性` `双向融合` `分层稠密化` `无闪烁渲染`

## 📋 核心要点

1. 现有4D高斯溅射方法在处理长程动态视频时，面临内存爆炸、时间闪烁以及难以处理遮挡等问题。
2. MoRel通过锚点中继双向融合机制，在关键帧锚点空间建模帧间形变，并自适应融合双向形变，增强时间一致性。
3. MoRel在SelfCap$_{	ext{LR}}$数据集上实现了时间连贯且无闪烁的长程4D重建，并保持了较低的内存占用。

## 📝 摘要（中文）

本文提出了一种名为MoRel的新型4D高斯溅射（4DGS）框架，旨在解决长程动态视频建模中的内存爆炸、时间闪烁以及遮挡处理失败等问题。MoRel的核心是基于锚点中继的双向融合（ARBB）机制，它通过在关键帧时间索引处逐步构建局部规范锚点空间，并在锚点级别对帧间形变进行建模，从而增强时间一致性。通过学习关键帧锚点之间的双向形变，并通过可学习的不透明度控制自适应地融合它们，该方法减轻了时间不连续性和闪烁伪影。此外，还引入了一种特征方差引导的分层稠密化（FHD）方案，该方案基于分配的特征方差级别，有效地稠密化关键帧锚点，同时保持渲染质量。为了有效评估模型处理真实世界长程4D运动的能力，作者构建了一个名为SelfCap$_{	ext{LR}}$的长程4D运动数据集。实验结果表明，MoRel实现了时间连贯且无闪烁的长程4D重建，同时保持了有限的内存使用，展示了动态高斯表示的可扩展性和效率。

## 🔬 方法详解

**问题定义**：现有4D高斯溅射方法在处理包含长程运动的动态视频时，会遇到严重的内存爆炸问题，导致时间上的闪烁，并且无法很好地处理随时间出现的或消失的遮挡。这些问题限制了4DGS在实际应用中的可行性。

**核心思路**：MoRel的核心思路是引入锚点中继的双向融合机制。通过在关键帧处建立局部规范的锚点空间，并在这些锚点之间建模帧间形变，从而在时间上保持一致性。双向融合则通过学习关键帧锚点之间的双向形变，并自适应地融合它们，来减轻时间上的不连续性和闪烁伪影。

**技术框架**：MoRel框架主要包含以下几个阶段：1) 在关键帧时间索引处构建局部规范锚点空间（KfA）。2) 学习帧间形变，在锚点级别建模形变。3) 通过可学习的不透明度控制，自适应地融合双向形变。4) 使用特征方差引导的分层稠密化（FHD）方案，有效地稠密化KfA，同时保持渲染质量。

**关键创新**：MoRel的关键创新在于锚点中继的双向融合（ARBB）机制和特征方差引导的分层稠密化（FHD）方案。ARBB机制通过锚点空间建模和双向融合，有效地解决了长程动态视频中的时间一致性问题和闪烁伪影。FHD方案则通过特征方差来指导稠密化过程，在保证渲染质量的同时，降低了计算复杂度。

**关键设计**：在ARBB机制中，关键帧的选择和锚点空间的构建是关键。双向形变的融合通过可学习的不透明度控制来实现，这使得模型能够自适应地选择更可靠的形变信息。FHD方案中，特征方差的阈值设置会影响稠密化的程度，需要在渲染质量和计算效率之间进行权衡。损失函数的设计也至关重要，需要同时考虑重建误差、时间一致性和正则化项。

## 📊 实验亮点

MoRel在自建的SelfCap$_{	ext{LR}}$数据集上进行了评估，该数据集包含更大范围的运动和更广阔的空间范围。实验结果表明，MoRel能够有效地处理长程动态视频，实现时间连贯且无闪烁的4D重建，同时保持了较低的内存占用。与现有方法相比，MoRel在时间一致性和渲染质量方面均取得了显著提升。

## 🎯 应用场景

MoRel在动态场景重建、虚拟现实、增强现实、自动驾驶等领域具有广泛的应用前景。它可以用于创建逼真的动态虚拟环境，提升用户体验。在自动驾驶领域，可以用于重建动态交通场景，提高感知系统的准确性和鲁棒性。此外，该方法还可以应用于电影特效制作、游戏开发等领域。

## 📄 摘要（原文）

> Recent advances in 4D Gaussian Splatting (4DGS) have extended the high-speed rendering capability of 3D Gaussian Splatting (3DGS) into the temporal domain, enabling real-time rendering of dynamic scenes. However, one of the major remaining challenges lies in modeling long-range motion-contained dynamic videos, where a naive extension of existing methods leads to severe memory explosion, temporal flickering, and failure to handle appearing or disappearing occlusions over time. To address these challenges, we propose a novel 4DGS framework characterized by an Anchor Relay-based Bidirectional Blending (ARBB) mechanism, named MoRel, which enables temporally consistent and memory-efficient modeling of long-range dynamic scenes. Our method progressively constructs locally canonical anchor spaces at key-frame time index and models inter-frame deformations at the anchor level, enhancing temporal coherence. By learning bidirectional deformations between KfA and adaptively blending them through learnable opacity control, our approach mitigates temporal discontinuities and flickering artifacts. We further introduce a Feature-variance-guided Hierarchical Densification (FHD) scheme that effectively densifies KfA's while keeping rendering quality, based on an assigned level of feature-variance. To effectively evaluate our model's capability to handle real-world long-range 4D motion, we newly compose long-range 4D motion-contained dataset, called SelfCap$_{\text{LR}}$. It has larger average dynamic motion magnitude, captured at spatially wider spaces, compared to previous dynamic video datasets. Overall, our MoRel achieves temporally coherent and flicker-free long-range 4D reconstruction while maintaining bounded memory usage, demonstrating both scalability and efficiency in dynamic Gaussian-based representations.

