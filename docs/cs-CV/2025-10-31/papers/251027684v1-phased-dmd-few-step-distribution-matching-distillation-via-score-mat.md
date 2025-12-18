---
layout: default
title: Phased DMD: Few-step Distribution Matching Distillation via Score Matching within Subintervals
---

# Phased DMD: Few-step Distribution Matching Distillation via Score Matching within Subintervals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27684" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27684v1</a>
  <a href="https://arxiv.org/pdf/2510.27684.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27684v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.27684v1', 'Phased DMD: Few-step Distribution Matching Distillation via Score Matching within Subintervals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiangyu Fan, Zesong Qiu, Zhuguanyu Wu, Fanzhou Wang, Zhiqian Lin, Tianxiang Ren, Dahua Lin, Ruihao Gong, Lei Yang

**分类**: cs.CV

**发布日期**: 2025-10-31

---

## 💡 一句话要点

**提出Phased DMD，通过子区间内的分数匹配蒸馏提升多步生成模型的性能和多样性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `蒸馏训练` `生成模型` `多步生成` `分布匹配` `分数匹配` `混合专家模型` `图像生成` `视频生成`

## 📋 核心要点

1. 现有DMD方法在复杂生成任务中，单步蒸馏模型受限于模型容量，多步蒸馏则面临内存和计算压力，且多样性降低。
2. Phased DMD通过将SNR范围划分为子区间，并进行渐进式分布匹配，结合混合专家模型，降低学习难度并提升模型容量。
3. 实验表明，Phased DMD在图像和视频生成任务中，相比DMD，能更好地保留输出多样性，同时保持关键的生成能力。

## 📝 摘要（中文）

分布匹配蒸馏(DMD)将基于分数的生成模型提炼为高效的单步生成器，无需与教师模型的采样轨迹一一对应。然而，有限的模型容量导致单步蒸馏模型在复杂的生成任务上表现不佳，例如在文本到视频生成中合成复杂的对象运动。直接将DMD扩展到多步蒸馏会增加内存使用和计算深度，导致不稳定和效率降低。虽然之前的工作提出了随机梯度截断作为一种潜在的解决方案，但我们观察到它大大降低了多步蒸馏模型的生成多样性，使其降至单步模型的水平。为了解决这些限制，我们提出了Phased DMD，这是一个多步蒸馏框架，它将阶段性蒸馏的思想与混合专家(MoE)相结合，降低了学习难度，同时增强了模型容量。Phased DMD建立在两个关键思想之上：渐进式分布匹配和子区间内的分数匹配。首先，我们的模型将信噪比(SNR)范围划分为子区间，逐步细化模型到更高的SNR水平，以更好地捕获复杂的分布。接下来，为了确保每个子区间内的训练目标是准确的，我们进行了严格的数学推导。我们通过蒸馏最先进的图像和视频生成模型(包括Qwen-Image(20B参数)和Wan2.2(28B参数))来验证Phased DMD。实验结果表明，Phased DMD比DMD更好地保留了输出多样性，同时保留了关键的生成能力。我们将发布我们的代码和模型。

## 🔬 方法详解

**问题定义**：论文旨在解决分布匹配蒸馏（DMD）在复杂生成任务中，将大型生成模型蒸馏为高效多步生成器时遇到的问题。现有DMD方法在模型容量有限的情况下，单步蒸馏效果不佳；直接扩展到多步蒸馏则面临内存占用高、计算量大以及生成多样性降低等问题。

**核心思路**：论文的核心思路是将蒸馏过程分解为多个阶段（Phases），每个阶段专注于信噪比（SNR）的一个子区间。通过渐进式地匹配目标分布，并结合混合专家（MoE）模型来提升模型容量，从而在保证生成质量的同时，提高生成的多样性。

**技术框架**：Phased DMD框架主要包含以下几个阶段：1. 将SNR范围划分为多个子区间。2. 在每个子区间内，进行分数匹配，优化模型在该SNR范围内的生成能力。3. 采用渐进式分布匹配策略，逐步提升模型在更高SNR水平上的性能。4. 使用混合专家模型，增加模型容量，以适应复杂的数据分布。

**关键创新**：Phased DMD的关键创新在于将多步蒸馏过程分解为多个阶段，并在每个阶段专注于特定的SNR子区间。这种分阶段的训练方式降低了学习难度，使得模型能够更好地捕捉复杂的数据分布。此外，结合混合专家模型进一步提升了模型容量，从而在保证生成质量的同时，提高了生成的多样性。与现有方法相比，Phased DMD避免了直接进行全局多步蒸馏带来的不稳定性和多样性损失。

**关键设计**：论文的关键设计包括：1. SNR子区间的划分策略，需要平衡每个子区间的学习难度和模型性能。2. 混合专家模型的结构设计，包括专家数量、专家网络的结构等。3. 损失函数的设计，确保每个子区间内的分数匹配能够准确地优化模型。4. 渐进式分布匹配的策略，如何平滑地过渡到下一个SNR子区间。

## 📊 实验亮点

实验结果表明，Phased DMD在蒸馏Qwen-Image (20B参数)和Wan2.2 (28B参数)等大型模型时，能够显著提升生成模型的多样性，同时保持关键的生成能力。相比于直接使用DMD进行多步蒸馏，Phased DMD能够更好地保留原始模型的生成质量和多样性。

## 🎯 应用场景

Phased DMD具有广泛的应用前景，可用于图像生成、视频生成、文本到图像/视频生成等领域。该方法能够将大型生成模型蒸馏为高效的多步生成器，降低计算成本，并提升生成内容的多样性，从而推动相关应用的发展，例如高质量内容创作、数据增强、以及虚拟现实等。

## 📄 摘要（原文）

> Distribution Matching Distillation (DMD) distills score-based generative models into efficient one-step generators, without requiring a one-to-one correspondence with the sampling trajectories of their teachers. However, limited model capacity causes one-step distilled models underperform on complex generative tasks, e.g., synthesizing intricate object motions in text-to-video generation. Directly extending DMD to multi-step distillation increases memory usage and computational depth, leading to instability and reduced efficiency. While prior works propose stochastic gradient truncation as a potential solution, we observe that it substantially reduces the generation diversity of multi-step distilled models, bringing it down to the level of their one-step counterparts. To address these limitations, we propose Phased DMD, a multi-step distillation framework that bridges the idea of phase-wise distillation with Mixture-of-Experts (MoE), reducing learning difficulty while enhancing model capacity. Phased DMD is built upon two key ideas: progressive distribution matching and score matching within subintervals. First, our model divides the SNR range into subintervals, progressively refining the model to higher SNR levels, to better capture complex distributions. Next, to ensure the training objective within each subinterval is accurate, we have conducted rigorous mathematical derivations. We validate Phased DMD by distilling state-of-the-art image and video generation models, including Qwen-Image (20B parameters) and Wan2.2 (28B parameters). Experimental results demonstrate that Phased DMD preserves output diversity better than DMD while retaining key generative capabilities. We will release our code and models.

