---
layout: default
title: One Battle After Another: Probing LLMs' Limits on Multi-Turn Instruction Following with a Benchmark Evolving Framework
---

# One Battle After Another: Probing LLMs' Limits on Multi-Turn Instruction Following with a Benchmark Evolving Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.03508" class="toolbar-btn" target="_blank">📄 arXiv: 2511.03508</a>
  <a href="https://arxiv.org/pdf/2511.03508.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03508" onclick="toggleFavorite(this, '2511.03508', 'One Battle After Another: Probing LLMs\' Limits on Multi-Turn Instruction Following with a Benchmark Evolving Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Jia, Ye Shen, Xiujie Song, Kaiwei Zhang, Shibo Wang, Dun Pei, Xiangyang Zhu, Guangtao Zhai

**分类**: cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出EvolIF框架，用于评估LLM在多轮交互中指令跟随能力，并揭示现有模型的局限性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮对话` `指令跟随` `LLM评估` `用户模拟` `心流理论`

## 📋 核心要点

1. 现有LLM评测基准在多轮对话指令跟随能力评估方面存在局限性，无法模拟真实用户交互。
2. 提出EvolIF框架，通过三层跟踪机制和查询合成代理，模拟用户连续交互行为，更贴近实际。
3. 实验结果表明，GPT-5在EvolIF基准上表现最佳，但在长程对话中仍存在鲁棒性问题。

## 📝 摘要（中文）

评估大型语言模型（LLM）在多主题对话中指令跟随能力至关重要，但也极具挑战性。现有的评测基准通常仅限于固定轮数，容易达到饱和，并且未能充分考虑用户的交互体验。本文提出了一个新颖的框架，该框架由三层跟踪机制和一个查询合成代理支持，以模拟连续的用户行为。结合心流理论，引入了以过程为中心的指标，并在用户耐心耗尽时终止对话评估。基于此框架，提出了EvolIF，一个涵盖12个约束组的演进基准。结果表明，GPT-5表现出色，能够维持14轮对话，鲁棒性达到66.40%。它比Gemini-3.0-Pro高出5.59%，而其他模型则落后。

## 🔬 方法详解

**问题定义**：论文旨在解决现有LLM评测基准在评估多轮对话中指令跟随能力时的不足。现有方法通常采用固定轮数的对话，无法模拟真实用户交互的动态性和复杂性，容易出现饱和现象，并且忽略了用户在交互过程中的耐心程度。这导致对LLM真实指令跟随能力的评估不够准确和全面。

**核心思路**：论文的核心思路是通过构建一个更贴近真实用户交互场景的评测框架，来更准确地评估LLM的指令跟随能力。该框架模拟用户在对话中的连续行为，并根据用户耐心程度动态调整对话轮数，从而避免了固定轮数带来的局限性。同时，引入了以过程为中心的指标，更全面地评估LLM在整个交互过程中的表现。

**技术框架**：EvolIF框架包含三个主要层次：用户模拟层、对话管理层和LLM交互层。用户模拟层负责生成模拟用户查询，模拟用户行为。对话管理层负责跟踪对话状态，维护对话历史，并根据用户耐心程度决定是否终止对话。LLM交互层负责接收用户查询，调用LLM生成回复，并将回复返回给用户模拟层。框架还包含一个查询合成代理，用于生成多样化的用户查询。

**关键创新**：EvolIF框架的关键创新在于其动态的对话轮数控制和以过程为中心的评估指标。传统的评测基准通常采用固定轮数的对话，而EvolIF框架则根据用户耐心程度动态调整对话轮数，更贴近真实用户交互场景。此外，EvolIF框架引入了以过程为中心的指标，例如对话一致性、信息完整性和用户满意度，更全面地评估LLM在整个交互过程中的表现。

**关键设计**：EvolIF框架的关键设计包括：1) 三层跟踪机制，用于跟踪对话状态和用户行为；2) 查询合成代理，用于生成多样化的用户查询；3) 基于心流理论的用户耐心模型，用于动态调整对话轮数；4) 以过程为中心的评估指标，用于全面评估LLM的指令跟随能力。具体的参数设置和网络结构等技术细节在论文中未详细描述，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.03508/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.03508/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.03508/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，GPT-5在EvolIF基准上表现最佳，能够维持14轮对话，鲁棒性达到66.40%。GPT-5的性能优于Gemini-3.0-Pro 5.59%，但其他模型表现相对落后。这些结果揭示了现有LLM在多轮交互指令跟随能力方面的差距，并为未来的研究方向提供了参考。

## 🎯 应用场景

该研究成果可应用于LLM的评测与优化，帮助开发者更全面地了解LLM在多轮交互场景下的指令跟随能力。通过EvolIF框架，可以更有效地发现LLM的不足之处，并针对性地进行改进，从而提升LLM在实际应用中的性能和用户体验。此外，该框架也可以用于训练LLM，提高其在多轮对话中的指令跟随能力。

## 📄 摘要（原文）

> Evaluating LLMs' instruction-following ability in multi-topic dialogues is essential yet challenging. Existing benchmarks are limited to a fixed number of turns, susceptible to saturation and failing to account for users' interactive experience. In this work, we propose a novel framework backed by a three-layer tracking mechanism and a query synthesis agent to mimic sequential user behaviors. Incorporating Flow Theory, we introduce process-centric metrics and terminate a conversational evaluation only upon exhausting user patience. Upon this framework, we present EvolIF, an evolving benchmark covering 12 constraint groups. Results indicate that GPT-5 excels, sustaining 14 turns with 66.40% robustness. It outperforms Gemini-3.0-Pro by a margin of 5.59%, while other models trail behind. Resources are available atthis https URL.

