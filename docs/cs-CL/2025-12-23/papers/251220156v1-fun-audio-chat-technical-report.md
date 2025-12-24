---
layout: default
title: Fun-Audio-Chat Technical Report
---

# Fun-Audio-Chat Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20156" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20156v1</a>
  <a href="https://arxiv.org/pdf/2512.20156.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20156v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20156v1', 'Fun-Audio-Chat Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qian Chen, Luyao Cheng, Chong Deng, Xiangang Li, Jiaqing Liu, Chao-Hong Tan, Wen Wang, Junhao Xu, Jieping Ye, Qinglin Zhang, Qiquan Zhang, Jingren Zhou

**分类**: cs.CL, cs.AI, cs.SD, eess.AS

**发布日期**: 2025-12-23

**备注**: 21 pages, https://github.com/FunAudioLLM/Fun-Audio-Chat

---

## 💡 一句话要点

**Fun-Audio-Chat：通过双分辨率语音表示和核心鸡尾酒训练，提升语音交互大模型性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音交互` `大型音频语言模型` `双分辨率语音表示` `核心鸡尾酒训练` `灾难性遗忘` `多任务学习` `语音理解`

## 📋 核心要点

1. 现有语音-文本模型存在语音和文本token分辨率不匹配的问题，导致语义信息损失和计算成本增加。
2. Fun-Audio-Chat通过双分辨率语音表示（DRSR）和核心鸡尾酒训练，在效率和质量之间取得平衡，并减轻灾难性遗忘。
3. Fun-Audio-Chat在语音转文本、语音转语音和口语QA等任务上取得了优异的性能，并在音频理解等方面表现出竞争力。

## 📝 摘要（中文）

本文介绍了Fun-Audio-Chat，一种大型音频语言模型，旨在解决现有语音-文本联合模型在语音交互中面临的挑战。这些挑战包括：语音token（25Hz）和文本token（~3Hz）之间的时间分辨率不匹配导致语义信息稀释、计算成本高昂以及灾难性地遗忘文本LLM知识。Fun-Audio-Chat通过借鉴DrVoice中的两项创新来克服这些限制。首先，双分辨率语音表示（DRSR）允许共享LLM以高效的5Hz处理音频（通过token分组），而语音精炼头以高质量的25Hz生成token，从而平衡效率（GPU减少约50%）和质量。其次，核心鸡尾酒训练是一种两阶段微调方法，通过中间合并来减轻灾难性遗忘。然后，应用多任务DPO训练来增强鲁棒性、音频理解、指令遵循和语音共情。这种多阶段后训练使Fun-Audio-Chat能够保留文本LLM知识，同时获得强大的音频理解、推理和生成能力。与最近需要大规模音频-文本预训练的LALM不同，Fun-Audio-Chat利用预训练模型和广泛的后训练。Fun-Audio-Chat 8B和MoE 30B-A3B在语音转文本和语音转语音任务上表现出竞争优势，在口语QA基准测试中，在类似规模的模型中名列前茅。它们还在音频理解、语音功能调用、指令遵循和语音共情方面取得了具有竞争力甚至更优越的性能。我们开发了Fun-Audio-Chat-Duplex，这是一种全双工变体，在口语QA和全双工交互方面表现出色。我们开源了Fun-Audio-Chat-8B，包括训练和推理代码，并提供了一个交互式演示。

## 🔬 方法详解

**问题定义**：现有联合语音-文本模型在处理语音交互时，由于语音token（25Hz）和文本token（~3Hz）之间的时间分辨率差异，导致语义信息被稀释，计算成本高昂，并且容易发生灾难性遗忘，即在学习新任务时忘记了之前学习的文本LLM知识。

**核心思路**：Fun-Audio-Chat的核心思路是通过双分辨率语音表示（DRSR）来解决时间分辨率不匹配的问题，并利用核心鸡尾酒训练来缓解灾难性遗忘。DRSR允许模型在不同分辨率下处理语音，兼顾效率和质量。核心鸡尾酒训练则通过两阶段微调和中间合并，使模型能够更好地保留文本LLM知识。

**技术框架**：Fun-Audio-Chat的整体框架包括以下几个主要模块/阶段：1) 双分辨率语音表示（DRSR）：将语音信号转换为两种不同分辨率的表示，一种用于高效处理，另一种用于高质量生成。2) 共享LLM：使用大型语言模型处理低分辨率的语音表示。3) 语音精炼头：生成高质量的语音token。4) 核心鸡尾酒训练：通过两阶段微调和中间合并来缓解灾难性遗忘。5) 多任务DPO训练：增强模型的鲁棒性、音频理解、指令遵循和语音共情能力。

**关键创新**：Fun-Audio-Chat最重要的技术创新点在于双分辨率语音表示（DRSR）和核心鸡尾酒训练。DRSR允许模型在不同分辨率下处理语音，从而在效率和质量之间取得平衡。核心鸡尾酒训练则通过两阶段微调和中间合并，有效地缓解了灾难性遗忘问题。与需要大规模音频-文本预训练的LALM不同，Fun-Audio-Chat主要依赖后训练。

**关键设计**：在DRSR中，共享LLM以5Hz处理音频，而语音精炼头以25Hz生成token。核心鸡尾酒训练包括两个阶段：首先，对模型进行微调以适应新的音频任务；然后，将微调后的模型与原始文本LLM进行合并，以保留文本知识。多任务DPO训练使用多种损失函数来优化模型的不同能力，例如音频理解、指令遵循和语音共情。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20156v1/figure/polar_bar_chart_1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20156v1/figure/polar_bar_chart_2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20156v1/figure/fun-audio-chat.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Fun-Audio-Chat 8B和MoE 30B-A3B在语音转文本和语音转语音任务上表现出竞争优势，并在口语QA基准测试中，在类似规模的模型中名列前茅。此外，它们还在音频理解、语音功能调用、指令遵循和语音共情方面取得了具有竞争力甚至更优越的性能。Fun-Audio-Chat-Duplex在口语QA和全双工交互方面表现出色。

## 🎯 应用场景

Fun-Audio-Chat具有广泛的应用前景，例如智能助手、语音搜索、语音翻译、语音游戏和人机交互等领域。它可以实现更自然、流畅和智能的语音交互体验，提升用户满意度。未来，该技术有望应用于各种智能设备和平台，例如智能家居、智能汽车和移动设备等。

## 📄 摘要（原文）

> Recent advancements in joint speech-text models show great potential for seamless voice interactions. However, existing models face critical challenges: temporal resolution mismatch between speech tokens (25Hz) and text tokens (~3Hz) dilutes semantic information, incurs high computational costs, and causes catastrophic forgetting of text LLM knowledge. We introduce Fun-Audio-Chat, a Large Audio Language Model addressing these limitations via two innovations from our previous work DrVoice. First, Dual-Resolution Speech Representations (DRSR): the Shared LLM processes audio at efficient 5Hz (via token grouping), while the Speech Refined Head generates high-quality tokens at 25Hz, balancing efficiency (~50% GPU reduction) and quality. Second, Core-Cocktail Training, a two-stage fine-tuning with intermediate merging that mitigates catastrophic forgetting. We then apply Multi-Task DPO Training to enhance robustness, audio understanding, instruction-following and voice empathy. This multi-stage post-training enables Fun-Audio-Chat to retain text LLM knowledge while gaining powerful audio understanding, reasoning, and generation. Unlike recent LALMs requiring large-scale audio-text pre-training, Fun-Audio-Chat leverages pre-trained models and extensive post-training. Fun-Audio-Chat 8B and MoE 30B-A3B achieve competitive performance on Speech-to-Text and Speech-to-Speech tasks, ranking top among similar-scale models on Spoken QA benchmarks. They also achieve competitive to superior performance on Audio Understanding, Speech Function Calling, Instruction-Following and Voice Empathy. We develop Fun-Audio-Chat-Duplex, a full-duplex variant with strong performance on Spoken QA and full-duplex interactions. We open-source Fun-Audio-Chat-8B with training and inference code, and provide an interactive demo.

