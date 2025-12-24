---
layout: default
title: "Speak Your Mind: The Speech Continuation Task as a Probe of Voice-Based Model Bias"
---

# Speak Your Mind: The Speech Continuation Task as a Probe of Voice-Based Model Bias

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22061" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22061v1</a>
  <a href="https://arxiv.org/pdf/2509.22061.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22061v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22061v1', 'Speak Your Mind: The Speech Continuation Task as a Probe of Voice-Based Model Bias')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shree Harsha Bokkahalli Satish, Harm Lameris, Olivier Perrotin, Gustav Eje Henter, Éva Székely

**分类**: eess.AS, cs.CL, cs.SD

**发布日期**: 2025-09-26

**备注**: 6 pages, 1 figure, Submitted to IEEE ICASSP 2026

---

## 💡 一句话要点

**提出语音延续任务以探测语音模型偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音延续` `模型偏见` `性别影响` `发声类型` `语音技术` `人机交互`

## 📋 核心要点

1. 现有方法在探测语音模型偏见时面临挑战，尤其是在性别和发声类型对延续行为的影响方面。
2. 论文提出通过语音延续任务系统性评估语音模型中的偏见，利用单一音频流的特性进行深入分析。
3. 实验结果表明，尽管连贯性仍存在挑战，但在高连贯性条件下，性别对文本指标如代理性和句子极性产生显著影响。

## 📝 摘要（中文）

语音延续（SC）是生成与语音提示一致的延续内容的任务，同时保持语义上下文和说话者身份。由于SC仅限于单一音频流，因此比对话更直接地探测语音基础模型中的偏见。本文首次系统评估了SC中的偏见，研究了性别和发声类型（如气声、喉音、尾声）对延续行为的影响。我们评估了三种近期模型：SpiritLM（基础和表现型）、VAE-GSLM和SpeechGPT，结果显示说话者相似性和连贯性仍然是挑战，而文本评估揭示了模型和性别之间的显著交互作用。这些发现强调了SC作为探测语音基础模型中社会相关表现偏见的有效工具，并表明随着延续质量的提高，它将成为越来越有价值的诊断工具。

## 🔬 方法详解

**问题定义**：本文旨在解决语音延续任务中存在的模型偏见问题，尤其是性别和发声类型对延续行为的影响。现有方法在探测这些偏见时缺乏系统性评估，导致对模型的理解不够深入。

**核心思路**：论文通过语音延续任务作为探测工具，系统评估不同模型在延续行为中的偏见表现，特别关注性别和发声类型的影响。这样的设计使得研究能够在控制条件下揭示模型的偏见特征。

**技术框架**：研究评估了三种模型（SpiritLM、VAE-GSLM和SpeechGPT），通过分析说话者相似性、声音质量保持和文本偏见指标，构建了一个多维度的评估框架。

**关键创新**：论文的创新在于首次将语音延续任务作为探测语音模型偏见的工具，揭示了性别和发声类型对模型行为的系统性影响，这在以往的研究中尚未得到充分探讨。

**关键设计**：在实验中，设置了不同的连贯性标准，并使用文本指标（如代理性和句子极性）进行评估，确保了对模型偏见的全面分析。

## 📊 实验亮点

实验结果显示，在高连贯性条件下，性别对文本指标如代理性和句子极性产生显著影响，尤其是女性提示的延续更倾向于回归到模态发声。这表明模型在声音质量上的偏见，强调了语音延续任务在探测模型偏见中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括语音助手、语音识别系统和人机交互等。通过深入理解语音模型中的偏见，可以为开发更公平和包容的语音技术提供指导，提升用户体验，减少社会偏见的传播。

## 📄 摘要（原文）

> Speech Continuation (SC) is the task of generating a coherent extension of a spoken prompt while preserving both semantic context and speaker identity. Because SC is constrained to a single audio stream, it offers a more direct setting for probing biases in speech foundation models than dialogue does. In this work we present the first systematic evaluation of bias in SC, investigating how gender and phonation type (breathy, creaky, end-creak) affect continuation behaviour. We evaluate three recent models: SpiritLM (base and expressive), VAE-GSLM, and SpeechGPT across speaker similarity, voice quality preservation, and text-based bias metrics. Results show that while both speaker similarity and coherence remain a challenge, textual evaluations reveal significant model and gender interactions: once coherence is sufficiently high (for VAE-GSLM), gender effects emerge on text-metrics such as agency and sentence polarity. In addition, continuations revert toward modal phonation more strongly for female prompts than for male ones, revealing a systematic voice-quality bias. These findings highlight SC as a controlled probe of socially relevant representational biases in speech foundation models, and suggest that it will become an increasingly informative diagnostic as continuation quality improves.

