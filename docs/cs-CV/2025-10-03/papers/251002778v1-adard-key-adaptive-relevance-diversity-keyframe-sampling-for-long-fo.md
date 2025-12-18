---
layout: default
title: AdaRD-key: Adaptive Relevance-Diversity Keyframe Sampling for Long-form Video understanding
---

# AdaRD-key: Adaptive Relevance-Diversity Keyframe Sampling for Long-form Video understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02778" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02778v1</a>
  <a href="https://arxiv.org/pdf/2510.02778.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02778v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02778v1', 'AdaRD-key: Adaptive Relevance-Diversity Keyframe Sampling for Long-form Video understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xian Zhang, Zexi Wu, Zinuo Li, Hongming Xu, Luqi Gong, Farid Boussaid, Naoufel Werghi, Mohammed Bennamoun

**分类**: cs.CV

**发布日期**: 2025-10-03

**🔗 代码/项目**: [GITHUB](https://github.com/Xian867/AdaRD-Key)

---

## 💡 一句话要点

**提出AdaRD-Key，用于查询驱动的长视频关键帧自适应采样，提升视频理解性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `关键帧采样` `视觉-语言模型` `查询驱动` `相关性-多样性` `自适应采样` `多模态学习`

## 📋 核心要点

1. 现有方法如均匀采样和固定间隔采样，难以捕捉长视频中的关键信息，导致视频理解效果不佳。
2. AdaRD-Key通过最大化相关性-多样性最大体积(RD-MV)目标，自适应地选择既相关又具有代表性的关键帧。
3. 实验表明，AdaRD-Key在LongVideoBench和Video-MME等数据集上取得了SOTA性能，尤其在长视频上提升显著。

## 📝 摘要（中文）

由于长视频的时间跨度和信息密度大，视觉-语言模型(VLMs)理解长视频仍然是一个巨大的挑战。目前大多数多模态大型语言模型(MLLMs)依赖于均匀采样，这通常会忽略关键时刻，导致对查询的错误响应。许多关键帧选择方法采用严格的时间间隔，一旦选择了一个帧，排除窗口会抑制相邻的时间戳以减少冗余。这种策略虽然能有效限制重叠，但经常会错过重要事件附近的短而精细的线索。其他方法强调视觉多样性，但忽略了查询相关性。我们提出了AdaRD-Key，一个用于查询驱动的长视频理解的免训练关键帧采样模块。AdaRD-Key最大化统一的相关性-多样性最大体积(RD-MV)目标，将查询条件下的相关性得分与对数行列式多样性分量相结合，以产生信息丰富且非冗余的帧。为了处理与视频弱对齐的广泛查询，AdaRD-Key采用了一种轻量级的相关性感知门控机制；当相关性分布表明弱对齐时，该方法无缝地切换到仅多样性模式，从而在无需额外监督的情况下增强覆盖范围。我们的流程是免训练的，计算效率高（在单个GPU上实时运行），并且可以即插即用地与现有VLM兼容。在LongVideoBench和Video-MME上的大量实验表明了最先进的性能，尤其是在长视频上。

## 🔬 方法详解

**问题定义**：现有长视频理解方法，特别是基于多模态大语言模型的方法，依赖于均匀采样或固定间隔采样，无法有效提取长视频中的关键信息。均匀采样容易忽略重要时刻，而固定间隔采样可能错过关键事件附近的细微线索。此外，一些方法只关注视觉多样性，忽略了与用户查询的相关性，导致回答质量下降。

**核心思路**：AdaRD-Key的核心思路是同时考虑关键帧与用户查询的相关性和关键帧之间的多样性，通过最大化一个统一的“相关性-多样性最大体积”（RD-MV）目标来实现。这种方法旨在选择既能反映视频内容，又能响应用户查询，同时避免冗余的关键帧集合。

**技术框架**：AdaRD-Key是一个即插即用的模块，可以与现有的视觉-语言模型(VLMs)结合使用。其主要流程包括：1) 提取视频帧的视觉特征；2) 计算每个帧与用户查询的相关性得分；3) 使用对数行列式计算帧之间的多样性；4) 通过最大化RD-MV目标函数选择关键帧。当检测到查询与视频弱相关时，会启动一个相关性感知门控机制，切换到仅多样性模式，以确保视频内容的全面覆盖。

**关键创新**：AdaRD-Key的关键创新在于其统一的相关性-多样性最大体积(RD-MV)目标函数。该函数将查询相关性和帧间多样性结合起来，使得选择的关键帧既能响应用户查询，又能避免信息冗余。此外，相关性感知门控机制能够在查询与视频弱相关时，自动调整采样策略，增强视频内容的覆盖。

**关键设计**：RD-MV目标函数由两部分组成：查询条件下的相关性得分和对数行列式多样性分量。相关性得分可以使用预训练的视觉-语言模型计算，例如CLIP。多样性分量通过计算帧特征矩阵的行列式来衡量，行列式越大，表示帧之间的差异越大。相关性感知门控机制使用一个轻量级的神经网络来预测查询与视频的相关性，并根据相关性得分动态调整RD-MV目标函数中相关性和多样性的权重。

## 📊 实验亮点

AdaRD-Key在LongVideoBench和Video-MME数据集上取得了显著的性能提升，尤其是在长视频上。实验结果表明，AdaRD-Key能够有效地选择与查询相关且具有代表性的关键帧，从而提高视频理解的准确性。例如，在LongVideoBench数据集上，AdaRD-Key的性能超过了现有SOTA方法。

## 🎯 应用场景

AdaRD-Key可广泛应用于各种需要理解长视频的场景，例如视频问答、视频摘要、视频检索和智能监控。通过提取更具信息量的关键帧，可以提高视频理解的准确性和效率，从而改善用户体验并降低计算成本。该方法尤其适用于处理包含大量信息和复杂事件的长视频。

## 📄 摘要（原文）

> Understanding long-form videos remains a significant challenge for vision--language models (VLMs) due to their extensive temporal length and high information density. Most current multimodal large language models (MLLMs) rely on uniform sampling, which often overlooks critical moments, leading to incorrect responses to queries. In parallel, many keyframe selection approaches impose rigid temporal spacing: once a frame is chosen, an exclusion window suppresses adjacent timestamps to reduce redundancy. While effective at limiting overlap, this strategy frequently misses short, fine-grained cues near important events. Other methods instead emphasize visual diversity but neglect query relevance. We propose AdaRD-Key, a training-free keyframe sampling module for query-driven long-form video understanding. AdaRD-Key maximizes a unified Relevance--Diversity Max-Volume (RD-MV) objective, combining a query-conditioned relevance score with a log-determinant diversity component to yield informative yet non-redundant frames. To handle broad queries with weak alignment to the video, AdaRD-Key employs a lightweight relevance-aware gating mechanism; when the relevance distribution indicates weak alignment, the method seamlessly shifts into a diversity-only mode, enhancing coverage without additional supervision. Our pipeline is training-free, computationally efficient (running in real time on a single GPU), and compatible with existing VLMs in a plug-and-play manner. Extensive experiments on LongVideoBench and Video-MME demonstrate state-of-the-art performance, particularly on long-form videos. Code available at https://github.com/Xian867/AdaRD-Key.

