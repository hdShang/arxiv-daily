---
layout: default
title: "One Tokenizer To Rule Them All: Emergent Language Plasticity via Multilingual Tokenizers"
---

# One Tokenizer To Rule Them All: Emergent Language Plasticity via Multilingual Tokenizers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10766" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10766v1</a>
  <a href="https://arxiv.org/pdf/2506.10766.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10766v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10766v1', 'One Tokenizer To Rule Them All: Emergent Language Plasticity via Multilingual Tokenizers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Diana Abagyan, Alejandro R. Salamanca, Andres Felipe Cruz-Salinas, Kris Cao, Hangyu Lin, Acyr Locatelli, Marzieh Fadaee, Ahmet Üstün, Sara Hooker

**分类**: cs.CL

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出通用分词器以提升多语言模型的适应能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言模型` `通用分词器` `语言适应性` `预训练` `自然语言处理`

## 📋 核心要点

1. 现有多语言模型在预训练阶段面临容量、数据和计算资源的限制，导致语言适应性不足。
2. 本文提出使用通用分词器，旨在通过训练更多语言来提升模型对新语言的适应能力。
3. 实验结果显示，通用分词器在语言适应性上提升显著，赢率提升高达20.2%，且对未见语言的适应性也有所提高。

## 📝 摘要（中文）

在预训练大规模多语言大型语言模型（LLMs）时，由于模型容量有限、高质量数据稀缺以及计算资源受限，面临诸多挑战。此外，分词器的语言覆盖不足使得在训练后阶段难以解决新语言的适应问题。本文研究了在训练早期进行相对廉价的干预，以提高模型在训练后对新语言的适应能力。我们提出使用一个通用分词器，该分词器针对比主要预训练语言更多的语言进行训练，从而在预训练后有效扩展语言覆盖。通过对不同语言组和训练策略的系统实验，结果表明，通用分词器显著提高了语言适应性，赢率提升高达20.2%。此外，通用分词器对完全未见过的语言也表现出更好的适应性，赢率提升可达5%。

## 🔬 方法详解

**问题定义**：本文旨在解决多语言大型语言模型在预训练阶段对新语言适应能力不足的问题。现有方法由于分词器的语言覆盖限制，难以在训练后有效适应新语言。

**核心思路**：我们提出设计一个通用分词器，该分词器针对比主要预训练语言更多的语言进行训练，以提高模型在预训练后对新语言的适应能力。这样的设计能够在不显著影响已有语言性能的情况下，扩展模型的语言覆盖范围。

**技术框架**：整体架构包括通用分词器的设计与训练、模型的预训练以及后续的语言适应性测试。主要模块包括分词器训练模块、模型预训练模块和适应性评估模块。

**关键创新**：最重要的创新在于提出了通用分词器的概念，并通过系统实验验证了其在语言适应性上的显著提升，与传统的特定语言分词器相比，通用分词器在适应新语言时表现出更高的灵活性。

**关键设计**：在设计通用分词器时，考虑了多种语言的特征，采用了适应性损失函数和多语言训练策略，以确保模型在不同语言上的性能平衡。

## 📊 实验亮点

实验结果显示，使用通用分词器的模型在语言适应性上显著提高，赢率相比于特定语言分词器提升高达20.2%。此外，对完全未见过的语言，通用分词器也表现出5%的赢率增益，表明其在语言适应性方面的优势。

## 🎯 应用场景

该研究的潜在应用领域包括多语言翻译、跨语言信息检索和全球化的自然语言处理应用。通过提升模型的语言适应能力，可以更好地服务于多语言用户，促进不同语言之间的交流与理解，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Pretraining massively multilingual Large Language Models (LLMs) for many languages at once is challenging due to limited model capacity, scarce high-quality data, and compute constraints. Moreover, the lack of language coverage of the tokenizer makes it harder to address the gap for new languages purely at the post-training stage. In this work, we study what relatively cheap interventions early on in training improve "language plasticity", or adaptation capabilities of the model post-training to new languages. We focus on tokenizer design and propose using a universal tokenizer that is trained for more languages than the primary pretraining languages to enable efficient adaptation in expanding language coverage after pretraining. Our systematic experiments across diverse groups of languages and different training strategies show that a universal tokenizer enables significantly higher language adaptation, with up to 20.2% increase in win rates compared to tokenizers specific to pretraining languages. Furthermore, a universal tokenizer also leads to better plasticity towards languages that are completely unseen in the tokenizer and pretraining, by up to 5% win rate gain. We achieve this adaptation to an expanded set of languages with minimal compromise in performance on the majority of languages included in pretraining.

