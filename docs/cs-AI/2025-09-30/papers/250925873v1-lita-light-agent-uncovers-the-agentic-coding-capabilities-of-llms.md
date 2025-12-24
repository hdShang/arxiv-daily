---
layout: default
title: "Lita: Light Agent Uncovers the Agentic Coding Capabilities of LLMs"
---

# Lita: Light Agent Uncovers the Agentic Coding Capabilities of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25873" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25873v1</a>
  <a href="https://arxiv.org/pdf/2509.25873.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25873v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25873v1', 'Lita: Light Agent Uncovers the Agentic Coding Capabilities of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hankun Dai, Maoquan Wang, Mengnan Qi, Yikai Zhang, Zijian Jin, Yongqiang Yao, Yufan Huang, Shengyu Fu, Elsie Nallipogu

**分类**: cs.AI, cs.CL, cs.LG, cs.PL, cs.SE

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**Lita：轻量级Agent揭示LLM的Agentic编码能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码Agent` `轻量化设计` `编码能力评估` `自动化代码生成`

## 📋 核心要点

1. 现有代码Agent设计依赖复杂工作流和工具集，过度依赖提示调优，掩盖模型真实能力，且pipeline成本高昂。
2. Lita通过最小化手动设计，保留自主Agent基本要素，实现轻量化，从而更真实统一地评估LLM的编码能力。
3. 实验表明，Lita在Aider Polyglot和SWE-Bench上达到或超过现有方法性能，同时消耗更少token，设计工作量更少。

## 📝 摘要（中文）

大型语言模型（LLM）越来越多地应用于编程任务，从单轮代码补全到自主Agent。当前的代码Agent设计通常依赖于复杂的手工工作流程和工具集。然而，这种对精心设计的脚手架的依赖带来了一些挑战：Agent性能过度依赖于提示调优和自定义设计选择，大量的人工干预掩盖了模型真正的底层能力，并且复杂的pipeline构建和维护成本高昂。此外，优化复杂的任务提示会增加数据泄露的风险。目前，像OpenAI和Anthropic这样的LLM提供商在引入新模型时，通常会发布基准分数来展示其模型的编码能力，但对其专有的评估框架保密。为了解决这些限制，我们引入了Lita（Lite Agent），它将轻量化原则付诸实践，即在保留完全自主Agent的基本要素的同时，最大限度地减少手动设计。Lita能够在没有精心设计的脚手架的情况下进行更真实和统一的评估。在前沿模型上进行的Aider Polyglot和SWE-Bench实验表明，与基于工作流程和Agentic的基线相比，Lita实现了有竞争力或更优越的性能。至关重要的是，Lita还消耗更少的token，并且需要显著更少的设计工作。我们的结果表明，Lita足以揭示现代LLM的底层编码能力。最后，我们提出了Agent复杂性定律：随着核心模型的改进，从简单到复杂设计的各种复杂度的Agent之间的性能差距将缩小，最终收敛到可以忽略不计的差异。

## 🔬 方法详解

**问题定义**：现有代码Agent设计依赖复杂的手工工作流程和工具集，导致性能过度依赖提示工程，难以评估LLM的真实编码能力。同时，复杂pipeline的构建和维护成本高昂，且存在数据泄露风险。因此，需要一种轻量级、更真实的评估方法来揭示LLM的底层编码能力。

**核心思路**：Lita的核心思路是最小化手动设计，保留自主Agent的基本要素，实现“轻量化”。通过减少对复杂工作流程和工具集的依赖，Lita能够更直接地评估LLM的编码能力，避免人工干预带来的偏差。这种轻量化的设计也降低了构建和维护成本，并减少了数据泄露的风险。

**技术框架**：Lita的技术框架主要包含以下几个核心模块：(1) 任务接收模块：接收来自用户的编程任务描述。(2) 代码生成模块：利用LLM生成代码。(3) 代码执行模块：执行生成的代码，并获取执行结果。(4) 结果评估模块：评估代码的执行结果，并生成反馈。(5) 迭代优化模块：根据反馈信息，迭代优化代码生成过程。整个流程简洁高效，避免了复杂工作流程带来的额外开销。

**关键创新**：Lita最重要的技术创新点在于其“轻量化”的设计理念。与传统的代码Agent相比，Lita减少了对复杂工作流程和工具集的依赖，更加注重LLM自身的编码能力。此外，Lita还提出了“Agent复杂性定律”，即随着核心模型的改进，不同复杂度的Agent之间的性能差距将缩小。

**关键设计**：Lita的关键设计包括：(1) 简洁的任务提示：避免过度复杂的提示工程，减少人工干预。(2) 统一的评估指标：采用统一的评估指标来衡量LLM的编码能力，避免因评估方法不同而产生的偏差。(3) 迭代优化策略：通过迭代优化代码生成过程，提高代码的质量和效率。具体的参数设置和损失函数等技术细节未在论文中详细描述，属于未知信息。

## 📊 实验亮点

Lita在Aider Polyglot和SWE-Bench等基准测试中，与基于工作流程和Agentic的基线方法相比，实现了具有竞争力的甚至更优越的性能。同时，Lita消耗的token更少，所需的设计工作量也显著降低。这些结果表明，Lita能够有效地揭示现代LLM的底层编码能力。

## 🎯 应用场景

Lita可应用于LLM的编码能力评估、自动化代码生成、软件开发辅助等领域。它能够帮助开发者更准确地了解LLM的编码能力，并利用LLM快速生成高质量的代码。未来，Lita有望成为LLM驱动的软件开发的重要工具，加速软件开发过程，提高开发效率。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly being applied to programming tasks, ranging from single-turn code completion to autonomous agents. Current code agent designs frequently depend on complex, hand-crafted workflows and tool sets. However, this reliance on elaborate scaffolding presents several challenges: agent performance becomes overly dependent on prompt tuning and custom design choices, heavy human intervention obscures a model's true underlying capabilities, and intricate pipelines are costly to build and maintain. Furthermore, optimizing complex task prompts increases the risk of data leakage. Currently, when introducing new models, LLM providers like OpenAI and Anthropic often publish benchmark scores to demonstrate their models' coding proficiency, but keep their proprietary evaluation frameworks confidential. To address these limitations, we introduce Lita (Lite Agent), which operationalizes liteness, a principle of minimizing manual design while retaining the essential elements of a fully autonomous agent. Lita enables a more faithful and unified evaluation without elaborate scaffolding. Experiments on the Aider Polyglot and SWE-Bench with frontier models demonstrate that Lita achieves competitive or superior performance compared to workflow-based and agentic baselines. Crucially, Lita also consumes fewer tokens and requires significantly less design effort. Our results suggest that Lita is sufficient to reveal the underlying coding competence of modern LLMs. Finally, we propose the Agent Complexity Law: the performance gap between agents of varying complexity, from simple to sophisticated designs, will shrink as the core model improves, ultimately converging to a negligible difference.

