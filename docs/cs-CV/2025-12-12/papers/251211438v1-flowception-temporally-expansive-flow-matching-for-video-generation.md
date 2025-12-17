---
layout: default
title: Flowception: Temporally Expansive Flow Matching for Video Generation
---

# Flowception: Temporally Expansive Flow Matching for Video Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.11438" class="toolbar-btn" target="_blank">📄 arXiv: 2512.11438v1</a>
  <a href="https://arxiv.org/pdf/2512.11438.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11438v1" onclick="toggleFavorite(this, '2512.11438v1', 'Flowception: Temporally Expansive Flow Matching for Video Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tariq Berrada Ifriqi, John Nguyen, Karteek Alahari, Jakob Verbeek, Ricky T. Q. Chen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-12

---

## 💡 一句话要点

**Flowception：时序扩展的Flow Matching用于可变长度视频生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频生成` `Flow Matching` `非自回归` `可变长度视频` `帧插入` `帧去噪` `长期上下文` `局部注意力`

## 📋 核心要点

1. 现有自回归视频生成方法存在误差累积和漂移问题，难以处理长期上下文。
2. Flowception通过交替进行离散帧插入和连续帧去噪，学习概率路径，有效压缩长期上下文。
3. 实验表明，Flowception在FVD和VBench指标上优于自回归和全序列基线，并可用于图像到视频生成和视频插值。

## 📝 摘要（中文）

Flowception是一种新颖的非自回归、可变长度的视频生成框架。它学习一种概率路径，该路径交替进行离散帧插入和连续帧去噪。与自回归方法相比，Flowception减轻了误差累积/漂移，因为采样期间的帧插入机制充当有效的压缩机制来处理长期上下文。与全序列流相比，我们的方法将训练的FLOPs减少了三倍，同时更适合局部注意力变体，并允许联合学习视频的长度及其内容。定量实验结果表明，与自回归和全序列基线相比，FVD和VBench指标有所提高，并通过定性结果进一步验证。最后，通过学习在序列中插入和去噪帧，Flowception无缝集成了不同的任务，例如图像到视频生成和视频插值。

## 🔬 方法详解

**问题定义**：视频生成任务旨在根据给定的条件（例如文本描述或初始图像）生成一段连贯的视频序列。现有的自回归方法在生成长视频时容易出现误差累积，导致视频质量下降。全序列流方法虽然可以并行生成所有帧，但计算复杂度高，难以处理长视频。

**核心思路**：Flowception的核心思路是结合离散帧插入和连续帧去噪，构建一个概率路径。通过帧插入，可以有效地压缩视频的长期上下文，减少误差累积。通过帧去噪，可以逐步提高视频的质量。这种交替进行的方式，既能保证视频的连贯性，又能降低计算复杂度。

**技术框架**：Flowception的整体框架包括两个主要模块：帧插入模块和帧去噪模块。帧插入模块负责在已有的视频帧之间插入新的帧，从而增加视频的长度。帧去噪模块负责对视频帧进行去噪，提高视频的质量。这两个模块交替执行，直到生成所需的视频长度。Flowception使用Flow Matching技术来学习帧插入和帧去噪的概率路径。

**关键创新**：Flowception的关键创新在于其时序扩展的Flow Matching方法。传统的Flow Matching方法通常用于图像生成，而Flowception将其扩展到视频生成领域，并引入了帧插入机制。这种机制使得Flowception能够有效地处理长视频的长期上下文，并降低计算复杂度。此外，Flowception还能够联合学习视频的长度和内容，从而实现可变长度的视频生成。

**关键设计**：Flowception使用Transformer网络作为帧插入和帧去噪模块的基本构建块。为了降低计算复杂度，Flowception采用了局部注意力机制。损失函数包括Flow Matching损失和对抗损失。Flow Matching损失用于训练帧插入和帧去噪的概率路径，对抗损失用于提高视频的真实感。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果表明，Flowception在FVD和VBench指标上均优于现有的自回归和全序列基线方法。具体而言，Flowception在FVD指标上取得了显著的提升，表明其生成的视频具有更高的质量和真实感。此外，Flowception还能够生成可变长度的视频，并能够处理长视频的长期上下文。与全序列流方法相比，Flowception将训练的FLOPs减少了三倍。

## 🎯 应用场景

Flowception具有广泛的应用前景，包括视频编辑、视频游戏、虚拟现实、电影制作等领域。它可以用于生成各种类型的视频，例如动画、特效、广告等。此外，Flowception还可以用于视频修复、视频插值等任务，提高视频的质量和流畅度。未来，Flowception有望成为视频生成领域的重要技术。

## 📄 摘要（原文）

> We present Flowception, a novel non-autoregressive and variable-length video generation framework. Flowception learns a probability path that interleaves discrete frame insertions with continuous frame denoising. Compared to autoregressive methods, Flowception alleviates error accumulation/drift as the frame insertion mechanism during sampling serves as an efficient compression mechanism to handle long-term context. Compared to full-sequence flows, our method reduces FLOPs for training three-fold, while also being more amenable to local attention variants, and allowing to learn the length of videos jointly with their content. Quantitative experimental results show improved FVD and VBench metrics over autoregressive and full-sequence baselines, which is further validated with qualitative results. Finally, by learning to insert and denoise frames in a sequence, Flowception seamlessly integrates different tasks such as image-to-video generation and video interpolation.

