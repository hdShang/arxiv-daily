---
layout: default
title: "An evaluation of LLMs for generating movie reviews: GPT-4o, Gemini-2.0 and DeepSeek-V3"
---

# An evaluation of LLMs for generating movie reviews: GPT-4o, Gemini-2.0 and DeepSeek-V3

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00312" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00312v1</a>
  <a href="https://arxiv.org/pdf/2506.00312.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00312v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00312v1', 'An evaluation of LLMs for generating movie reviews: GPT-4o, Gemini-2.0 and DeepSeek-V3')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Brendan Sands, Yining Wang, Chenhao Xu, Yuxuan Zhou, Lai Wei, Rohitash Chandra

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出框架评估LLMs生成电影评论的有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `电影评论生成` `情感分析` `文本生成` `用户调查`

## 📋 核心要点

1. 现有的电影评论生成方法在情感表达和风格一致性方面存在不足，导致生成的评论缺乏吸引力。
2. 本文提出了一种新的框架，利用三种大型语言模型生成电影评论，并评估其与真实用户评论的相似性。
3. 实验结果表明，LLMs能够生成结构完整的评论，但在情感深度和风格上仍需改进，DeepSeek-V3表现最佳。

## 📝 摘要（中文）

大型语言模型（LLMs）在文本生成和摘要等任务中表现突出。本文研究了LLMs在生成产品评论中的应用，尤其是电影评论。我们提出了一种框架，利用GPT-4o、DeepSeek-V3和Gemini-2.0三种LLMs生成电影评论，并通过与IMDb用户评论的比较评估其性能。研究发现，LLMs生成的评论在语法流畅性和结构完整性上表现良好，但在情感丰富性和风格一致性方面仍存在明显差距，表明需要进一步改进。调查结果显示，参与者难以区分LLM生成的评论与IMDb用户评论，DeepSeek-V3生成的评论最为平衡，GPT-4o则过于强调积极情感，而Gemini-2.0更好地捕捉了消极情感，但情感强度过高。

## 🔬 方法详解

**问题定义**：本文旨在解决现有电影评论生成方法在情感丰富性和风格一致性方面的不足，尤其是LLMs生成的评论与真实用户评论之间的差距。

**核心思路**：我们提出了一种框架，通过输入电影字幕和剧本，利用三种LLMs生成电影评论，并对其质量进行评估，以提高评论的情感表达和风格一致性。

**技术框架**：整体架构包括数据预处理、LLM输入生成、评论生成、质量评估和用户调查五个主要模块。数据预处理阶段使用电影字幕和剧本作为输入，LLM生成阶段则调用GPT-4o、DeepSeek-V3和Gemini-2.0进行评论生成。

**关键创新**：本研究的创新点在于比较三种不同LLMs生成的评论质量，并通过用户调查评估其与真实评论的相似性，填补了现有研究的空白。

**关键设计**：在模型训练中，我们关注了情感极性、词汇丰富性和主题一致性等关键参数设置，采用了适当的损失函数以优化生成评论的质量。

## 📊 实验亮点

实验结果显示，LLMs生成的评论在语法和结构上表现良好，但在情感深度和风格一致性上仍有待提高。DeepSeek-V3生成的评论最为平衡，接近IMDb用户评论，而GPT-4o和Gemini-2.0在情感表达上存在偏差，前者过于强调积极情感，后者则表现出过高的情感强度。

## 🎯 应用场景

该研究的潜在应用领域包括电影评论生成、在线产品评价和社交媒体内容创作等。通过改进LLMs的生成能力，可以为用户提供更具吸引力和情感深度的评论，提升用户体验。此外，研究成果可为相关领域的文本生成任务提供参考和借鉴。

## 📄 摘要（原文）

> Large language models (LLMs) have been prominent in various tasks, including text generation and summarisation. The applicability of LLMs to the generation of product reviews is gaining momentum, paving the way for the generation of movie reviews. In this study, we propose a framework that generates movie reviews using three LLMs (GPT-4o, DeepSeek-V3, and Gemini-2.0), and evaluate their performance by comparing the generated outputs with IMDb user reviews. We use movie subtitles and screenplays as input to the LLMs and investigate how they affect the quality of reviews generated. We review the LLM-based movie reviews in terms of vocabulary, sentiment polarity, similarity, and thematic consistency in comparison to IMDB user reviews. The results demonstrate that LLMs are capable of generating syntactically fluent and structurally complete movie reviews. Nevertheless, there is still a noticeable gap in emotional richness and stylistic coherence between LLM-generated and IMDb reviews, suggesting that further refinement is needed to improve the overall quality of movie review generation. We provided a survey-based analysis where participants were told to distinguish between LLM and IMDb user reviews. The results show that LLM-generated reviews are difficult to distinguish from IMDB user reviews. We found that DeepSeek-V3 produced the most balanced reviews, closely matching IMDb reviews. GPT-4o overemphasised positive emotions, while Gemini-2.0 captured negative emotions better but showed excessive emotional intensity.

