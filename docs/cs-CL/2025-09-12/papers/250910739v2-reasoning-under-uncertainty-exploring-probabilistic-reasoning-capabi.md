---
layout: default
title: "Reasoning Under Uncertainty: Exploring Probabilistic Reasoning Capabilities of LLMs"
---

# Reasoning Under Uncertainty: Exploring Probabilistic Reasoning Capabilities of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10739" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10739v2</a>
  <a href="https://arxiv.org/pdf/2509.10739.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10739v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10739v2', 'Reasoning Under Uncertainty: Exploring Probabilistic Reasoning Capabilities of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mobina Pournemat, Keivan Rezaei, Gaurang Sriramanan, Arman Zarei, Jiaxiang Fu, Yang Wang, Hamid Eghbalzadeh, Soheil Feizi

**分类**: cs.CL

**发布日期**: 2025-09-12 (更新: 2025-09-26)

**备注**: 27 pages, 4 figures

---

## 💡 一句话要点

**首个LLM概率推理能力综合研究：揭示优势与局限，探索未来改进方向**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `概率推理` `不确定性推理` `离散概率分布` `模式识别`

## 📋 核心要点

1. 现有LLM在概率推理任务中表现不一致，缺乏对显式概率分布的有效处理。
2. 通过设计模式识别、最大似然估计和样本生成任务，评估LLM的概率推理能力。
3. 实验表明，更大规模的模型表现更优，但在符号表示和上下文长度方面存在局限性。

## 📝 摘要（中文）

本文首次全面研究了大型语言模型（LLM）在显式离散概率分布上的推理能力。通过精心设计的三个任务，即模式识别、最大似然估计和样本生成，评估了模型在给定概率分布观测值的情况下，对联合分布或条件分布进行查询并给出响应的能力。这些任务涵盖了频率分析、边缘化和生成行为等一系列概率技能。实验结果表明，较大型模型在推理和样本生成方面表现出更强的能力，但同时也存在显著的局限性，包括对概率结果表示符号的敏感性以及上下文长度增加导致的性能下降。该研究详细分析了LLM的概率推理能力，并为未来的改进指明了方向。

## 🔬 方法详解

**问题定义**：论文旨在研究大型语言模型（LLM）在处理显式离散概率分布时的推理能力。现有方法缺乏对LLM概率推理能力的系统性评估，并且LLM在处理概率相关任务时表现出不一致性，难以保证结果的可靠性。

**核心思路**：论文的核心思路是通过设计一系列任务来评估LLM在不同概率推理场景下的表现。这些任务涵盖了频率分析、边缘化和生成行为等关键的概率技能，从而全面了解LLM的优势和局限性。通过分析模型在不同任务上的表现，可以揭示影响LLM概率推理能力的因素，并为未来的改进提供指导。

**技术框架**：该研究的技术框架主要包括三个阶段：1) 构建显式离散概率分布；2) 设计三种概率推理任务：模式识别、最大似然估计和样本生成；3) 使用不同的prompting方法，让LLM对概率分布进行查询并生成响应，最后评估LLM的性能。

**关键创新**：该研究最重要的创新在于首次对LLM在显式离散概率分布上的推理能力进行了全面的评估。通过设计专门的任务，揭示了LLM在概率推理方面的优势和局限性，例如对符号表示的敏感性和上下文长度的影响。

**关键设计**：在任务设计方面，模式识别任务旨在评估模型识别概率分布中出现频率最高的结果的能力；最大似然估计任务旨在评估模型根据观测数据估计概率分布参数的能力；样本生成任务旨在评估模型从概率分布中生成样本的能力。研究中使用了不同的prompting方法，例如zero-shot和few-shot prompting，以探索不同prompting策略对模型性能的影响。此外，还考察了不同模型规模和上下文长度对性能的影响。

## 📊 实验亮点

实验结果表明，较大规模的LLM在概率推理任务中表现出更强的能力，但在符号表示和上下文长度方面存在局限性。例如，随着上下文长度的增加，模型性能下降超过60%。此外，模型对概率结果的表示符号非常敏感，细微的符号变化可能导致性能显著下降。

## 🎯 应用场景

该研究成果可应用于提升LLM在风险评估、决策支持、自然语言理解等领域的应用能力。通过深入理解LLM的概率推理能力，可以开发更可靠、更智能的AI系统，例如在金融领域进行风险预测，在医疗领域辅助诊断，以及在自动驾驶领域进行决策。

## 📄 摘要（原文）

> Despite widespread success in language understanding and generation, large language models (LLMs) exhibit unclear and often inconsistent behavior when faced with tasks that require probabilistic reasoning. In this work, we present the first comprehensive study of the reasoning capabilities of LLMs over explicit discrete probability distributions. Given observations from a probability distribution, we evaluate models on three carefully designed tasks, mode identification, maximum likelihood estimation, and sample generation, by prompting them to provide responses to queries about either the joint distribution or its conditionals. These tasks thus probe a range of probabilistic skills, including frequency analysis, marginalization, and generative behavior. Through comprehensive empirical evaluations, we demonstrate that there exists a clear performance gap between smaller and larger models, with the latter demonstrating stronger inference and surprising capabilities in sample generation. Furthermore, our investigations reveal notable limitations, including sensitivity to variations in the notation utilized to represent probabilistic outcomes and performance degradation of over 60% as context length increases. Together, our results provide a detailed understanding of the probabilistic reasoning abilities of LLMs and identify key directions for future improvement.

