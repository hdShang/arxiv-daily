---
layout: default
title: "High Accuracy, Less Talk (HALT): Reliable LLMs through Capability-Aligned Finetuning"
---

# High Accuracy, Less Talk (HALT): Reliable LLMs through Capability-Aligned Finetuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04051" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04051v1</a>
  <a href="https://arxiv.org/pdf/2506.04051.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04051v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04051v1', 'High Accuracy, Less Talk (HALT): Reliable LLMs through Capability-Aligned Finetuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tim Franzmeyer, Archie Sravankumar, Lijuan Liu, Yuning Mao, Rui Hou, Sinong Wang, Jakob N. Foerster, Luke Zettlemoyer, Madian Khabsa

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-04

---

## 💡 一句话要点

**提出HALT方法以解决大语言模型的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `后训练` `能力对齐` `幻觉问题` `响应可靠性` `微调` `数据生成` `模型优化`

## 📋 核心要点

1. 现有的大语言模型在缺乏知识时容易产生错误回答，导致幻觉现象，影响其可靠性。
2. HALT方法通过生成能力对齐的后训练数据，使模型在不确定时选择部分放弃回答，从而提高生成内容的可靠性。
3. 在四个领域的实验中，HALT使得模型的片段正确性平均提高15%，F1分数提升4%，并显著提高了模型的整体可靠性。

## 📝 摘要（中文）

当前的大语言模型（LLMs）在面对每个提示时都会给出回应，但在缺乏知识或能力时可能产生错误答案，这一现象被称为幻觉。本文提出了一种后训练方法HALT，使得LLM在对其生成内容有信心时才进行回应，否则部分放弃。HALT通过将预训练LLM的响应分割为事实片段，并利用真实信息识别不正确的片段，从而生成能力对齐的后训练数据。通过调整阈值，HALT能够在响应完整性和片段正确性之间进行权衡。实验表明，HALT在四个领域的平均片段正确性提高了15%，F1分数提升了4%。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在面对不确定性时产生错误回答的问题。现有方法未能有效处理模型的幻觉现象，导致生成内容的可靠性不足。

**核心思路**：HALT方法通过后训练使模型在对生成内容有信心时才进行回应，避免在不确定时产生错误回答。具体而言，HALT生成的能力对齐数据能够明确模型可以和不可以可靠生成的内容。

**技术框架**：HALT的整体流程包括将预训练LLM的响应分割为事实片段，利用真实信息识别不正确片段，并通过调整阈值来决定是删除错误片段还是替换为“Unsure from Here”。

**关键创新**：HALT的创新在于其能力对齐的后训练数据生成方式，能够有效减少模型在不确定情况下的错误回答，与传统方法相比，显著提高了生成内容的可靠性。

**关键设计**：在实现过程中，HALT允许用户根据需求调整阈值，以在响应完整性和片段正确性之间进行权衡。此外，模型在四个不同领域的微调过程中，针对每个领域设定了不同的阈值，以优化性能。

## 📊 实验亮点

实验结果显示，HALT方法在四个领域的平均片段正确性提高了15%，F1分数提升了4%。通过针对最高正确性进行微调，Llama3-70B模型的正确性从51%提升至87%，同时保持了53%的响应完整性，展现了显著的性能提升。

## 🎯 应用场景

HALT方法具有广泛的应用潜力，尤其在需要高可靠性的领域，如医疗、法律和教育等。通过提高大语言模型的回答准确性，HALT能够为用户提供更可信的生成内容，减少错误信息的传播，提升用户体验。未来，该方法还可以扩展到其他领域，进一步增强模型的智能化水平。

## 📄 摘要（原文）

> Large Language Models (LLMs) currently respond to every prompt. However, they can produce incorrect answers when they lack knowledge or capability -- a problem known as hallucination. We instead propose post-training an LLM to generate content only when confident in its correctness and to otherwise (partially) abstain. Specifically, our method, HALT, produces capability-aligned post-training data that encodes what the model can and cannot reliably generate. We generate this data by splitting responses of the pretrained LLM into factual fragments (atomic statements or reasoning steps), and use ground truth information to identify incorrect fragments. We achieve capability-aligned finetuning responses by either removing incorrect fragments or replacing them with "Unsure from Here" -- according to a tunable threshold that allows practitioners to trade off response completeness and mean correctness of the response's fragments. We finetune four open-source models for biography writing, mathematics, coding, and medicine with HALT for three different trade-off thresholds. HALT effectively trades off response completeness for correctness, increasing the mean correctness of response fragments by 15% on average, while resulting in a 4% improvement in the F1 score (mean of completeness and correctness of the response) compared to the relevant baselines. By tuning HALT for highest correctness, we train a single reliable Llama3-70B model with correctness increased from 51% to 87% across all four domains while maintaining 53% of the response completeness achieved with standard finetuning.

