---
layout: default
title: "SwingArena: Competitive Programming Arena for Long-context GitHub Issue Solving"
---

# SwingArena: Competitive Programming Arena for Long-context GitHub Issue Solving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23932" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23932v2</a>
  <a href="https://arxiv.org/pdf/2505.23932.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23932v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23932v2', 'SwingArena: Competitive Programming Arena for Long-context GitHub Issue Solving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wendong Xu, Jing Xiong, Chenyang Zhao, Qiujiang Chen, Haoran Wang, Hui Shen, Zhongwei Wan, Jianbo Dai, Taiqiang Wu, He Xiao, Chaofan Tao, Z. Morley Mao, Ying Sheng, Zhijiang Guo, Hongxia Yang, Bei Yu, Lingpeng Kong, Quanquan Gu, Ngai Wong

**分类**: cs.CL

**发布日期**: 2025-05-29 (更新: 2025-06-02)

---

## 💡 一句话要点

**提出SwingArena以解决长上下文GitHub问题的评估挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `软件开发` `持续集成` `代码生成` `评估框架` `长上下文` `GitHub问题` `检索增强`

## 📋 核心要点

1. 现有方法在评估大型语言模型时缺乏对真实软件开发流程的模拟，无法有效处理长上下文问题。
2. SwingArena通过模拟软件迭代过程，结合提交者和审阅者角色，提供了一个动态的评估框架。
3. 实验结果显示，GPT-4o在补丁生成方面表现优异，而DeepSeek和Gemini在CI验证中更注重正确性，展示了不同模型的优势。

## 📝 摘要（中文）

我们提出了SwingArena，这是一个竞争性评估框架，旨在为大型语言模型（LLMs）提供一个与现实软件开发工作流程紧密相连的评估环境。与传统静态基准测试不同，SwingArena模拟了软件迭代的协作过程，通过将LLMs作为提交者生成补丁，并由审阅者创建测试用例并通过持续集成（CI）管道验证补丁。为支持这些交互式评估，我们引入了检索增强代码生成（RACG）模块，有效处理长上下文挑战，提供来自大型代码库的语法和语义相关代码片段，支持多种编程语言（C++、Python、Rust和Go）。我们的实验使用了从2300个问题中选出的400多个高质量真实GitHub问题，结果表明，像GPT-4o这样的模型在激进的补丁生成方面表现出色，而DeepSeek和Gemini则优先考虑CI验证的正确性。SwingArena为在现实的CI驱动软件开发环境中评估LLMs提供了一种可扩展和可延展的方法。

## 🔬 方法详解

**问题定义**：论文旨在解决现有评估框架无法真实反映软件开发过程的问题，尤其是在处理长上下文和协作评估时的不足。

**核心思路**：通过引入SwingArena框架，模拟软件开发中的提交和审阅过程，使得评估更加贴近真实场景，同时利用RACG模块解决长上下文的挑战。

**技术框架**：SwingArena框架包括两个主要模块：提交者和审阅者。提交者生成代码补丁，审阅者则创建测试用例并通过CI管道进行验证。RACG模块负责从大型代码库中检索相关代码片段，以支持多种编程语言。

**关键创新**：SwingArena的创新在于其动态交互评估机制和RACG模块的引入，使得评估不仅限于静态测试，而是模拟真实的开发流程，提升了评估的有效性和实用性。

**关键设计**：在RACG模块中，设计了高效的检索算法，以确保从大规模代码库中快速获取相关代码片段，同时支持多种编程语言的语法和语义分析。

## 📊 实验亮点

实验结果表明，GPT-4o在补丁生成方面表现优异，能够快速生成高质量的代码补丁，而DeepSeek和Gemini则在CI验证中展现了更高的正确性。这些结果表明不同模型在软件开发任务中的优势和适用场景，为未来的研究提供了重要的参考。

## 🎯 应用场景

SwingArena的研究成果可广泛应用于软件开发领域，尤其是在大型语言模型的评估和优化中。通过提供一个真实的评估环境，开发者可以更好地理解模型在实际开发中的表现，从而推动软件开发工具的智能化进程，提升开发效率和代码质量。

## 📄 摘要（原文）

> We present SwingArena, a competitive evaluation framework for Large Language Models (LLMs) that closely mirrors real-world software development workflows. Unlike traditional static benchmarks, SwingArena models the collaborative process of software iteration by pairing LLMs as submitters, who generate patches, and reviewers, who create test cases and verify the patches through continuous integration (CI) pipelines. To support these interactive evaluations, we introduce a retrieval-augmented code generation (RACG) module that efficiently handles long-context challenges by providing syntactically and semantically relevant code snippets from large codebases, supporting multiple programming languages (C++, Python, Rust, and Go). This enables the framework to scale across diverse tasks and contexts while respecting token limitations. Our experiments, using over 400 high-quality real-world GitHub issues selected from a pool of 2,300 issues, show that models like GPT-4o excel at aggressive patch generation, whereas DeepSeek and Gemini prioritize correctness in CI validation. SwingArena presents a scalable and extensible methodology for evaluating LLMs in realistic, CI-driven software development settings. More details are available on our project page: swing-bench.github.io

