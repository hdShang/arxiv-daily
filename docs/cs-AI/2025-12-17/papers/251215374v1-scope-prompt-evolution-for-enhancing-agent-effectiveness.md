---
layout: default
title: SCOPE: Prompt Evolution for Enhancing Agent Effectiveness
---

# SCOPE: Prompt Evolution for Enhancing Agent Effectiveness

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15374" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15374v1</a>
  <a href="https://arxiv.org/pdf/2512.15374.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15374v1" onclick="toggleFavorite(this, '2512.15374v1', 'SCOPE: Prompt Evolution for Enhancing Agent Effectiveness')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zehua Pei, Hui-Ling Zhen, Shixiong Kai, Sinno Jialin Pan, Yunhe Wang, Mingxuan Yuan, Bei Yu

**分类**: cs.AI

**发布日期**: 2025-12-17

**🔗 代码/项目**: [GITHUB](https://github.com/JarvisPei/SCOPE)

---

## 💡 一句话要点

**SCOPE：通过提示进化增强Agent有效性，解决大规模动态上下文中的管理瓶颈。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `Agent` `提示工程` `上下文管理` `在线优化` `自进化` `双流机制`

## 📋 核心要点

1. 现有LLM Agent在处理大规模动态上下文时，静态提示难以有效管理上下文信息，导致性能瓶颈。
2. SCOPE将上下文管理视为在线优化问题，通过从执行轨迹中提取信息，自动进化Agent的提示，提升其适应性。
3. SCOPE在HLE基准测试中，无需人工干预，将任务成功率从14.23%提升至38.64%，显著提高了Agent的性能。

## 📝 摘要（中文）

大型语言模型（LLM）Agent越来越多地部署在生成大量动态上下文的环境中。然而，一个关键瓶颈仍然存在：尽管Agent可以访问这些上下文，但其静态提示缺乏有效管理上下文的机制，导致反复出现纠正和增强失败。为了解决这一能力差距，我们引入了SCOPE（通过提示进化实现自进化上下文优化）。SCOPE将上下文管理构建为一个在线优化问题，从执行轨迹中综合指导原则，以自动进化Agent的提示。我们提出了一种双流机制，该机制平衡了战术特异性（解决直接错误）和战略通用性（进化长期原则）。此外，我们引入了视角驱动探索，以最大化策略覆盖范围，从而提高Agent针对任何给定任务都具有正确策略的可能性。在HLE基准上的实验表明，SCOPE在没有人为干预的情况下，将任务成功率从14.23％提高到38.64％。我们的代码已在https://github.com/JarvisPei/SCOPE上公开。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型Agent在处理大规模、动态上下文时，由于静态提示的局限性，无法有效管理上下文信息，从而导致任务失败的问题。现有方法缺乏根据环境变化动态调整提示的能力，使得Agent难以适应复杂场景。

**核心思路**：论文的核心思路是将上下文管理视为一个在线优化问题，通过自动进化Agent的提示来适应不断变化的环境。这种方法允许Agent从自身的执行轨迹中学习，并根据经验调整其策略，从而提高其在复杂环境中的表现。

**技术框架**：SCOPE采用双流机制和视角驱动探索。双流机制包含战术流和战略流，战术流专注于解决即时错误，战略流则致力于进化长期原则。视角驱动探索通过探索不同的策略视角，最大化策略覆盖范围，确保Agent能够应对各种任务。整体流程包括Agent执行任务、收集执行轨迹、从轨迹中提取指导原则、更新Agent提示，并重复此过程。

**关键创新**：SCOPE的关键创新在于其自进化提示机制，该机制允许Agent根据自身的经验动态调整提示，从而更好地适应不断变化的环境。与传统的静态提示方法相比，SCOPE能够更有效地管理上下文信息，并提高Agent的性能。此外，双流机制和视角驱动探索进一步增强了Agent的学习能力和适应性。

**关键设计**：SCOPE的具体实现细节包括：如何从执行轨迹中提取指导原则（例如，使用自然语言处理技术分析Agent的行动和结果），如何平衡战术流和战略流（例如，使用不同的权重或学习率），以及如何设计视角驱动探索策略（例如，使用不同的探索算法或奖励函数）。论文中可能还涉及一些超参数的设置，例如学习率、探索率等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15374v1/figs/result.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15374v1/figs/failures_2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15374v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SCOPE在HLE基准测试中表现出色，任务成功率从14.23%提升至38.64%，显著优于基线方法。这一结果表明，SCOPE的自进化提示机制能够有效提高Agent在复杂环境中的性能。实验结果还表明，双流机制和视角驱动探索对SCOPE的性能提升起到了重要作用。

## 🎯 应用场景

SCOPE的潜在应用领域包括智能客服、自动化流程管理、游戏AI等。该研究的实际价值在于提高Agent在复杂环境中的适应性和性能，降低人工干预的需求。未来，SCOPE可以应用于更广泛的Agent应用场景，并与其他技术（如强化学习、迁移学习）相结合，进一步提升Agent的智能化水平。

## 📄 摘要（原文）

> Large Language Model (LLM) agents are increasingly deployed in environments that generate massive, dynamic contexts. However, a critical bottleneck remains: while agents have access to this context, their static prompts lack the mechanisms to manage it effectively, leading to recurring Corrective and Enhancement failures. To address this capability gap, we introduce \textbf{SCOPE} (Self-evolving Context Optimization via Prompt Evolution). SCOPE frames context management as an \textit{online optimization} problem, synthesizing guidelines from execution traces to automatically evolve the agent's prompt. We propose a Dual-Stream mechanism that balances tactical specificity (resolving immediate errors) with strategic generality (evolving long-term principles). Furthermore, we introduce Perspective-Driven Exploration to maximize strategy coverage, increasing the likelihood that the agent has the correct strategy for any given task. Experiments on the HLE benchmark show that SCOPE improves task success rates from 14.23\% to 38.64\% without human intervention. We make our code publicly available at https://github.com/JarvisPei/SCOPE.

