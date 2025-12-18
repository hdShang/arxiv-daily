---
layout: default
title: Two CFG Nahuatl for automatic corpora expansion
---

# Two CFG Nahuatl for automatic corpora expansion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14239" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14239v1</a>
  <a href="https://arxiv.org/pdf/2512.14239.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14239v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14239v1', 'Two CFG Nahuatl for automatic corpora expansion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Juan-José Guzmán-Landa, Juan-Manuel Torres-Moreno, Miguel Figueroa-Saavedra, Ligia Quintana-Torres, Graham Ranger Martha-Lorena Avendaño-Garrido

**分类**: cs.CL

**发布日期**: 2025-12-16

**备注**: 15 pages, 5 figures, 8 tables

---

## 💡 一句话要点

**提出两种CFG Nahuatl方法，用于自动扩展Nawatl语料库**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低资源语言` `语料库扩展` `上下文无关文法` `Nawatl语` `词嵌入`

## 📋 核心要点

1. Nawatl语作为一种低资源语言，缺乏足够的语料库来支持大型语言模型的训练，限制了其自然语言处理应用。
2. 论文提出利用上下文无关文法（CFG）生成大量句法正确的Nawatl语句，以此来扩充现有的语料库。
3. 实验结果表明，使用生成的语料库训练的嵌入模型在语义相似度任务上表现更好，甚至优于某些大型语言模型。

## 📝 摘要（中文）

本文旨在介绍两种用于Nawatl语料库扩展的上下文无关文法（CFG）。Nawatl语是墨西哥的一种美洲印第安语（墨西哥的国家语言），属于$π$-语言类型，即数字资源匮乏的语言。因此，用于学习大型语言模型（LLM）的语料库实际上不存在，这构成了重大挑战。目标是生成大量句法上有效的Nawatl人工句子，从而扩展语料库，用于学习非上下文嵌入。为此，我们引入了两种新的Nawatl CFG，并在生成模式下使用它们。使用这些文法，可以显著扩展Nawatl语料库，随后可用于学习嵌入，并评估其在句子语义相似性任务中的相关性。结果表明，与仅使用原始语料库而不进行人工扩展相比，结果有所改善，并且还表明，经济型嵌入通常比某些LLM表现更好。

## 🔬 方法详解

**问题定义**：论文旨在解决Nawatl语（一种低资源的美洲原住民语言）语料库稀缺的问题。现有方法无法为Nawatl语提供足够的数据来训练有效的语言模型，特别是大型语言模型，这阻碍了Nawatl语的自然语言处理研究和应用。

**核心思路**：论文的核心思路是利用上下文无关文法（CFG）自动生成大量的Nawatl语句，从而人为地扩充现有的语料库。通过生成句法正确的句子，可以为语言模型提供更多的训练数据，提高模型的性能。

**技术框架**：该方法主要包含以下几个阶段：1) 设计并实现两种Nawatl语的上下文无关文法（CFG）。2) 使用CFG在生成模式下生成大量的Nawatl语句。3) 将生成的语句添加到现有的Nawatl语料库中，形成一个更大的语料库。4) 使用扩充后的语料库训练词嵌入模型。5) 在句子语义相似度任务上评估词嵌入模型的性能。

**关键创新**：该论文的关键创新在于针对Nawatl语设计了两种有效的上下文无关文法（CFG），并成功地利用这些文法生成了大量的句法正确的Nawatl语句。与直接收集和标注Nawatl语数据相比，使用CFG生成数据的方法更加经济高效。

**关键设计**：关于CFG的具体设计细节，论文中可能包含以下信息：1) 文法规则的数量和类型。2) 词汇表的规模和组成。3) 生成句子的长度和复杂度的控制策略。4) 如何保证生成句子的句法正确性。5) 训练词嵌入模型时使用的具体参数设置（例如，嵌入维度、训练算法等）。由于论文摘要信息有限，具体细节未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14239v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14239v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14239v1/resultats_models_tase_II_grammaires.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，使用CFG生成的语料库进行训练，能够有效提升Nawatl语的词嵌入模型在句子语义相似度任务上的表现。与仅使用原始语料库相比，性能有所提升，并且训练得到的经济型嵌入模型甚至优于某些大型语言模型，证明了该方法的有效性。

## 🎯 应用场景

该研究成果可应用于低资源语言的自然语言处理领域，例如机器翻译、信息检索、文本分类等。通过自动生成语料库，可以降低低资源语言自然语言处理研究的门槛，促进这些语言的数字化和保护。此外，该方法也可以用于其他数据稀缺的领域，例如罕见疾病的医学文本分析。

## 📄 摘要（原文）

> The aim of this article is to introduce two Context-Free Grammars (CFG) for Nawatl Corpora expansion. Nawatl is an Amerindian language (it is a National Language of Mexico) of the $π$-language type, i.e. a language with few digital resources. For this reason the corpora available for the learning of Large Language Models (LLMs) are virtually non-existent, posing a significant challenge. The goal is to produce a substantial number of syntactically valid artificial Nawatl sentences and thereby to expand the corpora for the purpose of learning non contextual embeddings. For this objective, we introduce two new Nawatl CFGs and use them in generative mode. Using these grammars, it is possible to expand Nawatl corpus significantly and subsequently to use it to learn embeddings and to evaluate their relevance in a sentences semantic similarity task. The results show an improvement compared to the results obtained using only the original corpus without artificial expansion, and also demonstrate that economic embeddings often perform better than some LLMs.

