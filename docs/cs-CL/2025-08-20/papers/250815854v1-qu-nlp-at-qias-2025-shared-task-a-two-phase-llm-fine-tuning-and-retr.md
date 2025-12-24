---
layout: default
title: "QU-NLP at QIAS 2025 Shared Task: A Two-Phase LLM Fine-Tuning and Retrieval-Augmented Generation Approach for Islamic Inheritance Reasoning"
---

# QU-NLP at QIAS 2025 Shared Task: A Two-Phase LLM Fine-Tuning and Retrieval-Augmented Generation Approach for Islamic Inheritance Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15854" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15854v1</a>
  <a href="https://arxiv.org/pdf/2508.15854.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15854v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15854v1', 'QU-NLP at QIAS 2025 Shared Task: A Two-Phase LLM Fine-Tuning and Retrieval-Augmented Generation Approach for Islamic Inheritance Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammad AL-Smadi

**分类**: cs.CL

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出基于RAG的LLM微调方法以解决伊斯兰继承推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `伊斯兰继承推理` `大语言模型` `微调` `检索增强生成` `低秩适应` `模型评估` `阿拉伯语处理`

## 📋 核心要点

1. 现有方法在处理伊斯兰继承法的复杂性时面临挑战，尤其是在理解继承场景和进行精确计算方面。
2. 论文提出了一种基于RAG的微调方法，通过LoRA对Fanar-1-9B模型进行优化，以增强其在特定领域的推理能力。
3. 实验结果显示，QU-NLP在最终测试中取得了85.8%的准确率，尤其在高级推理任务中表现优异，达到了97.6%的准确率。

## 📝 摘要（中文）

本文介绍了我们在QIAS 2025共享任务中针对伊斯兰继承推理的解决方案与结果。我们采用低秩适应（LoRA）对Fanar-1-9B因果语言模型进行了微调，并将其集成到检索增强生成（RAG）管道中。该系统能够处理伊斯兰继承法的复杂性，包括理解继承场景、识别合格继承人、应用固定份额规则及进行精确计算。最终测试中，我们的系统达到了0.858的准确率，超越了GPT 4.5、LLaMA等竞争模型，尤其在高级推理方面表现突出，达到了97.6%的准确率。这表明领域特定的微调结合检索基础能够使中型阿拉伯LLM在伊斯兰继承推理中超越前沿模型。

## 🔬 方法详解

**问题定义**：本文旨在解决伊斯兰继承推理中的复杂问题，现有方法在理解继承场景、识别合格继承人及进行精确计算时存在不足。

**核心思路**：我们通过对Fanar-1-9B模型进行低秩适应（LoRA）微调，并结合检索增强生成（RAG）技术，提升模型在特定领域的推理能力。

**技术框架**：整体架构包括两个主要阶段：首先是对Fanar-1-9B模型进行微调，随后将其集成到RAG管道中，以便在推理过程中利用外部知识库。

**关键创新**：本研究的创新点在于结合领域特定的微调与检索增强技术，使得中型阿拉伯LLM在处理伊斯兰继承推理时超越了现有的前沿模型。

**关键设计**：在模型微调过程中，采用了特定的损失函数和参数设置，以确保模型能够有效学习伊斯兰继承法的规则和逻辑。

## 📊 实验亮点

实验结果显示，QU-NLP在最终测试中达到了85.8%的准确率，尤其在高级推理任务中表现突出，准确率高达97.6%。这一结果显著超越了GPT 4.5、LLaMA等竞争模型，展示了领域特定微调的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括法律咨询、教育和智能问答系统，尤其是在涉及伊斯兰法的场景中。通过提升模型的推理能力，能够为用户提供更准确的法律建议和信息，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> This paper presents our approach and results for SubTask 1: Islamic Inheritance Reasoning at QIAS 2025, a shared task focused on evaluating Large Language Models (LLMs) in understanding and reasoning within Islamic inheritance knowledge. We fine-tuned the Fanar-1-9B causal language model using Low-Rank Adaptation (LoRA) and integrated it into a Retrieval-Augmented Generation (RAG) pipeline. Our system addresses the complexities of Islamic inheritance law, including comprehending inheritance scenarios, identifying eligible heirs, applying fixed-share rules, and performing precise calculations. Our system achieved an accuracy of 0.858 in the final test, outperforming other competitive models such as, GPT 4.5, LLaMA, Fanar, Mistral and ALLaM evaluated with zero-shot prompting. Our results demonstrate that QU-NLP achieves near state-of-the-art accuracy (85.8%), excelling especially on advanced reasoning (97.6%) where it outperforms Gemini 2.5 and OpenAI's o3. This highlights that domain-specific fine-tuning combined with retrieval grounding enables mid-scale Arabic LLMs to surpass frontier models in Islamic inheritance reasoning.

