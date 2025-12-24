---
layout: default
title: Concept-Level Explainability for Auditing & Steering LLM Responses
---

# Concept-Level Explainability for Auditing & Steering LLM Responses

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07610" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07610v2</a>
  <a href="https://arxiv.org/pdf/2505.07610.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07610v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07610v2', 'Concept-Level Explainability for Auditing & Steering LLM Responses')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kenza Amara, Rita Sevastjanova, Mennatallah El-Assady

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-12 (更新: 2025-05-19)

**备注**: 9 pages, 7 figures, Submission to Neurips 2025

---

## 💡 一句话要点

**提出ConceptX以解决大语言模型响应的可解释性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `可解释性` `概念级归因` `偏见审计` `模型引导` `自然语言处理` `安全性`

## 📋 核心要点

1. 现有的token级归因方法在文本生成中难以解释输出的整体语义，导致对模型行为的理解不足。
2. ConceptX通过识别提示中的语义丰富token，并根据输出的语义相似性为其分配重要性，从而提供概念级的可解释性。
3. 实验结果表明，ConceptX在情感转变和攻击成功率方面显著优于随机编辑和其他基线方法，提升幅度明显。

## 📝 摘要（中文）

随着大语言模型（LLMs）的广泛应用，关于其安全性和对齐性的问题日益突出。为引导LLM行为，如减轻偏见或防范越狱攻击，识别提示中影响模型输出的部分至关重要。现有的基于token的归因方法在文本生成中仍面临挑战，无法解释输出中每个token的存在，而是关注整个LLM响应的语义。本文提出了ConceptX，这是一种模型无关的概念级可解释性方法，能够识别提示中的语义丰富token，并根据输出的语义相似性为其分配重要性。与现有的token级方法不同，ConceptX还通过就地token替换来保持上下文完整性，并支持灵活的解释目标，如性别偏见。ConceptX不仅能揭示偏见来源，还能通过修改提示来改变情感或减少LLM响应的有害性，而无需重新训练。在三种LLM上，ConceptX在忠实性和人类对齐性方面均优于TokenSHAP等token级方法。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型响应的可解释性问题，现有的token级归因方法无法有效解释文本生成的整体语义，导致对模型输出的理解不足。

**核心思路**：ConceptX通过识别提示中的语义丰富token，并根据输出的语义相似性为其分配重要性，提供了一种新的可解释性方法，能够保持上下文完整性并支持灵活的解释目标。

**技术框架**：ConceptX的整体架构包括三个主要模块：1) 概念识别，2) 重要性分配，3) 上下文保持。通过这些模块，ConceptX能够有效分析和修改提示。

**关键创新**：ConceptX的主要创新在于其概念级的可解释性，与现有的token级方法相比，能够更好地捕捉输出的语义，并支持灵活的解释目标。

**关键设计**：在设计中，ConceptX采用了就地token替换的方法，确保上下文的完整性，同时在重要性分配中使用了语义相似性度量，以提高解释的准确性和有效性。

## 📊 实验亮点

实验结果显示，ConceptX在情感转变任务中提升了0.252，相较于随机编辑的0.131，且在攻击成功率方面从0.463降低至0.242，显著优于归因和改写基线，展示了其在可解释性和引导性方面的优势。

## 🎯 应用场景

ConceptX的潜在应用领域包括自然语言处理中的偏见审计、模型行为引导和安全性增强等。通过提供透明的可解释性，ConceptX能够帮助开发者更好地理解和控制大语言模型的输出，从而提高其安全性和对齐性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> As large language models (LLMs) become widely deployed, concerns about their safety and alignment grow. An approach to steer LLM behavior, such as mitigating biases or defending against jailbreaks, is to identify which parts of a prompt influence specific aspects of the model's output. Token-level attribution methods offer a promising solution, but still struggle in text generation, explaining the presence of each token in the output separately, rather than the underlying semantics of the entire LLM response. We introduce ConceptX, a model-agnostic, concept-level explainability method that identifies the concepts, i.e., semantically rich tokens in the prompt, and assigns them importance based on the outputs' semantic similarity. Unlike current token-level methods, ConceptX also offers to preserve context integrity through in-place token replacements and supports flexible explanation goals, e.g., gender bias. ConceptX enables both auditing, by uncovering sources of bias, and steering, by modifying prompts to shift the sentiment or reduce the harmfulness of LLM responses, without requiring retraining. Across three LLMs, ConceptX outperforms token-level methods like TokenSHAP in both faithfulness and human alignment. Steering tasks boost sentiment shift by 0.252 versus 0.131 for random edits and lower attack success rates from 0.463 to 0.242, outperforming attribution and paraphrasing baselines. While prompt engineering and self-explaining methods sometimes yield safer responses, ConceptX offers a transparent and faithful alternative for improving LLM safety and alignment, demonstrating the practical value of attribution-based explainability in guiding LLM behavior.

