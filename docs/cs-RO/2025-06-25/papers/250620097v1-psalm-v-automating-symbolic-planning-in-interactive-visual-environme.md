---
layout: default
title: "PSALM-V: Automating Symbolic Planning in Interactive Visual Environments with Large Language Models"
---

# PSALM-V: Automating Symbolic Planning in Interactive Visual Environments with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20097" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20097v1</a>
  <a href="https://arxiv.org/pdf/2506.20097.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20097v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20097v1', 'PSALM-V: Automating Symbolic Planning in Interactive Visual Environments with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wang Bill Zhu, Miaosen Chai, Ishika Singh, Robin Jia, Jesse Thomason

**分类**: cs.RO, cs.CL

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出PSALM-V以解决交互视觉环境中的符号规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `符号规划` `神经符号学习` `大型语言模型` `动态推导` `任务规划` `多智能体系统` `机器人操作` `智能家居`

## 📋 核心要点

1. 现有方法主要集中于文本领域或依赖不切实际的假设，限制了符号规划在动态视觉环境中的应用。
2. PSALM-V通过交互推导符号动作语义，动态生成PDDL问题文件，克服了对专家定义的依赖。
3. 在ALFRED等任务中，PSALM-V的计划成功率显著提高，且在多智能体环境中表现出更高的步骤效率。

## 📝 摘要（中文）

我们提出了PSALM-V，这是第一个能够通过交互在视觉环境中诱导符号动作语义（即前后条件）的自主神经符号学习系统。PSALM-V在没有专家动作定义的情况下，通过使用大型语言模型生成启发式计划和候选符号语义，从而引导可靠的符号规划。与以往主要集中于文本领域或依赖不切实际假设的研究不同，PSALM-V通过分析执行结果和合成可能的错误解释，动态推断PDDL问题文件和领域动作语义。该系统迭代生成和执行计划，同时保持对每个动作可能的动作语义的树状信念，直到达到目标状态。模拟实验表明，PSALM-V在部分观察设置中将计划成功率从37%（Claude-3.7）提高到74%。

## 🔬 方法详解

**问题定义**：本论文旨在解决在交互视觉环境中进行符号规划的挑战，现有方法往往依赖于专家定义的动作语义，限制了系统的灵活性和适应性。

**核心思路**：PSALM-V的核心思路是利用大型语言模型（LLMs）动态推导符号动作语义，通过分析执行结果和合成错误解释，自动生成PDDL问题文件，从而实现自主规划。

**技术框架**：PSALM-V的整体架构包括三个主要模块：1) 动作语义推导模块，通过执行结果分析生成符号语义；2) 计划生成模块，利用LLMs生成启发式计划；3) 计划执行模块，迭代执行生成的计划并更新信念树。

**关键创新**：PSALM-V的最大创新在于其能够在没有预定义问题文件和完全可观察性的情况下，动态推导符号语义并进行规划，与现有方法相比，显著提高了系统的适应性和实用性。

**关键设计**：在设计中，PSALM-V采用了树状信念结构来表示对动作语义的信念，并通过迭代更新来精炼这些信念，确保在执行过程中能够适应环境变化。

## 📊 实验亮点

PSALM-V在ALFRED任务中的计划成功率从37%提升至74%，显示出显著的性能改进。此外，在RTFM和Overcooked-AI等2D游戏环境中，PSALM-V不仅提高了步骤效率，还成功实现了领域诱导，展现了其在多智能体设置中的优越性。

## 🎯 应用场景

PSALM-V的研究成果在机器人操作、智能家居和自动化任务规划等领域具有广泛的应用潜力。通过提高符号规划的灵活性和效率，该系统能够在复杂的动态环境中实现更高效的任务执行，推动智能系统的自主决策能力。未来，PSALM-V的技术可以扩展到更多的交互式应用场景中，提升人机协作的智能化水平。

## 📄 摘要（原文）

> We propose PSALM-V, the first autonomous neuro-symbolic learning system able to induce symbolic action semantics (i.e., pre- and post-conditions) in visual environments through interaction. PSALM-V bootstraps reliable symbolic planning without expert action definitions, using LLMs to generate heuristic plans and candidate symbolic semantics. Previous work has explored using large language models to generate action semantics for Planning Domain Definition Language (PDDL)-based symbolic planners. However, these approaches have primarily focused on text-based domains or relied on unrealistic assumptions, such as access to a predefined problem file, full observability, or explicit error messages. By contrast, PSALM-V dynamically infers PDDL problem files and domain action semantics by analyzing execution outcomes and synthesizing possible error explanations. The system iteratively generates and executes plans while maintaining a tree-structured belief over possible action semantics for each action, iteratively refining these beliefs until a goal state is reached. Simulated experiments of task completion in ALFRED demonstrate that PSALM-V increases the plan success rate from 37% (Claude-3.7) to 74% in partially observed setups. Results on two 2D game environments, RTFM and Overcooked-AI, show that PSALM-V improves step efficiency and succeeds in domain induction in multi-agent settings. PSALM-V correctly induces PDDL pre- and post-conditions for real-world robot BlocksWorld tasks, despite low-level manipulation failures from the robot.

