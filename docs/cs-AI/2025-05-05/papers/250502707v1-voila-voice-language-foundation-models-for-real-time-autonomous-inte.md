---
layout: default
title: "Voila: Voice-Language Foundation Models for Real-Time Autonomous Interaction and Voice Role-Play"
---

# Voila: Voice-Language Foundation Models for Real-Time Autonomous Interaction and Voice Role-Play

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02707" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02707v1</a>
  <a href="https://arxiv.org/pdf/2505.02707.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02707v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02707v1', 'Voila: Voice-Language Foundation Models for Real-Time Autonomous Interaction and Voice Role-Play')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yemin Shi, Yu Shu, Siwei Dong, Guangyi Liu, Jaward Sesay, Jingwen Li, Zhiting Hu

**分类**: cs.AI, cs.CL, cs.SD

**发布日期**: 2025-05-05

**备注**: 18 pages, 7 figures, Website: https://voila.maitrix.org

---

## 💡 一句话要点

**提出Voila以实现实时自主互动和语音角色扮演**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音AI` `实时互动` `情感表达` `全双工对话` `大型语言模型` `声学建模` `语音定制` `人机交互`

## 📋 核心要点

1. 现有的语音AI系统往往只能被动响应命令，缺乏实时和情感表达能力，限制了人机交互的自然性和流畅性。
2. Voila采用全新的端到端架构，结合层次多尺度Transformer，支持全双工对话和丰富的声学特征生成，提升了互动的自然性。
3. Voila实现了195毫秒的响应延迟，超越了人类平均反应时间，并支持超过一百万个预构建声音，具有极高的定制化能力。

## 📝 摘要（中文）

Voila是一种大型语音语言基础模型，旨在实现与人类的自主、实时和情感丰富的互动。与传统的命令反应系统不同，Voila能够持续监听、推理并主动响应，促进流畅且动态的交流。其全双工、低延迟的对话能力使得响应时间仅为195毫秒，超越了人类的平均反应时间。Voila的层次多尺度Transformer将大型语言模型的推理能力与强大的声学建模相结合，支持用户通过文本指令定义说话者的身份和语调等特征。此外，Voila支持超过一百万个预构建的声音，并能从短至10秒的音频样本中高效定制新声音。Voila不仅适用于口语对话，还可广泛应用于自动语音识别、文本转语音和多语言语音翻译等领域。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有语音AI系统在实时互动和情感表达方面的不足，传统系统通常只能被动响应用户命令，缺乏主动交流的能力。

**核心思路**：Voila通过引入全双工、低延迟的对话能力和情感丰富的声学建模，构建了一种新的语音语言基础模型，能够实现更加自然和动态的人机互动。

**技术框架**：Voila的整体架构包括层次多尺度Transformer，集成了大型语言模型的推理能力与声学建模，支持用户通过文本指令定义说话者的身份和语调等特征。

**关键创新**：Voila的主要创新在于其全新的端到端架构和层次多尺度Transformer设计，使得其在响应延迟和声学特征生成上显著优于传统方法。

**关键设计**：在技术细节上，Voila采用了优化的损失函数和网络结构，能够从短至10秒的音频样本中高效定制新声音，并支持超过一百万个预构建声音。

## 📊 实验亮点

Voila在实验中实现了195毫秒的响应延迟，显著低于人类的平均反应时间，且支持超过一百万个预构建声音。与传统语音AI系统相比，Voila在自然性和情感表达方面表现出显著提升，展示了其在实时互动中的优势。

## 🎯 应用场景

Voila的研究成果在多个领域具有广泛的应用潜力，包括智能家居助手、客服机器人、教育辅导、游戏角色扮演等。其高效的语音生成和情感表达能力将极大提升人机交互的自然性和用户体验，推动下一代人机交互技术的发展。

## 📄 摘要（原文）

> A voice AI agent that blends seamlessly into daily life would interact with humans in an autonomous, real-time, and emotionally expressive manner. Rather than merely reacting to commands, it would continuously listen, reason, and respond proactively, fostering fluid, dynamic, and emotionally resonant interactions. We introduce Voila, a family of large voice-language foundation models that make a step towards this vision. Voila moves beyond traditional pipeline systems by adopting a new end-to-end architecture that enables full-duplex, low-latency conversations while preserving rich vocal nuances such as tone, rhythm, and emotion. It achieves a response latency of just 195 milliseconds, surpassing the average human response time. Its hierarchical multi-scale Transformer integrates the reasoning capabilities of large language models (LLMs) with powerful acoustic modeling, enabling natural, persona-aware voice generation -- where users can simply write text instructions to define the speaker's identity, tone, and other characteristics. Moreover, Voila supports over one million pre-built voices and efficient customization of new ones from brief audio samples as short as 10 seconds. Beyond spoken dialogue, Voila is designed as a unified model for a wide range of voice-based applications, including automatic speech recognition (ASR), Text-to-Speech (TTS), and, with minimal adaptation, multilingual speech translation. Voila is fully open-sourced to support open research and accelerate progress toward next-generation human-machine interactions.

