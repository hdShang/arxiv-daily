---
layout: default
title: "Don't Take the Premise for Granted: Evaluating the Premise Critique Ability of Large Language Models"
---

# Don't Take the Premise for Granted: Evaluating the Premise Critique Ability of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23715" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23715v2</a>
  <a href="https://arxiv.org/pdf/2505.23715.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23715v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23715v2', 'Don\'t Take the Premise for Granted: Evaluating the Premise Critique Ability of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinzhe Li, Gengxu Li, Yi Chang, Yuan Wu

**分类**: cs.CL

**发布日期**: 2025-05-29 (更新: 2025-11-24)

**备注**: EMNLP 2025 Findings camera-ready version

**🔗 代码/项目**: [GITHUB](https://github.com/MLGroupJLU/Premise_Critique)

---

## 💡 一句话要点

**提出Premise Critique Bench以提升大型语言模型的前提批判能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `前提批判能力` `推理能力` `评估基准` `错误类型` `系统评估`

## 📋 核心要点

1. 现有研究大多在理想环境下评估LLMs的推理能力，忽视了它们在面对有缺陷前提时的脆弱性。
2. 本文提出了前提批判基准（PCBench），通过设计多种错误类型和难度级别，评估LLMs的前提批判能力。
3. 实验结果显示，大多数模型依赖于提示来检测错误，自主批判能力有限，且推理能力与前提批判能力并不总是相关。

## 📝 摘要（中文）

大型语言模型（LLMs）在快速发展的同时，仍然存在一个显著的脆弱性：它们往往不加批判地接受有缺陷或矛盾的前提，从而导致推理效率低下和输出不可靠。本文强调了LLMs具备前提批判能力的重要性，即主动识别和阐述输入前提错误的能力。我们引入了前提批判基准（PCBench），通过四种错误类型和三个难度级别的结合，配合多维度评估指标，对15个代表性LLMs进行了系统评估。研究发现，大多数模型依赖于明确的提示来检测错误，且自主批判能力有限；前提批判能力依赖于问题的难度和错误类型；推理能力与前提批判能力并不总是相关；有缺陷的前提会导致推理模型的过度思考，显著延长响应时间。这些发现突显了增强LLMs主动评估输入有效性的迫切需求。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在面对有缺陷前提时缺乏批判能力的问题。现有方法往往在理想条件下评估模型，未能揭示其在实际应用中的脆弱性。

**核心思路**：论文的核心思路是通过引入前提批判基准（PCBench），系统性地评估LLMs在识别和批判输入前提错误方面的能力，强调主动评估的重要性。

**技术框架**：整体架构包括四种错误类型（直接矛盾、复杂错误、程序性错误等）和三个难度级别，结合多维度评估指标，形成全面的评估体系。

**关键创新**：最重要的技术创新点在于设计了PCBench这一评估工具，能够系统性地揭示LLMs在前提批判能力上的不足，与现有方法相比，提供了更为细致的评估标准。

**关键设计**：在设计中，考虑了不同错误类型对模型表现的影响，设置了多样化的评估指标，确保能够全面反映模型的前提批判能力。

## 📊 实验亮点

实验结果显示，大多数大型语言模型在检测错误时依赖于明确的提示，自主批判能力有限。不同错误类型的检测难度差异明显，直接矛盾的检测相对容易，而复杂或程序性错误则较难识别。这些发现强调了提升LLMs前提批判能力的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、对话系统和自动内容生成等。通过提升LLMs的前提批判能力，可以增强其在复杂场景下的推理可靠性，从而为人机交互提供更为稳健的支持，推动人性化系统的发展。

## 📄 摘要（原文）

> Large language models (LLMs) have witnessed rapid advancements, demonstrating remarkable capabilities. However, a notable vulnerability persists: LLMs often uncritically accept flawed or contradictory premises, leading to inefficient reasoning and unreliable outputs. This emphasizes the significance of possessing the \textbf{Premise Critique Ability} for LLMs, defined as the capacity to proactively identify and articulate errors in input premises. Most existing studies assess LLMs' reasoning ability in ideal settings, largely ignoring their vulnerabilities when faced with flawed premises. Thus, we introduce the \textbf{Premise Critique Bench (PCBench)}, designed by incorporating four error types across three difficulty levels, paired with multi-faceted evaluation metrics. We conducted systematic evaluations of 15 representative LLMs. Our findings reveal: (1) Most models rely heavily on explicit prompts to detect errors, with limited autonomous critique; (2) Premise critique ability depends on question difficulty and error type, with direct contradictions being easier to detect than complex or procedural errors; (3) Reasoning ability does not consistently correlate with the premise critique ability; (4) Flawed premises trigger overthinking in reasoning models, markedly lengthening responses due to repeated attempts at resolving conflicts. These insights underscore the urgent need to enhance LLMs' proactive evaluation of input validity, positioning premise critique as a foundational capability for developing reliable, human-centric systems. The code is available at https://github.com/MLGroupJLU/Premise_Critique.

