---
layout: default
title: "DrVoice: Parallel Speech-Text Voice Conversation Model via Dual-Resolution Speech Representations"
---

# DrVoice: Parallel Speech-Text Voice Conversation Model via Dual-Resolution Speech Representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09349" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09349v3</a>
  <a href="https://arxiv.org/pdf/2506.09349.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09349v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09349v3', 'DrVoice: Parallel Speech-Text Voice Conversation Model via Dual-Resolution Speech Representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chao-Hong Tan, Qian Chen, Wen Wang, Chong Deng, Qinglin Zhang, Luyao Cheng, Hai Yu, Xin Zhang, Xiang Lv, Tianyu Zhao, Chong Zhang, Yukun Ma, Yafeng Chen, Hui Wang, Jiaqing Liu, Xiangang Li, Jieping Ye

**分类**: cs.CL

**发布日期**: 2025-06-11 (更新: 2025-10-28)

**备注**: Work in progress

---

## 💡 一句话要点

**提出DrVoice以解决语音生成中的模态不一致问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音生成` `双分辨率` `联合自回归` `模态互知` `大语言模型` `开源模型` `计算效率`

## 📋 核心要点

1. 现有的E2E语音生成方法在模态互知和计算效率上存在不足，导致生成质量受限。
2. 本文提出的DrVoice模型通过联合自回归建模和双分辨率语音表示，提升了语音和文本生成的互知能力。
3. 实验结果显示，DRVOICE-7B在多个基准测试中取得了新的SOTA，展现了其在语音生成领域的领先地位。

## 📝 摘要（中文）

近年来，基于大语言模型（LLMs）的端到端（E2E）语音生成研究引起了广泛关注。现有E2E方法主要分为两类：一类是独立生成离散语音标记，未能与LLM的自回归过程结合；另一类是通过联合自回归建模生成交错或并行的语音-文本标记，实现生成过程中的模态互知。本文提出了DrVoice，一个基于联合自回归建模的并行语音-文本对话模型，采用双分辨率语音表示。与现有方法主要使用12.5Hz输入音频表示不同，我们的双分辨率机制将LLM的输入频率降低至5Hz，显著降低了计算成本，并缓解了语音和文本标记之间的频率差异，从而更好地利用LLMs的能力。实验结果表明，DRVOICE-7B在OpenAudioBench和Big Bench Audio基准上建立了新的最先进（SOTA）记录，同时在VoiceBench和UltraEval-Audio基准上表现出与SOTA相当的性能，使其成为约7B模型中的领先开源语音基础模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有E2E语音生成方法中模态不一致和计算效率低下的问题。现有方法往往未能有效结合语音和文本生成，导致生成质量不佳。

**核心思路**：DrVoice通过引入联合自回归建模和双分辨率语音表示，增强了语音和文本生成过程中的互知性，同时降低了计算成本。

**技术框架**：该模型的整体架构包括输入音频的双分辨率处理、联合自回归建模模块以及输出生成模块，确保语音和文本的同步生成。

**关键创新**：DrVoice的双分辨率机制是其核心创新点，通过将输入频率降低至5Hz，显著减少了计算负担，并改善了语音与文本之间的频率匹配。

**关键设计**：模型在参数设置上进行了优化，采用特定的损失函数以平衡语音和文本生成的质量，同时设计了适应性强的网络结构以支持双分辨率输入。

## 📊 实验亮点

实验结果表明，DRVOICE-7B在OpenAudioBench和Big Bench Audio基准上达到了新的最先进水平，性能超越了现有的最佳模型。同时，在VoiceBench和UltraEval-Audio基准上，其表现也与最先进模型相当，显示出显著的性能提升。

## 🎯 应用场景

DrVoice模型在智能语音助手、实时翻译、语音交互系统等领域具有广泛的应用潜力。其高效的语音生成能力能够提升用户体验，并在多模态交互中发挥重要作用。未来，该技术可能推动更自然的人机对话和更智能的语音应用发展。

## 📄 摘要（原文）

> Recent studies on end-to-end (E2E) speech generation with large language models (LLMs) have attracted significant community attention, with multiple works extending text-based LLMs to generate discrete speech tokens. Existing E2E approaches primarily fall into two categories: (1) Methods that generate discrete speech tokens independently without incorporating them into the LLM's autoregressive process, resulting in text generation being unaware of concurrent speech synthesis. (2) Models that generate interleaved or parallel speech-text tokens through joint autoregressive modeling, enabling mutual modality awareness during generation. This paper presents DrVoice, a parallel speech-text voice conversation model based on joint autoregressive modeling, featuring dual-resolution speech representations. Notably, while current methods utilize mainly 12.5Hz input audio representation, our proposed dual-resolution mechanism reduces the input frequency for the LLM to 5Hz, significantly reducing computational cost and alleviating the frequency discrepancy between speech and text tokens and in turn better exploiting LLMs' capabilities. Experimental results demonstrate that DRVOICE-7B establishes new state-of-the-art (SOTA) on OpenAudioBench and Big Bench Audio benchmarks, while achieving performance comparable to the SOTA on VoiceBench and UltraEval-Audio benchmarks, making it a leading open-source speech foundation model in ~7B models.

