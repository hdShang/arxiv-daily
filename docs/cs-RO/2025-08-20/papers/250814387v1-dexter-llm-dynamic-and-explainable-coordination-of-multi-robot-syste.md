---
layout: default
title: "DEXTER-LLM: Dynamic and Explainable Coordination of Multi-Robot Systems in Unknown Environments via Large Language Models"
---

# DEXTER-LLM: Dynamic and Explainable Coordination of Multi-Robot Systems in Unknown Environments via Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14387" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14387v1</a>
  <a href="https://arxiv.org/pdf/2508.14387.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14387v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14387v1', 'DEXTER-LLM: Dynamic and Explainable Coordination of Multi-Robot Systems in Unknown Environments via Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxiao Zhu, Junfeng Chen, Xintong Zhang, Meng Guo, Zhongkui Li

**分类**: cs.RO

**发布日期**: 2025-08-20

**备注**: submitted to IROS 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://tcxm.github.io/DEXTER-LLM/)

---

## 💡 一句话要点

**提出DEXTER-LLM以解决多机器人系统在未知环境中的动态协调问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多机器人系统` `动态任务规划` `大型语言模型` `在线适应` `可解释性` `任务分配` `事件驱动更新`

## 📋 核心要点

1. 现有方法在动态任务生成和在线适应能力方面存在不足，难以应对未知环境中的变化。
2. DEXTER-LLM框架通过集成任务理解、子任务生成、分配调度和动态适应模块，提供了一种动态任务规划的新方法。
3. 实验结果表明，DEXTER-LLM在任务完成率和质量上均显著优于基线，展示了其在复杂环境中的有效性。

## 📝 摘要（中文）

在开放且未知的环境中，多机器人系统的在线协调面临重大挑战，尤其是在操作过程中动态触发的新任务。现有基于大型语言模型（LLMs）的方法主要集中于已知环境中的一体化解决方案，缺乏在线操作的动态适应能力和规划过程的可解释性。为此，本文提出了一种新框架DEXTER-LLM，集成了任务理解、在线子任务生成、最优分配调度和动态适应验证等模块，有效结合了LLMs的开放世界推理能力与基于模型的最优分配方法。实验结果显示，该框架在所有场景中均实现100%的成功率，完成的任务和子任务数量显著高于基线，且在适应过程中对LLMs的查询减少62%。

## 🔬 方法详解

**问题定义**：本文旨在解决多机器人系统在开放且未知环境中进行动态任务规划的挑战。现有方法缺乏在线适应能力和可解释性，难以处理动态变化的任务需求。

**核心思路**：DEXTER-LLM框架通过集成多个模块，利用大型语言模型的推理能力，动态生成和分配任务，以适应环境变化并提高任务执行的可解释性。

**技术框架**：该框架包含四个主要模块：任务理解模块、在线子任务生成模块、最优分配调度模块和动态适应验证模块。任务理解模块解析自然语言或线性时序逻辑公式中的任务顺序，在线子任务生成模块基于LLMs进行多阶段推理，分配调度模块通过搜索优化分配子任务，动态适应模块则实现事件驱动的更新。

**关键创新**：DEXTER-LLM的创新在于其动态适应能力和可解释性，结合了LLMs的开放世界推理与基于模型的最优分配方法，解决了现有方法在动态环境中的局限性。

**关键设计**：框架中的任务理解模块采用自然语言处理技术，子任务生成模块通过多阶段推理提高准确性，分配调度模块使用搜索算法优化任务分配，动态适应模块则实现了多速率的事件驱动更新机制。

## 📊 实验亮点

实验结果显示，DEXTER-LLM在所有测试场景中实现了100%的成功率，平均完成160个任务和480个子任务，较基线提升了3倍。同时，适应过程中对LLMs的查询减少了62%，复合任务的计划质量提高了2倍，展现出卓越的性能。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其适用于无人驾驶、智能制造和灾害救援等领域。在这些场景中，机器人需要在复杂和动态的环境中进行协作，DEXTER-LLM能够提高任务执行的效率和灵活性，推动多机器人系统的智能化发展。

## 📄 摘要（原文）

> Online coordination of multi-robot systems in open and unknown environments faces significant challenges, particularly when semantic features detected during operation dynamically trigger new tasks. Recent large language model (LLMs)-based approaches for scene reasoning and planning primarily focus on one-shot, end-to-end solutions in known environments, lacking both dynamic adaptation capabilities for online operation and explainability in the processes of planning. To address these issues, a novel framework (DEXTER-LLM) for dynamic task planning in unknown environments, integrates four modules: (i) a mission comprehension module that resolves partial ordering of tasks specified by natural languages or linear temporal logic formulas (LTL); (ii) an online subtask generator based on LLMs that improves the accuracy and explainability of task decomposition via multi-stage reasoning; (iii) an optimal subtask assigner and scheduler that allocates subtasks to robots via search-based optimization; and (iv) a dynamic adaptation and human-in-the-loop verification module that implements multi-rate, event-based updates for both subtasks and their assignments, to cope with new features and tasks detected online. The framework effectively combines LLMs' open-world reasoning capabilities with the optimality of model-based assignment methods, simultaneously addressing the critical issue of online adaptability and explainability. Experimental evaluations demonstrate exceptional performances, with 100% success rates across all scenarios, 160 tasks and 480 subtasks completed on average (3 times the baselines), 62% less queries to LLMs during adaptation, and superior plan quality (2 times higher) for compound tasks. Project page at https://tcxm.github.io/DEXTER-LLM/

