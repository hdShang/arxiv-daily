---
layout: default
title: "CoAct-1: Computer-using Agents with Coding as Actions"
---

# CoAct-1: Computer-using Agents with Coding as Actions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03923" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03923v2</a>
  <a href="https://arxiv.org/pdf/2508.03923.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03923v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03923v2', 'CoAct-1: Computer-using Agents with Coding as Actions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linxin Song, Yutong Dai, Viraj Prabhu, Jieyu Zhang, Taiwei Shi, Li Li, Junnan Li, Silvio Savarese, Zeyuan Chen, Jieyu Zhao, Ran Xu, Caiming Xiong

**分类**: cs.CL

**发布日期**: 2025-08-05 (更新: 2025-08-08)

---

## 💡 一句话要点

**提出CoAct-1以解决复杂任务中的计算机操作效率问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自主代理` `图形用户界面` `编程执行` `任务效率` `计算机自动化` `多代理系统` `OSWorld基准测试`

## 📋 核心要点

1. 现有的自主代理在复杂任务中依赖GUI操作，效率低且容易出错，难以满足实际需求。
2. CoAct-1通过结合GUI操作与编程执行，允许代理在适当时机使用编码来提高任务执行效率。
3. 在OSWorld基准测试中，CoAct-1的成功率达到60.76%，显著优于之前的方法，并减少了任务完成所需的平均步骤数。

## 📝 摘要（中文）

自主代理在通过图形用户界面（GUI）操作计算机时，往往在复杂的长时间任务中面临效率和可靠性的问题。尽管通过规划器增强这些代理可以改善任务分解，但它们仍然受到通过GUI操作执行所有动作的固有限制，导致脆弱性和低效率。本文提出了一种更为稳健和灵活的范式：使代理能够将编码作为增强动作。我们介绍了CoAct-1，这是一种新颖的多代理系统，协同结合了基于GUI的控制与直接的程序执行。CoAct-1具有一个调度器，动态地将子任务分配给常规的GUI操作员或专门的程序员代理，后者可以编写和执行Python或Bash脚本。该混合方法使代理能够绕过低效的GUI动作序列，显著提高了任务完成的效率。

## 🔬 方法详解

**问题定义**：本文旨在解决自主代理在复杂长任务中通过GUI操作的效率和可靠性问题。现有方法依赖于GUI操作，导致任务执行脆弱且低效。

**核心思路**：CoAct-1的核心思路是将编码作为一种增强动作，允许代理在适当的情况下直接执行程序，从而提高任务执行的灵活性和效率。

**技术框架**：CoAct-1的整体架构包括一个调度器模块，该模块动态分配子任务给GUI操作员或程序员代理。程序员代理负责编写和执行Python或Bash脚本，优化任务执行流程。

**关键创新**：最重要的技术创新在于将编程与GUI操作结合，允许代理在需要时选择最优的执行方式，从而克服了传统方法的局限性。

**关键设计**：系统设计中，调度器的决策机制是关键，能够根据任务复杂性和执行效率选择合适的代理。此外，程序员代理的脚本执行能力显著提升了任务处理的速度和准确性。

## 📊 实验亮点

实验结果表明，CoAct-1在OSWorld基准测试中的成功率达到60.76%，显著高于之前的最佳结果。同时，任务完成的平均步骤数减少至10.15，相较于领先的GUI代理减少了近五步，显示出显著的效率提升。

## 🎯 应用场景

该研究的潜在应用领域包括自动化办公、数据处理和软件开发等场景。通过提高计算机操作的效率，CoAct-1可以在多个行业中实现更高效的工作流程，降低人工干预的需求，推动智能化办公的发展。

## 📄 摘要（原文）

> Autonomous agents that operate computers via Graphical User Interfaces (GUIs) often struggle with efficiency and reliability on complex, long-horizon tasks. While augmenting these agents with planners can improve task decomposition, they remain constrained by the inherent limitations of performing all actions through GUI manipulation, leading to brittleness and inefficiency. In this work, we introduce a more robust and flexible paradigm: enabling agents to use coding as a enhanced action. We present CoAct-1, a novel multi-agent system that synergistically combines GUI-based control with direct programmatic execution. CoAct-1 features an Orchestrator that dynamically delegates subtasks to either a conventional GUI Operator or a specialized Programmer agent, which can write and execute Python or Bash scripts. This hybrid approach allows the agent to bypass inefficient GUI action sequences for tasks like file management and data processing, while still leveraging visual interaction when necessary. We evaluate our system on the challenging OSWorld benchmark, where CoAct-1 achieves a new state-of-the-art success rate of 60.76%, significantly outperforming prior methods. Furthermore, our approach dramatically improves efficiency, reducing the average number of steps required to complete a task to just 10.15, compared to 15 for leading GUI agents. Our results demonstrate that integrating coding as a core action provides a more powerful, efficient, and scalable path toward generalized computer automation.

