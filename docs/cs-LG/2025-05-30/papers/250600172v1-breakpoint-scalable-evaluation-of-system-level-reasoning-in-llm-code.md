---
layout: default
title: "Breakpoint: Scalable evaluation of system-level reasoning in LLM code agents"
---

# Breakpoint: Scalable evaluation of system-level reasoning in LLM code agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00172" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00172v1</a>
  <a href="https://arxiv.org/pdf/2506.00172.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00172v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00172v1', 'Breakpoint: Scalable evaluation of system-level reasoning in LLM code agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaivalya Hariharan, Uzay Girit, Atticus Wang, Jacob Andreas

**分类**: cs.LG

**发布日期**: 2025-05-30

**备注**: 21 pages, 14 figures

---

## 💡 一句话要点

**提出Breakpoint以解决LLM代码代理的系统级推理评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `系统级推理` `代码修复` `基准测试` `自动化生成任务`

## 📋 核心要点

1. 现有的基准测试方法主要集中在短期推理，难以评估长时间跨度的系统级推理能力。
2. Breakpoint方法通过对抗性破坏真实软件库中的函数，自动生成多样化的代码修复任务，系统控制任务难度。
3. 在900多个生成任务的实验中，Breakpoint展示了其在难度扩展上的有效性，成功率从55%降至0%。

## 📝 摘要（中文）

大型语言模型（LLMs）的基准测试主要评估短期、局部推理能力。现有的长时间跨度基准（如SWE-bench）依赖人工策划的问题，扩展或调整难度需要昂贵的人力成本，且评估很快达到饱和。然而，许多现实任务，如软件工程或科学研究，要求代理快速理解和动态处理新颖复杂的结构。为此，我们提出了Breakpoint，一种通过对真实软件库中的函数进行对抗性破坏，自动生成代码修复任务的基准测试方法。Breakpoint系统地控制任务难度，涵盖局部推理和系统级推理两个维度。在900多个生成任务的实验中，我们证明了该方法能够扩展到任意难度，最先进模型的成功率从最简单任务的55%下降到最困难任务的0%。

## 🔬 方法详解

**问题定义**：论文旨在解决现有基准测试方法在评估大型语言模型（LLMs）系统级推理能力方面的不足，尤其是难以生成多样化和动态变化的任务。

**核心思路**：Breakpoint通过对真实软件库中的函数进行对抗性破坏，自动生成代码修复任务，从而实现任务的多样性和难度控制。这样的设计使得评估过程不再依赖人工策划，降低了成本并提高了效率。

**技术框架**：Breakpoint的整体架构包括任务生成模块、难度控制模块和评估模块。任务生成模块负责对抗性破坏函数，难度控制模块通过局部推理和系统级推理的指标来调整任务难度，评估模块则用于测试模型在生成任务上的表现。

**关键创新**：Breakpoint的主要创新在于其自动化生成任务的能力，以及系统地控制任务难度的机制。这与现有方法的人工策划方式形成了鲜明对比，显著提高了基准测试的灵活性和可扩展性。

**关键设计**：在设计中，局部推理通过代码复杂度指标（如圈复杂度）进行量化，系统级推理则通过调用图中心性和同时破坏的相互依赖函数数量来衡量。这样的设计确保了任务的多样性和挑战性。

## 📊 实验亮点

在900多个生成任务的实验中，Breakpoint展示了其强大的扩展能力，最先进模型在最简单任务上的成功率达到55%，而在最困难任务上则降至0%。这一结果表明，Breakpoint能够有效地评估和挑战大型语言模型的系统级推理能力。

## 🎯 应用场景

Breakpoint的研究成果在软件工程、科学研究等领域具有广泛的应用潜力。通过提供一种高效的评估机制，可以帮助开发更强大的代码生成和修复工具，提升自动化编程的能力，推动智能编程助手的发展。未来，该方法还可能扩展到其他需要复杂推理的任务，如自动化测试和系统优化等。

## 📄 摘要（原文）

> Benchmarks for large language models (LLMs) have predominantly assessed short-horizon, localized reasoning. Existing long-horizon suites (e.g. SWE-bench) rely on manually curated issues, so expanding or tuning difficulty demands expensive human effort and evaluations quickly saturate. However, many real-world tasks, such as software engineering or scientific research, require agents to rapidly comprehend and manipulate novel, complex structures dynamically; evaluating these capabilities requires the ability to construct large and varied sets of problems for agents to solve. We introduce Breakpoint, a benchmarking methodology that automatically generates code-repair tasks by adversarially corrupting functions within real-world software repositories. Breakpoint systematically controls task difficulty along two clear dimensions: local reasoning (characterized by code complexity metrics such as cyclomatic complexity) and system-level reasoning (characterized by call-graph centrality and the number of simultaneously corrupted interdependent functions). In experiments across more than 900 generated tasks we demonstrate that our methodology can scale to arbitrary difficulty, with state-of-the-art models' success rates ranging from 55% on the easiest tasks down to 0% on the hardest.

