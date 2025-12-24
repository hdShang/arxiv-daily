---
layout: default
title: "V-HUB: A Visual-Centric Humor Understanding Benchmark for Video LLMs"
---

# V-HUB: A Visual-Centric Humor Understanding Benchmark for Video LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25773" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25773v1</a>
  <a href="https://arxiv.org/pdf/2509.25773.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25773v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25773v1', 'V-HUB: A Visual-Centric Humor Understanding Benchmark for Video LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengpeng Shi, Hengli Li, Yanpeng Zhao, Jianqun Zhou, Yuxuan Wang, Qinrong Cui, Wei Bi, Songchun Zhu, Bo Zhao, Zilong Zheng

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**V-HUB：面向视频大语言模型的视觉中心幽默理解评测基准**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `幽默理解` `多模态学习` `大语言模型` `评测基准` `视觉中心` `人机交互`

## 📋 核心要点

1. 现有MLLM在理解视觉幽默方面存在不足，缺乏专门的评测基准。
2. 构建了v-HUB基准，包含无/少文本的幽默视频，并提供字幕、描述等丰富标注。
3. 实验表明，现有MLLM在仅凭视觉理解幽默方面表现不佳，音频信息有显著帮助。

## 📝 摘要（中文）

为了评估和诊断多模态大语言模型(MLLM)理解幽默的能力，本文提出了一个新的视觉中心视频幽默理解基准v-HUB。v-HUB包含精选的、极少语言的短视频，这些视频来源于经典默片和在线资源，反映了仅通过视觉线索就能理解幽默的真实场景。每个视频片段都配有丰富的注释，包括字幕、描述和解释，支持字幕匹配和幽默解释等评估任务。为了扩大其适用性，进一步构建了一个开放式的视频问答任务，使其易于集成到现有的视频理解基准中。评估了各种MLLM，从专门的Video-LLM到可以处理音频的多功能OmniLLM，涵盖了开源和专有领域。实验结果表明，MLLM在仅通过视觉线索理解幽默方面面临困难。例如，所有模型在从基于文本的评估转向基于视频的评估（没有音频）时，字幕匹配的性能都显著下降。研究结果还表明，加入音频有助于视频幽默理解，突出了声音的信息量以及整合更丰富的模态以进行复杂视频理解任务的前景。

## 🔬 方法详解

**问题定义**：现有方法缺乏对视频中纯视觉幽默理解能力的有效评估。现有的多模态大语言模型在处理视频幽默时，往往依赖于文本信息，而忽略了视觉线索的重要性。因此，需要一个专门的基准来评估模型仅通过视觉信息理解幽默的能力。

**核心思路**：核心思路是构建一个以视觉为中心的视频幽默理解基准，该基准包含大量无/少文本的幽默视频，并提供丰富的标注信息，例如字幕、描述和解释。通过设计不同的评估任务，例如字幕匹配和幽默解释，来评估模型理解视觉幽默的能力。同时，通过对比不同模态（例如，仅视觉、视觉+音频）下的模型表现，来分析不同模态信息对幽默理解的影响。

**技术框架**：v-HUB基准的构建流程主要包括以下几个阶段：1) 数据收集：从经典默片和在线资源中收集幽默视频片段。2) 数据标注：为每个视频片段提供丰富的标注信息，包括字幕、描述和解释。3) 任务构建：构建字幕匹配、幽默解释和开放式视频问答等评估任务。4) 模型评估：使用各种MLLM（包括Video-LLM和OmniLLM）在v-HUB基准上进行评估。

**关键创新**：该论文的关键创新在于构建了一个以视觉为中心的视频幽默理解基准v-HUB。与现有的视频理解基准相比，v-HUB更加关注模型仅通过视觉信息理解幽默的能力。此外，v-HUB还提供了丰富的标注信息，支持多种评估任务，可以更全面地评估模型对幽默的理解能力。

**关键设计**：在数据收集方面，论文侧重于选择那些几乎不包含文本信息的视频片段，以确保模型主要依赖视觉线索来理解幽默。在数据标注方面，论文采用了人工标注的方式，以确保标注信息的准确性和可靠性。在评估任务方面，论文设计了字幕匹配、幽默解释和开放式视频问答等多种任务，以从不同角度评估模型对幽默的理解能力。具体参数设置和网络结构取决于被评估的MLLM。

## 📊 实验亮点

实验结果表明，现有MLLM在仅通过视觉线索理解幽默方面表现不佳，在视频字幕匹配任务中，相比于文本输入，视频输入的性能显著下降。同时，加入音频信息可以显著提升模型对视频幽默的理解能力，这表明声音在视频幽默理解中扮演着重要的角色。

## 🎯 应用场景

该研究成果可应用于提升人机交互的趣味性和自然性，例如在智能客服、虚拟助手等领域，使AI能够更好地理解人类的情感和意图，从而提供更个性化和更具吸引力的服务。此外，该基准也可促进多模态大语言模型在视频理解方面的研究进展。

## 📄 摘要（原文）

> AI models capable of comprehending humor hold real-world promise -- for example, enhancing engagement in human-machine interactions. To gauge and diagnose the capacity of multimodal large language models (MLLMs) for humor understanding, we introduce v-HUB, a novel visual-centric video humor understanding benchmark. v-HUB comprises a curated collection of minimally verbal short videos, sourced from classic silent films and online resources, and reflecting real-world scenarios where humor can be appreciated purely through visual cues. Each video clip is paired with rich annotations, including captions, descriptions, and explanations, supporting evaluation tasks like caption matching and humor explanation. To broaden its applicability, we further construct an open-ended video QA task, making it readily integrable into existing video understanding benchmarks. We evaluate a diverse set of MLLMs, from specialized Video-LLMs to versatile OmniLLMs that can process audio, covering both open-source and proprietary domains. The experimental results expose the difficulties MLLMs face in comprehending humor from visual cues alone. For example, all models exhibit a marked performance drop on caption matching when moving from text-based to video-based evaluation (without audio). Our findings also demonstrate that incorporating audio helps with video humor understanding, highlighting the informativeness of sound and the promise of integrating richer modalities for complex video understanding tasks.

