---
layout: default
title: "Why LLM Safety Guardrails Collapse After Fine-tuning: A Similarity Analysis Between Alignment and Fine-tuning Datasets"
---

# Why LLM Safety Guardrails Collapse After Fine-tuning: A Similarity Analysis Between Alignment and Fine-tuning Datasets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05346" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05346v1</a>
  <a href="https://arxiv.org/pdf/2506.05346.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05346v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05346v1', 'Why LLM Safety Guardrails Collapse After Fine-tuning: A Similarity Analysis Between Alignment and Fine-tuning Datasets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lei Hsiung, Tianyu Pang, Yung-Chen Tang, Linyue Song, Tsung-Yi Ho, Pin-Yu Chen, Yaoqing Yang

**分类**: cs.CR, cs.CL, cs.LG

**发布日期**: 2025-06-05

**备注**: Project Page: https://hsiung.cc/llm-similarity-risk/

---

## 💡 一句话要点

**通过相似性分析提出新方法以增强LLM安全性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全对齐` `微调` `数据集设计` `相似性分析` `模型安全性` `有害性评分`

## 📋 核心要点

1. 现有的安全防护措施在微调后容易被攻击，缺乏有效的预防机制。
2. 论文提出通过分析上游对齐数据集与下游微调任务的相似性来增强安全防护。
3. 实验结果显示，低相似性数据集能显著提升模型的安全性，降低有害性评分。

## 📝 摘要（中文）

近期大型语言模型（LLMs）的进展揭示了其在安全对齐方面的脆弱性，尤其是在下游微调过程中。现有的缓解策略主要集中在事后应对安全防护措施被破坏的事件，或者在微调过程中去除有害梯度，或持续强化安全对齐。然而，这些方法往往忽视了一个关键的上游因素：原始安全对齐数据的作用。本文通过研究上游对齐数据集与下游微调任务之间的表示相似性，探讨了安全防护措施的退化。实验表明，这两种数据集之间的高相似性显著削弱了安全防护，使模型更易受到攻击。相反，低相似性则使模型更加稳健，降低有害性评分高达10.33%。这些发现强调了上游数据集设计在构建持久安全防护和减少现实世界攻击脆弱性中的重要性，为微调服务提供商提供了可行的见解。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在微调后安全防护措施的脆弱性，现有方法多集中于事后处理，未能有效预防潜在攻击。

**核心思路**：通过分析上游对齐数据集与下游微调任务之间的表示相似性，发现高相似性会削弱模型的安全性，从而提出优化数据集设计的策略。

**技术框架**：研究首先建立了对齐数据集与微调任务的相似性度量框架，然后通过实验验证不同相似性水平对模型安全性的影响，最后提出改进建议。

**关键创新**：论文的创新点在于首次系统性地将数据集相似性与模型安全性关联起来，揭示了上游数据集设计的重要性。

**关键设计**：在实验中，采用了多种相似性度量方法，设计了不同的对齐数据集和微调任务组合，以评估其对模型安全性的影响。

## 📊 实验亮点

实验结果表明，当上游对齐数据集与下游微调任务的相似性较低时，模型的有害性评分降低了高达10.33%。这一发现强调了数据集设计在提升模型安全性方面的重要性，为微调服务提供商提供了实用的指导。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能客服系统和自动内容生成等。通过优化数据集设计，可以有效提升模型的安全性，降低被攻击的风险，从而在实际应用中保护用户和系统的安全。

## 📄 摘要（原文）

> Recent advancements in large language models (LLMs) have underscored their vulnerability to safety alignment jailbreaks, particularly when subjected to downstream fine-tuning. However, existing mitigation strategies primarily focus on reactively addressing jailbreak incidents after safety guardrails have been compromised, removing harmful gradients during fine-tuning, or continuously reinforcing safety alignment throughout fine-tuning. As such, they tend to overlook a critical upstream factor: the role of the original safety-alignment data. This paper therefore investigates the degradation of safety guardrails through the lens of representation similarity between upstream alignment datasets and downstream fine-tuning tasks. Our experiments demonstrate that high similarity between these datasets significantly weakens safety guardrails, making models more susceptible to jailbreaks. Conversely, low similarity between these two types of datasets yields substantially more robust models and thus reduces harmfulness score by up to 10.33%. By highlighting the importance of upstream dataset design in the building of durable safety guardrails and reducing real-world vulnerability to jailbreak attacks, these findings offer actionable insights for fine-tuning service providers.

