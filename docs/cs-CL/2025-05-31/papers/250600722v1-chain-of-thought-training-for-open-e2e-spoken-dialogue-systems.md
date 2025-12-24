---
layout: default
title: Chain-of-Thought Training for Open E2E Spoken Dialogue Systems
---

# Chain-of-Thought Training for Open E2E Spoken Dialogue Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00722" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00722v1</a>
  <a href="https://arxiv.org/pdf/2506.00722.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00722v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00722v1', 'Chain-of-Thought Training for Open E2E Spoken Dialogue Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siddhant Arora, Jinchuan Tian, Hayato Futami, Jee-weon Jung, Jiatong Shi, Yosuke Kashiwagi, Emiru Tsunoo, Shinji Watanabe

**分类**: cs.CL, cs.SD, eess.AS

**发布日期**: 2025-05-31

**备注**: Accepted at INTERSPEECH 2025

---

## 💡 一句话要点

**提出链式思维训练以提升开放式端到端对话系统的语义一致性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `端到端对话系统` `链式思维` `语音识别` `文本到语音合成` `多模态学习`

## 📋 核心要点

1. 现有的端到端对话系统在语义一致性和训练数据需求上存在明显不足，导致生成的响应质量不高。
2. 论文提出了一种链式思维训练策略，通过将对话数据训练与多模态语言模型的预训练相结合，提升了对话系统的性能。
3. 实验结果显示，该方法在ROUGE-1指标上较基线提升超过1.5，且仅需300小时的训练数据即可实现有效训练。

## 📝 摘要（中文）

与传统的级联管道不同，端到端（E2E）语音对话系统保持完全的可微分性，并捕捉非音素信息，使其更适合建模语音交互。然而，现有的E2E方法通常需要大规模训练数据，并生成缺乏语义一致性的响应。我们提出了一种简单而有效的策略，利用链式思维（CoT）形式，确保在对话数据上的训练与多模态语言模型（LM）在语音识别（ASR）、文本到语音合成（TTS）和文本LM任务上的预训练紧密对齐。我们的方法在基线之上实现了超过1.5的ROUGE-1提升，成功在公开的人类对话数据集上训练语音对话系统，同时计算效率足够高，仅需300小时的公开人类对话数据，如Switchboard。我们将公开发布我们的模型和训练代码。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有端到端对话系统在语义一致性和训练数据需求方面的不足，现有方法往往需要大量数据且生成的响应缺乏连贯性。

**核心思路**：提出链式思维（CoT）训练策略，通过将对话数据的训练与多模态语言模型的预训练相结合，确保训练过程中的语义一致性和信息完整性。

**技术框架**：整体架构包括数据预处理、链式思维训练模块和模型优化阶段，主要模块包括语音识别、文本到语音合成和文本语言模型的集成。

**关键创新**：最重要的创新点在于引入链式思维训练，使得对话系统的训练过程与多模态预训练紧密结合，从而提升了生成响应的语义一致性。

**关键设计**：在参数设置上，采用了适应性学习率和特定的损失函数，以优化模型在对话生成任务中的表现，同时使用了300小时的公开人类对话数据进行训练。

## 📊 实验亮点

实验结果表明，所提出的方法在ROUGE-1指标上较基线提升超过1.5，显示出显著的性能改进。此外，该方法仅需300小时的公开人类对话数据，展现出良好的计算效率和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、语音助手和人机交互系统等，能够有效提升对话系统的响应质量和用户体验。未来，该方法可能推动更自然的语音交互技术的发展，促进人机沟通的智能化和人性化。

## 📄 摘要（原文）

> Unlike traditional cascaded pipelines, end-to-end (E2E) spoken dialogue systems preserve full differentiability and capture non-phonemic information, making them well-suited for modeling spoken interactions. However, existing E2E approaches often require large-scale training data and generates responses lacking semantic coherence. We propose a simple yet effective strategy leveraging a chain-of-thought (CoT) formulation, ensuring that training on conversational data remains closely aligned with the multimodal language model (LM)'s pre-training on speech recognition~(ASR), text-to-speech synthesis (TTS), and text LM tasks. Our method achieves over 1.5 ROUGE-1 improvement over the baseline, successfully training spoken dialogue systems on publicly available human-human conversation datasets, while being compute-efficient enough to train on just 300 hours of public human-human conversation data, such as the Switchboard. We will publicly release our models and training code.

