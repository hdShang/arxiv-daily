---
layout: default
title: Can LLMs Reason Abstractly Over Math Word Problems Without CoT? Disentangling Abstract Formulation From Arithmetic Computation
---

# Can LLMs Reason Abstractly Over Math Word Problems Without CoT? Disentangling Abstract Formulation From Arithmetic Computation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23701" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23701v1</a>
  <a href="https://arxiv.org/pdf/2505.23701.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23701v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23701v1', 'Can LLMs Reason Abstractly Over Math Word Problems Without CoT? Disentangling Abstract Formulation From Arithmetic Computation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziling Cheng, Meng Cao, Leila Pishdad, Yanshuai Cao, Jackie Chi Kit Cheung

**分类**: cs.CL

**发布日期**: 2025-05-29

---

## 💡 一句话要点

**提出分离评估方法以提升大语言模型在数学问题上的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `数学推理` `抽象表述` `算术计算` `分离评估` `链式推理` `GSM8K` `SVAMP`

## 📋 核心要点

1. 现有的评估方法将最终答案作为推理能力的代理，但未能区分抽象表述与算术计算的独立性。
2. 论文提出通过分离评估的方法，明确区分抽象表述与算术计算的影响，以更准确地评估模型能力。
3. 实验结果显示，Llama-3和Qwen2.5在算术计算上存在显著瓶颈，而抽象表述能力相对较强，挑战了传统观点。

## 📝 摘要（中文）

现有的大语言模型（LLMs）在数学文字问题的评估中，常用最终答案作为指标，然而这种方法混淆了抽象表述与算术计算两种不同的技能。通过对GSM8K和SVAMP数据集的分离评估，研究发现Llama-3和Qwen2.5模型的最终答案准确率主要受限于算术计算，而非抽象表述。与普遍看法相反，研究表明链式推理（CoT）主要有助于计算，对抽象表述的影响有限。机制分析显示，这两种技能在单次前向传播中是联合组成的，模型首先捕捉问题的抽象，然后进行计算。这些发现强调了分离评估的必要性，以准确评估LLM的推理能力并指导未来的改进。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有评估方法混淆抽象表述与算术计算的问题，导致对大语言模型推理能力的误判。

**核心思路**：通过分离评估的方式，明确区分抽象表述与算术计算的影响，揭示模型在这两方面的真实能力。

**技术框架**：研究采用了GSM8K和SVAMP数据集，设计了抽象-计算机制，模型首先进行问题抽象，然后执行计算。

**关键创新**：本研究的创新在于提出了分离评估方法，强调抽象表述与算术计算的独立性，挑战了链式推理对抽象能力的传统看法。

**关键设计**：在实验中，采用了不同规模的模型（1B-32B），并通过因果补丁验证抽象能力的存在、可转移性和可组合性，确保评估的准确性。

## 📊 实验亮点

实验结果表明，Llama-3和Qwen2.5在算术计算上的准确率显著低于抽象表述，最终答案的准确率主要受限于计算步骤。具体数据显示，未使用链式推理的情况下，模型在算术计算上的表现明显低于抽象能力，强调了分离评估的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和数学问题求解工具。通过更准确的评估方法，可以帮助开发更强大的大语言模型，提升其在数学推理和教育领域的实际应用价值。未来，这种分离评估方法可能会被广泛应用于其他类型的推理任务中。

## 📄 摘要（原文）

> Final-answer-based metrics are commonly used for evaluating large language models (LLMs) on math word problems, often taken as proxies for reasoning ability. However, such metrics conflate two distinct sub-skills: abstract formulation (capturing mathematical relationships using expressions) and arithmetic computation (executing the calculations). Through a disentangled evaluation on GSM8K and SVAMP, we find that the final-answer accuracy of Llama-3 and Qwen2.5 (1B-32B) without CoT is overwhelmingly bottlenecked by the arithmetic computation step and not by the abstract formulation step. Contrary to the common belief, we show that CoT primarily aids in computation, with limited impact on abstract formulation. Mechanistically, we show that these two skills are composed conjunctively even in a single forward pass without any reasoning steps via an abstract-then-compute mechanism: models first capture problem abstractions, then handle computation. Causal patching confirms these abstractions are present, transferable, composable, and precede computation. These behavioural and mechanistic findings highlight the need for disentangled evaluation to accurately assess LLM reasoning and to guide future improvements.

