---
layout: default
title: "HNote: Extending YNote with Hexadecimal Encoding for Fine-Tuning LLMs in Music Modeling"
---

# HNote: Extending YNote with Hexadecimal Encoding for Fine-Tuning LLMs in Music Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25694" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25694v2</a>
  <a href="https://arxiv.org/pdf/2509.25694.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25694v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25694v2', 'HNote: Extending YNote with Hexadecimal Encoding for Fine-Tuning LLMs in Music Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hung-Ying Chu, Shao-Yu Wei, Guan-Wei Chen, Tzu-Wei Hung, ChengYang Tsai, Yu-Cheng Lin

**分类**: cs.SD, cs.AI

**发布日期**: 2025-09-30 (更新: 2025-10-04)

---

## 💡 一句话要点

**提出HNote：一种基于十六进制编码的音乐表示方法，用于微调LLM进行音乐建模**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音乐生成` `大型语言模型` `十六进制编码` `音乐表示` `文化音乐建模`

## 📋 核心要点

1. 现有音乐表示方法（如MIDI）复杂或结构不一致，不适用于基于token的LLM音乐生成。
2. HNote通过十六进制编码音高和时长，在固定长度小节内对齐，简化了音乐表示并兼容LLM。
3. 实验表明，使用HNote微调LLM后，音乐生成在句法正确率和风格连贯性上表现良好。

## 📝 摘要（中文）

大型语言模型（LLM）的最新进展为符号音乐生成创造了新的机会。然而，现有的格式（如MIDI、ABC和MusicXML）要么过于复杂，要么结构不一致，限制了它们对基于token的学习架构的适用性。为了解决这些挑战，我们提出了HNote，这是一种新颖的基于十六进制的记谱系统，它扩展自YNote，在固定的32个单位的小节框架内编码音高和持续时间。这种设计确保了对齐，减少了歧义，并且与LLM架构直接兼容。我们将从YNote生成的12,300首江南风格的传统民歌转换为HNote，并使用参数高效的LoRA微调了LLaMA-3.1(8B)。实验结果表明，HNote实现了82.5%的句法正确率，BLEU和ROUGE评估表明了强大的符号和结构相似性，从而产生了风格连贯的作曲。这项研究确立了HNote作为将LLM与文化音乐建模相结合的有效框架。

## 🔬 方法详解

**问题定义**：现有音乐表示方法，如MIDI、ABC和MusicXML，在用于基于token的LLM音乐生成时存在局限性。MIDI过于复杂，ABC和MusicXML结构不一致，导致模型难以学习和生成高质量的音乐。这些格式的复杂性增加了模型训练的难度，降低了生成音乐的质量和风格一致性。

**核心思路**：HNote的核心思路是设计一种简洁、结构化的音乐表示方法，使其易于LLM学习和生成。通过使用十六进制编码音高和时长，并在固定的32单位小节框架内进行对齐，HNote简化了音乐的表示，减少了歧义，并与LLM的token化处理方式天然兼容。这种设计旨在提高LLM生成音乐的句法正确性和风格连贯性。

**技术框架**：HNote的技术框架主要包括以下几个步骤：1) 将现有的YNote格式的江南风格音乐转换为HNote格式。2) 使用转换后的HNote数据微调LLaMA-3.1(8B)模型，采用参数高效的LoRA方法。3) 使用微调后的模型生成音乐。4) 使用句法正确率、BLEU和ROUGE等指标评估生成音乐的质量。

**关键创新**：HNote的关键创新在于其基于十六进制的音乐表示方法。与现有的音乐表示方法相比，HNote更加简洁、结构化，并且与LLM的token化处理方式更加兼容。这种设计使得LLM更容易学习和生成高质量的音乐。此外，HNote的固定长度小节框架也有助于提高生成音乐的结构一致性。

**关键设计**：HNote使用十六进制编码音高和时长，每个音符的信息被编码为一个十六进制字符串。小节长度固定为32个单位，确保了音乐的节奏和结构一致性。在模型微调方面，使用了LoRA（Low-Rank Adaptation）方法，这是一种参数高效的微调技术，可以在不修改原始模型参数的情况下，通过添加少量可训练参数来适应新的任务。

## 📊 实验亮点

实验结果表明，使用HNote微调的LLaMA-3.1(8B)模型在生成音乐时达到了82.5%的句法正确率。BLEU和ROUGE评估表明，生成的音乐在符号和结构上与原始音乐具有很强的相似性，证明了HNote在音乐建模方面的有效性。这些结果表明，HNote可以作为一种有效的框架，将LLM与文化音乐建模相结合。

## 🎯 应用场景

HNote的应用场景包括文化音乐建模、自动作曲、音乐教育和音乐治疗。它可以用于生成特定风格的音乐，例如江南风格的传统民歌。此外，HNote还可以作为音乐教育的工具，帮助学生理解音乐的结构和理论。在音乐治疗方面，HNote可以用于生成个性化的音乐，以满足不同患者的需求。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have created new opportunities for symbolic music generation. However, existing formats such as MIDI, ABC, and MusicXML are either overly complex or structurally inconsistent, limiting their suitability for token-based learning architectures. To address these challenges, we propose HNote, a novel hexadecimal-based notation system extended from YNote, which encodes both pitch and duration within a fixed 32-unit measure framework. This design ensures alignment, reduces ambiguity, and is directly compatible with LLM architectures. We converted 12,300 Jiangnan-style songs generated from traditional folk pieces from YNote into HNote, and fine-tuned LLaMA-3.1(8B) using parameter-efficient LoRA. Experimental results show that HNote achieves a syntactic correctness rate of 82.5%, and BLEU and ROUGE evaluations demonstrate strong symbolic and structural similarity, producing stylistically coherent compositions. This study establishes HNote as an effective framework for integrating LLMs with cultural music modeling.

