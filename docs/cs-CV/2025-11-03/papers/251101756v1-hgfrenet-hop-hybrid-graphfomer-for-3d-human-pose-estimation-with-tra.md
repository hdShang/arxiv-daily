---
layout: default
title: "HGFreNet: Hop-hybrid GraphFomer for 3D Human Pose Estimation with Trajectory Consistency in Frequency Domain"
---

# HGFreNet: Hop-hybrid GraphFomer for 3D Human Pose Estimation with Trajectory Consistency in Frequency Domain

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.01756" class="toolbar-btn" target="_blank">📄 arXiv: 2511.01756v1</a>
  <a href="https://arxiv.org/pdf/2511.01756.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.01756v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.01756v1', 'HGFreNet: Hop-hybrid GraphFomer for 3D Human Pose Estimation with Trajectory Consistency in Frequency Domain')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai Zhai, Ziyan Huang, Qiang Nie, Xiang Li, Bo Ouyang

**分类**: cs.CV

**发布日期**: 2025-11-03

---

## 💡 一句话要点

**提出HGFreNet，利用Hop-hybrid GraphFomer解决单目视频3D人体姿态估计中的轨迹不一致问题。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D人体姿态估计` `单目视频` `图神经网络` `Transformer` `频域分析` `时空建模` `轨迹一致性`

## 📋 核心要点

1. 单目视频3D人体姿态估计易受深度歧义和2D误差影响，导致3D轨迹不连贯，现有方法缺乏对全局时空相关性的有效建模。
2. HGFreNet通过Hop-hybrid图注意力模块和Transformer编码器，捕捉关节的全局时空相关性，并在频域约束轨迹一致性，提升姿态估计的准确性和连贯性。
3. 在Human3.6M和MPI-INF-3DHP数据集上的实验表明，HGFreNet在位置精度和时间一致性方面均超越了现有最佳方法。

## 📝 摘要（中文）

本文针对单目视频中3D人体姿态估计的2D-to-3D姿态提升问题，该问题面临深度模糊和2D姿态估计误差导致的3D轨迹不一致性挑战。现有方法主要在时域限制抖动，忽略了骨骼关节运动的全局时空相关性。为此，我们设计了一种新颖的GraphFormer架构HGFreNet，它结合了跳跃混合特征聚合和频域中的3D轨迹一致性。具体而言，我们提出了一个跳跃混合图注意力（HGA）模块和一个Transformer编码器来建模全局关节时空相关性。HGA模块将骨骼关节的所有k跳邻居分组到一个混合组中，以扩大感受野，并应用注意力机制来发现这些组的潜在相关性。然后，我们通过约束频域中的轨迹一致性来利用全局时间相关性。为了为跨帧的深度推断提供3D信息并保持时间上的一致性，应用初步网络来估计3D姿态。在Human3.6M和MPI-INF-3DHP两个标准基准数据集上进行了大量实验。结果表明，所提出的HGFreNet在位置精度和时间一致性方面均优于最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决单目视频3D人体姿态估计中，由于2D姿态估计误差和深度模糊性导致的3D轨迹不一致问题。现有方法主要关注时域上的平滑，例如限制相邻帧之间的差异，但忽略了骨骼关节运动的全局时空相关性，导致估计的3D姿态序列存在抖动和不连贯现象。

**核心思路**：论文的核心思路是利用GraphFormer架构，结合跳跃混合图注意力机制和频域约束，同时建模关节的全局时空相关性和轨迹的时间一致性。通过扩大感受野和在频域进行约束，可以更有效地抑制噪声和提高估计的稳定性。

**技术框架**：HGFreNet的整体架构包含以下几个主要模块：1) 2D姿态输入；2) 初始3D姿态估计网络（为后续模块提供初步的3D信息）；3) Hop-hybrid图注意力（HGA）模块，用于聚合关节的k跳邻居信息；4) Transformer编码器，用于建模全局时空相关性；5) 频域轨迹一致性约束模块，用于保证估计的3D姿态序列在时间上的平滑性。

**关键创新**：论文的关键创新在于以下几点：1) 提出了Hop-hybrid图注意力（HGA）模块，通过将k跳邻居分组并应用注意力机制，扩大了感受野，更好地捕捉了关节之间的空间关系；2) 在频域上对3D轨迹进行一致性约束，有效地抑制了时间上的抖动，提高了姿态估计的稳定性；3) 将图神经网络和Transformer结合，充分利用了它们在建模空间和时间相关性方面的优势。

**关键设计**：HGA模块的关键设计在于如何选择合适的k值以及如何定义邻居组。频域约束的关键在于选择合适的变换方法（例如离散余弦变换DCT）以及如何设计损失函数来衡量轨迹的一致性。初步3D姿态估计网络可以使用现有的2D-to-3D lifting方法，但需要保证其输出的3D姿态具有一定的精度，以便为后续模块提供有用的信息。

## 📊 实验亮点

HGFreNet在Human3.6M和MPI-INF-3DHP数据集上取得了显著的性能提升。具体而言，在Human3.6M数据集上，HGFreNet在多个指标上超越了现有SOTA方法，尤其是在时间一致性方面有明显改善。实验结果表明，所提出的Hop-hybrid图注意力模块和频域约束能够有效地提高3D人体姿态估计的准确性和稳定性。

## 🎯 应用场景

该研究成果可应用于人机交互、动作捕捉、虚拟现实/增强现实、智能监控、运动分析等领域。通过提高单目视频3D人体姿态估计的准确性和稳定性，可以为这些应用提供更可靠的输入数据，从而提升用户体验和系统性能。未来，该方法有望扩展到更复杂的场景，例如多人交互、遮挡情况等。

## 📄 摘要（原文）

> 2D-to-3D human pose lifting is a fundamental challenge for 3D human pose estimation in monocular video, where graph convolutional networks (GCNs) and attention mechanisms have proven to be inherently suitable for encoding the spatial-temporal correlations of skeletal joints. However, depth ambiguity and errors in 2D pose estimation lead to incoherence in the 3D trajectory. Previous studies have attempted to restrict jitters in the time domain, for instance, by constraining the differences between adjacent frames while neglecting the global spatial-temporal correlations of skeletal joint motion. To tackle this problem, we design HGFreNet, a novel GraphFormer architecture with hop-hybrid feature aggregation and 3D trajectory consistency in the frequency domain. Specifically, we propose a hop-hybrid graph attention (HGA) module and a Transformer encoder to model global joint spatial-temporal correlations. The HGA module groups all $k$-hop neighbors of a skeletal joint into a hybrid group to enlarge the receptive field and applies the attention mechanism to discover the latent correlations of these groups globally. We then exploit global temporal correlations by constraining trajectory consistency in the frequency domain. To provide 3D information for depth inference across frames and maintain coherence over time, a preliminary network is applied to estimate the 3D pose. Extensive experiments were conducted on two standard benchmark datasets: Human3.6M and MPI-INF-3DHP. The results demonstrate that the proposed HGFreNet outperforms state-of-the-art (SOTA) methods in terms of positional accuracy and temporal consistency.

