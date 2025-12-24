---
layout: default
title: "PBa-LLM: Privacy- and Bias-aware NLP using Named-Entity Recognition (NER)"
---

# PBa-LLM: Privacy- and Bias-aware NLP using Named-Entity Recognition (NER)

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.02966" class="toolbar-btn" target="_blank">📄 arXiv: 2507.02966v2</a>
  <a href="https://arxiv.org/pdf/2507.02966.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.02966v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.02966v2', 'PBa-LLM: Privacy- and Bias-aware NLP using Named-Entity Recognition (NER)')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gonzalo Mancera, Aythami Morales, Julian Fierrez, Ruben Tolosana, Alejandro Penna, Miguel Lopez-Duran, Francisco Jurado, Alvaro Ortigosa

**分类**: cs.CL, cs.AI, cs.CR, cs.LG

**发布日期**: 2025-06-30 (更新: 2025-07-09)

**备注**: Presented at AAAI Workshop on Privacy-Preserving Artificial Intelligence (PPAI) 2025, Philadelphia, PA, USA, March 2025

---

## 💡 一句话要点

**提出PBa-LLM以解决隐私与偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐私保护` `命名实体识别` `大型语言模型` `数据偏见` `招聘系统` `AI伦理` `自然语言处理`

## 📋 核心要点

1. 现有的LLMs在隐私保护和数据偏见方面存在法律和伦理挑战，尤其是在高风险应用中。
2. 本文提出了一种利用NER技术进行敏感信息匿名化的框架，以实现LLMs的隐私保护训练。
3. 实验结果显示，所提出的隐私保护技术在简历评分任务中有效维护了系统性能，同时保护了候选人隐私。

## 📝 摘要（中文）

近年来，自然语言处理（NLP）在高风险AI应用中的使用显著增加，尤其是大型语言模型（LLMs）的出现。然而，LLMs引发了重要的法律和伦理问题，特别是在隐私、数据保护和透明度方面。本文探讨了使用命名实体识别（NER）技术来促进LLMs的隐私保护训练。我们提出了一个框架，利用NER技术对文本数据中的敏感信息进行匿名化处理。通过对AI招聘过程中简历评分的实验评估，结果表明所提出的隐私保护技术在维护系统性能的同时，有效保护了候选人的机密性，增强了信任。此外，我们还应用了一种现有方法来减少LLMs中的性别偏见，最终提出了隐私与偏见意识的LLMs（PBa-LLMs）。

## 🔬 方法详解

**问题定义**：本文旨在解决LLMs在高风险应用中面临的隐私保护和数据偏见问题。现有方法在处理敏感信息时常常忽视隐私保护，导致法律和伦理风险。

**核心思路**：论文提出通过命名实体识别（NER）技术对文本数据进行匿名化处理，从而在训练过程中保护用户隐私，同时结合现有的减少性别偏见的方法，形成PBa-LLMs。

**技术框架**：整体架构包括数据预处理、NER技术应用、隐私保护训练和偏见减少模块。具体流程为：首先对文本数据进行NER处理，识别并匿名化敏感信息，然后使用处理后的数据进行LLMs的训练。

**关键创新**：最重要的创新在于结合NER技术与隐私保护训练，确保在不损失系统性能的情况下有效保护用户隐私。这一方法与传统的隐私保护技术相比，具有更高的适应性和有效性。

**关键设计**：在实验中使用了BERT和RoBERTa两种语言模型，结合六种匿名化算法，参数设置经过优化以确保在隐私保护与模型性能之间取得平衡。

## 📊 实验亮点

实验结果表明，所提出的隐私保护技术在简历评分任务中有效保持了系统性能，且在保护候选人隐私方面表现出色。具体而言，在使用NER技术后，模型的准确率与基线模型相当，且隐私保护措施显著提升了用户信任度。

## 🎯 应用场景

该研究的潜在应用领域包括招聘、金融、医疗等高风险行业，能够有效保护用户隐私并减少数据偏见，提升AI系统的透明度和信任度。未来，该方法可推广至其他基于LLM的AI应用，促进更广泛的隐私保护和公平性。

## 📄 摘要（原文）

> The use of Natural Language Processing (NLP) in highstakes AI-based applications has increased significantly in recent years, especially since the emergence of Large Language Models (LLMs). However, despite their strong performance, LLMs introduce important legal/ ethical concerns, particularly regarding privacy, data protection, and transparency. Due to these concerns, this work explores the use of Named- Entity Recognition (NER) to facilitate the privacy-preserving training (or adaptation) of LLMs. We propose a framework that uses NER technologies to anonymize sensitive information in text data, such as personal identities or geographic locations. An evaluation of the proposed privacy-preserving learning framework was conducted to measure its impact on user privacy and system performance in a particular high-stakes and sensitive setup: AI-based resume scoring for recruitment processes. The study involved two language models (BERT and RoBERTa) and six anonymization algorithms (based on Presidio, FLAIR, BERT, and different versions of GPT) applied to a database of 24,000 candidate profiles. The findings indicate that the proposed privacy preservation techniques effectively maintain system performance while playing a critical role in safeguarding candidate confidentiality, thus promoting trust in the experimented scenario. On top of the proposed privacy-preserving approach, we also experiment applying an existing approach that reduces the gender bias in LLMs, thus finally obtaining our proposed Privacyand Bias-aware LLMs (PBa-LLMs). Note that the proposed PBa-LLMs have been evaluated in a particular setup (resume scoring), but are generally applicable to any other LLM-based AI application.

