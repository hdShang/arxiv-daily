---
layout: default
title: "SpeechRole: A Large-Scale Dataset and Benchmark for Evaluating Speech Role-Playing Agents"
---

# SpeechRole: A Large-Scale Dataset and Benchmark for Evaluating Speech Role-Playing Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02013" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02013v5</a>
  <a href="https://arxiv.org/pdf/2508.02013.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02013v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02013v5', 'SpeechRole: A Large-Scale Dataset and Benchmark for Evaluating Speech Role-Playing Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changhao Jiang, Jiajun Sun, Yifei Cao, Jiabao Zhuang, Hui Li, Baoyu Fan, Tao Ji, Tao Gui, Qi Zhang

**分类**: cs.CL

**发布日期**: 2025-08-04 (更新: 2025-12-03)

**备注**: This work is withdrawn as all authors are not in agreement on the work

---

## 💡 一句话要点

**构建SpeechRole数据集以评估语音角色扮演代理的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音角色扮演` `多模态交互` `数据集构建` `评估基准` `语音特征`

## 📋 核心要点

1. 现有研究主要集中于文本模态，缺乏对语音角色扮演代理的系统评估，限制了其在真实场景中的应用。
2. 本文构建了SpeechRole-Data数据集，包含多样化角色和丰富的语音对话，提供了评估SRPAs的新基准。
3. 实验结果表明，级联和端到端的语音角色扮演代理在声音风格一致性和角色连贯性方面存在明显的优势与挑战。

## 📝 摘要（中文）

近年来，角色扮演代理作为实现个性化互动和情感共鸣的有前景的范式逐渐兴起。然而，现有研究主要集中在文本模态上，忽视了语音在现实互动场景中的重要性。为填补这一空白，本文构建了SpeechRole-Data，这是一个大规模、高质量的数据集，包含98种多样化角色和112,000个基于语音的单轮和多轮对话。每个角色展现了独特的声音特征，包括音色和韵律，从而实现更复杂的语音角色扮演。此外，我们提出了SpeechRole-Eval，一个多维度评估基准，系统评估SRPAs在基本互动能力、语音表现力和角色扮演忠实度等关键方面的性能。实验结果揭示了级联和端到端语音角色扮演代理在保持声音风格一致性和角色连贯性方面的优势与挑战。我们发布了所有数据、代码和基线模型，为语音驱动的多模态角色扮演研究提供了坚实基础，并促进该领域的进一步发展。

## 🔬 方法详解

**问题定义**：本文旨在解决现有语音角色扮演代理在评估和应用中的不足，尤其是缺乏系统性的数据集和评估标准。现有方法未能充分考虑语音特征在角色扮演中的重要性。

**核心思路**：通过构建一个包含多样化角色和丰富语音对话的数据集，提供一个全面的评估框架，以便更好地评估和提升语音角色扮演代理的性能。

**技术框架**：整体架构包括数据集构建、角色特征定义、对话生成和评估标准制定等主要模块。数据集包含单轮和多轮对话，角色特征通过音色和韵律进行定义。

**关键创新**：最重要的创新在于构建了一个大规模的语音对话数据集，并提出了多维度的评估基准，系统性地评估SRPAs在互动能力和角色扮演忠实度等方面的表现。

**关键设计**：在数据集构建中，采用了多样化的角色定义和丰富的对话场景；评估标准则涵盖了基本互动能力、语音表现力和角色扮演忠实度等多个维度。

## 📊 实验亮点

实验结果显示，级联和端到端的语音角色扮演代理在声音风格一致性和角色连贯性方面的表现存在显著差异，具体性能数据和提升幅度将在后续研究中详细探讨。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟助手、游戏角色互动、教育培训等。通过提升语音角色扮演代理的表现，可以实现更自然和个性化的用户体验，推动人机交互的进一步发展。

## 📄 摘要（原文）

> Recently, role-playing agents have emerged as a promising paradigm for achieving personalized interaction and emotional resonance. Existing research primarily focuses on the textual modality, neglecting the critical dimension of speech in realistic interactive scenarios. In particular, there is a lack of systematic evaluation for Speech Role-Playing Agents (SRPAs). To address this gap, we construct SpeechRole-Data, a large-scale, high-quality dataset that comprises 98 diverse roles and 112k speech-based single-turn and multi-turn conversations. Each role demonstrates distinct vocal characteristics, including timbre and prosody, thereby enabling more sophisticated speech role-playing. Furthermore, we propose SpeechRole-Eval, a multidimensional evaluation benchmark that systematically assesses SRPAs performance in key aspects such as fundamental interaction ability, speech expressiveness, and role-playing fidelity. Experimental results reveal the advantages and challenges of both cascaded and end-to-end speech role-playing agents in maintaining vocal style consistency and role coherence. We release all data, code, and baseline models to provide a solid foundation for speech-driven multimodal role-playing research and to foster further developments in this field.

