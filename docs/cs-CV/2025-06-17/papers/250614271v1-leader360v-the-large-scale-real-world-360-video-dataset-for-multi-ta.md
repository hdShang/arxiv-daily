---
layout: default
title: "Leader360V: The Large-scale, Real-world 360 Video Dataset for Multi-task Learning in Diverse Environment"
---

# Leader360V: The Large-scale, Real-world 360 Video Dataset for Multi-task Learning in Diverse Environment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14271" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14271v1</a>
  <a href="https://arxiv.org/pdf/2506.14271.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14271v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14271v1', 'Leader360V: The Large-scale, Real-world 360 Video Dataset for Multi-task Learning in Diverse Environment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weiming Zhang, Dingwen Xiao, Aobotao Dai, Yexin Liu, Tianbo Pan, Shiqi Wen, Lei Chen, Lin Wang

**分类**: cs.CV

**发布日期**: 2025-06-17

**备注**: 23 pages, 16 figures

---

## 💡 一句话要点

**提出Leader360V以解决360视频数据集缺乏的问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `360视频理解` `实例分割` `自动标注` `多任务学习` `真实世界数据集` `机器人视觉` `语义分割`

## 📋 核心要点

1. 现有方法面临缺乏大规模、标注真实世界360视频数据集的挑战，导致360场景理解任务受限。
2. 本文提出Leader360V数据集，并设计了自动标注管道，结合2D分割器和大型语言模型以提高标注效率。
3. 实验结果表明，Leader360V显著提升了360视频分割和跟踪模型的性能，推动了360场景理解的发展。

## 📝 摘要（中文）

360视频捕捉了完整的周围场景，具有360X180的超大视野。这使得360场景理解任务（如分割和跟踪）在自动驾驶和机器人等应用中至关重要。然而，现有的基础模型面临缺乏大规模标注真实世界数据集的挑战。本文介绍了Leader360V，这是首个大规模标注的真实世界360视频数据集，专注于实例分割和跟踪。我们设计了一种自动标注管道，结合预训练的2D分割器和大型语言模型，显著提高了标注效率和准确性。实验表明，Leader360V显著提升了360视频分割和跟踪模型的性能，为更可扩展的360场景理解奠定了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决360视频数据集缺乏的问题，现有方法在标注真实世界数据集时面临高成本和复杂性，尤其是在极地区域的严重失真和内容不连续性方面。

**核心思路**：论文提出了一种自动标注管道，通过协调预训练的2D分割器和大型语言模型，来提高标注的效率和准确性。该管道分为三个阶段，旨在减少人工干预。

**技术框架**：整体架构包括初始标注阶段、自动修正标注阶段和人工修订阶段。初始标注阶段引入了语义和失真感知的细化模块，后续阶段则通过再次应用SDR或处理水平边界附近的不连续性来修正缺失区域。

**关键创新**：最重要的创新在于结合了多种2D分割器的物体掩码提案与大型语言模型验证的语义标签，从而生成失真感知的掩码。这一方法与传统的单一标注方法有本质区别。

**关键设计**：在初始标注阶段，使用了SAM2生成失真感知掩码的掩码提示；在自动修正阶段，采用了SDR技术来处理缺失区域，确保标注的完整性和准确性。

## 📊 实验亮点

实验结果显示，Leader360V在360视频分割和跟踪任务中显著提升了模型性能，具体提升幅度达到XX%（具体数据待补充），相较于基线方法表现出更好的效果，验证了自动标注管道的有效性。

## 🎯 应用场景

Leader360V数据集的提出为自动驾驶、机器人等领域的360场景理解提供了重要的数据支持。通过高效的标注管道，研究者可以更快速地获取高质量的标注数据，从而推动相关算法的发展和应用，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> 360 video captures the complete surrounding scenes with the ultra-large field of view of 360X180. This makes 360 scene understanding tasks, eg, segmentation and tracking, crucial for appications, such as autonomous driving, robotics. With the recent emergence of foundation models, the community is, however, impeded by the lack of large-scale, labelled real-world datasets. This is caused by the inherent spherical properties, eg, severe distortion in polar regions, and content discontinuities, rendering the annotation costly yet complex. This paper introduces Leader360V, the first large-scale, labeled real-world 360 video datasets for instance segmentation and tracking. Our datasets enjoy high scene diversity, ranging from indoor and urban settings to natural and dynamic outdoor scenes. To automate annotation, we design an automatic labeling pipeline, which subtly coordinates pre-trained 2D segmentors and large language models to facilitate the labeling. The pipeline operates in three novel stages. Specifically, in the Initial Annotation Phase, we introduce a Semantic- and Distortion-aware Refinement module, which combines object mask proposals from multiple 2D segmentors with LLM-verified semantic labels. These are then converted into mask prompts to guide SAM2 in generating distortion-aware masks for subsequent frames. In the Auto-Refine Annotation Phase, missing or incomplete regions are corrected either by applying the SDR again or resolving the discontinuities near the horizontal borders. The Manual Revision Phase finally incorporates LLMs and human annotators to further refine and validate the annotations. Extensive user studies and evaluations demonstrate the effectiveness of our labeling pipeline. Meanwhile, experiments confirm that Leader360V significantly enhances model performance for 360 video segmentation and tracking, paving the way for more scalable 360 scene understanding.

