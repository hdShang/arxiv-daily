---
layout: default
title: "VCMamba: Bridging Convolutions with Multi-Directional Mamba for Efficient Visual Representation"
---

# VCMamba: Bridging Convolutions with Multi-Directional Mamba for Efficient Visual Representation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04669" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04669v1</a>
  <a href="https://arxiv.org/pdf/2509.04669.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04669v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04669v1', 'VCMamba: Bridging Convolutions with Multi-Directional Mamba for Efficient Visual Representation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mustafa Munir, Alex Zhang, Radu Marculescu

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-09-04

**备注**: Proceedings of the 2025 IEEE/CVF International Conference on Computer Vision (ICCV) Workshops

**🔗 代码/项目**: [GITHUB](https://github.com/Wertyuui345/VCMamba)

---

## 💡 一句话要点

**VCMamba：融合卷积与多向Mamba，实现高效视觉表征**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉骨干网络` `卷积神经网络` `状态空间模型` `Mamba` `图像分类` `语义分割` `长程依赖` `局部特征`

## 📋 核心要点

1. 现有ViT和Mamba模型在捕获全局信息方面表现出色，但对局部细粒度特征的提取能力不如CNN。
2. VCMamba融合CNN和多向Mamba SSM的优势，利用CNN提取局部特征，Mamba建模长程依赖，实现高效视觉表征。
3. 实验表明，VCMamba在ImageNet-1K和ADE20K上均取得了优异的性能，参数量显著减少。

## 📝 摘要（中文）

近年来，视觉Transformer (ViT) 和状态空间模型 (SSM) 对卷积神经网络 (CNN) 在计算机视觉领域的统治地位提出了挑战。ViT擅长捕获全局上下文，而像Mamba这样的SSM为长序列提供了线性复杂度，但它们在捕获细粒度的局部特征方面不如CNN有效。相反，CNN具有强大的局部特征归纳偏置，但缺乏Transformer和Mamba的全局推理能力。为了弥合这一差距，我们引入了VCMamba，一种新颖的视觉骨干网络，它集成了CNN和多向Mamba SSM的优势。VCMamba采用卷积stem和具有卷积块的分层结构，以提取丰富的局部特征。这些卷积块随后由包含多向Mamba块的后续阶段处理，旨在有效地建模长程依赖关系和全局上下文。这种混合设计允许实现卓越的特征表示，同时保持相对于图像分辨率的线性复杂度。我们在ImageNet-1K分类和ADE20K语义分割上进行了大量实验，证明了VCMamba的有效性。我们的VCMamba-B在ImageNet-1K上实现了82.6%的top-1准确率，超过PlainMamba-L3 0.3%，参数减少了37%，并且超过Vision GNN-B 0.3%，参数减少了64%。此外，VCMamba-B在ADE20K上获得了47.1 mIoU，超过EfficientFormer-L7 2.0 mIoU，同时参数减少了62%。代码可在https://github.com/Wertyuui345/VCMamba 获取。

## 🔬 方法详解

**问题定义**：现有视觉模型，如ViT和Mamba，虽然在全局信息建模上有所突破，但在局部特征提取方面仍有不足，无法充分利用图像的局部结构信息。CNN虽然擅长局部特征提取，但缺乏全局建模能力。因此，如何有效地结合CNN和Mamba的优势，构建一个既能提取局部特征又能建模全局依赖的视觉骨干网络，是本文要解决的问题。

**核心思路**：VCMamba的核心思路是将CNN和多向Mamba SSM结合起来，利用CNN提取局部特征，利用Mamba建模长程依赖关系。通过这种混合架构，VCMamba可以同时捕获图像的局部细节和全局上下文信息，从而实现更有效的视觉表征。这种设计旨在弥补现有视觉模型在局部和全局信息建模方面的不足。

**技术框架**：VCMamba的整体架构包括一个卷积stem和分层结构。卷积stem用于提取初始的局部特征。分层结构包含多个阶段，早期阶段使用卷积块来提取丰富的局部特征，后续阶段使用多向Mamba块来建模长程依赖和全局上下文。这种分层结构使得VCMamba能够逐步地从局部到全局地提取图像特征。

**关键创新**：VCMamba的关键创新在于将卷积和多向Mamba SSM有机地结合在一起。通过卷积stem和早期卷积块，VCMamba能够有效地提取局部特征，而多向Mamba块则能够建模长程依赖关系和全局上下文。这种混合架构使得VCMamba能够同时捕获图像的局部细节和全局上下文信息，从而实现更有效的视觉表征。与纯CNN或纯Mamba模型相比，VCMamba能够更好地平衡局部和全局信息建模。

**关键设计**：VCMamba的关键设计包括卷积stem的参数设置、卷积块的结构设计、多向Mamba块的配置以及分层结构的层数和通道数。具体来说，卷积stem通常采用较小的卷积核和步长，以提取细粒度的局部特征。卷积块可以采用不同的卷积操作，如深度可分离卷积或分组卷积，以减少计算量。多向Mamba块的设计需要考虑不同方向上的信息交互，以更好地建模长程依赖关系。分层结构的层数和通道数需要根据具体的任务和数据集进行调整，以达到最佳的性能。

## 📊 实验亮点

VCMamba-B在ImageNet-1K上实现了82.6%的top-1准确率，超过PlainMamba-L3 0.3%，参数减少了37%，超过Vision GNN-B 0.3%，参数减少了64%。在ADE20K上获得了47.1 mIoU，超过EfficientFormer-L7 2.0 mIoU，同时参数减少了62%。这些结果表明，VCMamba在性能和效率方面均优于现有模型。

## 🎯 应用场景

VCMamba作为一种通用的视觉骨干网络，可以广泛应用于各种计算机视觉任务，如图像分类、目标检测、语义分割等。其高效的特征表示能力和线性复杂度使其在资源受限的设备上也能实现高性能。未来，VCMamba有望在自动驾驶、智能监控、医学图像分析等领域发挥重要作用。

## 📄 摘要（原文）

> Recent advances in Vision Transformers (ViTs) and State Space Models (SSMs) have challenged the dominance of Convolutional Neural Networks (CNNs) in computer vision. ViTs excel at capturing global context, and SSMs like Mamba offer linear complexity for long sequences, yet they do not capture fine-grained local features as effectively as CNNs. Conversely, CNNs possess strong inductive biases for local features but lack the global reasoning capabilities of transformers and Mamba. To bridge this gap, we introduce \textit{VCMamba}, a novel vision backbone that integrates the strengths of CNNs and multi-directional Mamba SSMs. VCMamba employs a convolutional stem and a hierarchical structure with convolutional blocks in its early stages to extract rich local features. These convolutional blocks are then processed by later stages incorporating multi-directional Mamba blocks designed to efficiently model long-range dependencies and global context. This hybrid design allows for superior feature representation while maintaining linear complexity with respect to image resolution. We demonstrate VCMamba's effectiveness through extensive experiments on ImageNet-1K classification and ADE20K semantic segmentation. Our VCMamba-B achieves 82.6% top-1 accuracy on ImageNet-1K, surpassing PlainMamba-L3 by 0.3% with 37% fewer parameters, and outperforming Vision GNN-B by 0.3% with 64% fewer parameters. Furthermore, VCMamba-B obtains 47.1 mIoU on ADE20K, exceeding EfficientFormer-L7 by 2.0 mIoU while utilizing 62% fewer parameters. Code is available at https://github.com/Wertyuui345/VCMamba.

