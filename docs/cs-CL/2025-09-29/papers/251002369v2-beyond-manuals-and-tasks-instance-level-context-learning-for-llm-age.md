---
layout: default
title: "Beyond Manuals and Tasks: Instance-Level Context Learning for LLM Agents"
---

# Beyond Manuals and Tasks: Instance-Level Context Learning for LLM Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02369" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02369v2</a>
  <a href="https://arxiv.org/pdf/2510.02369.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02369v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02369v2', 'Beyond Manuals and Tasks: Instance-Level Context Learning for LLM Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kuntai Cai, Juncheng Liu, Xianglin Yang, Zhaojie Niu, Xiaokui Xiao, Xing Chen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-29 (更新: 2025-10-06)

---

## 💡 一句话要点

**提出实例级上下文学习方法，提升LLM Agent在复杂任务中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM Agent` `实例级上下文学习` `环境探索` `知识获取` `任务规划`

## 📋 核心要点

1. 现有LLM Agent在复杂任务中常因缺乏实例级上下文（如对象位置、局部规则）而失败。
2. 提出实例级上下文学习（ILCL）方法，通过引导式探索自动获取并验证环境中的关键事实。
3. 实验表明，该方法显著提升了LLM Agent在TextWorld、ALFWorld和Crafter等环境中的成功率和效率。

## 📝 摘要（中文）

大型语言模型（LLM）Agent通常接收两种上下文：（i）定义交互界面和全局规则的环境级手册，以及（ii）与特定目标相关的任务级指导或演示。本文指出了一种关键但被忽视的第三种上下文，即实例级上下文，它由与特定环境实例相关的可验证和可重用的事实组成，例如对象位置、制作配方和局部规则。我们认为，缺乏实例级上下文是LLM Agent在复杂任务中失败的常见原因，因为成功不仅取决于对全局规则或任务提示的推理，还取决于基于精确和持久事实的决策。获取此类上下文需要的不仅仅是记忆：挑战在于在严格的交互预算下高效地探索、验证和格式化这些事实。我们将此问题形式化为实例级上下文学习（ILCL），并介绍我们与任务无关的方法来解决它。我们的方法执行引导式探索，使用紧凑的TODO森林来智能地确定其下一步行动的优先级，并使用轻量级的计划-行动-提取循环来执行它们。此过程自动生成高精度的上下文文档，该文档可在许多下游任务和Agent中重用，从而分摊初始探索成本。在TextWorld、ALFWorld和Crafter上的实验表明，在成功率和效率方面都有持续的提高：例如，ReAct在TextWorld中的平均成功率从37%提高到95%，而IGE从81%提高到95%。通过将一次性探索转化为持久的、可重用的知识，我们的方法补充了现有的上下文，从而使LLM Agent更加可靠和高效。

## 🔬 方法详解

**问题定义**：现有LLM Agent在复杂任务中，主要依赖环境级手册和任务级指导，忽略了实例级上下文的重要性。实例级上下文包含特定环境实例的可验证事实，例如物品位置、制作配方等。缺乏这些信息会导致Agent无法做出正确的决策，从而影响任务完成的成功率。现有方法难以在有限的交互预算下高效地探索、验证和格式化这些事实。

**核心思路**：论文的核心思路是让Agent主动探索环境，学习并验证实例级上下文，并将其存储为可重用的知识。通过这种方式，Agent可以基于精确的事实进行推理和决策，从而提高任务完成的成功率和效率。该方法旨在将一次性的探索转化为持久的、可重用的知识，从而降低后续任务的探索成本。

**技术框架**：该方法的核心是一个引导式探索框架，主要包含以下几个模块：1) TODO森林：用于智能地确定下一步行动的优先级，指导Agent探索环境。2) 计划-行动-提取循环：用于执行探索行动，并从环境中提取相关信息。3) 上下文文档：用于存储和管理学习到的实例级上下文。Agent首先根据TODO森林选择下一步行动，然后执行该行动并从环境中提取信息。提取的信息经过验证后，被添加到上下文文档中。这个过程不断循环，直到Agent学习到足够的实例级上下文。

**关键创新**：该方法最重要的创新点在于提出了实例级上下文学习的概念，并设计了一个任务无关的引导式探索框架来实现它。与现有方法相比，该方法能够自动地学习和验证环境中的关键事实，并将其存储为可重用的知识。此外，该方法还使用了TODO森林来智能地确定下一步行动的优先级，从而提高了探索效率。

**关键设计**：TODO森林的设计是关键。它是一个树状结构，每个节点代表一个待完成的任务（TODO）。TODO森林的根节点是初始任务，子节点是根据当前环境状态生成的子任务。Agent根据一定的策略（例如，优先级最高的任务）选择一个TODO节点执行。执行完该节点后，Agent会根据环境反馈更新TODO森林。TODO森林的设计使得Agent能够有条不紊地探索环境，并避免重复探索。

## 📊 实验亮点

实验结果表明，该方法在TextWorld、ALFWorld和Crafter等多个环境中都取得了显著的性能提升。例如，在TextWorld中，ReAct的平均成功率从37%提高到95%，IGE的平均成功率从81%提高到95%。这些结果表明，该方法能够有效地学习和利用实例级上下文，从而提高LLM Agent在复杂任务中的表现。

## 🎯 应用场景

该研究成果可应用于各种需要LLM Agent与复杂环境交互的场景，例如游戏AI、机器人导航、智能家居控制等。通过学习和利用实例级上下文，Agent可以更好地理解环境，做出更明智的决策，从而提高任务完成的效率和可靠性。该方法有望推动LLM Agent在现实世界中的广泛应用。

## 📄 摘要（原文）

> Large language model (LLM) agents typically receive two kinds of context: (i) environment-level manuals that define interaction interfaces and global rules, and (ii) task-level guidance or demonstrations tied to specific goals. In this work, we identify a crucial but overlooked third type of context, instance-level context, which consists of verifiable and reusable facts tied to a specific environment instance, such as object locations, crafting recipes, and local rules. We argue that the absence of instance-level context is a common source of failure for LLM agents in complex tasks, as success often depends not only on reasoning over global rules or task prompts but also on making decisions based on precise and persistent facts. Acquiring such context requires more than memorization: the challenge lies in efficiently exploring, validating, and formatting these facts under tight interaction budgets. We formalize this problem as Instance-Level Context Learning (ILCL) and introduce our task-agnostic method to solve it. Our method performs a guided exploration, using a compact TODO forest to intelligently prioritize its next actions and a lightweight plan-act-extract loop to execute them. This process automatically produces a high-precision context document that is reusable across many downstream tasks and agents, thereby amortizing the initial exploration cost. Experiments across TextWorld, ALFWorld, and Crafter demonstrate consistent gains in both success and efficiency: for instance, ReAct's mean success rate in TextWorld rises from 37% to 95%, while IGE improves from 81% to 95%. By transforming one-off exploration into persistent, reusable knowledge, our method complements existing contexts to enable more reliable and efficient LLM agents.

