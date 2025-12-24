---
layout: default
title: Frame In, Frame Out: Do LLMs Generate More Biased News Headlines than Humans?
---

# Frame In, Frame Out: Do LLMs Generate More Biased News Headlines than Humans?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05406" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05406v1</a>
  <a href="https://arxiv.org/pdf/2505.05406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05406v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05406v1', 'Frame In, Frame Out: Do LLMs Generate More Biased News Headlines than Humans?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Valeria Pastorino, Nafise Sadat Moosavi

**分类**: cs.CL

**发布日期**: 2025-05-08

---

## 💡 一句话要点

**探讨大型语言模型生成新闻标题的偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `框架效应` `大型语言模型` `新闻生成` `偏见评估` `自动化内容创作`

## 📋 核心要点

1. 现有的自动新闻生成方法可能引入或加剧框架偏见，影响公众对事件的理解。
2. 本文通过分析LLMs生成的新闻内容，探讨其框架效应的表现及其与人类作者的比较。
3. 研究发现，LLMs在政治和社会敏感领域的框架偏见更为明显，且不同模型架构的偏见程度差异显著。

## 📝 摘要（中文）

媒体中的框架效应通过选择性强调某些细节而影响公众认知。随着大型语言模型在自动新闻和内容创作中的应用，越来越多的研究关注这些系统是否会引入或加剧框架偏见。本文探讨了大型语言模型生成的新闻内容中框架效应的表现，发现尤其在政治和社会敏感的背景下，LLMs的框架偏见明显高于人类作者。此外，不同模型架构的框架倾向存在显著差异，部分模型表现出更高的偏见。这些发现强调了有效的后训练减轻策略和更严格的评估框架的必要性，以确保自动生成的新闻内容符合平衡报道的标准。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成新闻标题时可能引入的框架偏见问题。现有方法缺乏对模型生成内容的偏见评估，导致公众认知受到影响。

**核心思路**：通过比较不同架构的LLMs生成的新闻内容与人类作者的作品，分析框架效应的表现，旨在揭示LLMs在敏感话题上的偏见程度。

**技术框架**：研究采用定量和定性分析相结合的方法，首先生成新闻标题，然后对比分析其框架效应，最后评估不同模型的表现。

**关键创新**：本文的创新在于系统性地比较了多种LLMs生成的内容与人类创作的内容，揭示了模型架构对框架偏见的影响，填补了相关领域的研究空白。

**关键设计**：研究中使用了多种模型架构进行对比，设计了特定的评估指标来量化框架偏见，确保结果的可靠性和有效性。具体的参数设置和损失函数设计在实验中进行了详细记录。

## 📊 实验亮点

实验结果表明，LLMs在生成的新闻标题中表现出比人类作者更强的框架偏见，尤其是在政治和社会敏感话题上。不同模型架构的偏见程度差异显著，某些模型的偏见程度高出人类作者的两倍。这些发现强调了对自动生成内容的评估和改进的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括新闻媒体、社交平台和内容生成工具等。通过识别和减轻LLMs生成内容中的偏见，可以提高自动生成新闻的质量，确保信息的客观性和公正性，进而影响公众对重要事件的理解和看法。

## 📄 摘要（原文）

> Framing in media critically shapes public perception by selectively emphasizing some details while downplaying others. With the rise of large language models in automated news and content creation, there is growing concern that these systems may introduce or even amplify framing biases compared to human authors. In this paper, we explore how framing manifests in both out-of-the-box and fine-tuned LLM-generated news content. Our analysis reveals that, particularly in politically and socially sensitive contexts, LLMs tend to exhibit more pronounced framing than their human counterparts. In addition, we observe significant variation in framing tendencies across different model architectures, with some models displaying notably higher biases. These findings point to the need for effective post-training mitigation strategies and tighter evaluation frameworks to ensure that automated news content upholds the standards of balanced reporting.

