---
layout: default
title: "PredGen: Accelerated Inference of Large Language Models through Input-Time Speculation for Real-Time Speech Interaction"
---

# PredGen: Accelerated Inference of Large Language Models through Input-Time Speculation for Real-Time Speech Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15556" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15556v2</a>
  <a href="https://arxiv.org/pdf/2506.15556.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15556v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15556v2', 'PredGen: Accelerated Inference of Large Language Models through Input-Time Speculation for Real-Time Speech Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shufan Li, Aditya Grover

**分类**: cs.CL, cs.SD, eess.AS

**发布日期**: 2025-06-18 (更新: 2025-10-08)

**备注**: 16 pages,4 figures

---

## 💡 一句话要点

**提出PredGen以解决大语言模型实时语音交互中的延迟问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `实时语音交互` `推测解码` `文本转语音` `用户体验` `计算效率` `智能助手`

## 📋 核心要点

1. 现有方法在实时语音交互中存在显著延迟，影响用户体验，尤其是在资源有限的消费级硬件上。
2. 论文提出的PredGen框架通过输入时的推测解码，允许在用户输入时生成候选响应，从而减少延迟。
3. 实验结果显示，PredGen在多种场景下有效将延迟减少约2倍，且计算成本增加极小。

## 📝 摘要（中文）

大语言模型（LLMs）在实时语音聊天应用中广泛使用，通常与文本转语音（TTS）系统结合生成音频响应。然而，由于其庞大的模型规模，用户输入结束与音频输出开始之间的延迟显著，影响用户体验。我们发现，这种延迟主要由LLMs生成第一句所需的时间主导。为了解决这一瓶颈，我们提出了预测生成（PredGen）框架，通过输入时的推测解码来减轻甚至消除这种延迟。PredGen在用户说话时生成候选响应，使系统能够以最小延迟开始TTS处理。模拟实验表明，该方法在多种使用场景中有效将延迟减少约2倍，同时在输入时仅增加了极少的计算成本。

## 🔬 方法详解

**问题定义**：本论文旨在解决大语言模型在实时语音交互中存在的显著延迟问题，尤其是当LLMs作为单用户语音助手在计算能力有限的硬件上运行时，延迟尤为明显。现有方法在生成第一句时耗时较长，导致用户体验不佳。

**核心思路**：论文的核心思路是通过预测生成（PredGen）框架，在用户输入时进行推测解码，提前生成候选响应，从而使得TTS系统能够更快地开始音频输出。这样的设计旨在减少用户等待时间，提高交互的流畅性。

**技术框架**：PredGen框架包括输入时推测解码模块和TTS处理模块。推测解码模块在用户说话时生成候选响应，而TTS处理模块则在接收到第一句后立即开始音频合成。

**关键创新**：PredGen的主要创新在于其推测解码机制，能够在用户输入的同时进行响应生成，这与传统方法需要等待用户输入结束后再进行处理的方式有本质区别。

**关键设计**：在设计中，PredGen采用了轻量级的计算策略，确保在输入时的计算成本保持在最低水平，避免了传统方法中因等待而产生的计算浪费。

## 📊 实验亮点

实验结果表明，PredGen在多种使用场景中有效将延迟减少约2倍，相较于基线方法，性能提升显著，同时仅增加了极少的计算成本。这一成果展示了在实时语音交互中优化用户体验的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能语音助手、实时语音翻译和互动游戏等场景。通过减少响应延迟，PredGen能够显著提升用户体验，促进语音交互技术的广泛应用和发展。未来，该技术可能在更多实时交互系统中发挥重要作用，推动人机交互的进步。

## 📄 摘要（原文）

> Large Language Models (LLMs) are widely used in real-time voice chat applications, typically in combination with text-to-speech (TTS) systems to generate audio responses. However, their large size often leads to noticeable latency between the end of user input and the start of audio output, resulting in suboptimal user experiences. This latency is particularly evident when LLMs are deployed as single-user voice assistants on consumer-grade hardware with limited computing capacity. We discovered that this latency is primarily dominated by the time it takes for the LLMs to generate the first sentence, which is required as input by the TTS systems that synthesize audio responses on a sentence-by-sentence basis. To address this bottleneck, we propose Predictive Generation (PredGen), a novel framework that mitigates-or even eliminates-this delay through speculative decoding at input time. PredGen generates candidate responses while the user is still speaking, enabling the system to begin TTS processing with minimal delay. Simulated experiments on the Lmsys and MT-Bench datasets show that the proposed method can effectively reduce the latency by around 2x across a wide range of use cases, while incurring only minimal additional computation cost at input time-computation that would otherwise go unused.

