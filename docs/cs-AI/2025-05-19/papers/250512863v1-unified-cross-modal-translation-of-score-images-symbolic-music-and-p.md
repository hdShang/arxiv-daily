---
layout: default
title: Unified Cross-modal Translation of Score Images, Symbolic Music, and Performance Audio
---

# Unified Cross-modal Translation of Score Images, Symbolic Music, and Performance Audio

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12863" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12863v1</a>
  <a href="https://arxiv.org/pdf/2505.12863.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12863v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12863v1', 'Unified Cross-modal Translation of Score Images, Symbolic Music, and Performance Audio')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jongmin Jung, Dongmin Kim, Sihun Lee, Seola Cho, Hyungjoon Soh, Irmak Bukey, Chris Donahue, Dasaem Jeong

**分类**: cs.SD, cs.AI, cs.CV, eess.AS

**发布日期**: 2025-05-19

**备注**: Submitted to IEEE Transactions on Audio, Speech and Language Processing (TASLPRO)

---

## 💡 一句话要点

**提出统一跨模态翻译方法以解决音乐信息检索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跨模态翻译` `音乐信息检索` `光学音乐识别` `自动音乐转录` `Transformer模型` `多任务学习` `数据集构建`

## 📋 核心要点

1. 现有的多模态翻译方法通常针对单一任务训练专门模型，缺乏统一的解决方案。
2. 本文提出了一种统一的跨模态翻译方法，通过新的大规模数据集和标记化框架实现多任务训练。
3. 实验结果显示，统一模型在光学音乐识别等任务中显著降低了错误率，并实现了乐谱图像条件音频生成。

## 📝 摘要（中文）

音乐存在于多种模态中，如乐谱图像、符号乐谱、MIDI和音频。各模态之间的翻译是音乐信息检索的核心任务，如自动音乐转录和光学音乐识别。然而，过去的研究多为针对单一翻译任务训练专门模型。本文提出了一种统一的方法，通过同时训练通用模型来处理多种翻译任务。我们提出了一个新的大规模数据集，包含来自YouTube视频的1300小时配对音频-乐谱图像数据，并设计了一个统一的标记化框架，将不同模态离散化为令牌序列，使得单个编码-解码Transformer能够将多个跨模态翻译视为一个连贯的序列到序列任务。实验结果表明，该统一多任务模型在多个关键领域超越了单任务基线，特别是在光学音乐识别中将符号错误率从24.58%降低至13.67%，同时在其他翻译任务中也观察到了显著的改善。值得注意的是，我们的方法实现了首次成功的乐谱图像条件音频生成，标志着跨模态音乐生成的重要突破。

## 🔬 方法详解

**问题定义**：本文旨在解决音乐信息检索中不同模态（如乐谱图像、音频等）之间的翻译问题。现有方法通常专注于单一任务，导致模型的泛化能力不足，且缺乏跨模态的协同效应。

**核心思路**：我们提出了一种统一的模型，通过同时训练多个翻译任务，利用一个大规模的数据集和统一的标记化框架，使得不同模态之间的转换能够在同一模型中实现。

**技术框架**：整体架构包括数据收集、标记化、模型训练和评估四个主要阶段。首先，从YouTube视频中收集音频和乐谱图像数据，然后将其标记化为令牌序列，最后使用一个编码-解码的Transformer模型进行训练和评估。

**关键创新**：最重要的技术创新在于提出了一个新的大规模数据集和统一的标记化框架，使得多个模态的翻译可以在一个模型中高效实现。这与以往单一任务模型的设计有本质区别。

**关键设计**：在模型设计中，我们采用了Transformer架构，设置了适当的损失函数以优化多任务学习效果，并通过数据增强和正则化技术提高模型的泛化能力。

## 📊 实验亮点

实验结果显示，统一多任务模型在光学音乐识别中将符号错误率从24.58%降低至13.67%，实现了显著的性能提升。此外，该方法首次成功实现了乐谱图像条件音频生成，标志着跨模态音乐生成的重大进展。

## 🎯 应用场景

该研究的潜在应用领域包括音乐创作、教育和音乐信息检索等。通过实现不同模态之间的高效转换，能够为音乐创作者提供新的工具，帮助他们在创作过程中更好地利用不同形式的音乐信息。此外，该技术还可以应用于音乐教育中，帮助学生更直观地理解音乐结构和表现。

## 📄 摘要（原文）

> Music exists in various modalities, such as score images, symbolic scores, MIDI, and audio. Translations between each modality are established as core tasks of music information retrieval, such as automatic music transcription (audio-to-MIDI) and optical music recognition (score image to symbolic score). However, most past work on multimodal translation trains specialized models on individual translation tasks. In this paper, we propose a unified approach, where we train a general-purpose model on many translation tasks simultaneously. Two key factors make this unified approach viable: a new large-scale dataset and the tokenization of each modality. Firstly, we propose a new dataset that consists of more than 1,300 hours of paired audio-score image data collected from YouTube videos, which is an order of magnitude larger than any existing music modal translation datasets. Secondly, our unified tokenization framework discretizes score images, audio, MIDI, and MusicXML into a sequence of tokens, enabling a single encoder-decoder Transformer to tackle multiple cross-modal translation as one coherent sequence-to-sequence task. Experimental results confirm that our unified multitask model improves upon single-task baselines in several key areas, notably reducing the symbol error rate for optical music recognition from 24.58% to a state-of-the-art 13.67%, while similarly substantial improvements are observed across the other translation tasks. Notably, our approach achieves the first successful score-image-conditioned audio generation, marking a significant breakthrough in cross-modal music generation.

