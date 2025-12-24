---
layout: default
title: Probing Audio-Generation Capabilities of Text-Based Language Models
---

# Probing Audio-Generation Capabilities of Text-Based Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00003" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00003v1</a>
  <a href="https://arxiv.org/pdf/2506.00003.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00003v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00003v1', 'Probing Audio-Generation Capabilities of Text-Based Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arjun Prasaath Anbazhagan, Parteek Kumar, Ujjwal Kaur, Aslihan Akalin, Kevin Zhu, Sean O'Brien

**分类**: cs.SD, cs.CL, eess.AS

**发布日期**: 2025-05-04

**备注**: Accepted at Conference of the North American Chapter of the Association for Computational Linguistics 2025, Student Research Workshop (NAACL SRW)

---

## 💡 一句话要点

**探讨文本基础语言模型的音频生成能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频生成` `大型语言模型` `多模态学习` `代码生成` `音频处理`

## 📋 核心要点

1. 现有的文本基础语言模型在音频生成方面的能力有限，尤其是在处理复杂音频时表现不佳。
2. 本文提出通过逐步增加音频生成复杂性的方法，利用代码生成音频，弥补文本与音频之间的差距。
3. 实验结果显示，LLMs在生成基本音频特征方面表现良好，但在复杂音频生成时性能下降，提示需进一步研究改进方法。

## 📝 摘要（中文）

本文研究了文本表示的音频与大型语言模型（LLMs）在音频世界学习之间的关系。研究采用三层次的方法，逐步增加音频生成的复杂性：1）音乐音符，2）环境声音，3）人类语音。通过利用代码作为中介，提示LLMs生成可执行的代码以产生所需音频输出。评估生成音频的质量和准确性时，采用了FAD和CLAP评分。研究发现，尽管LLMs能够生成基本的音频特征，但随着音频复杂性的增加，其性能显著下降。这表明LLMs对听觉世界有潜在理解，但将这种理解转化为实际音频输出的能力仍然较为初步。进一步研究可以提升LLM生成音频的质量和多样性，从而改善文本基础LLMs在音频生成中的表现。

## 🔬 方法详解

**问题定义**：本文旨在探讨文本基础语言模型在音频生成方面的能力，现有方法在处理复杂音频时效果不佳，限制了其应用潜力。

**核心思路**：通过逐步增加音频生成的复杂性，采用音乐音符、环境声音和人类语音三种类型，利用代码作为中介，提示LLMs生成可执行代码以产生音频。

**技术框架**：研究分为三个主要阶段：首先生成音乐音符，其次生成环境声音，最后生成人类语音。每个阶段的复杂性逐步增加，评估生成音频的质量使用FAD和CLAP评分。

**关键创新**：本研究的创新在于将代码生成作为音频生成的桥梁，利用LLMs的文本理解能力来生成音频，突破了传统音频生成方法的局限。

**关键设计**：在实验中，设置了不同的音频复杂性层次，并采用了特定的损失函数和评估指标（FAD和CLAP），以确保生成音频的质量和准确性。实验设计考虑了不同音频类型的特性，优化了生成过程。

## 📊 实验亮点

实验结果表明，LLMs在生成基本音频特征时表现良好，但在复杂音频生成方面性能显著下降，尤其是在生成环境声音和人类语音时，准确性和质量均有所降低。这一发现为未来的研究提供了重要的方向，强调了提升生成音频质量的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括音乐创作、环境声音模拟和语音合成等。通过提升文本基础LLMs在音频生成方面的能力，可以为多模态交互系统、智能助手和创意工具等提供更丰富的功能，推动相关技术的发展与应用。

## 📄 摘要（原文）

> How does textual representation of audio relate to the Large Language Model's (LLMs) learning about the audio world? This research investigates the extent to which LLMs can be prompted to generate audio, despite their primary training in textual data. We employ a three-tier approach, progressively increasing the complexity of audio generation: 1) Musical Notes, 2) Environmental Sounds, and 3) Human Speech. To bridge the gap between text and audio, we leverage code as an intermediary, prompting LLMs to generate code that, when executed, produces the desired audio output. To evaluate the quality and accuracy of the generated audio, we employ FAD and CLAP scores. Our findings reveal that while LLMs can generate basic audio features, their performance deteriorates as the complexity of the audio increases. This suggests that while LLMs possess a latent understanding of the auditory world, their ability to translate this understanding into tangible audio output remains rudimentary. Further research into techniques that can enhance the quality and diversity of LLM-generated audio can lead to an improvement in the performance of text-based LLMs in generating audio.

