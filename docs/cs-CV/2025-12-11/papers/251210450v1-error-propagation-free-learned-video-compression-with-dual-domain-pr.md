---
layout: default
title: Error-Propagation-Free Learned Video Compression With Dual-Domain Progressive Temporal Alignment
---

# Error-Propagation-Free Learned Video Compression With Dual-Domain Progressive Temporal Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10450" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10450v1</a>
  <a href="https://arxiv.org/pdf/2512.10450.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10450v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.10450v1', 'Error-Propagation-Free Learned Video Compression With Dual-Domain Progressive Temporal Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Han Li, Shaohui Li, Wenrui Dai, Chenglin Li, Xinlong Pan, Haipeng Wang, Junni Zou, Hongkai Xiong

**分类**: cs.CV

**发布日期**: 2025-12-11

---

## 💡 一句话要点

**提出双域渐进式时序对齐的无误差传播学习视频压缩框架**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视频压缩` `学习视频压缩` `运动估计` `时序对齐` `可变形Transformer` `码率控制` `无误差传播` `质量条件混合专家`

## 📋 核心要点

1. 现有学习视频压缩方法在时序对齐精度和误差传播控制间存在矛盾，影响压缩性能。
2. 提出双域渐进式时序对齐，结合像素域和潜在域的运动估计，提升时序建模能力。
3. 设计质量条件混合专家模块，实现连续比特率自适应，并在率失真性能上取得竞争优势。

## 📝 摘要（中文）

现有的学习视频压缩框架在运动估计和补偿（ME/MC）方面面临着不准确的时序对齐和误差传播之间的两难选择。分离变换框架对帧内和帧间压缩采用不同的变换，从而产生令人印象深刻的率失真（R-D）性能，但会导致明显的误差传播，而统一变换框架通过共享变换消除误差传播，但在共享潜在域中的ME/MC方面表现较差。为了解决这个限制，本文提出了一种新的统一变换框架，该框架具有双域渐进式时序对齐和质量条件混合专家（QCMoE），从而为学习视频压缩实现质量一致且无误差传播的流式传输。具体来说，我们提出了用于ME/MC的双域渐进式时序对齐，该对齐利用粗略的像素域对齐和精细的潜在域对齐，以粗到精的方式显着增强时序上下文建模。粗略的像素域对齐有效地处理了来自单个参考帧的光流估计的简单运动模式，而精细的潜在域对齐开发了一种基于多个参考帧的潜在变量的流引导可变形Transformer（FGDT），以实现复杂运动模式的长期运动细化（LTMR）。此外，我们设计了一个QCMoE模块，用于连续比特率自适应，该模块动态地分配不同的专家，以根据目标质量和内容调整每个像素的量化步长，而不是依赖于单个量化步长。QCMoE允许连续且一致的速率控制，并具有吸引人的R-D性能。实验结果表明，与最先进的方法相比，该方法实现了具有竞争力的R-D性能，同时成功消除了误差传播。

## 🔬 方法详解

**问题定义**：现有学习视频压缩框架在运动估计和补偿(ME/MC)中面临两难：分离变换框架虽然率失真性能好，但误差传播严重；统一变换框架虽能避免误差传播，但在ME/MC上表现较差，尤其是在复杂运动场景下，难以准确对齐时序信息，导致压缩效率降低。

**核心思路**：本文的核心在于提出一种统一变换框架下的双域渐进式时序对齐方法，以及质量条件混合专家模块。通过像素域的粗略对齐和潜在域的精细对齐，提升时序建模能力，同时利用QCMoE实现更灵活的码率控制，从而在保证无误差传播的前提下，提高压缩性能。

**技术框架**：整体框架采用统一变换结构，主要包含以下模块：1) 像素域光流估计：利用单参考帧估计光流，进行粗略的像素域对齐。2) 潜在域流引导可变形Transformer (FGDT)：在潜在域中，利用多个参考帧的潜在变量，通过FGDT进行长期运动细化(LTMR)。3) 质量条件混合专家(QCMoE)：根据目标质量和内容，动态分配不同的专家来调整量化步长。整个流程旨在实现从粗到精的时序对齐，并根据质量需求进行灵活的码率控制。

**关键创新**：主要创新点在于双域渐进式时序对齐和QCMoE模块。双域对齐结合了像素域和潜在域的优势，能够更有效地处理复杂运动。QCMoE则打破了传统方法中单一量化步长的限制，实现了更精细的码率控制。与现有方法相比，该方法在保证无误差传播的同时，显著提升了压缩性能。

**关键设计**：FGDT的关键在于如何将光流信息融入到Transformer中，以引导注意力机制。QCMoE的关键在于如何设计专家网络，以及如何根据目标质量和内容动态地选择专家。损失函数的设计需要平衡率失真性能，同时考虑模型的复杂度。

## 📊 实验亮点

实验结果表明，该方法在率失真性能上与当前最先进的方法具有竞争力，同时成功消除了误差传播。具体性能数据未知，但摘要强调了其在保证质量一致性和无误差传播方面的优势。该方法为学习视频压缩提供了一种新的思路，具有重要的研究价值。

## 🎯 应用场景

该研究成果可应用于各种视频流媒体服务、视频会议、远程监控等领域。通过提高视频压缩效率，可以在相同带宽下传输更高质量的视频，或者在相同质量下节省带宽成本。无误差传播的特性使得该方法尤其适用于对视频质量要求较高的应用场景，例如医疗影像、工业检测等。

## 📄 摘要（原文）

> Existing frameworks for learned video compression suffer from a dilemma between inaccurate temporal alignment and error propagation for motion estimation and compensation (ME/MC). The separate-transform framework employs distinct transforms for intra-frame and inter-frame compression to yield impressive rate-distortion (R-D) performance but causes evident error propagation, while the unified-transform framework eliminates error propagation via shared transforms but is inferior in ME/MC in shared latent domains. To address this limitation, in this paper, we propose a novel unifiedtransform framework with dual-domain progressive temporal alignment and quality-conditioned mixture-of-expert (QCMoE) to enable quality-consistent and error-propagation-free streaming for learned video compression. Specifically, we propose dualdomain progressive temporal alignment for ME/MC that leverages coarse pixel-domain alignment and refined latent-domain alignment to significantly enhance temporal context modeling in a coarse-to-fine fashion. The coarse pixel-domain alignment efficiently handles simple motion patterns with optical flow estimated from a single reference frame, while the refined latent-domain alignment develops a Flow-Guided Deformable Transformer (FGDT) over latents from multiple reference frames to achieve long-term motion refinement (LTMR) for complex motion patterns. Furthermore, we design a QCMoE module for continuous bit-rate adaptation that dynamically assigns different experts to adjust quantization steps per pixel based on target quality and content rather than relies on a single quantization step. QCMoE allows continuous and consistent rate control with appealing R-D performance. Experimental results show that the proposed method achieves competitive R-D performance compared with the state-of-the-arts, while successfully eliminating error propagation.

