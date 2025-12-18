---
layout: default
title: On Assessing the Relevance of Code Reviews Authored by Generative Models
---

# On Assessing the Relevance of Code Reviews Authored by Generative Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15466" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15466v1</a>
  <a href="https://arxiv.org/pdf/2512.15466.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15466v1" onclick="toggleFavorite(this, '2512.15466v1', 'On Assessing the Relevance of Code Reviews Authored by Generative Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Robert Heumüller, Frank Ortmeier

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-17

**备注**: Replication Package: https://github.com/robert-heumueller-ovgu/repl-generative-review-relevance

---

## 💡 一句话要点

**提出多主观排序评估方法，评估生成模型在代码评审中的有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码评审` `生成模型` `大型语言模型` `多主观排序` `评估方法`

## 📋 核心要点

1. 现有代码评审生成评估方法未能充分考虑人类评审的多样性，且主观“有用性”评估标准模糊。
2. 论文提出多主观排序方法，通过多个人工评审员对生成模型和人工回复进行排序，更全面评估质量。
3. 实验结果表明，ChatGPT生成的代码评审评论质量优于人工评论，甚至超过StackExchange的采纳答案。

## 📝 摘要（中文）

在代码评审中使用像ChatGPT这样的大型语言模型，虽然有望提高效率，但也引发了对正确性和安全性的担忧。现有的代码评审生成评估方法要么依赖于与单一标准答案的自动比较，无法捕捉人类观点的多样性，要么依赖于对“有用性”的主观评估，这是一个高度模糊的概念。我们提出了一种基于多主观排序的新型评估方法。使用包含280个独立代码评审请求和来自CodeReview StackExchange的相应评论的数据集，多个人工评审员对ChatGPT生成的评论质量与平台上最佳的人工回复进行了排序。结果表明，ChatGPT的评论排名明显优于人工评论，甚至超过了StackExchange上被接受的答案。更进一步，我们提出的方法激发并实现了对生成式AI在代码评审中性能的更有意义的评估，同时也提高了对未经检查的集成到评审流程中的潜在风险的认识。

## 🔬 方法详解

**问题定义**：现有代码评审生成模型的评估方法存在局限性。自动评估依赖单一标准答案，忽略了人类评审的多样性；主观评估则依赖于模糊的“有用性”概念，缺乏客观性。因此，需要一种更全面、更客观的评估方法来衡量生成模型在代码评审中的有效性。

**核心思路**：论文的核心思路是采用多主观排序（Multi-Subjective Ranking）的方法。即，不依赖于单一标准答案，而是邀请多个人工评审员对生成模型生成的评论和人工回复进行排序，综合多个评审员的意见，从而更全面地评估生成模型的质量。

**技术框架**：该方法主要包含以下几个步骤：1) 构建包含代码评审请求和对应评论的数据集；2) 使用生成模型（如ChatGPT）生成针对代码评审请求的评论；3) 邀请多个人工评审员，对生成模型生成的评论和人工回复进行排序；4) 综合多个评审员的排序结果，计算生成模型和人工回复的平均排名，并进行统计分析。

**关键创新**：该方法最重要的创新点在于引入了多主观排序的思想，克服了传统评估方法的局限性。通过综合多个评审员的意见，能够更全面地评估生成模型在代码评审中的表现，避免了单一标准答案带来的偏差，也避免了主观“有用性”评估的模糊性。

**关键设计**：论文使用了来自CodeReview StackExchange的数据集，包含280个代码评审请求和对应的评论。人工评审员的数量未知，但强调了多个人工评审员的重要性。排序的具体方法未知，但最终会计算平均排名并进行统计显著性分析。论文侧重于评估方法的提出，而非特定的模型或参数设置。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15466v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15466v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，使用多主观排序方法评估后，ChatGPT生成的代码评审评论的排名显著优于人工评论，甚至超过了StackExchange上被采纳的答案。这表明生成模型在代码评审方面具有巨大的潜力，但也提示我们需要关注未经检查的集成可能带来的风险。

## 🎯 应用场景

该研究成果可应用于代码评审工具的开发和评估，帮助开发者更有效地利用生成模型进行代码评审，提高代码质量和开发效率。此外，该评估方法也可推广到其他需要主观评估的生成式AI应用场景，例如文本摘要、机器翻译等，为生成式AI的评估提供更可靠的依据。

## 📄 摘要（原文）

> The use of large language models like ChatGPT in code review offers promising efficiency gains but also raises concerns about correctness and safety. Existing evaluation methods for code review generation either rely on automatic comparisons to a single ground truth, which fails to capture the variability of human perspectives, or on subjective assessments of "usefulness", a highly ambiguous concept. We propose a novel evaluation approach based on what we call multi-subjective ranking. Using a dataset of 280 self-contained code review requests and corresponding comments from CodeReview StackExchange, multiple human judges ranked the quality of ChatGPT-generated comments alongside the top human responses from the platform. Results show that ChatGPT's comments were ranked significantly better than human ones, even surpassing StackExchange's accepted answers. Going further, our proposed method motivates and enables more meaningful assessments of generative AI's performance in code review, while also raising awareness of potential risks of unchecked integration into review processes.

