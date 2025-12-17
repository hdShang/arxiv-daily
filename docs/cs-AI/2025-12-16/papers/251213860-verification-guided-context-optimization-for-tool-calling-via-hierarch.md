---
layout: default
title: Verification-Guided Context Optimization for Tool Calling via Hierarchical LLMs-as-Editors
---

# Verification-Guided Context Optimization for Tool Calling via Hierarchical LLMs-as-Editors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13860" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13860</a>
  <a href="https://arxiv.org/pdf/2512.13860.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13860" onclick="toggleFavorite(this, '2512.13860', 'Verification-Guided Context Optimization for Tool Calling via Hierarchical LLMs-as-Editors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Henger Li, Shuangjie You, Flavio Di Palo, Yiyue Qian, Ayush Jain

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出VGCO框架，通过分层LLM编辑器优化工具调用上下文，提升工具使用效果。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `工具调用` `大型语言模型` `上下文优化` `分层编辑` `知识库` `自动化` `LLM编辑器`

## 📋 核心要点

1. 现有工具调用方法依赖于为人类编写的文档，与LLM的理解存在偏差，导致工具使用效果不佳。
2. VGCO框架利用LLM作为编辑器，通过分层结构和验证引导，自动优化工具相关的文档和知识库上下文。
3. 实验表明，VGCO在单轮大规模工具调用问题上，显著提升了LLM的准确性、鲁棒性和泛化能力。

## 📝 摘要（中文）

本文提出了一种名为Verification-Guided Context Optimization (VGCO) 的框架，该框架利用大型语言模型 (LLM) 作为编辑器，自动优化与工具相关的文档和知识库上下文，从而提升工具调用的有效性。VGCO 分为两个阶段：首先，评估阶段收集真实世界的失败案例，识别工具及其上下文之间的不匹配；其次，优化阶段通过离线学习，利用结构感知的上下文优化进行分层编辑。LLM 编辑器的创新之处在于：采用与工具调用工作流程自然集成的分层结构；具备状态感知、动作特定和验证引导的特性，从而约束搜索空间并实现高效、有针对性的改进；支持经济高效的子任务专业化，可以通过提示工程大型编辑器模型或通过后训练较小的编辑器模型来实现。与强调多轮推理的先前工作不同，VGCO 专注于单轮、大规模的工具调用问题，并在 LLM 的准确性、鲁棒性和泛化能力方面取得了显著的改进。

## 🔬 方法详解

**问题定义**：现有工具调用方法依赖于人工编写的工具文档和知识库，这些材料通常是为人类设计的，与LLM理解信息的方式存在偏差。尤其是在工业环境中，存在大量功能重叠的工具，导致可扩展性、变异性和歧义性问题，严重影响工具调用的准确性和效率。

**核心思路**：VGCO的核心思路是将LLM作为编辑器，自动地对工具相关的文档和知识库上下文进行优化。通过收集真实世界的失败案例，识别工具及其上下文之间的不匹配，然后利用LLM的编辑能力，对这些上下文进行改进，使其更适合LLM的理解和使用。

**技术框架**：VGCO框架包含两个主要阶段：评估（Evaluation）和优化（Optimization）。评估阶段负责收集真实世界的工具调用失败案例，并分析失败原因，找出工具文档和知识库中存在的问题。优化阶段则利用LLM作为编辑器，对评估阶段发现的问题进行修复和改进。优化过程采用分层编辑的方式，首先对文档的整体结构进行调整，然后逐步细化到具体的细节。

**关键创新**：VGCO的关键创新在于其LLM编辑器的设计。该编辑器采用分层结构，能够自然地融入到工具调用的工作流程中。同时，编辑器具备状态感知、动作特定和验证引导的特性，能够根据当前的状态和需要执行的动作，有针对性地对上下文进行优化。验证引导则通过对编辑结果进行验证，确保优化后的上下文能够提高工具调用的准确性。

**关键设计**：VGCO采用离线学习的方式训练LLM编辑器。在训练过程中，使用大量的工具调用失败案例作为训练数据，通过优化损失函数，使编辑器能够学习到如何根据失败案例对上下文进行改进。此外，VGCO还支持通过提示工程或后训练的方式，对编辑器进行子任务专业化，使其能够更好地处理特定类型的工具调用问题。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13860/aaai2026/framework_diagram.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13860/aaai2026/accuracy_line_graph_Claude_Sonnet_3.5.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13860/aaai2026/accuracy_line_graph_Claude_Sonnet_3.7.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

VGCO在单轮大规模工具调用问题上取得了显著的性能提升。实验结果表明，VGCO能够显著提高LLM在工具调用任务中的准确性、鲁棒性和泛化能力。具体的数据提升幅度在论文中给出，相较于基线方法有显著提高。

## 🎯 应用场景

VGCO框架可应用于各种需要工具调用的场景，例如智能助手、自动化运维、代码生成等。通过自动优化工具相关的文档和知识库上下文，可以显著提高工具调用的准确性和效率，降低人工维护成本，并提升用户体验。该研究对于推动LLM在实际应用中的落地具有重要意义。

## 📄 摘要（原文）

> Tool calling enables large language models (LLMs) to interact with external environments through tool invocation, providing a practical way to overcome the limitations of pretraining. However, the effectiveness of tool use depends heavily on the quality of the associated documentation and knowledge base context. These materials are usually written for human users and are often misaligned with how LLMs interpret information. This problem is even more pronounced in industrial settings, where hundreds of tools with overlapping functionality create challenges in scalability, variability, and ambiguity. We propose Verification-Guided Context Optimization (VGCO), a framework that uses LLMs as editors to automatically refine tool-related documentation and knowledge base context. VGCO works in two stages. First, Evaluation collects real-world failure cases and identifies mismatches between tools and their context. Second, Optimization performs hierarchical editing through offline learning with structure-aware, in-context optimization. The novelty of our LLM editors has three main aspects. First, they use a hierarchical structure that naturally integrates into the tool-calling workflow. Second, they are state-aware, action-specific, and verification-guided, which constrains the search space and enables efficient, targeted improvements. Third, they enable cost-efficient sub-task specialization, either by prompt engineering large editor models or by post-training smaller editor models. Unlike prior work that emphasizes multi-turn reasoning, VGCO focuses on the single-turn, large-scale tool-calling problem and achieves significant improvements in accuracy, robustness, and generalization across LLMs.

