---
layout: default
title: "Kling-Foley: Multimodal Diffusion Transformer for High-Quality Video-to-Audio Generation"
---

# Kling-Foley: Multimodal Diffusion Transformer for High-Quality Video-to-Audio Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19774" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19774v1</a>
  <a href="https://arxiv.org/pdf/2506.19774.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19774v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19774v1', 'Kling-Foley: Multimodal Diffusion Transformer for High-Quality Video-to-Audio Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun Wang, Xijuan Zeng, Chunyu Qiang, Ruilong Chen, Shiyao Wang, Le Wang, Wangjing Zhou, Pengfei Cai, Jiahui Zhao, Nan Li, Zihan Li, Yuzhe Liang, Xiaopeng Wang, Haorui Zheng, Ming Wen, Kang Yin, Yiran Wang, Nan Li, Feng Deng, Liang Dong, Chen Zhang, Di Zhang, Kun Gai

**分类**: eess.AS, cs.AI, cs.CL, cs.SD

**发布日期**: 2025-06-24

---

## 💡 一句话要点

**提出Kling-Foley以解决视频与音频生成的同步问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态生成` `音频合成` `视频理解` `扩散变换器` `音视频同步` `语义对齐` `潜在音频编解码器`

## 📋 核心要点

1. 现有的视频到音频生成方法在音频质量和同步性方面存在不足，难以满足高质量生成的需求。
2. Kling-Foley通过引入多模态扩散变换器和音视频同步模块，增强了视频与音频之间的对齐能力，提升生成效果。
3. 实验结果显示，Kling-Foley在多个指标上超越了现有公共模型，尤其在音频质量和对齐精度方面表现突出。

## 📝 摘要（中文）

我们提出Kling-Foley，一个大规模的多模态视频到音频生成模型，能够合成与视频内容同步的高质量音频。在Kling-Foley中，我们引入了多模态扩散变换器来建模视频、音频和文本模态之间的交互，并结合视觉语义表示模块和音视频同步模块以增强对齐能力。这些模块在帧级别上对齐视频条件与潜在音频元素，从而改善语义对齐和音视频同步。结合文本条件，这种集成方法能够精确生成与视频匹配的音效。此外，我们提出了一种通用的潜在音频编解码器，能够在音效、语音、歌唱和音乐等多种场景中实现高质量建模。我们的实验表明，Kling-Foley在分布匹配、语义对齐、时间对齐和音频质量方面在公共模型中达到了新的音视频SOTA性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决视频到音频生成中的音频质量和同步性不足的问题。现有方法在生成音频时往往无法与视频内容精确对齐，导致生成效果不佳。

**核心思路**：Kling-Foley通过引入多模态扩散变换器来建模视频、音频和文本之间的交互，结合视觉语义表示和音视频同步模块，提升了音频生成的对齐能力和质量。

**技术框架**：整体架构包括多模态扩散变换器、视觉语义表示模块和音视频同步模块。多模态扩散变换器负责建模不同模态之间的关系，视觉语义模块提供视频内容的语义信息，而音视频同步模块确保生成音频与视频内容的时间一致性。

**关键创新**：最重要的技术创新在于引入了多模态扩散变换器和通用潜在音频编解码器，这使得模型能够在多种场景下实现高质量的音频生成，并且在音频与视频的对齐上表现优异。

**关键设计**：模型采用了流匹配目标作为损失函数，以优化生成的音频与视频之间的分布匹配。同时，设计了立体渲染方法，使合成音频具有空间感，增强了用户体验。实验中还构建了Kling-Audio-Eval基准，以补充现有数据集的不足。

## 📊 实验亮点

实验结果表明，Kling-Foley在音频质量、语义对齐和时间对齐等方面达到了新的SOTA性能，尤其在分布匹配上表现优异，相较于现有公共模型有显著提升，具体性能数据未详述。

## 🎯 应用场景

Kling-Foley的研究成果在多个领域具有广泛的应用潜力，包括电影制作、游戏开发、虚拟现实和增强现实等。通过高质量的音频生成，能够提升用户的沉浸感和体验质量。此外，该模型的通用性使其在音效、语音和音乐生成等场景中也具备实用价值，推动相关领域的发展。

## 📄 摘要（原文）

> We propose Kling-Foley, a large-scale multimodal Video-to-Audio generation model that synthesizes high-quality audio synchronized with video content. In Kling-Foley, we introduce multimodal diffusion transformers to model the interactions between video, audio, and text modalities, and combine it with a visual semantic representation module and an audio-visual synchronization module to enhance alignment capabilities. Specifically, these modules align video conditions with latent audio elements at the frame level, thereby improving semantic alignment and audio-visual synchronization. Together with text conditions, this integrated approach enables precise generation of video-matching sound effects. In addition, we propose a universal latent audio codec that can achieve high-quality modeling in various scenarios such as sound effects, speech, singing, and music. We employ a stereo rendering method that imbues synthesized audio with a spatial presence. At the same time, in order to make up for the incomplete types and annotations of the open-source benchmark, we also open-source an industrial-level benchmark Kling-Audio-Eval. Our experiments show that Kling-Foley trained with the flow matching objective achieves new audio-visual SOTA performance among public models in terms of distribution matching, semantic alignment, temporal alignment and audio quality.

