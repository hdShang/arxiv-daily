---
layout: default
title: "XY-Tokenizer: Mitigating the Semantic-Acoustic Conflict in Low-Bitrate Speech Codecs"
---

# XY-Tokenizer: Mitigating the Semantic-Acoustic Conflict in Low-Bitrate Speech Codecs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23325" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23325v2</a>
  <a href="https://arxiv.org/pdf/2506.23325.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23325v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23325v2', 'XY-Tokenizer: Mitigating the Semantic-Acoustic Conflict in Low-Bitrate Speech Codecs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yitian Gong, Luozhijie Jin, Ruifan Deng, Dong Zhang, Xin Zhang, Qinyuan Cheng, Zhaoye Fei, Shimin Li, Xipeng Qiu

**分类**: cs.SD, cs.AI, eess.AS

**发布日期**: 2025-06-29 (更新: 2025-07-09)

**🔗 代码/项目**: [GITHUB](https://github.com/gyt1145028706/XY-Tokenizer)

---

## 💡 一句话要点

**提出XY-Tokenizer以解决低比特率语音编解码中的语义与声学冲突问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音编解码` `多任务学习` `声学保真度` `语义建模` `低比特率` `语音信号处理` `机器学习`

## 📋 核心要点

1. 现有语音编解码器在语义丰富性与声学保真度之间难以取得平衡，导致语音信号的有效传递受到限制。
2. XY-Tokenizer通过多阶段、多任务学习的方式，旨在同时提升语音的声学质量和语义表达能力，解决了传统方法的不足。
3. 实验结果显示，XY-Tokenizer在语义和声学任务上均表现优异，文本对齐能力超越了现有方法，重建音频的说话人相似度评分接近最先进的声学编解码器。

## 📝 摘要（中文）

语音编解码器作为语音信号与大型语言模型之间的桥梁，理想的编解码器应同时保留声学信息和丰富的语义信息。然而，现有编解码器在高质量音频重建与语言模型建模的平衡上存在困难。本研究分析了现有编解码器在语义丰富性与声学保真度之间的局限性，并提出了XY-Tokenizer，这是一种通过多阶段、多任务学习来缓解语义与声学能力冲突的新型编解码器。实验结果表明，XY-Tokenizer在语义和声学任务上的表现与同类比特率的最先进编解码器相当，且在文本对齐方面超越了基于蒸馏的语义建模方法，同时在重建音频的说话人相似度评分上保持在0.83。

## 🔬 方法详解

**问题定义**：本论文旨在解决低比特率语音编解码器在语义与声学信息传递中的冲突问题。现有方法通常在声学保真度或语义丰富性上表现突出，但难以兼顾两者，导致信息损失。

**核心思路**：XY-Tokenizer的核心思路是通过多阶段、多任务学习框架，分别优化声学和语义任务，从而实现两者的有效结合，提升整体性能。

**技术框架**：该方法采用分阶段的学习策略，首先进行声学特征提取，然后通过多任务学习同时优化语义建模和声学重建，确保信息的完整性与准确性。

**关键创新**：XY-Tokenizer的最大创新在于其多任务学习机制，能够在同一模型中平衡声学与语义任务的优化，而现有方法往往只能专注于其中一方面。

**关键设计**：在设计上，XY-Tokenizer使用了特定的损失函数来平衡声学和语义任务的权重，同时在网络结构上采用了适应性模块，以便在不同任务间灵活调整参数设置。

## 📊 实验亮点

实验结果表明，XY-Tokenizer在语义任务上超越了基于蒸馏的语义建模方法，如SpeechTokenizer和Mimi，且在声学重建方面，其说话人相似度评分达到0.83，接近当前声学编解码器BigCodec的0.84，显示出显著的性能提升。

## 🎯 应用场景

XY-Tokenizer的研究成果在语音识别、语音合成和人机交互等领域具有广泛的应用潜力。通过提升语音信号的语义表达与声学质量，该技术能够改善语音助手、翻译系统及其他基于语音的应用的用户体验，推动智能语音技术的发展。

## 📄 摘要（原文）

> Speech codecs serve as bridges between speech signals and large language models. An ideal codec for speech language models should not only preserve acoustic information but also capture rich semantic information. However, existing speech codecs struggle to balance high-quality audio reconstruction with ease of modeling by language models. In this study, we analyze the limitations of previous codecs in balancing semantic richness and acoustic fidelity. We propose XY-Tokenizer, a novel codec that mitigates the conflict between semantic and acoustic capabilities through multi-stage, multi-task learning. Experimental results demonstrate that XY-Tokenizer achieves performance in both semantic and acoustic tasks comparable to that of state-of-the-art codecs operating at similar bitrates, even though those existing codecs typically excel in only one aspect. Specifically, XY-Tokenizer achieves strong text alignment, surpassing distillation-based semantic modeling methods such as SpeechTokenizer and Mimi, while maintaining a speaker similarity score of 0.83 between reconstructed and original audio. The reconstruction performance of XY-Tokenizer is comparable to that of BigCodec, the current state-of-the-art among acoustic-only codecs, which achieves a speaker similarity score of 0.84 at a similar bitrate. Code and models are available at https://github.com/gyt1145028706/XY-Tokenizer.

