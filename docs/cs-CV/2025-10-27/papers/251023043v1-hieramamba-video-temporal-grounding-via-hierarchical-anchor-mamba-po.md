---
layout: default
title: HieraMamba: Video Temporal Grounding via Hierarchical Anchor-Mamba Pooling
---

# HieraMamba: Video Temporal Grounding via Hierarchical Anchor-Mamba Pooling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23043" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23043v1</a>
  <a href="https://arxiv.org/pdf/2510.23043.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23043v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.23043v1', 'HieraMamba: Video Temporal Grounding via Hierarchical Anchor-Mamba Pooling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joungbin An, Kristen Grauman

**分类**: cs.CV

**发布日期**: 2025-10-27

**备注**: Project Page: https://vision.cs.utexas.edu/projects/hieramamba/

---

## 💡 一句话要点

**HieraMamba：通过分层Anchor-Mamba池化实现视频时序定位**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `视频时序定位` `长视频理解` `Mamba模型` `分层架构` `对比学习`

## 📋 核心要点

1. 现有视频时序定位方法在处理长视频时，常因过度下采样或固定窗口而损失时间精度。
2. HieraMamba利用分层架构和Anchor-Mamba池化，在不同尺度上保留时间结构和语义信息。
3. 实验表明，HieraMamba在多个数据集上达到SOTA，实现了更精确的时序定位。

## 📝 摘要（中文）

视频时序定位旨在未裁剪视频中定位自然语言查询对应的起始和结束时间。该任务需要捕捉全局上下文和精细的时间细节。在长视频中，这一挑战尤为突出，现有方法通常通过过度下采样或依赖固定窗口来牺牲时间保真度。我们提出了HieraMamba，一种分层架构，可在不同尺度上保留时间结构和语义丰富性。其核心是Anchor-Mamba池化（AMP）块，它利用Mamba的选择性扫描来生成紧凑的anchor token，以总结多个粒度的视频内容。两个互补的目标，即anchor条件对比损失和分段池化对比损失，鼓励anchor保留局部细节，同时保持全局区分性。HieraMamba在Ego4D-NLQ、MAD和TACoS上取得了新的state-of-the-art，展示了在长未裁剪视频中精确、时间保真的定位。

## 🔬 方法详解

**问题定义**：视频时序定位旨在给定一个未裁剪的长视频和一个自然语言查询，预测视频中与查询相关的片段的起始和结束时间。现有方法在处理长视频时，为了降低计算复杂度，通常会进行过度下采样，导致时间分辨率降低，或者使用固定大小的窗口，无法适应不同长度的查询片段，从而影响定位精度。

**核心思路**：HieraMamba的核心思路是利用分层架构和Anchor-Mamba池化（AMP）块，在不同尺度上提取视频特征，从而同时捕捉全局上下文和精细的时间细节。通过选择性扫描机制，AMP块能够生成紧凑的anchor token，这些token既能保留局部细节，又能具备全局区分性。

**技术框架**：HieraMamba的整体架构是一个分层结构，包含多个Anchor-Mamba池化（AMP）块。每个AMP块接收上一层的特征作为输入，并输出更高级别的特征表示。AMP块的核心是Mamba模型，它通过选择性扫描机制，对输入特征进行处理，生成anchor token。这些anchor token被用于后续的对比学习，以提高模型的定位精度。整个流程包括视频特征提取、分层特征编码和时序边界预测三个阶段。

**关键创新**：HieraMamba的关键创新在于Anchor-Mamba池化（AMP）块的设计。AMP块利用Mamba的选择性扫描机制，能够有效地处理长序列数据，并生成具有全局上下文信息的anchor token。此外，HieraMamba还提出了anchor条件对比损失和分段池化对比损失，这两种损失函数能够有效地提高anchor token的区分性和定位精度。与现有方法相比，HieraMamba能够在保持时间分辨率的同时，有效地捕捉全局上下文信息。

**关键设计**：Anchor-Mamba池化（AMP）块包含Mamba层和池化层。Mamba层负责对输入特征进行选择性扫描，生成anchor token。池化层负责对anchor token进行降维，以减少计算复杂度。Anchor条件对比损失通过对比anchor token和对应的视频片段特征，来提高anchor token的区分性。分段池化对比损失通过对比不同视频片段的特征，来提高模型的定位精度。具体参数设置包括Mamba层的层数、隐藏层维度、池化层的池化大小等。损失函数的权重也需要根据具体任务进行调整。

## 📊 实验亮点

HieraMamba在Ego4D-NLQ、MAD和TACoS三个视频时序定位数据集上取得了新的state-of-the-art。在Ego4D-NLQ数据集上，HieraMamba的性能显著优于现有方法，证明了其在长视频时序定位方面的优势。实验结果表明，HieraMamba能够有效地捕捉全局上下文和精细的时间细节，从而实现更精确的定位。

## 🎯 应用场景

HieraMamba在视频内容理解、视频检索、智能监控等领域具有广泛的应用前景。它可以用于在海量视频数据中快速定位用户感兴趣的片段，提高视频检索的效率和准确性。此外，HieraMamba还可以应用于智能监控系统中，用于检测异常事件和行为，提高安全防范能力。未来，该技术有望在更多视频相关的应用中发挥重要作用。

## 📄 摘要（原文）

> Video temporal grounding, the task of localizing the start and end times of a natural language query in untrimmed video, requires capturing both global context and fine-grained temporal detail. This challenge is particularly pronounced in long videos, where existing methods often compromise temporal fidelity by over-downsampling or relying on fixed windows. We present HieraMamba, a hierarchical architecture that preserves temporal structure and semantic richness across scales. At its core are Anchor-MambaPooling (AMP) blocks, which utilize Mamba's selective scanning to produce compact anchor tokens that summarize video content at multiple granularities. Two complementary objectives, anchor-conditioned and segment-pooled contrastive losses, encourage anchors to retain local detail while remaining globally discriminative. HieraMamba sets a new state-of-the-art on Ego4D-NLQ, MAD, and TACoS, demonstrating precise, temporally faithful localization in long, untrimmed videos.

