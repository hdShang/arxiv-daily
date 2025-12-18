---
layout: default
title: FastHMR: Accelerating Human Mesh Recovery via Token and Layer Merging with Diffusion Decoding
---

# FastHMR: Accelerating Human Mesh Recovery via Token and Layer Merging with Diffusion Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10868" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10868v1</a>
  <a href="https://arxiv.org/pdf/2510.10868.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10868v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.10868v1', 'FastHMR: Accelerating Human Mesh Recovery via Token and Layer Merging with Diffusion Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Soroush Mehraban, Andrea Iaboni, Babak Taati

**分类**: cs.CV

**发布日期**: 2025-10-13

**备注**: Project page: https://soroushmehraban.github.io/FastHMR/

---

## 💡 一句话要点

**FastHMR：通过Token和层合并及扩散解码加速人体网格重建**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `人体网格重建` `Transformer` `模型加速` `层合并` `Token合并` `扩散模型` `姿态估计`

## 📋 核心要点

1. 基于Transformer的HMR模型计算成本高昂，深层架构和冗余token是主要瓶颈。
2. 通过误差约束层合并和掩码引导的Token合并，减少计算量并保留关键信息。
3. 引入扩散解码器，利用时间上下文和姿势先验，弥补合并带来的性能损失。

## 📝 摘要（中文）

本文提出FastHMR，旨在加速基于Transformer的3D人体网格重建(HMR)模型。现有方法虽然性能强大，但由于深层Transformer架构和冗余token，计算成本和复杂度较高。本文引入两种HMR特定的合并策略：误差约束层合并(ECLM)和掩码引导的Token合并(Mask-ToMe)。ECLM选择性地合并对平均关节位置误差(MPJPE)影响最小的Transformer层，而Mask-ToMe侧重于合并对最终预测贡献较小的背景token。为了进一步解决合并可能导致的性能下降，本文提出了一种基于扩散的解码器，该解码器结合了时间上下文，并利用从大规模运动捕捉数据集中学习到的姿势先验。在多个基准测试上的实验表明，该方法在略微提高性能的同时，实现了高达2.3倍的加速。

## 🔬 方法详解

**问题定义**：现有基于Transformer的人体网格重建方法，虽然精度较高，但计算复杂度高，难以满足实时性要求。深层Transformer结构和大量冗余的token是导致计算瓶颈的主要原因。因此，如何在保证精度的前提下，降低计算成本是本文要解决的核心问题。

**核心思路**：本文的核心思路是通过合并Transformer层和token来减少计算量。具体来说，通过误差约束层合并(ECLM)选择性地合并对精度影响小的层，通过掩码引导的Token合并(Mask-ToMe)去除背景token。为了弥补合并操作可能带来的精度损失，引入了基于扩散模型的解码器，利用时间上下文信息和姿势先验知识进行优化。

**技术框架**：FastHMR的整体框架包括三个主要部分：Transformer编码器、层和token合并模块、以及扩散解码器。首先，输入图像经过Transformer编码器提取特征。然后，ECLM和Mask-ToMe模块分别对Transformer层和token进行合并，减少计算量。最后，扩散解码器利用合并后的特征，结合时间上下文和姿势先验，生成最终的人体网格重建结果。

**关键创新**：本文的关键创新在于提出了两种HMR特定的合并策略：ECLM和Mask-ToMe。ECLM能够根据层对MPJPE的影响程度，自适应地合并不重要的层，避免了盲目合并带来的精度损失。Mask-ToMe则利用掩码信息，去除对人体姿态估计贡献较小的背景token，进一步降低计算量。此外，扩散解码器的引入也有效提升了重建精度。

**关键设计**：ECLM的关键在于如何评估每一层的重要性。本文通过计算合并该层后MPJPE的变化来衡量其重要性，并设定一个误差阈值，只有当误差变化小于阈值时才进行合并。Mask-ToMe则利用预训练的分割模型生成掩码，将掩码区域外的token视为背景token并进行合并。扩散解码器采用DDPM结构，以合并后的特征作为条件，逐步生成人体网格。损失函数包括重建损失和姿势先验损失，其中姿势先验损失通过预训练的运动捕捉数据集学习得到。

## 📊 实验亮点

实验结果表明，FastHMR在多个基准测试上实现了显著的加速，最高可达2.3倍，同时略微提升了性能。例如，在Human3.6M数据集上，FastHMR在保持甚至略微提升MPJPE指标的同时，显著降低了计算时间。与基线方法相比，FastHMR在速度和精度之间取得了更好的平衡。

## 🎯 应用场景

FastHMR具有广泛的应用前景，包括虚拟现实、增强现实、游戏、动画制作、运动分析和人机交互等领域。其加速特性使得实时人体姿态估计和网格重建成为可能，为用户提供更流畅、自然的交互体验。未来，该技术有望应用于智能监控、自动驾驶等领域，实现对人体行为的实时分析和理解。

## 📄 摘要（原文）

> Recent transformer-based models for 3D Human Mesh Recovery (HMR) have achieved strong performance but often suffer from high computational cost and complexity due to deep transformer architectures and redundant tokens. In this paper, we introduce two HMR-specific merging strategies: Error-Constrained Layer Merging (ECLM) and Mask-guided Token Merging (Mask-ToMe). ECLM selectively merges transformer layers that have minimal impact on the Mean Per Joint Position Error (MPJPE), while Mask-ToMe focuses on merging background tokens that contribute little to the final prediction. To further address the potential performance drop caused by merging, we propose a diffusion-based decoder that incorporates temporal context and leverages pose priors learned from large-scale motion capture datasets. Experiments across multiple benchmarks demonstrate that our method achieves up to 2.3x speed-up while slightly improving performance over the baseline.

