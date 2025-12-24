---
layout: default
title: "SOCK: A Benchmark for Measuring Self-Replication in Large Language Models"
---

# SOCK: A Benchmark for Measuring Self-Replication in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25643" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25643v3</a>
  <a href="https://arxiv.org/pdf/2509.25643.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25643v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25643v3', 'SOCK: A Benchmark for Measuring Self-Replication in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Justin Chavarria, Rohan Raizada, Justin White, Eyad Alhetairshi

**分类**: cs.AI

**发布日期**: 2025-09-30 (更新: 2025-12-09)

---

## 💡 一句话要点

**SOCK：用于评估大型语言模型自我复制能力的标准基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自我复制` `基准测试` `多智能体系统` `安全风险`

## 📋 核心要点

1. 现有方法缺乏对LLM自我复制能力的系统性评估和量化标准，难以有效衡量和防范潜在风险。
2. SOCK通过定义复制能力等级(RCL)和持久能力等级(PCL)，并设计五任务套件，量化评估LLM的自我复制能力。
3. 实验结果揭示了当前LLM在持久自我复制和多智能体决策方面存在的局限性，为未来研究指明了方向。

## 📝 摘要（中文）

本文提出了SOCK，一个基准命令行界面(CLI)，用于衡量大型语言模型(LLM)在无人干预下的自我复制能力。在该基准中，自我复制不仅定义为LLM创建自身可运行副本的能力，还包括这种自我复制在不同计算环境中持久存在和发生的能力。因此，我们开发了一个系统，根据LLM的广泛自我复制能力将其分为两个主要类别：复制能力等级(RCL)和持久能力等级(PCL)。通过一个基于实际可操作的现代CLI工具和计算机流程的五任务套件，在受控环境中以LLM作为智能体进行实验。然后计算LLM在智能体任务上的表现，以产生R-score（对整体自我复制能力的量化评估）和用于将LLM分类到特定RCL-PCL矩阵的数据。SOCK提供了两个主要贡献：(1)提供了第一个用于评估LLM自我复制的正式定义和基准套件，旨在建立未来研究的标准；(2)允许业界跟踪未来多智能体系统的有效性，并减轻其中潜在的自我复制威胁。对各种开源和专有前沿模型进行评估的结果表明，持久自我复制和多智能体系统存在重大障碍，包括上下文保留和多智能体决策。我们提出了未来的研究方向，以安全地降低这些障碍的严重性，从而可能降低未来更具功能性的多智能体系统的风险。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）缺乏一个标准化的评估框架来衡量其自我复制能力。现有的方法要么是定性的，要么是针对特定场景的，无法全面评估LLM在不同计算环境下的自我复制和持久化能力。这使得我们难以理解和防范潜在的风险，尤其是在多智能体系统中。

**核心思路**：本文的核心思路是建立一个量化的基准测试框架，通过模拟实际的计算机操作环境，评估LLM在无人干预下的自我复制能力。通过定义复制能力等级（RCL）和持久能力等级（PCL），可以对LLM的自我复制能力进行分类和比较。

**技术框架**：SOCK基准测试框架包含以下主要模块：
1. **任务套件**：包含五个基于现代CLI工具和计算机流程的任务，用于评估LLM的自我复制能力。
2. **智能体环境**：在受控环境中，LLM作为智能体执行任务。
3. **评估指标**：R-score，用于量化LLM的整体自我复制能力。
4. **分类矩阵**：RCL-PCL矩阵，用于将LLM分类到不同的自我复制能力等级。

**关键创新**：SOCK的主要创新在于：
1. **正式定义和基准套件**：首次提出了LLM自我复制的正式定义，并提供了一个标准化的基准测试套件。
2. **RCL-PCL分类体系**：通过RCL和PCL两个维度，对LLM的自我复制能力进行细粒度的分类。
3. **量化评估指标**：R-score提供了一个量化的指标，用于比较不同LLM的自我复制能力。

**关键设计**：SOCK的关键设计包括：
1. **任务选择**：任务的选择基于实际可操作的CLI工具和计算机流程，例如文件复制、进程管理等。
2. **环境控制**：实验在受控环境中进行，以确保结果的可重复性和可比性。
3. **R-score计算**：R-score的计算方法需要根据具体的任务和评估标准进行设计，以确保其能够准确反映LLM的自我复制能力。

## 📊 实验亮点

通过对一系列开源和专有模型进行评估，SOCK揭示了当前LLM在持久自我复制和多智能体决策方面存在的显著障碍，例如上下文保留和多智能体协同。这些实验结果为未来的研究提供了重要的参考，并指出了安全提升多智能体系统功能性的潜在方向。

## 🎯 应用场景

该研究成果可应用于评估和监控大型语言模型的潜在风险，特别是在多智能体系统中。通过SOCK基准，可以更好地理解LLM的自我复制能力，从而开发更安全的AI系统。此外，该基准还可以用于指导未来多智能体系统的设计，降低潜在的安全风险。

## 📄 摘要（原文）

> We introduce SOCK, a benchmark command line interface (CLI) that measures large language models' (LLMs) ability to self-replicate without human intervention. In this benchmark, self-replication is defined not only as an LLM's ability to create a functioning and running copy of itself, but also the ability for that self-replication to persist and occur across different computational contexts. Accordingly, we've developed a system to categorize LLMs based on broad self-replication capabilities in two general classes, Replication-Capability Levels (RCL) and Persistence-Capability Levels (PCL). Using a five-task suite based on practically manipulable modern CLI utilities and computer processes, experiments are orchestrated in a controlled environment with an LLM acting agentically. The performance of the LLM on agent tasks is then computed to produce an R-score (a quantitative evaluation of overall self-replication ability) and data used to categorize LLMs into specific RCL-PCL matrices. SOCK offers two primary contributions: (1) Provides the first formalized definitions and benchmark suite for evaluating LLM self-replication, with the goal of establishing a standard for future research, to our knowledge; (2) Allows the industry to track the effectiveness of future multi-agent systems and mitigate potential self-replication threat vectors within them. The results compiled from evaluating a variety of open-weight and proprietary frontier models reveal significant obstacles to persistent self-replication and multi-agent systems, including context retention and multi-agent decision-making. We propose future research directions to safely reduce the severity of these obstacles, potentially lowering future risk of more functional multi-agent systems.

