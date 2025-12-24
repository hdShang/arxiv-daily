---
layout: default
title: "SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks"
---

# SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10954" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10954v2</a>
  <a href="https://arxiv.org/pdf/2506.10954.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10954v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10954v2', 'SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lianghong Guo, Yanlin Wang, Caihua Li, Pengyu Yang, Jiachi Chen, Wei Tao, Yingtian Zou, Duyu Tang, Zibin Zheng

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-12 (更新: 2025-06-19)

**🔗 代码/项目**: [GITHUB](https://github.com/DeepSoftwareAnalytics/swe-factory)

---

## 💡 一句话要点

**提出SWE-Factory以解决GitHub问题解决数据集构建难题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动化管道` `数据集构建` `GitHub问题解决` `多代理系统` `评分方法` `软件工程`

## 📋 核心要点

1. 现有方法在构建GitHub问题解决数据集时面临环境搭建、结果评分和任务验证等多重挑战，效率低下且劳动密集。
2. 论文提出的SWE-Factory通过自动化管道集成多代理系统、标准化评分方法和自动化验证流程，显著提高了数据集构建效率。
3. 实验结果显示，SWE-Factory在构建有效任务实例的同时，评分准确率达到100%，fail2pass验证精度为0.92，召回率为1.00。

## 📝 摘要（中文）

构建大规模的GitHub问题解决数据集对于训练和评估大型语言模型（LLMs）的软件工程能力至关重要。然而，传统的基准创建过程繁琐且劳动密集，尤其是在评估环境搭建、测试结果评分和任务实例验证阶段。本文提出了SWE-Factory，一个自动化管道，旨在解决这些挑战。该管道集成了三个核心自动化组件：首先，SWE-Builder是一个多代理系统，自动化评估环境的构建；其次，采用基于退出代码的标准化评分方法，消除了手动编写解析器的需求；最后，利用可靠的退出代码信号自动化fail2pass验证过程。实验表明，该管道能够有效构建有效的任务实例，并在评分和验证精度上表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决构建大规模GitHub问题解决数据集的困难，现有方法在环境搭建、结果评分和任务验证上效率低下，且劳动强度大。

**核心思路**：SWE-Factory通过自动化管道整合多个组件，利用多代理系统提升环境构建效率，采用标准化评分方法简化评分流程，从而加速数据集的构建。

**技术框架**：整体架构包括三个主要模块：SWE-Builder（多代理系统）、基于退出代码的评分方法和fail2pass验证流程。SWE-Builder通过四个专门代理协作构建评估环境，并利用环境记忆池提升效率。

**关键创新**：最重要的创新在于引入了多代理系统和基于退出代码的评分方法，显著减少了手动干预，提升了数据集构建的自动化程度和准确性。

**关键设计**：在SWE-Builder中，代理通过迭代循环协作，环境记忆池用于存储和重用环境配置；评分方法基于退出代码，避免了手动解析的复杂性；fail2pass验证过程则依赖于可靠的退出代码信号，确保验证的高效性和准确性。

## 📊 实验亮点

实验结果显示，使用GPT-4.1-mini，SWE-Builder以每个实例0.045美元的成本构建了269个有效实例，而使用Gemini-2.5-flash时，成本最低为0.024美元。评分方法的准确率达到100%，而fail2pass验证的精度为0.92，召回率为1.00，展现了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括软件工程教育、自动化测试和大型语言模型的训练与评估。通过提供高质量的GitHub问题解决数据集，SWE-Factory能够加速模型的训练过程，提高模型在实际应用中的表现，推动软件开发领域的自动化进程。

## 📄 摘要（原文）

> Constructing large-scale datasets for the GitHub issue resolution task is crucial for both training and evaluating the software engineering capabilities of Large Language Models (LLMs). However, the traditional process for creating such benchmarks is notoriously challenging and labor-intensive, particularly in the stages of setting up evaluation environments, grading test outcomes, and validating task instances. In this paper, we propose SWE-Factory, an automated pipeline designed to address these challenges. To tackle these issues, our pipeline integrates three core automated components. First, we introduce SWE-Builder, a multi-agent system that automates evaluation environment construction, which employs four specialized agents that work in a collaborative, iterative loop and leverages an environment memory pool to enhance efficiency. Second, we introduce a standardized, exit-code-based grading method that eliminates the need for manually writing custom parsers. Finally, we automate the fail2pass validation process using these reliable exit code signals. Experiments on 671 issues across four programming languages show that our pipeline can effectively construct valid task instances; for example, with GPT-4.1-mini, our SWE-Builder constructs 269 valid instances at $0.045 per instance, while with Gemini-2.5-flash, it achieves comparable performance at the lowest cost of $0.024 per instance. We also demonstrate that our exit-code-based grading achieves 100% accuracy compared to manual inspection, and our automated fail2pass validation reaches a precision of 0.92 and a recall of 1.00. We hope our automated pipeline will accelerate the collection of large-scale, high-quality GitHub issue resolution datasets for both training and evaluation. Our code and datasets are released at https://github.com/DeepSoftwareAnalytics/swe-factory.

