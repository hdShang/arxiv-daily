---
layout: default
title: "LARC: Towards Human-level Constrained Retrosynthesis Planning through an Agentic Framework"
---

# LARC: Towards Human-level Constrained Retrosynthesis Planning through an Agentic Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11860" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11860v1</a>
  <a href="https://arxiv.org/pdf/2508.11860.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11860v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11860v1', 'LARC: Towards Human-level Constrained Retrosynthesis Planning through an Agentic Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Frazier N. Baker, Daniel Adu-Ampratwum, Reza Averly, Botao Yu, Huan Sun, Xia Ning

**分类**: cs.AI, cs.CL

**发布日期**: 2025-08-16

**备注**: 24 pages, 5 figures

---

## 💡 一句话要点

**提出LARC框架以解决受限逆合成规划问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `逆合成规划` `大型语言模型` `代理评估` `化学合成` `工具推理` `路径生成` `约束优化`

## 📋 核心要点

1. 现有的逆合成规划方法在处理复杂约束时表现不佳，难以有效支持科学研究。
2. LARC框架通过引入代理评估机制，结合工具推理，优化逆合成路径生成过程。
3. 在48个受限逆合成任务中，LARC的成功率达到72.9%，显著优于传统LLM方法。

## 📝 摘要（中文）

大型语言模型（LLM）代理评估器利用专门工具来支持LLM的理性决策，使其在科学发现中表现出色，尤其是在受限逆合成规划中。受限逆合成规划是化学领域一项重要而具有挑战性的过程，旨在从商业可得的起始材料识别合成路径，同时满足实际约束。本文提出了LARC，这是首个基于LLM的代理框架，用于受限逆合成规划。LARC通过代理评估约束，将代理反馈与基于工具的推理直接融入逆合成规划过程中。我们在48个受限逆合成规划任务上对LARC进行了严格评估，成功率达到72.9%，显著超越了LLM基线，并在更短时间内接近人类专家水平。LARC框架具有可扩展性，为人类专家提供了有效的代理工具或共同科学家的第一步。

## 🔬 方法详解

**问题定义**：本文旨在解决受限逆合成规划中的路径生成问题。现有方法在面对复杂约束时，往往无法有效地找到合适的合成路线，限制了其在实际应用中的有效性。

**核心思路**：LARC框架的核心思路是通过引入代理评估机制，将约束评估直接整合到逆合成规划过程中。通过代理反馈，LARC能够在生成合成路径时更好地遵循实际约束，从而提高成功率。

**技术框架**：LARC的整体架构包括三个主要模块：首先是输入处理模块，负责解析起始材料和目标分子；其次是路径生成模块，利用LLM生成可能的合成路径；最后是代理评估模块，通过工具推理对生成的路径进行约束评估和优化。

**关键创新**：LARC的主要创新在于将代理评估机制与逆合成规划紧密结合，形成了一个闭环反馈系统。这一设计使得生成的路径不仅符合化学合成的实际要求，还能在时间效率上接近人类专家的水平。

**关键设计**：在LARC中，关键参数包括约束类型的定义、路径生成的算法选择以及代理评估的反馈机制。损失函数设计上，考虑了路径的合成可行性和约束满足度，以确保生成的路径具有实际应用价值。

## 📊 实验亮点

LARC在48个受限逆合成规划任务中的成功率达到72.9%，显著高于传统LLM基线。这一结果表明，LARC不仅在路径生成的准确性上有显著提升，同时在时间效率上也接近人类专家水平，为化学合成提供了新的解决方案。

## 🎯 应用场景

LARC框架在化学合成领域具有广泛的应用潜力，能够帮助化学家快速识别合成路线，尤其是在面对复杂约束时。其有效性和高成功率使其成为未来化学研究中不可或缺的工具，可能推动新材料和药物的开发。随着技术的进步，LARC有望扩展到其他科学领域，成为跨学科研究的有力助手。

## 📄 摘要（原文）

> Large language model (LLM) agent evaluators leverage specialized tools to ground the rational decision-making of LLMs, making them well-suited to aid in scientific discoveries, such as constrained retrosynthesis planning. Constrained retrosynthesis planning is an essential, yet challenging, process within chemistry for identifying synthetic routes from commercially available starting materials to desired target molecules, subject to practical constraints. Here, we present LARC, the first LLM-based Agentic framework for Retrosynthesis planning under Constraints. LARC incorporates agentic constraint evaluation, through an Agent-as-a-Judge, directly into the retrosynthesis planning process, using agentic feedback grounded in tool-based reasoning to guide and constrain route generation. We rigorously evaluate LARC on a carefully curated set of 48 constrained retrosynthesis planning tasks across 3 constraint types. LARC achieves a 72.9% success rate on these tasks, vastly outperforming LLM baselines and approaching human expert-level success in substantially less time. The LARC framework is extensible, and serves as a first step towards an effective agentic tool or a co-scientist to human experts for constrained retrosynthesis.

