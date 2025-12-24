---
layout: default
title: "Multimodal Cultural Safety: Evaluation Framework and Alignment Strategies"
---

# Multimodal Cultural Safety: Evaluation Framework and Alignment Strategies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14972" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14972v2</a>
  <a href="https://arxiv.org/pdf/2505.14972.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14972v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14972v2', 'Multimodal Cultural Safety: Evaluation Framework and Alignment Strategies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyi Qiu, Kung-Hsiang Huang, Ruichen Zheng, Jiao Sun, Nanyun Peng

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-12-19)

---

## 💡 一句话要点

**提出CROSS基准以评估大型视觉语言模型的文化安全性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文化安全` `多模态评估` `视觉语言模型` `跨文化交流` `监督微调` `偏好调优` `人工智能伦理`

## 📋 核心要点

1. 现有多模态安全基准主要关注物理安全，忽视文化规范的违规行为，导致文化适宜性响应能力不足。
2. 提出CROSS基准和CROSS-Eval框架，评估LVLMs在文化安全推理中的表现，涵盖文化意识等四个维度。
3. 实验结果显示，最佳模型在文化意识和合规性方面表现不佳，通过监督微调和偏好调优策略显著提升了模型性能。

## 📝 摘要（中文）

大型视觉语言模型（LVLMs）在全球应用中日益普及，但其生成文化适宜性响应的能力尚未得到充分探索。现有的多模态安全基准主要关注物理安全，忽视了文化规范的违规行为，这可能导致象征性伤害。为填补这一空白，本文提出了CROSS基准，旨在评估LVLMs的文化安全推理能力。CROSS包含来自16个国家、三个日常领域和14种语言的1284个多语言视觉基础查询，文化规范的违规行为仅在图像的上下文中被解释时才会出现。我们提出了CROSS-Eval框架，衡量文化意识、规范教育、合规性和帮助性四个关键维度。通过该框架，我们评估了21个领先的LVLMs，结果显示文化安全存在显著差距。为提高模型性能，我们开发了两种增强策略，显著提升了GPT-4o的文化意识和合规性，同时保持了多模态能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型视觉语言模型在文化适宜性响应中的不足，现有方法未能有效评估文化安全性，导致模型在全球应用中的潜在风险。

**核心思路**：提出CROSS基准和CROSS-Eval框架，通过多维度评估LVLMs的文化安全推理能力，强调文化意识和合规性的重要性。

**技术框架**：整体架构包括CROSS基准的构建、CROSS-Eval框架的设计，以及对21个LVLMs的评估，涵盖文化意识、规范教育、合规性和帮助性四个维度。

**关键创新**：CROSS基准的提出是本研究的核心创新，填补了现有多模态安全评估中对文化安全的忽视，提供了系统的评估方法。

**关键设计**：在模型评估中，采用了多语言视觉基础查询，设计了监督微调和偏好调优策略，以提升模型在文化安全方面的表现。

## 📊 实验亮点

实验结果显示，最佳模型在文化意识和合规性方面的得分分别为61.79%和37.73%。通过监督微调和偏好调优，GPT-4o的文化意识提升了60.14%，合规性提升了55.2%，同时在一般多模态理解基准上的性能保持相对稳定。

## 🎯 应用场景

该研究的潜在应用领域包括旅游助手、跨文化交流平台以及任何需要生成文化适宜性内容的人工智能系统。通过提升模型的文化安全性，能够有效减少文化误解和冲突，增强用户体验，促进全球化背景下的文化交流与理解。

## 📄 摘要（原文）

> Large vision-language models (LVLMs) are increasingly deployed in globally distributed applications, such as tourism assistants, yet their ability to produce culturally appropriate responses remains underexplored. Existing multimodal safety benchmarks primarily focus on physical safety and overlook violations rooted in cultural norms, which can result in symbolic harm. To address this gap, we introduce CROSS, a benchmark designed to assess the cultural safety reasoning capabilities of LVLMs. CROSS includes 1,284 multilingual visually grounded queries from 16 countries, three everyday domains, and 14 languages, where cultural norm violations emerge only when images are interpreted in context. We propose CROSS-Eval, an intercultural theory-based framework that measures four key dimensions: cultural awareness, norm education, compliance, and helpfulness. Using this framework, we evaluate 21 leading LVLMs, including mixture-of-experts models and reasoning models. Results reveal significant cultural safety gaps: the best-performing model achieves only 61.79% in awareness and 37.73% in compliance. While some open-source models reach GPT-4o-level performance, they still fall notably short of proprietary models. Our results further show that increasing reasoning capacity improves cultural alignment but does not fully resolve the issue. To improve model performance, we develop two enhancement strategies: supervised fine-tuning with culturally grounded, open-ended data and preference tuning with contrastive response pairs that highlight safe versus unsafe behaviors. These methods substantially improve GPT-4o's cultural awareness (+60.14%) and compliance (+55.2%), while preserving general multimodal capabilities with minimal performance reduction on general multimodal understanding benchmarks.

