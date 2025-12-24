---
layout: default
title: Traveling Across Languages: Benchmarking Cross-Lingual Consistency in Multimodal LLMs
---

# Traveling Across Languages: Benchmarking Cross-Lingual Consistency in Multimodal LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.15075" class="toolbar-btn" target="_blank">📄 arXiv: 2505.15075v5</a>
  <a href="https://arxiv.org/pdf/2505.15075.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.15075v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.15075v5', 'Traveling Across Languages: Benchmarking Cross-Lingual Consistency in Multimodal LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Wang, Pinzhi Huang, Jihan Yang, Saining Xie, Daisuke Kawahara

**分类**: cs.CL, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-05-21 (更新: 2025-08-24)

**备注**: The first version of this paper mistakenly included a prompt injection phrase, which was inappropriate and unprofessional. Although we corrected the version on arXiv and withdrew from the conference, my co-authors and university strongly request a full withdrawal. Given the situation, I no longer have the authority to manage this paper, and withdrawing it from arXiv is the most responsible action

---

## 💡 一句话要点

**提出KnowRecall和VisRecall基准以解决多语言一致性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大型语言模型` `跨语言一致性` `文化知识` `视觉记忆` `基准测试`

## 📋 核心要点

1. 现有多模态大型语言模型在跨语言一致性方面表现不佳，尤其是在文化知识的整合上存在显著挑战。
2. 本文提出KnowRecall和VisRecall两个基准，旨在系统性评估多语言模型在文化和视觉记忆方面的一致性表现。
3. 实验结果显示，当前的最先进模型在跨语言一致性上仍有明显不足，亟需更强的模型设计以提升多语言能力。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）的快速发展显著提升了其在现实世界中的应用。然而，跨语言的一致性表现，尤其是在整合文化知识时，仍然是一个重大挑战。为此，本文引入了两个新的基准：KnowRecall和VisRecall，旨在评估MLLMs的跨语言一致性。KnowRecall是一个视觉问答基准，专注于15种语言中关于全球地标的文化和历史问题的事实知识一致性。VisRecall则通过要求模型在不访问图像的情况下描述9种语言中的地标外观，来评估视觉记忆一致性。实验结果表明，当前最先进的MLLMs，包括一些专有模型，仍然难以实现跨语言一致性，这突显了开发真正多语言和文化敏感模型的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大型语言模型在跨语言一致性方面的不足，特别是在文化知识整合和视觉记忆一致性上存在的挑战。现有方法未能有效评估模型在不同语言中的表现一致性。

**核心思路**：论文提出了两个新的基准KnowRecall和VisRecall，分别针对事实知识和视觉记忆进行评估，旨在提供更全面的跨语言一致性测试框架。

**技术框架**：KnowRecall通过视觉问答的形式，评估模型在15种语言中对全球地标的文化和历史问题的回答一致性；VisRecall则要求模型在不依赖图像的情况下，用9种语言描述地标外观。

**关键创新**：最重要的创新在于引入了针对多语言和文化知识的系统性评估基准，填补了现有研究在跨语言一致性评估中的空白。

**关键设计**：在KnowRecall中，设计了针对文化和历史问题的问答集；在VisRecall中，模型需在没有图像的情况下进行描述，考察其视觉记忆的跨语言一致性。

## 📊 实验亮点

实验结果表明，当前的最先进多模态大型语言模型在KnowRecall和VisRecall基准测试中表现不佳，未能达到跨语言一致性，显示出在文化知识整合和视觉记忆方面的显著不足。这一发现强调了未来研究在多语言和文化敏感模型设计上的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括多语言智能助手、跨文化教育工具以及全球化市场的内容生成。通过提升模型的跨语言一致性，可以更好地满足不同文化背景用户的需求，增强用户体验。

## 📄 摘要（原文）

> The rapid evolution of multimodal large language models (MLLMs) has significantly enhanced their real-world applications. However, achieving consistent performance across languages, especially when integrating cultural knowledge, remains a significant challenge. To better assess this issue, we introduce two new benchmarks: KnowRecall and VisRecall, which evaluate cross-lingual consistency in MLLMs. KnowRecall is a visual question answering benchmark designed to measure factual knowledge consistency in 15 languages, focusing on cultural and historical questions about global landmarks. VisRecall assesses visual memory consistency by asking models to describe landmark appearances in 9 languages without access to images. Experimental results reveal that state-of-the-art MLLMs, including proprietary ones, still struggle to achieve cross-lingual consistency. This underscores the need for more robust approaches that produce truly multilingual and culturally aware models.

