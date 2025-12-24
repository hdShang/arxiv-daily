---
layout: default
title: "CAP-LLM: Context-Augmented Personalized Large Language Models for News Headline Generation"
---

# CAP-LLM: Context-Augmented Personalized Large Language Models for News Headline Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03935" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03935v1</a>
  <a href="https://arxiv.org/pdf/2508.03935.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03935v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03935v1', 'CAP-LLM: Context-Augmented Personalized Large Language Models for News Headline Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Raymond Wilson, Cole Graham, Chase Carter, Zefeng Yang, Ruiqi Gu

**分类**: cs.CL

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出CAP-LLM以解决个性化新闻标题生成中的事实一致性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化生成` `新闻标题` `事实一致性` `大型语言模型` `上下文增强` `对比损失` `用户偏好`

## 📋 核心要点

1. 现有个性化新闻标题生成方法难以有效捕捉用户复杂兴趣，且常常导致事实不一致。
2. CAP-LLM通过用户偏好编码器和上下文注入适配器，将用户偏好与文章上下文结合，提升生成质量。
3. 在PENS数据集上，CAP-LLM在事实一致性、个性化和内容覆盖方面均显著优于现有基线，表现出色。

## 📝 摘要（中文）

在信息过载的时代，个性化新闻标题生成对于吸引用户至关重要，需根据用户偏好定制内容并准确传达新闻事实。现有方法难以有效捕捉复杂的用户兴趣并确保事实一致性，常导致生成的标题过于通用或误导。为此，本文提出了上下文增强个性化大型语言模型（CAP-LLM），该框架将用户偏好和事实一致性约束整合到强大的预训练语言模型中。CAP-LLM通过用户偏好编码器捕捉长期用户兴趣，通过上下文注入适配器将这些偏好与当前文章上下文无缝整合到生成过程中，并采用对比损失的事实一致性强化模块以减轻幻觉现象。CAP-LLM在真实世界的PENS数据集上评估，取得了各项指标的最先进性能。

## 🔬 方法详解

**问题定义**：本文旨在解决个性化新闻标题生成中的事实一致性问题。现有方法在捕捉用户兴趣和确保生成标题的准确性方面存在不足，导致生成的标题往往缺乏个性化和真实性。

**核心思路**：CAP-LLM的核心思想是将用户偏好与当前文章上下文结合，通过上下文增强的方式提升生成标题的个性化和事实一致性。设计上，CAP-LLM通过特定模块来捕捉用户长期兴趣，并在生成过程中进行有效整合。

**技术框架**：CAP-LLM的整体架构包括三个主要模块：用户偏好编码器、上下文注入适配器和事实一致性强化模块。用户偏好编码器负责提取用户的长期兴趣，上下文注入适配器将这些偏好与当前文章的上下文信息结合，而事实一致性强化模块则通过对比损失来确保生成内容的真实性。

**关键创新**：CAP-LLM的关键创新在于其对用户偏好和事实一致性的双重关注，通过上下文注入和对比损失的结合，显著提升了生成标题的质量。这一设计与现有方法的本质区别在于其综合考虑了用户个性化需求与事实准确性。

**关键设计**：在设计上，CAP-LLM采用了对比损失函数来强化事实一致性，确保生成的标题不仅符合用户偏好，还能准确反映新闻内容。此外，用户偏好编码器的结构经过优化，以更好地捕捉用户的长期兴趣。整体网络结构经过精心设计，以支持高效的上下文整合和生成过程。

## 📊 实验亮点

CAP-LLM在PENS数据集上的实验结果显示，其事实一致性（FactCC 87.50）显著优于强基线BART（86.67），同时在个性化（Pc(avg) 2.73, Pc(max) 17.25）和内容覆盖（ROUGE-1 26.55, ROUGE-2 9.95, ROUGE-L 23.01）方面也取得了显著提升，展示了其在各项指标上的领先性能。

## 🎯 应用场景

CAP-LLM在个性化新闻推荐、社交媒体内容生成及信息推送等领域具有广泛的应用潜力。通过提升生成标题的个性化和事实一致性，能够有效提高用户的阅读体验和信息获取效率，进而推动新闻行业的智能化发展。未来，该技术还可扩展至其他文本生成任务，如个性化广告和内容创作等。

## 📄 摘要（原文）

> In the era of information overload, personalized news headline generation is crucial for engaging users by tailoring content to their preferences while accurately conveying news facts. Existing methods struggle with effectively capturing complex user interests and ensuring factual consistency, often leading to generic or misleading headlines. Leveraging the unprecedented capabilities of Large Language Models (LLMs) in text generation, we propose Context-Augmented Personalized LLM (CAP-LLM), a novel framework that integrates user preferences and factual consistency constraints into a powerful pre-trained LLM backbone. CAP-LLM features a User Preference Encoder to capture long-term user interests, a Context Injection Adapter to seamlessly integrate these preferences and current article context into the LLM's generation process, and a Fact-Consistency Reinforcement Module employing a novel contrastive loss to mitigate hallucination. Evaluated on the real-world PENS dataset, CAP-LLM achieves state-of-the-art performance across all metrics. Notably, it significantly improves factual consistency (FactCC of 87.50) over strong baselines like BART (86.67), while simultaneously enhancing personalization (Pc(avg) 2.73, Pc(max) 17.25) and content coverage (ROUGE-1 26.55, ROUGE-2 9.95, ROUGE-L 23.01). Our ablation studies, human evaluations, and sensitivity analyses further validate the effectiveness of each component and the robustness of our approach, demonstrating CAP-LLM's ability to achieve a superior balance between personalization and factual accuracy in news headline generation.

