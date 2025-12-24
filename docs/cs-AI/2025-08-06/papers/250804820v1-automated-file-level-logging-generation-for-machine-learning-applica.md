---
layout: default
title: "Automated File-Level Logging Generation for Machine Learning Applications using LLMs: A Case Study using GPT-4o Mini"
---

# Automated File-Level Logging Generation for Machine Learning Applications using LLMs: A Case Study using GPT-4o Mini

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04820" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04820v1</a>
  <a href="https://arxiv.org/pdf/2508.04820.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04820v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04820v1', 'Automated File-Level Logging Generation for Machine Learning Applications using LLMs: A Case Study using GPT-4o Mini')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mayra Sofia Ruiz Rodriguez, SayedHassan Khatoonabadi, Emad Shihab

**分类**: cs.SE, cs.AI, cs.LG

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**利用GPT-4o Mini生成机器学习应用的文件级日志**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `日志生成` `机器学习` `大型语言模型` `自动化` `软件开发` `GPT-4o Mini` `代码调试`

## 📋 核心要点

1. 现有研究主要集中在代码函数中的日志生成，文件级日志生成在机器学习应用中尚未得到充分探索。
2. 本研究通过使用GPT-4o Mini，评估其在机器学习项目中生成文件级日志的能力，旨在提升日志记录的全面性和可靠性。
3. 实验结果显示，LLM在63.91%的情况下能够准确生成日志位置，但过度记录率高达82.66%，显示出在实际应用中的局限性。

## 📝 摘要（中文）

日志记录在软件开发中至关重要，帮助开发者监控系统行为并调试应用。尽管大型语言模型（LLMs）在生成自然语言和代码方面表现出色，但文件级日志生成在机器学习应用中仍未得到充分探索。本研究以GPT-4o Mini为案例，评估其在171个机器学习项目中的日志生成能力。我们发现LLM在63.91%的情况下能够在与人类相同的位置生成日志，但过度记录率高达82.66%。手动分析显示，LLM在文件级日志生成中面临诸多挑战，包括在函数开头或结尾的过度记录、在大型代码块中记录困难以及与项目特定日志约定的不一致。尽管LLM在生成完整文件日志方面展现出潜力，但这些局限性仍需解决以实现实际应用。

## 🔬 方法详解

**问题定义**：本研究旨在解决机器学习应用中缺乏有效的文件级日志生成问题。现有方法主要集中在函数级别的日志记录，导致文件级日志生成的不足，影响了系统的可靠性和可调试性。

**核心思路**：本研究提出利用大型语言模型GPT-4o Mini生成机器学习项目的文件级日志，旨在通过自动化提升日志生成的效率和一致性。通过对171个机器学习项目的分析，评估LLM在日志生成中的表现。

**技术框架**：研究流程包括收集包含日志的Python文件，去除原有日志，使用LLM生成新的日志，并评估生成日志的位置、级别、变量及文本质量。主要模块包括数据收集、日志生成和质量评估。

**关键创新**：本研究的创新点在于首次系统性地评估LLM在文件级日志生成中的应用，填补了现有研究的空白，并揭示了LLM在此领域的潜力与局限。

**关键设计**：在实验中，设置了特定的提示以引导LLM生成日志，并对生成的日志进行手动分析，以识别常见模式和挑战。关键参数包括日志生成的位置和内容质量的评估标准。

## 📊 实验亮点

实验结果表明，GPT-4o Mini在63.91%的情况下能够准确生成日志位置，但同时存在82.66%的过度记录率。这些数据揭示了LLM在文件级日志生成中的潜力与挑战，为后续研究提供了重要参考。

## 🎯 应用场景

该研究的潜在应用领域包括机器学习项目的开发与维护，尤其是在需要高可靠性和可调试性的系统中。通过自动化日志生成，可以显著提高开发效率，减少人工干预，推动机器学习应用的广泛采用。未来，随着技术的进步，LLM在日志生成中的应用可能会进一步扩展到其他软件开发领域。

## 📄 摘要（原文）

> Logging is essential in software development, helping developers monitor system behavior and aiding in debugging applications. Given the ability of large language models (LLMs) to generate natural language and code, researchers are exploring their potential to generate log statements. However, prior work focuses on evaluating logs introduced in code functions, leaving file-level log generation underexplored -- especially in machine learning (ML) applications, where comprehensive logging can enhance reliability. In this study, we evaluate the capacity of GPT-4o mini as a case study to generate log statements for ML projects at file level. We gathered a set of 171 ML repositories containing 4,073 Python files with at least one log statement. We identified and removed the original logs from the files, prompted the LLM to generate logs for them, and evaluated both the position of the logs and log level, variables, and text quality of the generated logs compared to human-written logs. In addition, we manually analyzed a representative sample of generated logs to identify common patterns and challenges. We find that the LLM introduces logs in the same place as humans in 63.91% of cases, but at the cost of a high overlogging rate of 82.66%. Furthermore, our manual analysis reveals challenges for file-level logging, which shows overlogging at the beginning or end of a function, difficulty logging within large code blocks, and misalignment with project-specific logging conventions. While the LLM shows promise for generating logs for complete files, these limitations remain to be addressed for practical implementation.

