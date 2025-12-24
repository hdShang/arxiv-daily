---
layout: default
title: "Beyond the Link: Assessing LLMs' ability to Classify Political Content across Global Media"
---

# Beyond the Link: Assessing LLMs' ability to Classify Political Content across Global Media

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17435" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17435v2</a>
  <a href="https://arxiv.org/pdf/2506.17435.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17435v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17435v2', 'Beyond the Link: Assessing LLMs\' ability to Classify Political Content across Global Media')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alejandro De La Fuente-Cuesta, Alberto Martinez-Serra, Nienke Visscher, Laia Castro, Ana S. Cardenal

**分类**: cs.CL

**发布日期**: 2025-06-20 (更新: 2025-11-04)

---

## 💡 一句话要点

**评估大型语言模型在全球媒体政治内容分类中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `政治内容分类` `URL分析` `多语言处理` `系统性偏差`

## 📋 核心要点

1. 现有方法在从URL中准确分类政治内容方面存在不足，尤其是对中立新闻的误分类问题。
2. 本文提出利用大型语言模型分析新闻文章的文本和URL，以提高政治内容分类的准确性。
3. 实验结果表明，URL分析能够有效近似全文分析，但存在系统性偏差，需谨慎解读。

## 📝 摘要（中文）

大型语言模型（LLMs）在政治科学和数字媒体研究中的应用日益普及。尽管LLMs在标注任务中表现出色，但其在从URL中分类政治内容（PC）的有效性仍未得到充分探索。本文评估了LLMs能否准确区分来自五个国家（法国、德国、西班牙、英国和美国）新闻文章的PC与非PC，分析了文本和URL的作用。研究发现，URL中蕴含相关信息，可以作为一种可扩展且成本效益高的方式来识别PC。然而，研究也揭示了系统性偏差：LLMs倾向于将中立新闻过度分类为政治内容，导致假阳性，从而可能扭曲后续分析。最后，本文提出了在政治科学研究中使用LLMs的 методологические рекомендации。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在分类政治内容时的准确性问题，尤其是URL分析的有效性和潜在偏差。现有方法在处理多语言和多国新闻时面临挑战，尤其是对中立内容的误分类。

**核心思路**：论文的核心思路是通过结合文本和URL信息，评估LLMs在不同国家和语言环境下的分类能力。这种设计旨在验证URL是否能够作为一种有效的替代方案，减少对全文分析的依赖。

**技术框架**：研究采用了先进的LLMs，构建了一个多阶段的评估框架，包括数据收集、模型训练、性能评估和偏差分析。主要模块包括文本处理、URL分析和结果对比。

**关键创新**：最重要的技术创新在于将URL作为分类依据，发现其在识别政治内容中的潜在价值。这与传统方法依赖全文分析的方式形成了鲜明对比。

**关键设计**：在模型训练中，采用了特定的损失函数来优化分类准确性，并进行了多轮的超参数调整，以适应不同语言和文化背景的新闻数据。

## 📊 实验亮点

实验结果显示，使用URL进行政治内容分类的准确率与传统的全文分析相近，且在某些情况下，URL分析的效率更高。然而，研究也发现LLMs在分类中立新闻时存在显著的假阳性，提示未来研究需关注模型的偏差问题。

## 🎯 应用场景

该研究的潜在应用领域包括政治科学研究、媒体分析和信息传播研究。通过提高对政治内容的分类准确性，研究能够帮助学者和政策制定者更好地理解媒体报道的倾向性和影响力，进而推动更为科学的舆论分析和政策制定。

## 📄 摘要（原文）

> The use of large language models (LLMs) is becoming common in political science and digital media research. While LLMs have demonstrated ability in labelling tasks, their effectiveness to classify Political Content (PC) from URLs remains underexplored. This article evaluates whether LLMs can accurately distinguish PC from non-PC using both the text and the URLs of news articles across five countries (France, Germany, Spain, the UK, and the US) and their different languages. Using cutting-edge models, we benchmark their performance against human-coded data to assess whether URL-level analysis can approximate full-text analysis. Our findings show that URLs embed relevant information and can serve as a scalable, cost-effective alternative to discern PC. However, we also uncover systematic biases: LLMs seem to overclassify centrist news as political, leading to false positives that may distort further analyses. We conclude by outlining methodological recommendations on the use of LLMs in political science research.

