---
layout: default
title: "Performance of LLMs on Stochastic Modeling Operations Research Problems: From Theory to Practice"
---

# Performance of LLMs on Stochastic Modeling Operations Research Problems: From Theory to Practice

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23924" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23924v1</a>
  <a href="https://arxiv.org/pdf/2506.23924.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23924v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23924v1', 'Performance of LLMs on Stochastic Modeling Operations Research Problems: From Theory to Practice')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Akshit Kumar, Tianyi Peng, Yuhang Wu, Assaf Zeevi

**分类**: cs.AI

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**评估大型语言模型在随机建模运筹学问题上的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `随机建模` `运筹学` `决策支持` `自动化` `不确定性` `SimOpt` `AI应用`

## 📋 核心要点

1. 现有方法在运筹学领域对随机建模问题的解决能力尚未得到充分验证，尤其是在不确定性环境下的应用。
2. 本文通过手动收集研究生作业和博士考试问题，评估LLMs在随机建模问题上的解决能力，并利用SimOpt库进行深入分析。
3. 实验结果显示，尽管仍需改进，LLMs在课堂和实践中的表现已接近人类专家，展示了其在运筹学领域的应用潜力。

## 📝 摘要（中文）

大型语言模型（LLMs）在多个领域展现出专家级能力，但其在运筹学（OR）问题中的应用仍然未被充分探讨。本文首次评估LLMs解决随机建模问题的能力，这类问题以不确定性为特征，通常涉及概率、统计和随机过程的工具。研究团队手动收集了一组研究生水平的作业和博士资格考试问题，并测试了LLMs的解决能力。同时，利用开源库SimOpt，研究LLMs在不确定性下做出实际决策的能力。结果表明，尽管在现实中自动化随机建模流程仍需大量工作，但当前最先进的LLMs在课堂和实际场景中表现出与人类专家相当的能力。这些发现突显了构建AI代理以辅助OR研究人员的潜力，并通过自动化提升OR的现实影响。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在随机建模运筹学问题中的应用能力不足，现有方法在处理不确定性时面临挑战。

**核心思路**：通过手动收集和测试研究生及博士生的作业和考试问题，评估LLMs的解决能力，并结合SimOpt库进行实际决策分析。

**技术框架**：研究分为数据收集、模型评估和决策分析三个主要模块。首先收集问题数据，然后使用LLMs进行解答，最后分析模型在不确定性下的决策能力。

**关键创新**：本文首次系统性地评估LLMs在随机建模问题上的表现，填补了这一领域的研究空白，展示了LLMs与人类专家的比较能力。

**关键设计**：在实验中，选择了多种随机建模问题，使用了SimOpt库中的多种求解器，并对LLMs的输出进行详细评估，确保结果的可靠性和有效性。

## 📊 实验亮点

实验结果显示，当前最先进的LLMs在解决随机建模问题时的表现与人类专家相当，尤其在课堂和实际应用中，展示出显著的解决能力。这一发现为运筹学领域的AI应用提供了新的视角和可能性。

## 🎯 应用场景

该研究的潜在应用领域包括运筹学、决策支持系统和智能优化等。通过将LLMs应用于随机建模问题，研究可以帮助研究人员和从业者更高效地进行决策，提升实际问题的解决能力，未来可能推动运筹学领域的自动化进程。

## 📄 摘要（原文）

> Large language models (LLMs) have exhibited expert-level capabilities across various domains. However, their abilities to solve problems in Operations Research (OR) -- the analysis and optimization of mathematical models derived from real-world problems or their verbal descriptions -- remain underexplored. In this work, we take a first step toward evaluating LLMs' abilities to solve stochastic modeling problems, a core class of OR problems characterized by uncertainty and typically involving tools from probability, statistics, and stochastic processes. We manually procure a representative set of graduate-level homework and doctoral qualification-exam problems and test LLMs' abilities to solve them. We further leverage SimOpt, an open-source library of simulation-optimization problems and solvers, to investigate LLMs' abilities to make real-world decisions under uncertainty. Our results show that, though a nontrivial amount of work is still needed to reliably automate the stochastic modeling pipeline in reality, state-of-the-art LLMs demonstrate proficiency on par with human experts in both classroom and practical settings. These findings highlight the potential of building AI agents that assist OR researchers and amplify the real-world impact of OR through automation.

