---
layout: default
title: "COMPASS: A Multi-Dimensional Benchmark for Evaluating Code Generation in Large Language Models"
---

# COMPASS: A Multi-Dimensional Benchmark for Evaluating Code Generation in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13757" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13757v1</a>
  <a href="https://arxiv.org/pdf/2508.13757.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13757v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13757v1', 'COMPASS: A Multi-Dimensional Benchmark for Evaluating Code Generation in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: James Meaden, Michał Jarosz, Piotr Jodłowski, Grigori Melnik

**分类**: cs.SE, cs.AI

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出COMPASS以解决代码生成评估的多维度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `多维度评估` `算法效率` `代码质量` `人工智能`

## 📋 核心要点

1. 现有的代码生成基准主要集中在功能正确性上，忽视了算法效率和代码质量这两个重要方面。
2. 论文提出COMPASS，一个多维度的评估框架，系统性地评估代码生成的正确性、效率和质量。
3. 实验结果表明，尽管某些模型在正确性上得分较高，但它们在算法效率和代码可维护性方面表现不佳，强调了多维度评估的重要性。

## 📝 摘要（中文）

当前的代码生成基准主要关注功能正确性，而忽视了现实编程中的两个关键方面：算法效率和代码质量。我们引入COMPASS（COdility的多维编程评估），这是一个全面的评估框架，评估代码生成的三个维度：正确性、效率和质量。COMPASS包含来自真实Codility竞赛的50个竞争性编程问题，提供来自393,150次提交的真实人类基准。与现有基准不同，COMPASS系统性地评估运行时效率和代码质量，使用行业标准分析工具。对三种领先的推理增强模型的评估显示，高正确性得分的模型不一定能生成高效算法或可维护代码。这些发现强调了评估不仅仅是正确性的重要性，以真正理解代码生成模型的现实能力。COMPASS为未来研究提供了指导框架，指明了朝着强大、可靠和适合生产使用的AI系统的方向。

## 🔬 方法详解

**问题定义**：论文要解决的问题是现有代码生成基准过于单一，主要关注功能正确性，而忽略了算法效率和代码质量的评估，这导致无法全面了解模型的实际能力。

**核心思路**：论文的核心解决思路是引入COMPASS评估框架，通过三个维度（正确性、效率和质量）对代码生成进行全面评估，以更好地反映模型在实际应用中的表现。

**技术框架**：COMPASS框架包括三个主要模块：首先是正确性评估，通过标准测试用例进行验证；其次是效率评估，使用运行时分析工具评估算法的性能；最后是代码质量评估，采用行业标准的代码分析工具进行质量检查。

**关键创新**：COMPASS的最大创新在于其多维度评估方法，系统性地将算法效率和代码质量纳入评估体系，与现有方法仅关注正确性的做法形成鲜明对比。

**关键设计**：在设计上，COMPASS使用真实的Codility竞赛问题作为基准，确保评估的真实性和竞争性；同时，采用行业标准的工具进行效率和质量分析，确保评估结果的可靠性。

## 📊 实验亮点

在对三种领先的推理增强模型进行评估时，COMPASS显示出高正确性得分的模型并不一定能生成高效的算法或可维护的代码。这一发现强调了多维度评估的重要性，推动了对代码生成模型能力的深入理解。

## 🎯 应用场景

COMPASS的研究成果可广泛应用于代码生成模型的评估和优化，尤其是在软件开发、自动化编程和AI辅助编程等领域。通过提供更全面的评估标准，COMPASS能够帮助开发者选择和改进代码生成工具，从而提升软件开发的效率和质量。未来，COMPASS还可能推动AI系统在生产环境中的应用，使其更加可靠和高效。

## 📄 摘要（原文）

> Current code generation benchmarks focus primarily on functional correctness while overlooking two critical aspects of real-world programming: algorithmic efficiency and code quality. We introduce COMPASS (COdility's Multi-dimensional Programming ASSessment), a comprehensive evaluation framework that assesses code generation across three dimensions: correctness, efficiency, and quality. COMPASS consists of 50 competitive programming problems from real Codility competitions, providing authentic human baselines from 393,150 submissions. Unlike existing benchmarks that treat algorithmically inefficient solutions identically to optimal ones provided they pass test cases, COMPASS systematically evaluates runtime efficiency and code quality using industry-standard analysis tools. Our evaluation of three leading reasoning-enhanced models, Anthropic Claude Opus 4, Google Gemini 2.5 Pro, and OpenAI O4-Mini-High, reveals that models achieving high correctness scores do not necessarily produce efficient algorithms or maintainable code. These findings highlight the importance of evaluating more than just correctness to truly understand the real-world capabilities of code generation models. COMPASS serves as a guiding framework, charting a path for future research toward AI systems that are robust, reliable, and ready for production use.

