---
layout: default
title: "Less is More: Token-Efficient Video-QA via Adaptive Frame-Pruning and Semantic Graph Integration"
---

# Less is More: Token-Efficient Video-QA via Adaptive Frame-Pruning and Semantic Graph Integration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03337" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03337v7</a>
  <a href="https://arxiv.org/pdf/2508.03337.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03337v7" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03337v7', 'Less is More: Token-Efficient Video-QA via Adaptive Frame-Pruning and Semantic Graph Integration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaoguang Wang, Weiyu Guo, Ziyang Chen, Yijie Xu, Xuming Hu, Hui Xiong

**分类**: cs.CV

**发布日期**: 2025-08-05 (更新: 2025-11-23)

**备注**: This manuscript is a preprint. 22 pages, 19 figures

---

## 💡 一句话要点

**提出自适应帧剪枝与语义图集成以解决视频问答中的冗余问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频问答` `自适应帧剪枝` `语义图` `多模态学习` `高效处理` `视觉回声` `上下文完整性`

## 📋 核心要点

1. 现有的视频问答方法在处理大量视频帧时面临高令牌成本和时间冗余的问题，导致性能下降。
2. 本文提出的自适应帧剪枝（AFP）方法通过智能聚类帧来剪除视觉回声，并结合语义图进行低成本补偿。
3. 在多个基准测试中，本文的方法减少了高达80%的输入令牌，同时提升了选择器的准确性，表现优于使用更多帧的基线方法。

## 📝 摘要（中文）

多模态大型语言模型在视频问答中的实际应用受到处理大量视频帧的高令牌成本的严重制约。尽管关键帧选择是缓解这一问题的主要策略，但现有的选择器仍产生显著的时间冗余，导致上下文稀释，反而降低性能。为此，本文提出了一种新颖的精炼框架，结合自适应帧剪枝和轻量级文本语义图，智能剪除视觉回声，同时通过语义图提供低成本的语义补偿。实验结果表明，该方法在LongVideoBench和VideoMME基准上显著减少了输入令牌数量，提升了选择器的准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决视频问答中由于高令牌成本和时间冗余（视觉回声）导致的性能下降问题。现有的关键帧选择方法无法有效消除这些冗余，影响了上下文的完整性。

**核心思路**：提出自适应帧剪枝（AFP）与轻量级语义图的结合，通过智能聚类帧来减少冗余信息，同时利用语义图提供必要的语义补偿，从而提高效率和准确性。

**技术框架**：整体框架包括两个主要模块：自适应帧剪枝模块负责动态选择关键帧，语义图模块则提供语义信息的补充。两者协同工作，形成一个高效的视频问答系统。

**关键创新**：最重要的创新在于提出了视觉回声的概念，并通过自适应帧剪枝有效地解决了这一问题，显著提升了视频问答的性能。与传统方法相比，本文的方法在减少输入令牌的同时保持了信息的完整性。

**关键设计**：在设计中，采用了动态聚类算法进行帧选择，语义图则通过低成本的文本表示来补充信息。具体的参数设置和损失函数设计旨在优化剪枝效果与语义补偿的平衡。

## 📊 实验亮点

实验结果显示，本文的方法在LongVideoBench和VideoMME基准上实现了高达80%的输入令牌减少，同时提升了选择器的准确性，表现出色，超越了使用更多帧的基线方法，证明了其有效性和竞争力。

## 🎯 应用场景

该研究在视频问答、视频内容理解和多模态学习等领域具有广泛的应用潜力。通过提高视频处理的效率和准确性，该方法可以为教育、娱乐和安全监控等行业提供更智能的解决方案，推动相关技术的发展与应用。

## 📄 摘要（原文）

> The practical application of Multimodal Large Language Models (MLLMs) to Video Question Answering (Video-QA) is severely hindered by the high token cost of processing numerous video frames. While keyframe selection is the dominant strategy to mitigate this, we identify that even state-of-the-art selectors produce prompts laden with significant temporal redundancy, a challenge unique to video that we term 'visual echoes'. This issue leads to context dilution and can paradoxically degrade performance. To address this dual challenge, we propose a novel refinement framework that synergistically combines Adaptive Frame-Pruning (AFP) with a lightweight text-based semantic graph. AFP intelligently prunes 'visual echoes' by adaptively clustering frames, while the semantic graph provides crucial, low-cost semantic compensation. Conducting extensive experiments on the LongVideoBench and VideoMME benchmarks against multiple state-of-the-art selectors, our approach demonstrates a drastic reduction in total input tokens by up to 80%. Crucially, by creating a concise, high-quality prompt, our framework not only enhances efficiency but also demonstrates a remarkable ability to robustify and improve the accuracy of upstream selectors, achieving results that are highly competitive with, and often superior to, baselines that use vastly more frames.

