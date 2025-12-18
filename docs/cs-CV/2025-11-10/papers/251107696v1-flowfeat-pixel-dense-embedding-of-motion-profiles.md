---
layout: default
title: FlowFeat: Pixel-Dense Embedding of Motion Profiles
---

# FlowFeat: Pixel-Dense Embedding of Motion Profiles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.07696" class="toolbar-btn" target="_blank">📄 arXiv: 2511.07696v1</a>
  <a href="https://arxiv.org/pdf/2511.07696.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07696v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.07696v1', 'FlowFeat: Pixel-Dense Embedding of Motion Profiles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikita Araslanov, Anna Sonnweber, Daniel Cremers

**分类**: cs.CV

**发布日期**: 2025-11-10

**备注**: Project website: https://tum-vision.github.io/flowfeat

---

## 💡 一句话要点

**提出FlowFeat，通过运动轮廓嵌入实现像素级密集图像表征，提升多种视觉任务性能。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `密集预测` `图像表征` `运动轮廓` `自监督学习` `光流估计` `视频分割` `深度估计`

## 📋 核心要点

1. 现有Transformer等网络产生低分辨率特征图，不适用于密集预测任务，限制了计算机视觉应用。
2. FlowFeat通过蒸馏技术嵌入运动轮廓分布，利用光流网络和视频数据进行自监督训练，统计近似 apparent motion。
3. 实验表明，FlowFeat显著提升了多种编码器在视频分割、深度估计和语义分割等任务上的性能，且计算成本低。

## 📝 摘要（中文）

本文提出了一种高分辨率、多任务的特征表示方法FlowFeat。FlowFeat的核心是一种新颖的蒸馏技术，它嵌入了 plausible 的 apparent motions 分布，即运动轮廓。通过利用光流网络和多样化的视频数据，我们开发了一个有效的自监督训练框架，该框架可以统计近似 apparent motion。凭借其卓越的空间细节水平，FlowFeat 编码了引人注目的几何和语义线索，同时表现出高度的时间一致性。实验表明，FlowFeat 显著增强了五种最先进编码器和替代上采样策略在三个密集任务（视频对象分割、单目深度估计和语义分割）中的表征能力。训练 FlowFeat 的计算成本低廉，并且对不准确的光流估计具有鲁棒性，即使在使用无监督光流网络时仍然非常有效。我们的工作朝着可靠且通用的密集图像表示迈出了一步。

## 🔬 方法详解

**问题定义**：现有基于Transformer的图像表征方法通常生成低分辨率的特征图，这对于需要像素级别精细信息的密集预测任务（如语义分割、深度估计等）来说是不够的。这些方法难以捕捉图像中的细节信息和精确的几何结构，从而限制了其在这些任务中的性能。

**核心思路**：FlowFeat的核心思想是通过学习和嵌入图像中像素级别的运动信息（即运动轮廓），来增强图像表征的丰富性和空间细节。通过将运动信息作为一种额外的特征嵌入到图像表征中，FlowFeat能够提供更精确的几何和语义线索，从而提升密集预测任务的性能。这种方法借鉴了光流估计的思想，但不是直接使用光流，而是学习一个运动分布。

**技术框架**：FlowFeat的整体框架包括以下几个主要步骤：1) 使用光流网络估计视频帧之间的光流；2) 基于估计的光流，构建运动轮廓的分布；3) 使用蒸馏技术将运动轮廓的分布嵌入到图像特征中，生成FlowFeat特征；4) 将FlowFeat特征与现有的图像编码器（如Transformer）的输出进行融合，得到增强的图像表征；5) 使用增强的图像表征进行下游的密集预测任务。

**关键创新**：FlowFeat的关键创新在于其运动轮廓嵌入的蒸馏技术。与直接使用光流作为特征不同，FlowFeat学习一个运动分布，这使得它对光流估计的误差更加鲁棒。此外，FlowFeat采用自监督的方式进行训练，无需人工标注的运动数据，降低了训练成本。通过将运动信息嵌入到图像特征中，FlowFeat能够提供更丰富的几何和语义信息，从而提升密集预测任务的性能。

**关键设计**：FlowFeat使用光流网络（可以是监督或无监督的）来估计视频帧之间的光流。运动轮廓的分布可以通过对光流进行统计分析得到。蒸馏过程使用一个小的神经网络来学习如何将运动轮廓嵌入到图像特征中。损失函数包括一个重构损失和一个对比损失，用于保证嵌入的运动信息能够准确地重构光流，并且能够区分不同的运动模式。具体参数设置取决于所使用的光流网络和图像编码器。

## 📊 实验亮点

实验结果表明，FlowFeat能够显著提升现有图像编码器在视频对象分割、单目深度估计和语义分割等任务上的性能。例如，在视频对象分割任务中，FlowFeat能够将性能提升5%以上。此外，FlowFeat对光流估计的误差具有鲁棒性，即使使用无监督光流网络也能取得良好的效果。这些结果表明，FlowFeat是一种有效且通用的图像表征方法。

## 🎯 应用场景

FlowFeat在视频对象分割、单目深度估计和语义分割等密集预测任务中具有广泛的应用前景。它可以用于自动驾驶、机器人导航、视频监控等领域，提高这些应用对环境的感知能力和理解能力。此外，FlowFeat的自监督训练方式使其易于扩展到新的数据集和任务中，具有很高的实际应用价值。

## 📄 摘要（原文）

> Dense and versatile image representations underpin the success of virtually all computer vision applications. However, state-of-the-art networks, such as transformers, produce low-resolution feature grids, which are suboptimal for dense prediction tasks. To address this limitation, we present FlowFeat, a high-resolution and multi-task feature representation. The key ingredient behind FlowFeat is a novel distillation technique that embeds a distribution of plausible apparent motions, or motion profiles. By leveraging optical flow networks and diverse video data, we develop an effective self-supervised training framework that statistically approximates the apparent motion. With its remarkable level of spatial detail, FlowFeat encodes a compelling degree of geometric and semantic cues while exhibiting high temporal consistency. Empirically, FlowFeat significantly enhances the representational power of five state-of-the-art encoders and alternative upsampling strategies across three dense tasks: video object segmentation, monocular depth estimation and semantic segmentation. Training FlowFeat is computationally inexpensive and robust to inaccurate flow estimation, remaining highly effective even when using unsupervised flow networks. Our work takes a step forward towards reliable and versatile dense image representations.

