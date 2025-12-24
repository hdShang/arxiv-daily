---
layout: default
title: "Introducing OmniGEC: A Silver Multilingual Dataset for Grammatical Error Correction"
---

# Introducing OmniGEC: A Silver Multilingual Dataset for Grammatical Error Correction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14504" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14504v1</a>
  <a href="https://arxiv.org/pdf/2509.14504.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14504v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14504v1', 'Introducing OmniGEC: A Silver Multilingual Dataset for Grammatical Error Correction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Roman Kovalchuk, Mariana Romanyshyn, Petro Ivaniuk

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-18

**期刊**: Proceedings of the Fourth Ukrainian Natural Language Processing Workshop (UNLP 2025)

**DOI**: [10.18653/v1/2025.unlp-1](https://doi.org/10.18653/v1/2025.unlp-1)

---

## 💡 一句话要点

**OmniGEC：提出多语言语法纠错的银标准数据集，促进跨语言GEC模型发展**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语法纠错` `多语言` `数据集` `大型语言模型` `银标准数据`

## 📋 核心要点

1. 现有的语法纠错（GEC）方法在多语言环境下面临数据稀缺的挑战，阻碍了跨语言GEC模型的发展。
2. OmniGEC通过收集和处理多种来源的多语言数据，构建了一个银标准数据集，为多语言GEC提供了宝贵资源。
3. 通过在OmniGEC上微调大型语言模型，Aya-Expanse和Gemma-3在段落级多语言GEC任务上取得了SOTA结果。

## 📝 摘要（中文）

本文介绍了OmniGEC，一个用于语法纠错（GEC）的多语言银标准数据集集合，涵盖11种语言：捷克语、英语、爱沙尼亚语、德语、希腊语、冰岛语、意大利语、拉脱维亚语、斯洛文尼亚语、瑞典语和乌克兰语。这些数据集有助于开发多语言GEC解决方案，并弥合了将英语GEC解决方案适配到多语言GEC中的数据缺口。数据集中的文本来源于三个方面：11种目标语言的维基百科编辑、Reddit的子版块以及仅限乌克兰语的UberText 2.0社交媒体语料库。维基百科编辑源于人工校正，而Reddit和UberText 2.0数据则使用GPT-4o-mini模型自动校正。对数据集中校正的质量进行了自动和手动评估。最后，我们在多语言OmniGEC语料库上微调了两个开源大型语言模型——Aya-Expanse (8B) 和 Gemma-3 (12B)，并在段落级多语言GEC中取得了最先进（SOTA）的结果。数据集集合和性能最佳的模型可在Hugging Face上获取。

## 🔬 方法详解

**问题定义**：论文旨在解决多语言语法纠错（GEC）领域数据稀缺的问题。现有的GEC研究主要集中在英语上，缺乏高质量的多语言数据集，这限制了跨语言GEC模型的发展和应用。现有方法难以直接迁移到其他语言，且在处理不同语言的语法错误时表现不佳。

**核心思路**：论文的核心思路是构建一个多语言银标准数据集，通过结合人工校正和自动校正的方法，生成包含多种语言的GEC训练数据。利用这些数据，可以训练和微调大型语言模型，使其具备多语言GEC能力。这种方法旨在弥合数据缺口，促进跨语言GEC技术的发展。

**技术框架**：OmniGEC的构建流程包括以下几个主要阶段：1) 数据收集：从维基百科编辑、Reddit子版块和UberText 2.0社交媒体语料库中收集11种语言的文本数据。2) 数据校正：对于维基百科编辑，利用人工校正数据；对于Reddit和UberText 2.0数据，使用GPT-4o-mini模型进行自动校正。3) 数据评估：通过自动指标和人工评估，评估校正数据的质量。4) 模型训练：使用OmniGEC数据集微调Aya-Expanse (8B) 和 Gemma-3 (12B) 等大型语言模型。

**关键创新**：该论文的关键创新在于构建了一个多语言银标准GEC数据集，该数据集涵盖了11种语言，并结合了人工校正和自动校正的方法。与现有方法相比，OmniGEC提供了更丰富、更多样化的训练数据，有助于提高多语言GEC模型的性能。此外，论文还通过实验验证了在OmniGEC上微调大型语言模型可以取得SOTA结果。

**关键设计**：论文的关键设计包括：1) 数据来源的选择：选择维基百科、Reddit和UberText 2.0等不同来源的数据，以增加数据的多样性。2) 自动校正模型：使用GPT-4o-mini模型进行自动校正，该模型具有较强的文本生成和纠错能力。3) 模型微调：使用Aya-Expanse (8B) 和 Gemma-3 (12B) 等大型语言模型进行微调，利用其强大的语言建模能力。4) 评估指标：采用自动指标和人工评估相结合的方法，全面评估校正数据的质量。

## 📊 实验亮点

实验结果表明，在OmniGEC数据集上微调的Aya-Expanse (8B) 和 Gemma-3 (12B) 模型在段落级多语言GEC任务上取得了SOTA结果。具体性能数据未在摘要中给出，但强调了相对于现有方法的显著提升。数据集和模型已在Hugging Face上发布，方便研究人员使用。

## 🎯 应用场景

该研究成果可广泛应用于多语言文本处理、机器翻译、语言学习等领域。例如，可以用于提高机器翻译的质量，辅助语言学习者进行语法纠错，以及提升多语言社交媒体内容审核的准确性。未来，该数据集可以扩展到更多语言，并与其他自然语言处理技术相结合，进一步推动多语言自然语言处理的发展。

## 📄 摘要（原文）

> In this paper, we introduce OmniGEC, a collection of multilingual silver-standard datasets for the task of Grammatical Error Correction (GEC), covering eleven languages: Czech, English, Estonian, German, Greek, Icelandic, Italian, Latvian, Slovene, Swedish, and Ukrainian. These datasets facilitate the development of multilingual GEC solutions and help bridge the data gap in adapting English GEC solutions to multilingual GEC. The texts in the datasets originate from three sources: Wikipedia edits for the eleven target languages, subreddits from Reddit in the eleven target languages, and the Ukrainian-only UberText 2.0 social media corpus. While Wikipedia edits were derived from human-made corrections, the Reddit and UberText 2.0 data were automatically corrected with the GPT-4o-mini model. The quality of the corrections in the datasets was evaluated both automatically and manually. Finally, we fine-tune two open-source large language models - Aya-Expanse (8B) and Gemma-3 (12B) - on the multilingual OmniGEC corpora and achieve state-of-the-art (SOTA) results for paragraph-level multilingual GEC. The dataset collection and the best-performing models are available on Hugging Face.

