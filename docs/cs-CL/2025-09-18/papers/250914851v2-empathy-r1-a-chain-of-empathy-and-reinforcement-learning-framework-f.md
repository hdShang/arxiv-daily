---
layout: default
title: "Empathy-R1: A Chain-of-Empathy and Reinforcement Learning Framework for Long-Form Mental Health Support"
---

# Empathy-R1: A Chain-of-Empathy and Reinforcement Learning Framework for Long-Form Mental Health Support

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14851" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14851v2</a>
  <a href="https://arxiv.org/pdf/2509.14851.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14851v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14851v2', 'Empathy-R1: A Chain-of-Empathy and Reinforcement Learning Framework for Long-Form Mental Health Support')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianrong Yao, Dong She, Chenxu Zhang, Yimeng Zhang, Yueru Sun, Noman Ahmed, Yang Gao, Zhanpeng Jin

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-18 (更新: 2025-09-19)

---

## 💡 一句话要点

**Empathy-R1：基于同理心链和强化学习的长文本心理健康支持框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心理健康支持` `同理心链` `强化学习` `长文本咨询` `认知行为疗法`

## 📋 核心要点

1. 现有大语言模型在心理健康支持中缺乏结构化推理，难以提供真正有益的回复，尤其是在中文语境下。
2. 提出Empathy-R1框架，结合同理心链（CoE）推理和强化学习，提升模型在长文本咨询中的回复质量。
3. 实验表明，Empathy-R1在自动指标和人工评估中均表现出色，Win@1率达到44.30%，优于现有基线。

## 📝 摘要（中文）

本文提出Empathy-R1，一个新颖的框架，它整合了同理心链（CoE）推理过程与强化学习（RL），以提高长篇咨询文本（LCTs）的回复质量。受认知行为疗法启发，CoE范式引导模型按顺序推理求助者的情绪、原因和意图，使其思维过程透明且可解释。该框架基于一个新的大型中文数据集Empathy-QA和一个两阶段训练过程。首先，有监督微调灌输CoE的推理结构。随后，在专用奖励模型的指导下，RL优化最终回复的治疗相关性和上下文适当性。实验表明，Empathy-R1在关键自动指标上表现出色。更重要的是，人工评估证实了其优越性，表明其明显优于强大的基线，并在我们的新基准测试中实现了44.30%的Win@1率。通过实现可解释和上下文细致的回复，Empathy-R1代表了在开发负责任且真正有益于心理健康支持的AI方面的一个重大进步。

## 🔬 方法详解

**问题定义**：现有的大语言模型（LLMs）在处理长篇咨询文本（LCTs）时，虽然能够生成语义流畅的回复，但缺乏结构化的推理能力，难以提供真正具有心理治疗价值的支持。尤其是在中文语境下，这种不足更为明显。现有的方法难以准确捕捉求助者的情绪、原因和意图，导致回复缺乏同理心和针对性。

**核心思路**：Empathy-R1的核心思路是模仿认知行为疗法（CBT）的流程，通过同理心链（Chain-of-Empathy, CoE）引导模型进行结构化推理。CoE范式要求模型按顺序分析求助者的情绪、导致情绪的原因以及潜在的意图，从而使模型的思考过程更加透明和可解释。此外，利用强化学习（RL）进一步优化回复的治疗相关性和上下文适当性。

**技术框架**：Empathy-R1框架包含以下主要模块和阶段：1) **Empathy-QA数据集**：构建一个新的大型中文数据集，用于训练和评估模型。2) **同理心链（CoE）推理**：设计CoE范式，指导模型进行结构化推理。3) **两阶段训练**：首先，使用有监督微调（SFT）在Empathy-QA数据集上训练模型，使其具备CoE的推理能力。然后，使用强化学习（RL）进一步优化模型的回复质量。4) **奖励模型**：训练一个奖励模型，用于评估模型回复的治疗相关性和上下文适当性，并作为RL的指导信号。

**关键创新**：Empathy-R1的关键创新在于将同理心链（CoE）推理与强化学习相结合，用于提升长文本心理健康支持的质量。CoE范式使得模型的推理过程更加透明和可解释，而强化学习则能够进一步优化回复的治疗效果。与现有方法相比，Empathy-R1能够生成更具同理心、更具针对性和更有效的回复。

**关键设计**：Empathy-R1的关键设计包括：1) **CoE提示词设计**：设计合适的提示词，引导模型按顺序推理求助者的情绪、原因和意图。2) **奖励函数设计**：设计合适的奖励函数，用于评估模型回复的治疗相关性和上下文适当性。奖励函数可以结合人工评估和自动指标。3) **强化学习算法选择**：选择合适的强化学习算法，例如PPO或DQN，用于优化模型的回复策略。4) **数据集构建**：Empathy-QA数据集包含大量的长篇咨询文本和相应的CoE推理过程，用于训练和评估模型。

## 📊 实验亮点

Empathy-R1在Empathy-QA数据集上进行了实验，结果表明其在关键自动指标上表现出色。更重要的是，人工评估证实了其优越性，表明其明显优于强大的基线，并在新基准测试中实现了44.30%的Win@1率。这表明Empathy-R1能够生成更具同理心、更具针对性和更有效的回复。

## 🎯 应用场景

Empathy-R1具有广泛的应用前景，可用于构建智能心理健康支持系统，为用户提供个性化的心理咨询和支持。该技术可以应用于在线咨询平台、心理健康App等，帮助缓解心理健康资源不足的问题，提高心理健康服务的可及性和效率。未来，Empathy-R1有望成为心理健康领域的重要辅助工具。

## 📄 摘要（原文）

> Empathy is critical for effective mental health support, especially when addressing Long Counseling Texts (LCTs). However, existing Large Language Models (LLMs) often generate replies that are semantically fluent but lack the structured reasoning necessary for genuine psychological support, particularly in a Chinese context. To bridge this gap, we introduce Empathy-R1, a novel framework that integrates a Chain-of-Empathy (CoE) reasoning process with Reinforcement Learning (RL) to enhance response quality for LCTs. Inspired by cognitive-behavioral therapy, our CoE paradigm guides the model to sequentially reason about a help-seeker's emotions, causes, and intentions, making its thinking process both transparent and interpretable. Our framework is empowered by a new large-scale Chinese dataset, Empathy-QA, and a two-stage training process. First, Supervised Fine-Tuning instills the CoE's reasoning structure. Subsequently, RL, guided by a dedicated reward model, refines the therapeutic relevance and contextual appropriateness of the final responses. Experiments show that Empathy-R1 achieves strong performance on key automatic metrics. More importantly, human evaluations confirm its superiority, showing a clear preference over strong baselines and achieving a Win@1 rate of 44.30% on our new benchmark. By enabling interpretable and contextually nuanced responses, Empathy-R1 represents a significant advancement in developing responsible and genuinely beneficial AI for mental health support.

