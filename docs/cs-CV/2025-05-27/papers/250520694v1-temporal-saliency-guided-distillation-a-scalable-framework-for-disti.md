---
layout: default
title: Temporal Saliency-Guided Distillation: A Scalable Framework for Distilling Video Datasets
---

# Temporal Saliency-Guided Distillation: A Scalable Framework for Distilling Video Datasets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20694" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20694v1</a>
  <a href="https://arxiv.org/pdf/2505.20694.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20694v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20694v1', 'Temporal Saliency-Guided Distillation: A Scalable Framework for Distilling Video Datasets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xulin Gu, Xinhao Zhong, Zhixing Wei, Yimin Zhou, Shuoyang Sun, Bin Chen, Hongpeng Wang, Yuan Luo

**分类**: cs.CV, cs.LG

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出时间显著性引导蒸馏框架以解决视频数据集压缩问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频蒸馏` `数据集压缩` `时间显著性` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有视频蒸馏方法计算成本高且难以保留时间动态，简单扩展图像方法导致性能下降。
2. 提出一种单级视频数据集蒸馏框架，直接优化合成视频，利用时间显著性引导过滤机制。
3. 在标准视频基准上进行的实验表明，该方法实现了最先进的性能，提升了蒸馏视频的质量。

## 📝 摘要（中文）

数据集蒸馏（DD）作为一种强大的数据集压缩范式，能够合成紧凑的替代数据集，以近似大规模数据集的训练效用。尽管在图像数据集蒸馏方面取得了显著进展，但将DD扩展到视频领域仍然面临挑战，主要由于视频数据的高维性和时间复杂性。现有的视频蒸馏方法往往面临过高的计算成本，并且难以保留时间动态，因为简单扩展基于图像的方法通常会导致性能下降。本文提出了一种新颖的单级视频数据集蒸馏框架，直接针对预训练模型优化合成视频。为了解决时间冗余并增强运动保留，我们引入了一种时间显著性引导的过滤机制，利用帧间差异来指导蒸馏过程，鼓励保留信息丰富的时间线索，同时抑制帧级冗余。大量在标准视频基准上的实验表明，我们的方法实现了最先进的性能，弥合了真实视频数据与蒸馏视频数据之间的差距，为视频数据集压缩提供了可扩展的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决视频数据集蒸馏中的高维性和时间复杂性问题。现有方法在计算成本和时间动态保留方面存在显著不足，导致蒸馏性能下降。

**核心思路**：提出的框架通过直接优化合成视频来提升蒸馏效果，并引入时间显著性引导的过滤机制，以保留重要的时间信息，抑制冗余。

**技术框架**：整体架构包括数据输入、时间显著性计算、合成视频生成和优化四个主要模块。首先计算帧间差异，然后根据显著性指导合成过程。

**关键创新**：引入时间显著性引导的过滤机制是本文的核心创新，与现有方法相比，能够更有效地保留视频中的重要动态信息。

**关键设计**：在参数设置上，采用了特定的损失函数以平衡时间信息保留与冗余抑制，网络结构则基于预训练模型进行优化，确保合成视频的质量。

## 📊 实验亮点

实验结果表明，提出的方法在多个标准视频基准上达到了最先进的性能，相较于基线方法，蒸馏视频的质量提升显著，具体性能数据未明确提供。

## 🎯 应用场景

该研究的潜在应用领域包括视频监控、自动驾驶、视频分析等场景，能够有效压缩视频数据集，降低存储和计算成本，同时保持高质量的训练效果。未来，该框架有望推动视频理解和生成任务的发展。

## 📄 摘要（原文）

> Dataset distillation (DD) has emerged as a powerful paradigm for dataset compression, enabling the synthesis of compact surrogate datasets that approximate the training utility of large-scale ones. While significant progress has been achieved in distilling image datasets, extending DD to the video domain remains challenging due to the high dimensionality and temporal complexity inherent in video data. Existing video distillation (VD) methods often suffer from excessive computational costs and struggle to preserve temporal dynamics, as naïve extensions of image-based approaches typically lead to degraded performance. In this paper, we propose a novel uni-level video dataset distillation framework that directly optimizes synthetic videos with respect to a pre-trained model. To address temporal redundancy and enhance motion preservation, we introduce a temporal saliency-guided filtering mechanism that leverages inter-frame differences to guide the distillation process, encouraging the retention of informative temporal cues while suppressing frame-level redundancy. Extensive experiments on standard video benchmarks demonstrate that our method achieves state-of-the-art performance, bridging the gap between real and distilled video data and offering a scalable solution for video dataset compression.

