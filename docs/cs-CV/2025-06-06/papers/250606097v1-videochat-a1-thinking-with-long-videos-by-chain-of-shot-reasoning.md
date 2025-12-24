---
layout: default
title: "VideoChat-A1: Thinking with Long Videos by Chain-of-Shot Reasoning"
---

# VideoChat-A1: Thinking with Long Videos by Chain-of-Shot Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06097" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06097v1</a>
  <a href="https://arxiv.org/pdf/2506.06097.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06097v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06097v1', 'VideoChat-A1: Thinking with Long Videos by Chain-of-Shot Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zikang Wang, Boyu Chen, Zhengrong Yue, Yi Wang, Yu Qiao, Limin Wang, Yali Wang

**分类**: cs.CV

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出VideoChat-A1以解决长视频理解问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `链式推理` `多模态大语言模型` `视频问答` `智能交互`

## 📋 核心要点

1. 现有多模态大语言模型在长视频理解上存在显著不足，难以有效处理长时间上下文。
2. 本文提出VideoChat-A1，通过链式镜头推理逐步分析长视频，模拟人类思维过程。
3. 实验结果显示，VideoChat-A1在长视频问答基准上表现优异，超越了多个强基线模型。

## 📝 摘要（中文）

近年来，视频理解的进展主要得益于多模态大语言模型（MLLMs）。然而，这些模型在分析短视频时表现良好，但在理解长视频时却面临困难。为了解决这一问题，本文提出了VideoChat-A1，一个新颖的长视频代理范式。与现有方法不同，VideoChat-A1通过链式镜头推理，逐步选择与用户问题相关的镜头，并进行粗到细的分析。通过沿着镜头链进行多模态推理，VideoChat-A1能够有效模拟人类的思维过程，交互式地发现适合的时间上下文。实验结果表明，VideoChat-A1在主流长视频问答基准上达到了最先进的性能，显著超越了强基线。

## 🔬 方法详解

**问题定义**：本文旨在解决长视频理解中的关键问题，即现有方法无法有效识别和利用长视频中的相关镜头，导致理解能力受限。

**核心思路**：VideoChat-A1的核心思路是通过链式镜头推理，逐步选择与用户问题相关的镜头，并进行深入分析，以模拟人类的思维过程。

**技术框架**：该方法的整体架构包括镜头选择模块、粗到细分析模块和多模态推理模块。首先，系统根据用户问题选择相关镜头，然后对这些镜头进行细致的分析，最后进行多模态推理以整合信息。

**关键创新**：VideoChat-A1的主要创新在于其链式镜头推理机制，这一机制使得模型能够逐步理解长视频的复杂结构，而不是简单地处理冗余或噪声信息。

**关键设计**：在设计上，VideoChat-A1采用了特定的损失函数以优化镜头选择的准确性，并在网络结构中引入了多模态融合技术，以提高推理的有效性和准确性。

## 📊 实验亮点

实验结果表明，VideoChat-A1在VideoMME和EgoSchema等主流长视频问答基准上分别达到了77.0和70.1的分数，超越了强基线模型（如Intern2.5VL-8B和InternVideo2.5-8B）达10.8%和6.2%。与领先的闭源模型GPT-4o和Gemini 1.5 Pro相比，VideoChat-A1在输入帧和推理时间上分别减少了7%和12%。

## 🎯 应用场景

该研究的潜在应用领域包括视频问答系统、智能监控、教育视频分析等。通过提升长视频理解能力，VideoChat-A1可以为用户提供更精准的信息检索和交互体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The recent advance in video understanding has been driven by multimodal large language models (MLLMs). But these MLLMs are good at analyzing short videos, while suffering from difficulties in understanding videos with a longer context. To address this difficulty, several agent paradigms have recently been proposed, using MLLMs as agents for retrieving extra contextual knowledge in a long video. However, most existing agents ignore the key fact that a long video is composed with multiple shots, i.e., to answer the user question from a long video, it is critical to deeply understand its relevant shots like human. Without such insight, these agents often mistakenly find redundant even noisy temporal context, restricting their capacity for long video understanding. To fill this gap, we propose VideoChat-A1, a novel long video agent paradigm. Different from the previous works, our VideoChat-A1 can deeply think with long videos, via a distinct chain-of-shot reasoning paradigm. More specifically, it can progressively select the relevant shots of user question, and look into these shots in a coarse-to-fine partition. By multi-modal reasoning along the shot chain, VideoChat-A1 can effectively mimic step-by-step human thinking process, allowing to interactively discover preferable temporal context for thoughtful understanding in long videos. Extensive experiments show that, our VideoChat-A1 achieves the state-of-the-art performance on the mainstream long video QA benchmarks, e.g., it achieves 77.0 on VideoMME and 70.1 on EgoSchema, outperforming its strong baselines (e.g., Intern2.5VL-8B and InternVideo2.5-8B), by up to 10.8\% and 6.2\%. Compared to leading close-source GPT-4o and Gemini 1.5 Pro, VideoChat-A1 offers competitive accuracy, but with 7\% input frames and 12\% inference time on average.

