---
layout: default
title: "Inclusion Arena: An Open Platform for Evaluating Large Foundation Models with Real-World Apps"
---

# Inclusion Arena: An Open Platform for Evaluating Large Foundation Models with Real-World Apps

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11452" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11452v2</a>
  <a href="https://arxiv.org/pdf/2508.11452.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11452v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11452v2', 'Inclusion Arena: An Open Platform for Evaluating Large Foundation Models with Real-World Apps')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kangyu Wang, Hongliang He, Lin Liu, Ruiqi Liang, Zhenzhong Lan, Jianguo Li

**分类**: cs.AI, cs.CL, cs.HC

**发布日期**: 2025-08-15 (更新: 2025-09-02)

**备注**: Our platform is publicly accessible at https://www.tbox.cn/about/model-ranking

---

## 💡 一句话要点

**提出Inclusion Arena以解决LLMs与真实应用评估的不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多模态模型` `模型评估` `用户反馈` `实时排行榜`

## 📋 核心要点

1. 现有的评估方法多依赖静态数据集，无法真实反映大型语言模型在实际应用中的表现，存在评估不准确的问题。
2. Inclusion Arena通过实时收集用户反馈，结合成对比较的方法，确保评估结果更贴近实际使用场景，提高了模型排名的可靠性。
3. 实验证明，Inclusion Arena在数据传递性上优于传统众包数据集，并显著降低了恶意操控的风险，提升了模型评估的稳定性。

## 📝 摘要（中文）

大型语言模型（LLMs）和多模态大型语言模型（MLLMs）在各类场景中展现出接近人类的性能。然而，现有的基准测试和排行榜大多依赖静态数据集或众包的通用提示，无法真实反映模型在实际应用中的表现。为此，本文提出了Inclusion Arena，一个基于人类反馈的实时排行榜，旨在通过自然用户交互中的成对模型比较来评估模型性能。该平台采用Bradley-Terry模型，并引入了Placement Matches和Proximity Sampling等创新机制，以提高模型排名的可靠性和稳定性。实证分析表明，Inclusion Arena能够有效降低恶意操控风险，并促进LLMs和MLLMs的用户中心化发展。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型语言模型评估方法在真实应用场景中表现不佳的问题。现有方法往往依赖静态数据集，无法准确反映模型的实际性能。

**核心思路**：Inclusion Arena通过实时收集来自AI驱动应用的用户反馈，结合成对模型比较的方式，确保评估结果更具实用性和准确性。

**技术框架**：该平台的整体架构包括用户交互模块、反馈收集模块和模型排名模块。用户在使用应用时进行模型比较，系统实时收集反馈并更新模型排名。

**关键创新**：本文的主要创新在于引入Placement Matches和Proximity Sampling机制，前者用于快速估计新模型的初始评分，后者则优先比较能力相近的模型，以最大化信息增益和提升评分稳定性。

**关键设计**：在模型排名过程中，采用Bradley-Terry模型作为基础框架，结合上述创新机制，确保评估过程的高效性和准确性。

## 📊 实验亮点

实验结果显示，Inclusion Arena在模型排名的可靠性和稳定性方面表现优异，相较于传统众包数据集，其数据传递性显著提高，且有效降低了恶意操控的风险。这些结果表明，该平台能够为LLMs和MLLMs的评估提供更为可信的依据。

## 🎯 应用场景

Inclusion Arena的潜在应用场景包括AI助手、智能客服和内容生成等领域。通过提供更准确的模型评估，能够帮助开发者选择最适合的模型，从而提升用户体验和应用效果。未来，该平台可能推动大型语言模型的持续优化和用户中心化发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) have ushered in a new era of AI capabilities, demonstrating near-human-level performance across diverse scenarios. While numerous benchmarks (e.g., MMLU) and leaderboards (e.g., Chatbot Arena) have been proposed to help evolve the development of LLMs and MLLMs, most rely on static datasets or crowdsourced general-domain prompts, often falling short of reflecting performance in real-world applications. To bridge this critical gap, we present Inclusion Arena, a live leaderboard that ranks models based on human feedback collected directly from AI-powered applications. Our platform integrates pairwise model comparisons into natural user interactions, ensuring evaluations reflect practical usage scenarios. For robust model ranking, we employ the Bradley-Terry model augmented with two key innovations: (1) Placement Matches, a cold-start mechanism to quickly estimate initial ratings for newly integrated models, and (2) Proximity Sampling, an intelligent comparison strategy that prioritizes battles between models of similar capabilities to maximize information gain and enhance rating stability. Extensive empirical analyses and simulations demonstrate that Inclusion Arena yields reliable and stable rankings, exhibits higher data transitivity compared to general crowdsourced datasets, and significantly mitigates the risk of malicious manipulation. By fostering an open alliance between foundation models and real-world applications, Inclusion Arena aims to accelerate the development of LLMs and MLLMs truly optimized for practical, user-centric deployments. The platform is publicly accessible at https://www.tbox.cn/about/model-ranking.

