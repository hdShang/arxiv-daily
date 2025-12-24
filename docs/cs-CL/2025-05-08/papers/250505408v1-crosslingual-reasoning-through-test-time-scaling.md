---
layout: default
title: Crosslingual Reasoning through Test-Time Scaling
---

# Crosslingual Reasoning through Test-Time Scaling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05408" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05408v1</a>
  <a href="https://arxiv.org/pdf/2505.05408.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05408v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05408v1', 'Crosslingual Reasoning through Test-Time Scaling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zheng-Xin Yong, M. Farid Adilazuarda, Jonibek Mansurov, Ruochen Zhang, Niklas Muennighoff, Carsten Eickhoff, Genta Indra Winata, Julia Kreutzer, Stephen H. Bach, Alham Fikri Aji

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-08

---

## 💡 一句话要点

**通过测试时扩展实现跨语言推理能力提升**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跨语言推理` `长链思维` `多语言模型` `推理计算资源` `低资源语言` `领域外推理` `数学推理`

## 📋 核心要点

1. 现有的大型语言模型推理能力主要集中在英语，导致多语言推理能力不足，尤其是在低资源语言中。
2. 本文提出通过增加推理计算资源和控制长链思维的语言来提升多语言推理能力，尤其是在高资源语言中。
3. 实验结果表明，英语中心的推理模型在多语言数学推理中表现优异，且在高资源语言中推理效率更高。

## 📝 摘要（中文）

大型语言模型的推理能力主要集中在英语上，尽管这些模型是多语言预训练的。本文研究了英语推理微调如何通过长链思维（CoTs）在多语言中进行推广。研究发现，增加推理计算资源可以显著提升多语言数学推理能力，尤其是在低资源语言中。此外，虽然英语模型的CoTs主要为英语，但在处理非英语输入时，它们依然遵循引用与思考的模式。最后，研究表明高资源语言的推理效果更佳，而在领域外推理方面表现不佳，尤其是从STEM到文化常识知识的迁移。总的来说，本文展示了英语推理在测试时扩展的潜力、机制及局限性。

## 🔬 方法详解

**问题定义**：本文旨在解决英语推理模型在多语言推理中的局限性，尤其是在低资源语言和领域外知识的推理能力不足的问题。

**核心思路**：通过增加推理计算资源和优化长链思维的语言控制，提升模型在多语言环境中的推理能力，尤其是高资源语言的表现。

**技术框架**：研究采用了英语中心的推理语言模型，分为推理计算资源扩展、长链思维语言控制和多语言推理能力评估三个主要模块。

**关键创新**：提出了在推理时扩展计算资源的策略，使得英语推理模型在多语言推理中表现超越其规模更大的模型，尤其是在低资源语言上。

**关键设计**：在模型训练中，采用了特定的损失函数和参数设置，以优化长链思维的语言控制，确保模型在处理非英语输入时依然保持高效的推理能力。

## 📊 实验亮点

实验结果显示，增加推理计算资源后，英语中心的推理模型在多语言数学推理中表现优于规模更大的模型，尤其是在低资源语言中，推理能力提升显著。具体而言，模型在高资源语言中的推理效率更高，展现出良好的跨语言推广能力。

## 🎯 应用场景

该研究的潜在应用领域包括多语言教育、跨文化交流和国际化产品开发。通过提升多语言推理能力，能够更好地服务于全球用户，促进不同语言之间的理解与合作。未来，随着低资源语言推理能力的提升，模型的应用范围将进一步扩大。

## 📄 摘要（原文）

> Reasoning capabilities of large language models are primarily studied for English, even when pretrained models are multilingual. In this work, we investigate to what extent English reasoning finetuning with long chain-of-thoughts (CoTs) can generalize across languages. First, we find that scaling up inference compute for English-centric reasoning language models (RLMs) improves multilingual mathematical reasoning across many languages including low-resource languages, to an extent where they outperform models twice their size. Second, we reveal that while English-centric RLM's CoTs are naturally predominantly English, they consistently follow a quote-and-think pattern to reason about quoted non-English inputs. Third, we discover an effective strategy to control the language of long CoT reasoning, and we observe that models reason better and more efficiently in high-resource languages. Finally, we observe poor out-of-domain reasoning generalization, in particular from STEM to cultural commonsense knowledge, even for English. Overall, we demonstrate the potentials, study the mechanisms and outline the limitations of crosslingual generalization of English reasoning test-time scaling. We conclude that practitioners should let English-centric RLMs reason in high-resource languages, while further work is needed to improve reasoning in low-resource languages and out-of-domain contexts.

