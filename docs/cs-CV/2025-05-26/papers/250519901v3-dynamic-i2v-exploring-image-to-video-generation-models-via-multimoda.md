---
layout: default
title: "Dynamic-I2V: Exploring Image-to-Video Generation Models via Multimodal LLM"
---

# Dynamic-I2V: Exploring Image-to-Video Generation Models via Multimodal LLM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19901" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19901v3</a>
  <a href="https://arxiv.org/pdf/2505.19901.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19901v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19901v3', 'Dynamic-I2V: Exploring Image-to-Video Generation Models via Multimodal LLM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peng Liu, Xiaoming Ren, Fengkai Liu, Qingsong Xie, Quanlong Zheng, Yanhao Zhang, Haonan Lu, Yujiu Yang

**分类**: cs.CV

**发布日期**: 2025-05-26 (更新: 2025-06-03)

---

## 💡 一句话要点

**提出Dynamic-I2V以解决复杂场景下图像到视频生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像到视频生成` `多模态大语言模型` `扩散变换器` `动态视频评估` `运动可控性` `时间一致性` `生成模型` `视频质量`

## 📋 核心要点

1. 现有图像到视频生成方法在处理复杂场景时，难以有效理解细微的运动和复杂的物体-动作关系。
2. Dynamic-I2V框架通过整合多模态大语言模型，增强了对视觉和文本条件的编码能力，从而改善了生成视频的运动可控性和时间一致性。
3. 实验结果表明，Dynamic-I2V在动态范围、可控性和视频质量上分别提升了42.5%、7.9%和11.8%，显示出显著的性能优势。

## 📝 摘要（中文）

近年来，图像到视频（I2V）生成的进展在常规场景中表现出色。然而，现有方法在处理复杂场景时仍面临重大挑战，尤其是在理解细微运动和复杂物体-动作关系方面。为此，本文提出了Dynamic-I2V框架，结合多模态大语言模型（MLLMs）共同编码视觉和文本条件，以增强扩散变换器（DiT）架构的性能。通过利用MLLMs的多模态理解能力，模型显著提高了合成视频的运动可控性和时间一致性。此外，Dynamic-I2V的多模态特性支持多样的条件输入，扩展了其在下游生成任务中的适用性。我们还提出了DIVE评估基准，以解决现有I2V基准在动态视频评估中的偏差问题。实验结果表明，Dynamic-I2V在图像到视频生成中达到了最先进的性能，动态范围、可控性和质量分别提升42.5%、7.9%和11.8%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有图像到视频生成方法在复杂场景下的不足，特别是对细微运动和复杂物体-动作关系的理解能力不足。现有基准测试存在偏向低动态视频的问题，导致评估不全面。

**核心思路**：Dynamic-I2V框架通过引入多模态大语言模型（MLLMs），实现视觉和文本条件的联合编码，从而提升生成视频的运动可控性和时间一致性。这种设计利用了MLLMs在多模态理解方面的优势，增强了模型的生成能力。

**技术框架**：Dynamic-I2V的整体架构包括多个模块：首先是视觉和文本条件的输入模块，然后是基于扩散变换器（DiT）的生成模块，最后是输出视频的后处理模块。各模块协同工作，确保生成视频的质量和一致性。

**关键创新**：本文的主要创新在于将多模态大语言模型与图像到视频生成相结合，显著提升了模型在复杂场景下的表现。这一方法与传统I2V方法的本质区别在于其对多模态信息的深度融合和理解。

**关键设计**：在模型设计中，采用了特定的损失函数来平衡运动复杂性和视觉质量，同时在网络结构上进行了优化，以适应多模态输入的需求。

## 📊 实验亮点

实验结果显示，Dynamic-I2V在图像到视频生成任务中表现出色，特别是在动态范围、可控性和视频质量方面，分别提升了42.5%、7.9%和11.8%。这些结果通过新的DIVE评估基准得以验证，表明该方法在生成动态视频方面的显著优势。

## 🎯 应用场景

Dynamic-I2V的研究成果在多个领域具有广泛的应用潜力，包括电影制作、游戏开发、虚拟现实和增强现实等。通过生成高质量的动态视频，该技术能够为创作者提供更丰富的内容生成工具，提升用户体验。此外，未来可能在教育、广告等领域发挥重要作用，推动多媒体内容的创新与发展。

## 📄 摘要（原文）

> Recent advancements in image-to-video (I2V) generation have shown promising performance in conventional scenarios. However, these methods still encounter significant challenges when dealing with complex scenes that require a deep understanding of nuanced motion and intricate object-action relationships. To address these challenges, we present Dynamic-I2V, an innovative framework that integrates Multimodal Large Language Models (MLLMs) to jointly encode visual and textual conditions for a diffusion transformer (DiT) architecture. By leveraging the advanced multimodal understanding capabilities of MLLMs, our model significantly improves motion controllability and temporal coherence in synthesized videos. The inherent multimodality of Dynamic-I2V further enables flexible support for diverse conditional inputs, extending its applicability to various downstream generation tasks. Through systematic analysis, we identify a critical limitation in current I2V benchmarks: a significant bias towards favoring low-dynamic videos, stemming from an inadequate balance between motion complexity and visual quality metrics. To resolve this evaluation gap, we propose DIVE - a novel assessment benchmark specifically designed for comprehensive dynamic quality measurement in I2V generation. In conclusion, extensive quantitative and qualitative experiments confirm that Dynamic-I2V attains state-of-the-art performance in image-to-video generation, particularly revealing significant improvements of 42.5%, 7.9%, and 11.8% in dynamic range, controllability, and quality, respectively, as assessed by the DIVE metric in comparison to existing methods.

