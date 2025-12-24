---
layout: default
title: "UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench"
---

# UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09289" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09289v1</a>
  <a href="https://arxiv.org/pdf/2506.09289.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09289v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09289v1', 'UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boxi Yu, Yuxuan Zhu, Pinjia He, Daniel Kang

**分类**: cs.SE, cs.CL

**发布日期**: 2025-06-10

**期刊**: ACL 2025

---

## 💡 一句话要点

**提出UTBoost以解决SWE-Bench中测试用例不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `编码代理` `测试用例生成` `大型语言模型` `自动化测试` `软件工程` `基准测试` `代码生成`

## 📋 核心要点

1. 现有的SWE-Bench基准测试中，手动编写的测试用例不足，导致生成的补丁未能有效解决问题。
2. 提出UTGenerator作为测试用例生成器，自动分析代码库并生成适用于真实Python项目的测试用例，进而构建UTBoost框架。
3. 评估结果显示，修正了345个错误补丁，显著影响了SWE-Bench的多个条目排名，提升了基准测试的有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）的出现推动了编码代理的开发，旨在解决实际代码生成问题。SWE-Bench作为评估这些代理代码生成能力的基准，使用基于GitHub问题及其对应拉取请求的真实世界问题。然而，这些拉取请求中手动编写的测试用例往往不足，导致生成的补丁在未解决根本问题的情况下通过测试。为此，本文提出了UTGenerator，一个基于LLM的测试用例生成器，能够自动分析代码库及其依赖关系，为真实的Python项目生成测试用例。在此基础上，提出了UTBoost，一个全面的测试用例增强框架。我们的评估发现36个任务实例的测试用例不足，并揭示了345个错误补丁被错误标记为通过，这些修正影响了SWE-Bench Lite的40.9%和SWE-Bench Verified的24.4%条目，分别导致18和11个排名变化。

## 🔬 方法详解

**问题定义**：本文旨在解决SWE-Bench基准测试中测试用例不足的问题，现有方法的手动测试用例常常无法有效验证生成补丁的正确性。

**核心思路**：通过引入UTGenerator，利用大型语言模型自动生成测试用例，确保生成的补丁能够真正解决代码中的问题。

**技术框架**：UTBoost框架包括UTGenerator模块，该模块分析代码库及其依赖关系，生成适合的测试用例，并与现有的SWE-Bench进行集成。

**关键创新**：UTGenerator的引入是本文的主要创新点，通过自动化生成测试用例，显著提高了测试的全面性和有效性，与传统手动编写测试用例的方法形成鲜明对比。

**关键设计**：在UTGenerator中，采用了基于LLM的分析方法，结合特定的参数设置和损失函数，以确保生成的测试用例能够覆盖更多的代码路径和潜在错误。

## 📊 实验亮点

实验结果显示，UTBoost修正了345个错误补丁，这些补丁在原SWE-Bench中被错误标记为通过，影响了40.9%的SWE-Bench Lite和24.4%的SWE-Bench Verified条目，分别导致18和11个排名变化，显著提升了基准测试的准确性。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、自动化测试和代码审查等。通过提高测试用例的质量和覆盖率，UTBoost能够帮助开发者更有效地识别和修复代码中的问题，从而提升软件的可靠性和安全性。未来，该框架有望扩展到其他编程语言和开发环境中，进一步推动自动化测试技术的发展。

## 📄 摘要（原文）

> The advent of Large Language Models (LLMs) has spurred the development of coding agents for real-world code generation. As a widely used benchmark for evaluating the code generation capabilities of these agents, SWE-Bench uses real-world problems based on GitHub issues and their corresponding pull requests. However, the manually written test cases included in these pull requests are often insufficient, allowing generated patches to pass the tests without resolving the underlying issue. To address this challenge, we introduce UTGenerator, an LLM-driven test case generator that automatically analyzes codebases and dependencies to generate test cases for real-world Python projects. Building on UTGenerator, we propose UTBoost, a comprehensive framework for test case augmentation. In our evaluation, we identified 36 task instances with insufficient test cases and uncovered 345 erroneous patches incorrectly labeled as passed in the original SWE Bench. These corrections, impacting 40.9% of SWE-Bench Lite and 24.4% of SWE-Bench Verified leaderboard entries, yield 18 and 11 ranking changes, respectively.

