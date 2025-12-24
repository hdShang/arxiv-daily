---
layout: default
title: "SEPS: A Separability Measure for Robust Unlearning in LLMs"
---

# SEPS: A Separability Measure for Robust Unlearning in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14832" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14832v2</a>
  <a href="https://arxiv.org/pdf/2505.14832.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14832v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14832v2', 'SEPS: A Separability Measure for Robust Unlearning in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wonje Jeung, Sangyeon Yoon, Albert No

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-05-27)

**备注**: 32 pages

---

## 💡 一句话要点

**提出SEPS框架以解决大语言模型的混合查询遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `机器遗忘` `混合查询` `评估框架` `数据隐私` `模型更新` `个性化推荐`

## 📋 核心要点

1. 现有的遗忘方法在处理混合查询时表现不佳，无法有效区分遗忘和保留内容。
2. 本文提出SEPS框架，通过混合提示策略将遗忘和保留查询整合为统一的训练目标。
3. 实验结果表明，新的方法在复杂场景下的遗忘效果显著提升，能够处理多达八个混合查询。

## 📝 摘要（中文）

机器遗忘旨在从大语言模型中选择性地移除特定知识，确保模型忘记指定内容的同时保留重要信息。现有的遗忘评估指标主要关注模型是否正确回答保留查询和拒绝遗忘查询，但未能考虑到现实场景中遗忘查询通常与保留查询共存的情况。为此，本文提出了SEPS评估框架，明确测量模型在单个提示中遗忘和保留信息的能力。通过在三个基准上的广泛实验，我们识别出现有遗忘方法的两个主要失败模式，并提出了混合提示（MP）遗忘策略，显著提高了遗忘效果，尤其是在复杂场景中表现出色。

## 🔬 方法详解

**问题定义**：本文解决的是大语言模型在处理混合查询时的遗忘问题。现有方法在面对同时出现的遗忘和保留查询时，往往无法有效区分，导致信息遗忘不当。

**核心思路**：论文的核心思路是提出SEPS评估框架，并引入混合提示（MP）遗忘策略，将遗忘和保留查询整合为一个统一的训练目标，以提高模型的遗忘效果。

**技术框架**：整体架构包括两个主要模块：一是SEPS评估框架，用于测量模型在混合查询下的表现；二是MP遗忘策略，通过联合训练来优化模型的遗忘和保留能力。

**关键创新**：最重要的技术创新点在于提出了混合提示遗忘策略，解决了现有方法在多查询场景下的失效问题，使得模型能够在复杂情况下保持更高的遗忘准确性。

**关键设计**：在关键设计上，本文采用了特定的损失函数来平衡遗忘和保留的目标，并在网络结构上进行了调整，以适应混合查询的处理需求。具体参数设置和训练流程在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，采用混合提示遗忘策略的模型在处理复杂查询时，遗忘效果提升了显著，尤其在多达八个混合查询的场景中，模型的表现优于现有基线，展示了更强的鲁棒性和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括数据隐私保护、模型更新和个性化推荐等。通过有效的遗忘机制，模型能够在不损失重要信息的情况下，快速适应新的数据需求，提升用户体验和安全性。未来，该方法可能在法律合规和道德AI等领域产生深远影响。

## 📄 摘要（原文）

> Machine unlearning aims to selectively remove targeted knowledge from Large Language Models (LLMs), ensuring they forget specified content while retaining essential information. Existing unlearning metrics assess whether a model correctly answers retain queries and rejects forget queries, but they fail to capture real-world scenarios where forget queries rarely appear in isolation. In fact, forget and retain queries often coexist within the same prompt, making mixed-query evaluation crucial.
>   We introduce SEPS, an evaluation framework that explicitly measures a model's ability to both forget and retain information within a single prompt. Through extensive experiments across three benchmarks, we identify two key failure modes in existing unlearning methods: (1) untargeted unlearning indiscriminately erases both forget and retain content once a forget query appears, and (2) targeted unlearning overfits to single-query scenarios, leading to catastrophic failures when handling multiple queries. To address these issues, we propose Mixed Prompt (MP) unlearning, a strategy that integrates both forget and retain queries into a unified training objective. Our approach significantly improves unlearning effectiveness, demonstrating robustness even in complex settings with up to eight mixed forget and retain queries in a single prompt.

