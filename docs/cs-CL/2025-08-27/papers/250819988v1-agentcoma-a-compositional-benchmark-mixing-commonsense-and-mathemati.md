---
layout: default
title: "AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios"
---

# AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19988" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19988v1</a>
  <a href="https://arxiv.org/pdf/2508.19988.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19988v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19988v1', 'AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lisa Alazraki, Lihu Chen, Ana Brassard, Joe Stacey, Hossein A. Rahmani, Marek Rei

**分类**: cs.CL

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出AgentCoMa以解决混合常识与数学推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `常识推理` `数学推理` `组合基准` `模型评估` `可解释性分析` `人机交互` `智能助手`

## 📋 核心要点

1. 现有的组合基准测试通常只关注常识或数学推理，缺乏对两者结合的评估，导致LLMs在实际应用中表现不佳。
2. 本文提出了AgentCoMa基准，要求每个任务同时包含常识推理和数学推理，以更真实地模拟现实世界的任务需求。
3. 实验结果显示，LLMs在组合任务中的准确率平均下降约30%，而非专家人类标注者的表现则保持高水平，揭示了模型的脆弱性。

## 📝 摘要（中文）

大型语言模型（LLMs）在复杂的常识和数学问题上取得了高准确率，但现有的组合基准测试通常只关注常识或数学推理。本文提出了Agentic Commonsense and Math基准（AgentCoMa），每个组合任务都需要一个常识推理步骤和一个数学推理步骤。我们对61个不同规模、模型家族和训练策略的LLMs进行了测试，发现LLMs通常能够单独解决这两个步骤，但当两者结合时，准确率平均下降约30%。这一性能差距显著高于以往组合基准的结果。此外，非专家人类标注者在AgentCoMa中能够以同样高的准确率解决组合问题及其单独步骤。我们的研究强调了在混合类型组合推理中的模型脆弱性，并为未来的改进提供了测试平台。

## 🔬 方法详解

**问题定义**：本文旨在解决现有组合基准测试中缺乏对常识与数学推理结合的评估问题。现有方法在处理复杂任务时，往往只关注单一推理类型，导致LLMs在实际应用中的性能不足。

**核心思路**：论文提出AgentCoMa基准，设计每个任务同时包含常识推理和数学推理步骤，以更好地模拟真实场景中的复杂推理需求。通过这种组合，研究者能够更全面地评估LLMs的推理能力。

**技术框架**：整体架构包括任务设计、模型评估和可解释性分析三个主要模块。任务设计部分创建了包含常识与数学推理的组合问题，模型评估则对61个不同的LLMs进行性能测试，可解释性分析则通过神经元模式、注意力图和成员推断等方法深入理解模型表现。

**关键创新**：最重要的技术创新在于提出了AgentCoMa基准，强调了常识与数学推理的结合对LLMs性能的影响。这一基准不仅揭示了模型的脆弱性，还为未来的研究提供了新的方向。

**关键设计**：在实验中，采用了多种模型规模和训练策略，确保评估的全面性。损失函数和网络结构的具体细节未在摘要中明确，但可解释性分析使用了神经元激活模式和注意力机制，以探讨模型在不同推理步骤中的表现。

## 📊 实验亮点

实验结果显示，LLMs在组合任务中的准确率平均下降约30%，而非专家人类标注者的表现则保持高水平，显示出模型在处理混合推理时的脆弱性。这一发现为未来的模型改进提供了重要依据。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能助手和自动化决策系统等，能够帮助开发更智能的LLMs，以应对复杂的现实世界任务。通过改进模型在混合推理任务中的表现，未来可以提升人机交互的自然性和有效性。

## 📄 摘要（原文）

> Large Language Models (LLMs) have achieved high accuracy on complex commonsense and mathematical problems that involve the composition of multiple reasoning steps. However, current compositional benchmarks testing these skills tend to focus on either commonsense or math reasoning, whereas LLM agents solving real-world tasks would require a combination of both. In this work, we introduce an Agentic Commonsense and Math benchmark (AgentCoMa), where each compositional task requires a commonsense reasoning step and a math reasoning step. We test it on 61 LLMs of different sizes, model families, and training strategies. We find that LLMs can usually solve both steps in isolation, yet their accuracy drops by ~30% on average when the two are combined. This is a substantially greater performance gap than the one we observe in prior compositional benchmarks that combine multiple steps of the same reasoning type. In contrast, non-expert human annotators can solve the compositional questions and the individual steps in AgentCoMa with similarly high accuracy. Furthermore, we conduct a series of interpretability studies to better understand the performance gap, examining neuron patterns, attention maps and membership inference. Our work underscores a substantial degree of model brittleness in the context of mixed-type compositional reasoning and offers a test bed for future improvement.

