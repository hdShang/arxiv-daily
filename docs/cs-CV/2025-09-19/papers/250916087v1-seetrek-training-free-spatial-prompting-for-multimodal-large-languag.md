---
layout: default
title: "See&Trek: Training-Free Spatial Prompting for Multimodal Large Language Model"
---

# See&Trek: Training-Free Spatial Prompting for Multimodal Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16087" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16087v1</a>
  <a href="https://arxiv.org/pdf/2509.16087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16087v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16087v1', 'See&Trek: Training-Free Spatial Prompting for Multimodal Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pengteng Li, Pinhao Song, Wuyang Li, Weiyu Guo, Huizai Yao, Yijie Xu, Dugang Liu, Hui Xiong

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-19

**备注**: Accepted by NeurIPS 2025

---

## 💡 一句话要点

**提出SEE&TREK，一种免训练的空间提示框架，提升MLLM的视觉空间理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `空间理解` `视觉提示` `免训练学习` `运动重建`

## 📋 核心要点

1. 现有MLLM在纯视觉下的空间理解能力不足，依赖深度等模态，限制了其应用场景。
2. SEE&TREK通过最大语义丰富度采样和运动重建，增加视觉多样性，保留空间关系和时间连贯性。
3. SEE&TREK无需训练，易于集成，在VSI-BENCH和STI-BENCH上取得了显著的性能提升。

## 📝 摘要（中文）

本文提出SEE&TREK，首个免训练的提示框架，旨在增强多模态大语言模型(MLLM)在纯视觉约束下的空间理解能力。现有方法主要依赖深度或点云等模态来提升空间推理，而纯视觉空间理解仍有待探索。SEE&TREK通过增加视觉多样性和运动重建来解决这一问题。在视觉多样性方面，我们采用最大语义丰富度采样，利用现成的感知模型提取语义丰富的关键帧，捕捉场景结构。在运动重建方面，我们模拟视觉轨迹，并将相对空间位置编码到关键帧中，以保留空间关系和时间连贯性。我们的方法无需训练和GPU，只需一次前向传播，即可无缝集成到现有的MLLM中。在VSI-BENCH和STI-BENCH上的大量实验表明，SEE&TREK在各种空间推理任务中持续提升了各种MLLM的性能，最高提升达3.5%，为更强的空间智能提供了有希望的途径。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLM）在仅有视觉信息输入的情况下，空间理解能力不足的问题。现有方法通常依赖于深度信息、点云数据等辅助模态来增强空间推理，但在缺乏这些信息时，纯视觉的空间理解能力仍然是一个挑战。现有方法的痛点在于对视觉信息的利用不够充分，无法有效地提取和利用场景中的空间关系。

**核心思路**：SEE&TREK的核心思路是通过增加视觉输入的多样性和重建运动轨迹来提升MLLM的空间理解能力。具体来说，通过最大语义丰富度采样（Maximum Semantic Richness Sampling）来选择信息量大的关键帧，从而捕捉场景结构；通过模拟视觉轨迹并将相对空间位置编码到关键帧中，来保留空间关系和时间连贯性。这样设计的目的是为了让MLLM能够从更丰富的视觉信息中学习到更准确的空间表征。

**技术框架**：SEE&TREK的整体框架包含两个主要模块：最大语义丰富度采样（MSRS）和运动重建。首先，MSRS模块利用一个现成的感知模型（off-the-shell perception model）提取图像的语义信息，并选择语义最丰富的关键帧。然后，运动重建模块模拟视觉轨迹，并将相对空间位置信息编码到关键帧中。最后，将处理后的关键帧输入到MLLM中进行空间推理。

**关键创新**：SEE&TREK最重要的技术创新点在于其免训练的提示框架。与需要大量训练数据和计算资源的现有方法不同，SEE&TREK只需要一次前向传播即可完成空间信息的增强，可以无缝集成到现有的MLLM中。此外，通过最大语义丰富度采样和运动重建，有效地提升了视觉信息的利用率，从而增强了MLLM的空间理解能力。

**关键设计**：在最大语义丰富度采样中，论文使用预训练的感知模型（具体模型未知）提取图像的语义特征，并根据语义特征的丰富程度选择关键帧。在运动重建中，论文模拟视觉轨迹的具体方法未知，但其核心思想是将相对空间位置信息编码到关键帧中，以便MLLM能够学习到空间关系。损失函数和网络结构方面，由于是免训练方法，因此没有涉及。

## 📊 实验亮点

SEE&TREK在VSI-BENCH和STI-BENCH数据集上进行了广泛的实验，结果表明该方法能够显著提升各种MLLM的性能。具体而言，SEE&TREK在多个空间推理任务中取得了高达3.5%的性能提升，证明了其有效性。值得注意的是，SEE&TREK是一种免训练的方法，这意味着它可以在不增加额外训练成本的情况下，提升现有MLLM的性能。

## 🎯 应用场景

SEE&TREK具有广泛的应用前景，例如机器人导航、自动驾驶、虚拟现实和增强现实等领域。通过提升MLLM在纯视觉下的空间理解能力，可以使机器人在复杂环境中更好地感知和理解周围环境，从而实现更智能的决策和控制。此外，该方法还可以应用于图像检索、视频分析等任务，提升相关应用的性能。

## 📄 摘要（原文）

> We introduce SEE&TREK, the first training-free prompting framework tailored to enhance the spatial understanding of Multimodal Large Language Models (MLLMS) under vision-only constraints. While prior efforts have incorporated modalities like depth or point clouds to improve spatial reasoning, purely visualspatial understanding remains underexplored. SEE&TREK addresses this gap by focusing on two core principles: increasing visual diversity and motion reconstruction. For visual diversity, we conduct Maximum Semantic Richness Sampling, which employs an off-the-shell perception model to extract semantically rich keyframes that capture scene structure. For motion reconstruction, we simulate visual trajectories and encode relative spatial positions into keyframes to preserve both spatial relations and temporal coherence. Our method is training&GPU-free, requiring only a single forward pass, and can be seamlessly integrated into existing MLLM'S. Extensive experiments on the VSI-B ENCH and STI-B ENCH show that S EE &T REK consistently boosts various MLLM S performance across diverse spatial reasoning tasks with the most +3.5% improvement, offering a promising path toward stronger spatial intelligence.

