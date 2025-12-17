---
layout: default
title: Multi-speaker Attention Alignment for Multimodal Social Interaction
---

# Multi-speaker Attention Alignment for Multimodal Social Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.17952" class="toolbar-btn" target="_blank">📄 arXiv: 2511.17952v1</a>
  <a href="https://arxiv.org/pdf/2511.17952.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.17952v1" onclick="toggleFavorite(this, '2511.17952v1', 'Multi-speaker Attention Alignment for Multimodal Social Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liangyang Ouyang, Yifei Huang, Mingfang Zhang, Caixin Kang, Ryosuke Furuta, Yoichi Sato

**分类**: cs.CV

**发布日期**: 2025-11-22

**🔗 代码/项目**: [GITHUB](https://github.com/ut-vision/SocialInteraction)

---

## 💡 一句话要点

**提出多说话人注意力对齐方法，提升MLLM在多模态社交互动中的理解能力**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `多模态学习` `社交互动理解` `注意力机制` `多说话人场景` `跨模态对齐`

## 📋 核心要点

1. 现有MLLM在多说话人场景中，视觉和文本token缺乏说话人一致的对齐，导致跨模态注意力较弱，影响社交互动理解。
2. 提出一种多模态多说话人注意力对齐方法，通过动态跨模态头选择和自适应社交感知注意力偏差来增强说话人视觉和文本的对齐。
3. 在TVQA+、MMSI、OnlineMMSI等基准测试中，该方法显著提升了MLLM在社交任务中的性能，达到SOTA水平。

## 📝 摘要（中文）

理解视频中的社交互动需要推理口头和非口头线索的动态交互：谁在说话，对谁说，以及伴随的眼神或手势。虽然多模态大型语言模型（MLLM）是理想选择，但简单地添加视觉输入在社交任务上的收益却出人意料地不稳定。我们对最先进的MLLM内部的跨模态注意力进行定量分析，揭示了一个核心失效模式：在多说话人场景中，视觉和文本token缺乏说话人一致的对齐，表现出比以对象为中心的图像弱得多的跨模态注意力。为了解决这个问题，我们提出了一种多模态多说话人注意力对齐方法，可以集成到现有的MLLM中。首先，我们引入动态跨模态头选择来识别最负责接地的注意力头。然后，将从现有注意力模式和说话人位置计算出的自适应社交感知注意力偏差注入到注意力机制中。这种偏差增强了说话人的视觉表示和他们的言语之间的对齐，而无需引入可训练的参数或架构更改。我们将我们的方法集成到三个不同的MLLM（LLaVA-NeXT-Video、Qwen2.5-VL 和 InternVL3）中，并在三个基准（TVQA+、MMSI、OnlineMMSI）上进行评估。在四个社交任务中，结果表明我们的方法提高了MLLM的能力，并实现了最先进的结果。注意力可视化证实了我们的方法成功地将模型集中在与说话人相关的区域，从而实现了更强大的多方社交推理。我们的实现和模型将在https://github.com/ut-vision/SocialInteraction上提供。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLM）在理解多说话人社交互动场景时，由于视觉和文本信息缺乏说话人一致的对齐而导致的性能瓶颈。现有方法简单地将视觉信息加入MLLM，无法有效捕捉说话人之间的关系，导致模型在社交推理任务中表现不佳。

**核心思路**：论文的核心思路是通过增强MLLM中视觉和文本token之间的说话人一致性对齐来提升模型性能。具体而言，通过动态选择负责跨模态接地的注意力头，并引入自适应的社交感知注意力偏差，从而引导模型关注与说话人相关的视觉区域，并将其与对应的文本信息对齐。

**技术框架**：该方法主要包含两个关键模块：动态跨模态头选择和自适应社交感知注意力偏差。首先，动态跨模态头选择模块用于识别对跨模态信息融合贡献最大的注意力头。然后，自适应社交感知注意力偏差模块利用说话人的位置信息和现有的注意力模式，计算出一个注意力偏差，并将其注入到注意力机制中，从而增强说话人视觉表示和文本信息之间的对齐。整个框架可以无缝集成到现有的MLLM中，无需修改模型架构或引入额外的可训练参数。

**关键创新**：该方法最重要的创新点在于提出了一个无需训练参数的注意力对齐机制，能够有效地增强多说话人场景下视觉和文本信息的对齐。与现有方法相比，该方法更加轻量级，易于集成到不同的MLLM中，并且能够显著提升模型在社交推理任务中的性能。

**关键设计**：动态跨模态头选择模块通过计算每个注意力头对跨模态信息融合的贡献度来选择合适的注意力头。自适应社交感知注意力偏差模块利用说话人的位置信息和现有的注意力模式，计算出一个注意力偏差，该偏差能够引导模型关注与说话人相关的视觉区域，并将其与对应的文本信息对齐。注意力偏差的具体计算方式可能涉及到距离衰减、注意力权重归一化等技术细节。

## 📊 实验亮点

该方法在TVQA+、MMSI和OnlineMMSI三个基准测试中取得了显著的性能提升。例如，在TVQA+数据集上，该方法相较于基线模型取得了X%的性能提升（具体数据请参考原论文）。注意力可视化结果表明，该方法能够有效地引导模型关注与说话人相关的视觉区域，从而提升模型在社交推理任务中的性能。

## 🎯 应用场景

该研究成果可应用于智能监控、人机交互、社交媒体分析等领域。例如，在智能监控中，可以利用该方法理解监控视频中人群的互动行为，从而实现更智能的安全预警。在人机交互中，可以帮助机器人更好地理解人类的社交意图，从而实现更自然的人机交互。在社交媒体分析中，可以用于分析社交媒体视频中用户的互动行为，从而挖掘更有价值的信息。

## 📄 摘要（原文）

> Understanding social interaction in video requires reasoning over a dynamic interplay of verbal and non-verbal cues: who is speaking, to whom, and with what gaze or gestures. While Multimodal Large Language Models (MLLMs) are natural candidates, simply adding visual inputs yields surprisingly inconsistent gains on social tasks. Our quantitative analysis of cross-modal attention inside state-of-the-art MLLMs reveals a core failure mode: in multi-speaker scenes, visual and textual tokens lack speaker-consistent alignment, exhibiting substantially weaker cross-modal attention than in object-centric images. To address this, we propose a multimodal multi-speaker attention alignment method that can be integrated into existing MLLMs. First, we introduce dynamic cross-modal head selection to identify attention heads most responsible for grounding. Then, an adaptive social-aware attention bias, computed from existing attention patterns and speaker locations, is injected into the attention mechanism. This bias reinforces alignment between a speaker's visual representation and their utterances without introducing trainable parameters or architectural changes. We integrate our method into three distinct MLLMs (LLaVA-NeXT-Video, Qwen2.5-VL, and InternVL3) and evaluate on three benchmarks (TVQA+, MMSI, OnlineMMSI). Across four social tasks, results demonstrate that our approach improves the ability of MLLMs and achieves state-of-the-art results. Attention visualizations confirm our method successfully focuses the model on speaker-relevant regions, enabling more robust multi-party social reasoning. Our implementation and model will be available at https://github.com/ut-vision/SocialInteraction.

