---
layout: default
title: RepoMaster: Autonomous Exploration and Understanding of GitHub Repositories for Complex Task Solving
---

# RepoMaster: Autonomous Exploration and Understanding of GitHub Repositories for Complex Task Solving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21577" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21577v3</a>
  <a href="https://arxiv.org/pdf/2505.21577.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21577v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21577v3', 'RepoMaster: Autonomous Exploration and Understanding of GitHub Repositories for Complex Task Solving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huacan Wang, Ziyi Ni, Shuo Zhang, Shuo Lu, Sen Hu, Ziyang He, Chen Hu, Jiaye Lin, Yifu Guo, Ronghao Chen, Xin Li, Daxin Jiang, Yuntao Du, Pin Lyu

**分类**: cs.SE, cs.AI

**发布日期**: 2025-05-27 (更新: 2025-08-25)

**备注**: A novel approach; Very practical

**🔗 代码/项目**: [GITHUB](https://github.com/QuantaAlpha/RepoMaster)

---

## 💡 一句话要点

**提出RepoMaster以解决GitHub仓库复杂任务自动探索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码自动化` `开源代码` `任务解决` `信息提取` `图结构` `上下文优化` `自主代理`

## 📋 核心要点

1. 现有方法在利用GitHub仓库时面临信息过载和复杂依赖关系的挑战，导致任务解决效率低下。
2. RepoMaster通过构建函数调用图和模块依赖图等结构，优化了对GitHub仓库的探索和重用过程。
3. 在实验中，RepoMaster在有效提交率上比基线OpenHands提升了110%，任务通过率从40.7%提升至62.9%。

## 📝 摘要（中文）

代码代理的最终目标是自主解决复杂任务。尽管大型语言模型在代码生成方面取得了显著进展，但现实任务通常需要完整的代码仓库，而不仅仅是简单的脚本。从头构建这样的仓库仍然是一个重大挑战。GitHub上有大量开源仓库，开发者经常将其作为复杂任务的模块组件进行重用。然而，现有框架如OpenHands和SWE-Agent在有效利用这些资源方面仍存在困难。仅依赖README文件提供的指导不足以应对信息过载和仓库依赖关系复杂的问题。为此，我们提出了RepoMaster，一个旨在探索和重用GitHub仓库以解决复杂任务的自主代理框架。RepoMaster通过构建函数调用图、模块依赖图和层次代码树来识别核心组件，从而优化上下文使用。经过评估，RepoMaster在任务通过率和有效提交方面均显著提升。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何有效地利用GitHub上的开源代码仓库来解决复杂任务。现有方法如OpenHands在处理信息过载和复杂依赖关系时表现不佳，导致无法充分利用可用资源。

**核心思路**：RepoMaster的核心思路是通过构建函数调用图、模块依赖图和层次代码树来识别和提取核心组件，从而优化大型语言模型的上下文使用，避免信息冗余。

**技术框架**：RepoMaster的整体架构包括三个主要模块：信息提取模块、上下文优化模块和自主执行模块。信息提取模块负责构建图结构，优化信息的选择；上下文优化模块则根据提取的信息调整输入给语言模型的内容；自主执行模块负责逐步探索相关组件。

**关键创新**：RepoMaster的关键创新在于其图结构的构建和信息选择策略，能够有效应对信息过载和依赖关系复杂的问题。这与现有方法的线性处理方式形成鲜明对比。

**关键设计**：在设计中，RepoMaster采用了动态上下文窗口调整策略，确保在不同阶段只提供最相关的信息给语言模型，从而显著减少了token的使用。

## 📊 实验亮点

RepoMaster在实验中表现出色，相较于最强基线OpenHands，其有效提交率提升了110%。在新发布的GitTaskBench上，RepoMaster的任务通过率从40.7%提升至62.9%，同时token使用量减少了95%，显示出其在资源优化方面的显著优势。

## 🎯 应用场景

RepoMaster的研究成果在软件开发、自动化测试和代码生成等领域具有广泛的应用潜力。通过提高对开源代码的利用效率，开发者可以更快速地构建复杂应用，降低开发成本。此外，该框架的设计理念也可扩展到其他领域的知识获取与利用。未来，RepoMaster可能会推动更智能的代码生成工具的发展，提升软件工程的整体效率。

## 📄 摘要（原文）

> The ultimate goal of code agents is to solve complex tasks autonomously. Although large language models (LLMs) have made substantial progress in code generation, real-world tasks typically demand full-fledged code repositories rather than simple scripts. Building such repositories from scratch remains a major challenge. Fortunately, GitHub hosts a vast, evolving collection of open-source repositories, which developers frequently reuse as modular components for complex tasks. Yet, existing frameworks like OpenHands and SWE-Agent still struggle to effectively leverage these valuable resources. Relying solely on README files provides insufficient guidance, and deeper exploration reveals two core obstacles: overwhelming information and tangled dependencies of repositories, both constrained by the limited context windows of current LLMs. To tackle these issues, we propose RepoMaster, an autonomous agent framework designed to explore and reuse GitHub repositories for solving complex tasks. For efficient understanding, RepoMaster constructs function-call graphs, module-dependency graphs, and hierarchical code trees to identify essential components, providing only identified core elements to the LLMs rather than the entire repository. During autonomous execution, it progressively explores related components using our exploration tools and prunes information to optimize context usage. Evaluated on the adjusted MLE-bench, RepoMaster achieves a 110% relative boost in valid submissions over the strongest baseline OpenHands. On our newly released GitTaskBench, RepoMaster lifts the task-pass rate from 40.7% to 62.9% while reducing token usage by 95%. Our code and demonstration materials are publicly available at https://github.com/QuantaAlpha/RepoMaster.

