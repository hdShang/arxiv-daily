---
layout: default
title: Probing Association Biases in LLM Moderation Over-Sensitivity
---

# Probing Association Biases in LLM Moderation Over-Sensitivity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23914" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23914v1</a>
  <a href="https://arxiv.org/pdf/2505.23914.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23914v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23914v1', 'Probing Association Biases in LLM Moderation Over-Sensitivity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxin Wang, Botao Yu, Ivory Yang, Saeed Hassanpour, Soroush Vosoughi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-29

**备注**: Under review

---

## 💡 一句话要点

**提出主题关联分析以解决LLM内容审核过度敏感问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `内容审核` `主题关联分析` `过度敏感` `隐性偏见` `语义分析` `自动化过滤`

## 📋 核心要点

1. 现有的内容审核方法往往将良性评论误判为有毒评论，导致过度敏感的问题，主要归因于攻击性词汇的存在。
2. 论文提出了一种新的分析方法——主题关联分析，通过量化LLMs如何将特定主题与有毒性关联，揭示其潜在的主题偏见。
3. 实验结果表明，尽管更先进的模型如GPT-4 Turbo的假阳性率较低，但其主题刻板印象更强，显示出LLMs在审核决策中依赖于学习到的主题关联。

## 📝 摘要（中文）

大型语言模型（LLMs）广泛应用于内容审核，但常常将良性评论误判为有毒评论，导致过度敏感。以往研究主要将此问题归因于攻击性词汇的存在，而我们揭示了一个超越词汇层面的潜在原因：LLMs在隐性关联中表现出系统性的主题偏见。受认知心理学隐性关联测试的启发，我们提出了主题关联分析，这是一种语义层面的分析方法，用于量化LLMs如何将特定主题与有毒性关联。通过提示LLMs生成对误分类良性评论的自由场景想象并分析其主题放大水平，我们发现更先进的模型（如GPT-4 Turbo）尽管整体假阳性率较低，但表现出更强的主题刻板印象。这些偏见表明，LLMs不仅仅对显性攻击性语言做出反应，而是依赖于学习到的主题关联，从而影响其审核决策。我们的发现强调了超越基于关键词过滤的必要性，为理解LLM过度敏感的潜在机制提供了新见解。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在内容审核中出现的过度敏感问题，现有方法主要集中于攻击性词汇，未能充分考虑主题偏见的影响。

**核心思路**：通过引入主题关联分析，论文探讨了LLMs如何在语义层面上将特定主题与有毒性关联，从而影响其审核决策。

**技术框架**：整体流程包括：首先，提示LLMs生成对误分类良性评论的自由场景想象；其次，分析生成内容中的主题放大水平，以量化其主题偏见。

**关键创新**：最重要的创新点在于提出了主题关联分析这一新方法，超越了传统的基于关键词的过滤，揭示了LLMs在内容审核中潜在的主题偏见。

**关键设计**：在实验中，设计了特定的提示策略以引导LLMs生成相关场景，并采用了主题放大水平作为评估指标，以量化模型的主题偏见。

## 📊 实验亮点

实验结果显示，尽管GPT-4 Turbo的整体假阳性率较低，但其在主题刻板印象方面表现出更强的偏见。这一发现强调了在内容审核中，模型不仅依赖于显性语言特征，还受到隐性主题关联的影响。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、在线评论监控和自动化内容过滤系统。通过理解LLMs的主题偏见，可以优化内容审核算法，减少误判，提高用户体验，未来可能推动更智能的内容管理工具的发展。

## 📄 摘要（原文）

> Large Language Models are widely used for content moderation but often misclassify benign comments as toxic, leading to over-sensitivity. While previous research attributes this issue primarily to the presence of offensive terms, we reveal a potential cause beyond token level: LLMs exhibit systematic topic biases in their implicit associations. Inspired by cognitive psychology's implicit association tests, we introduce Topic Association Analysis, a semantic-level approach to quantify how LLMs associate certain topics with toxicity. By prompting LLMs to generate free-form scenario imagination for misclassified benign comments and analyzing their topic amplification levels, we find that more advanced models (e.g., GPT-4 Turbo) demonstrate stronger topic stereotype despite lower overall false positive rates. These biases suggest that LLMs do not merely react to explicit, offensive language but rely on learned topic associations, shaping their moderation decisions. Our findings highlight the need for refinement beyond keyword-based filtering, providing insights into the underlying mechanisms driving LLM over-sensitivity.

