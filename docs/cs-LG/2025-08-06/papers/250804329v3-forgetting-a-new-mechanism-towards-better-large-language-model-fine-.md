---
layout: default
title: "Forgetting: A New Mechanism Towards Better Large Language Model Fine-tuning"
---

# Forgetting: A New Mechanism Towards Better Large Language Model Fine-tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04329" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04329v3</a>
  <a href="https://arxiv.org/pdf/2508.04329.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04329v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04329v3', 'Forgetting: A New Mechanism Towards Better Large Language Model Fine-tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ali Taheri Ghahrizjani, Alireza Taban, Shanshan Ye, Abdolreza Mirzaei, Tongliang Liu, Bo Han

**分类**: cs.LG

**发布日期**: 2025-08-06 (更新: 2025-08-20)

---

## 💡 一句话要点

**提出遗忘机制以改善大语言模型的微调效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `监督微调` `遗忘机制` `模型训练` `自然语言处理` `性能提升`

## 📋 核心要点

1. 现有的监督微调方法对数据质量和数量高度依赖，可能导致性能提升有限或下降。
2. 本文提出将语料中的标记分为正向和负向标记，正向标记用于训练，负向标记则需遗忘。
3. 实验结果显示，该遗忘机制显著提升了模型性能，并增加了模型响应的多样性。

## 📝 摘要（中文）

监督微调（SFT）在预训练的大语言模型（LLMs）中扮演着关键角色，显著提升其获取领域特定知识的能力，同时保持或增强其通用能力。然而，SFT的有效性依赖于数据质量和数量，若不满足要求，可能导致性能提升有限甚至下降。为此，本文提出将语料中的标记分为正向和负向标记，正向标记用于模型训练，而负向标记则应被显式遗忘。这样的标记分类有助于模型学习更少的信息，并通过遗忘过程形成知识边界，指导模型更精确地学习信息。实验结果表明，该遗忘机制不仅提升了模型的整体性能，还促进了模型响应的多样性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在监督微调过程中对数据质量和数量的高度依赖问题，现有方法在数据不足时可能导致性能下降。

**核心思路**：提出将语料中的标记分为正向和负向标记，正向标记用于模型训练，而负向标记则需被遗忘，以减少无效信息对模型的影响。

**技术框架**：整体流程包括数据预处理、标记分类、模型训练和评估。首先对语料进行标记分类，然后使用正向标记进行训练，负向标记则在训练过程中被遗忘。

**关键创新**：最重要的创新点在于引入了标记遗忘机制，通过明确区分有用和无用的信息，帮助模型更有效地学习。与传统方法相比，该方法减少了对低质量数据的依赖。

**关键设计**：在模型训练中，采用特定的损失函数来强化正向标记的学习，同时设计机制确保负向标记被有效遗忘，具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，采用遗忘机制后，模型在标准基准测试上的性能显著提升，具体提升幅度达到X%（具体数据待补充），同时模型响应的多样性也得到了增强，显示出更好的适应性和灵活性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等。通过优化大语言模型的微调过程，能够在特定领域中提升模型的表现，进而推动智能助手、客服机器人等应用的实际价值和用户体验。未来，该方法可能影响更多领域的模型训练策略。

## 📄 摘要（原文）

> Supervised fine-tuning (SFT) plays a critical role for pretrained large language models (LLMs), notably enhancing their capacity to acquire domain-specific knowledge while preserving or potentially augmenting their general-purpose capabilities. However, the efficacy of SFT hinges on data quality as well as data volume, otherwise it may result in limited performance gains or even degradation relative to the associated baselines. To mitigate such reliance, we suggest categorizing tokens within each corpus into two parts -- positive and negative tokens -- based on whether they are useful to improve model performance. Positive tokens can be trained in common ways, whereas negative tokens, which may lack essential semantics or be misleading, should be explicitly forgotten. Overall, the token categorization facilitate the model to learn less informative message, and the forgetting process shapes a knowledge boundary to guide the model on what information to learn more precisely. We conduct experiments on well-established benchmarks, finding that this forgetting mechanism not only improves overall model performance and also facilitate more diverse model responses.

