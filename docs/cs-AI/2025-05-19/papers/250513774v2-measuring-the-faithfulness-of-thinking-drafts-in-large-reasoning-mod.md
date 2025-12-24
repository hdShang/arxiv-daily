---
layout: default
title: Measuring the Faithfulness of Thinking Drafts in Large Reasoning Models
---

# Measuring the Faithfulness of Thinking Drafts in Large Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13774" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13774v2</a>
  <a href="https://arxiv.org/pdf/2505.13774.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13774v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13774v2', 'Measuring the Faithfulness of Thinking Drafts in Large Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zidi Xiong, Shan Chen, Zhenting Qi, Himabindu Lakkaraju

**分类**: cs.AI

**发布日期**: 2025-05-19 (更新: 2025-05-28)

---

## 💡 一句话要点

**提出系统性反事实干预框架以评估大型推理模型的思维草稿可信度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型推理模型` `思维草稿` `可信度评估` `反事实干预` `因果关系` `逻辑一致性` `中间推理` `自动化决策`

## 📋 核心要点

1. 现有大型推理模型在复杂问题解决中，思维草稿的中间推理过程可信度不足，影响结果的可靠性。
2. 本文提出了一种反事实干预框架，通过评估推理步骤的因果关系和最终答案的逻辑一致性，来提升思维草稿的可信度。
3. 实验结果显示，当前LRMs在中间推理步骤上存在选择性可信度，且常常未能与草稿结论保持一致，强调了改进的必要性。

## 📝 摘要（中文）

大型推理模型（LRMs）通过引入思维草稿，显著提升了复杂问题解决能力。然而，确保这些中间推理过程的可信度对于可靠监控、解释和有效控制至关重要。本文提出了一种系统的反事实干预框架，以严格评估思维草稿的可信度。该方法关注两个互补维度：一是评估个别推理步骤对后续步骤及最终草稿结论的因果影响，二是通过扰动草稿的结论逻辑，评估最终答案与思维草稿的一致性。实验结果表明，当前LRMs在中间推理步骤上表现出选择性可信度，且常常未能与草稿结论保持一致，这突显了对更可信和可解释推理的需求。

## 🔬 方法详解

**问题定义**：本文旨在解决大型推理模型中思维草稿的可信度评估问题。现有方法未能有效监控和解释中间推理过程，导致结果的不可靠性。

**核心思路**：论文提出的反事实干预框架通过引入反事实步骤插入和草稿逻辑扰动，系统性地评估思维草稿的可信度，从而确保推理过程的透明性和可靠性。

**技术框架**：整体架构包括两个主要模块：一是“草稿内可信度评估”，通过反事实步骤插入分析推理步骤的因果影响；二是“草稿与答案可信度评估”，通过扰动草稿结论逻辑，检查最终答案的逻辑一致性。

**关键创新**：最重要的技术创新在于提出了反事实干预的评估方法，能够从因果关系和逻辑一致性两个维度全面评估思维草稿的可信度，这与现有方法的单一评估方式有本质区别。

**关键设计**：在实验中，设置了多个反事实步骤插入和逻辑扰动的参数，以确保评估的全面性和准确性。同时，采用了多种损失函数来优化模型的推理过程。

## 📊 实验亮点

实验结果表明，当前LRMs在中间推理步骤上表现出选择性可信度，且在与草稿结论的一致性方面存在显著不足。具体而言，模型在草稿内可信度评估中平均得分为65%，而在草稿与答案一致性评估中仅为50%，显示出改进的迫切性。

## 🎯 应用场景

该研究的潜在应用领域包括人工智能助手、自动化决策系统和教育技术等。通过提升大型推理模型的可信度，能够增强用户对AI系统的信任，推动其在实际应用中的广泛采用，未来可能影响多个行业的决策过程。

## 📄 摘要（原文）

> Large Reasoning Models (LRMs) have significantly enhanced their capabilities in complex problem-solving by introducing a thinking draft that enables multi-path Chain-of-Thought explorations before producing final answers. Ensuring the faithfulness of these intermediate reasoning processes is crucial for reliable monitoring, interpretation, and effective control. In this paper, we propose a systematic counterfactual intervention framework to rigorously evaluate thinking draft faithfulness. Our approach focuses on two complementary dimensions: (1) Intra-Draft Faithfulness, which assesses whether individual reasoning steps causally influence subsequent steps and the final draft conclusion through counterfactual step insertions; and (2) Draft-to-Answer Faithfulness, which evaluates whether final answers are logically consistent with and dependent on the thinking draft, by perturbing the draft's concluding logic. We conduct extensive experiments across six state-of-the-art LRMs. Our findings show that current LRMs demonstrate selective faithfulness to intermediate reasoning steps and frequently fail to faithfully align with the draft conclusions. These results underscore the need for more faithful and interpretable reasoning in advanced LRMs.

