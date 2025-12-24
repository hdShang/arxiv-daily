---
layout: default
title: "Text Slider: Efficient and Plug-and-Play Continuous Concept Control for Image/Video Synthesis via LoRA Adapters"
---

# Text Slider: Efficient and Plug-and-Play Continuous Concept Control for Image/Video Synthesis via LoRA Adapters

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18831" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18831v1</a>
  <a href="https://arxiv.org/pdf/2509.18831.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18831v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18831v1', 'Text Slider: Efficient and Plug-and-Play Continuous Concept Control for Image/Video Synthesis via LoRA Adapters')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pin-Yen Chiu, I-Sheng Fang, Jun-Cheng Chen

**分类**: cs.GR, cs.AI, cs.CV, cs.LG, cs.MM

**发布日期**: 2025-09-23

---

## 💡 一句话要点

**Text Slider：一种高效即插即用的LoRA适配器，用于图像/视频合成中的连续概念控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `图像合成` `视频合成` `概念控制` `扩散模型` `LoRA适配器`

## 📋 核心要点

1. 现有概念控制方法训练成本高昂，需要大量时间和GPU资源来学习滑块或嵌入，且需针对不同扩散模型骨干网络进行重新训练。
2. Text Slider通过在预训练文本编码器中寻找低秩方向，实现视觉概念的连续控制，无需大量训练和重新训练。
3. 实验表明，Text Slider在显著降低训练时间和GPU内存消耗的同时，实现了对图像和视频属性的平滑连续控制，且效率远超现有方法。

## 📝 摘要（中文）

本文提出了一种名为Text Slider的轻量级、高效且即插即用的框架，用于实现图像和视频合成中的连续概念控制。该方法通过识别预训练文本编码器中的低秩方向，从而实现对视觉概念的连续控制，同时显著减少了训练时间、GPU内存消耗和可训练参数的数量。Text Slider支持多概念组合和连续控制，从而在图像和视频合成中实现细粒度和灵活的操作。实验结果表明，Text Slider能够在保持输入图像原始空间布局和结构的同时，对特定属性进行平滑和连续的调整。Text Slider在效率方面表现出色：训练速度比Concept Slider快5倍，比Attribute Control快47倍，同时GPU内存使用量分别减少了近2倍和4倍。

## 🔬 方法详解

**问题定义**：现有概念控制方法在图像和视频合成中存在训练成本高、GPU内存消耗大以及泛化能力弱的问题。具体来说，这些方法需要针对每个概念或属性训练独立的滑块或嵌入，导致训练时间和计算资源需求巨大。此外，这些方法通常依赖于特定的扩散模型骨干网络，难以直接应用于其他模型，限制了其可扩展性和适应性。

**核心思路**：Text Slider的核心思路是在预训练文本编码器的潜在空间中寻找与特定概念或属性相关的低秩方向。通过沿着这些低秩方向移动，可以实现对图像或视频中相应属性的连续控制。这种方法利用了预训练文本编码器强大的语义表示能力，避免了从头开始训练的需要，从而显著降低了训练成本。

**技术框架**：Text Slider的整体框架包括以下几个主要步骤：1) 选择一个预训练的文本编码器（例如CLIP）。2) 针对每个需要控制的概念或属性，通过少量样本数据训练一个LoRA适配器，以识别文本编码器中的低秩方向。3) 在图像或视频合成过程中，通过调整LoRA适配器的权重，沿着低秩方向移动，从而实现对相应属性的连续控制。

**关键创新**：Text Slider的关键创新在于利用LoRA适配器在预训练文本编码器中寻找低秩方向，从而实现对视觉概念的连续控制。与现有方法相比，Text Slider无需训练独立的滑块或嵌入，而是直接利用预训练模型的知识，从而显著降低了训练成本和GPU内存消耗。此外，Text Slider具有良好的泛化能力，可以轻松应用于不同的扩散模型骨干网络。

**关键设计**：Text Slider的关键设计包括：1) 使用LoRA适配器来学习低秩方向，LoRA通过引入少量可训练参数来调整预训练模型的权重，从而避免了对整个模型进行微调。2) 使用连续的权重调整来实现对属性的连续控制，通过调整LoRA适配器的权重，可以沿着低秩方向平滑地改变图像或视频中的相应属性。3) 支持多概念组合，通过组合多个LoRA适配器的权重，可以同时控制图像或视频中的多个属性。

## 📊 实验亮点

Text Slider在效率方面表现出色，训练速度比Concept Slider快5倍，比Attribute Control快47倍，同时GPU内存使用量分别减少了近2倍和4倍。此外，Text Slider能够在保持输入图像原始空间布局和结构的同时，对特定属性进行平滑和连续的调整，实现了高质量的图像和视频合成效果。这些实验结果表明，Text Slider是一种高效、灵活且易于使用的概念控制方法。

## 🎯 应用场景

Text Slider可广泛应用于图像和视频编辑、内容创作、风格迁移等领域。例如，用户可以使用Text Slider轻松调整图像的亮度、对比度、饱和度等属性，或者改变视频中人物的表情、年龄等特征。此外，Text Slider还可以用于生成具有特定风格或主题的图像和视频，为创意设计提供更多可能性。该研究的潜在价值在于降低了图像和视频编辑的门槛，使得普通用户也能轻松创作出高质量的内容。

## 📄 摘要（原文）

> Recent advances in diffusion models have significantly improved image and video synthesis. In addition, several concept control methods have been proposed to enable fine-grained, continuous, and flexible control over free-form text prompts. However, these methods not only require intensive training time and GPU memory usage to learn the sliders or embeddings but also need to be retrained for different diffusion backbones, limiting their scalability and adaptability. To address these limitations, we introduce Text Slider, a lightweight, efficient and plug-and-play framework that identifies low-rank directions within a pre-trained text encoder, enabling continuous control of visual concepts while significantly reducing training time, GPU memory consumption, and the number of trainable parameters. Furthermore, Text Slider supports multi-concept composition and continuous control, enabling fine-grained and flexible manipulation in both image and video synthesis. We show that Text Slider enables smooth and continuous modulation of specific attributes while preserving the original spatial layout and structure of the input. Text Slider achieves significantly better efficiency: 5$\times$ faster training than Concept Slider and 47$\times$ faster than Attribute Control, while reducing GPU memory usage by nearly 2$\times$ and 4$\times$, respectively.

