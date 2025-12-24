---
layout: default
title: Are LLMs Better Formalizers than Solvers on Complex Problems?
---

# Are LLMs Better Formalizers than Solvers on Complex Problems?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13252" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13252v2</a>
  <a href="https://arxiv.org/pdf/2505.13252.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13252v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13252v2', 'Are LLMs Better Formalizers than Solvers on Complex Problems?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rikhil Amonkar, May Lai, Ronan Le Bras, Li Zhang

**分类**: cs.CL

**发布日期**: 2025-05-19 (更新: 2025-09-19)

---

## 💡 一句话要点

**评估LLM在复杂问题中的形式化能力与求解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `逻辑推理` `形式化工具` `约束满足问题` `性能评估` `系统分析` `智能系统`

## 📋 核心要点

1. 现有研究普遍认为LLM作为形式化工具优于作为求解器，但在实际应用中表现并不理想。
2. 论文通过系统评估不同LLM在复杂约束满足问题中的表现，提出了对现有方法的深入分析和改进建议。
3. 实验结果显示，在少量样本设置下，LLM作为形式化工具的性能低于作为求解器的LLM，揭示了当前LLM的局限性。

## 📝 摘要（中文）

近年来的研究趋势提倡将大型语言模型（LLMs）作为形式化工具，而非直接求解逻辑推理问题。LLM生成一个形式化程序，通过外部求解器推导解决方案。尽管LLM作为形式化工具在性能上被广泛报道优于作为求解器的LLM，但我们表明这种优势在现实约束满足问题上并不成立。通过对6个LLM和5种管道的系统评估，我们发现，在少量样本设置下，LLM作为形式化工具的表现不如作为求解器的LLM。当前LLM在生成形式化程序的能力有限，导致其在复杂性上无法扩展，且存在硬编码解决方案和过多推理令牌的问题。我们提供了详细分析和可行的改进建议，以推动未来研究。

## 🔬 方法详解

**问题定义**：本论文旨在解决LLM在复杂约束满足问题中的表现不足，尤其是LLM作为形式化工具的有效性。现有方法在生成形式化程序时存在能力有限、无法扩展复杂性等痛点。

**核心思路**：论文的核心思路是通过系统评估不同LLM在形式化和求解任务中的表现，揭示LLM作为形式化工具的局限性，并提出改进建议。

**技术框架**：整体架构包括对6个LLM的评估，涵盖4种大型推理模型和5种管道，采用两种形式化类型。评估过程包括少量样本设置下的性能对比。

**关键创新**：论文的关键创新在于系统性地比较LLM作为形式化工具与求解器的表现，提出了LLM在复杂问题中未能实现的准确性、鲁棒性和效率的实证分析。

**关键设计**：在实验中，设置了多种参数以评估LLM的生成能力，关注推理令牌的使用和硬编码解决方案的影响，确保评估的全面性和准确性。

## 📊 实验亮点

实验结果表明，在少量样本设置下，LLM作为形式化工具的表现显著低于作为求解器的LLM，具体性能数据未公开，但揭示了当前LLM在复杂问题处理中的局限性，需进一步研究改进。

## 🎯 应用场景

该研究的潜在应用领域包括逻辑推理、自动化决策和复杂系统建模等。通过改进LLM作为形式化工具的能力，可以提升其在实际问题解决中的有效性，推动智能系统的进一步发展。

## 📄 摘要（原文）

> A trending line of recent work advocates for using large language models (LLMs) as formalizers instead of as end-to-end solvers for logical reasoning problems. Instead of generating the solution, the LLM generates a formal program that derives a solution via an external solver. While performance gain of the seemingly scalable LLM-as-formalizer over the seemingly unscalable LLM-as-solver has been widely reported, we show that this superiority does not hold on real-life constraint satisfaction problems. On 4 domains, we systematically evaluate 6 LLMs including 4 large reasoning models with inference-time scaling, paired with 5 pipelines including 2 types of formalism. We show that in few-shot settings, LLM-as-formalizer underperforms LLM-as-solver. While LLM-as-formalizer promises accuracy, robustness, faithfulness, and efficiency, we observe that the present LLMs do not yet deliver any of those, as their limited ability to generate formal programs leads to failure to scale with complexity, hard-coded solutions, and excessive reasoning tokens. We present our detailed analysis and actionable remedies to drive future research that improves LLM-as-formalizer.

