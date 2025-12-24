---
layout: default
title: "RPG: A Repository Planning Graph for Unified and Scalable Codebase Generation"
---

# RPG: A Repository Planning Graph for Unified and Scalable Codebase Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16198" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16198v5</a>
  <a href="https://arxiv.org/pdf/2509.16198.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16198v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16198v5', 'RPG: A Repository Planning Graph for Unified and Scalable Codebase Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jane Luo, Xin Zhang, Steven Liu, Jie Wu, Jianfeng Liu, Yiming Huang, Yangyu Huang, Chengyu Yin, Ying Xin, Yuefeng Zhan, Hao Sun, Qi Chen, Scarlett Li, Mao Yang

**分类**: cs.CL, cs.AI, cs.SE

**发布日期**: 2025-09-19 (更新: 2025-10-20)

---

## 💡 一句话要点

**提出RPG，用于统一和可扩展的代码库生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `大型语言模型` `代码库规划` `图神经网络` `自动化软件开发`

## 📋 核心要点

1. 现有方法依赖自然语言进行代码库生成规划，存在规范模糊、组件错位和设计脆弱等问题。
2. 论文提出代码库规划图（RPG），以结构化方式统一表示代码库的能力、结构、数据流和函数。
3. ZeroRepo框架基于RPG，在RepoCraft基准测试中，代码生成量和测试准确率显著优于现有基线。

## 📝 摘要（中文）

大型语言模型在生成单个函数或代码文件方面表现出色，但从头开始生成完整的代码库仍然是一个根本性的挑战。这种能力是构建来自高级规范的连贯软件系统并实现自动化代码生成的全部潜力的关键。该过程需要在两个层面上进行规划：决定要构建哪些特性和模块（提议阶段）以及定义它们的实现细节（实现阶段）。当前的方法依赖于自然语言规划，由于其固有的模糊性和缺乏结构，通常会产生不清晰的规范、未对齐的组件和脆弱的设计。为了解决这些限制，我们引入了代码库规划图（RPG），这是一种结构化的表示，它在统一的图中编码了能力、文件结构、数据流和函数。通过用显式蓝图替换自由形式的自然语言，RPG 能够为代码库生成实现一致的长期规划。在 RPG 的基础上，我们开发了 ZeroRepo，这是一个图驱动的框架，它在三个阶段运行：提议级规划、实现级构建以及带有测试验证的图引导代码生成。为了评估，我们构建了 RepoCraft，这是一个包含 6 个真实世界项目和 1,052 个任务的基准。在 RepoCraft 上，ZeroRepo 平均生成近 36K 行代码和 445K 个代码 Token，比最强的基线（Claude Code）大 3.9 倍，比其他基线大 68 倍。它实现了 81.5% 的覆盖率和 69.7% 的测试准确率，比 Claude Code 提高了 27.3 和 35.8 个百分点。进一步的分析表明，RPG 可以对复杂的依赖关系进行建模，通过接近线性的扩展实现更复杂的规划，并提高代理对代码库的理解，从而加速定位。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在生成单个函数或文件时表现良好，但从零开始生成完整的、复杂的代码库仍然是一个挑战。现有方法主要依赖自然语言进行规划，这导致规范不清晰、组件之间缺乏对齐，以及最终代码库的脆弱性。自然语言的模糊性和缺乏结构是主要痛点。

**核心思路**：论文的核心思路是用结构化的图表示（Repository Planning Graph, RPG）来替代自然语言进行代码库的规划。RPG 能够显式地编码代码库的能力、文件结构、数据流和函数之间的关系，从而避免自然语言带来的歧义和不一致性。通过这种方式，可以实现更清晰、更一致的长期规划，并最终生成更健壮的代码库。

**技术框架**：ZeroRepo 框架包含三个主要阶段：1) **提议级规划**：使用 RPG 对代码库的整体结构和功能进行规划。2) **实现级构建**：根据 RPG 的规划，逐步构建代码库的各个组件。3) **图引导代码生成与测试验证**：利用 RPG 的信息，指导代码生成过程，并进行测试验证，确保代码的正确性。

**关键创新**：最重要的技术创新点是 RPG 这种结构化的代码库表示方法。与传统的自然语言规划相比，RPG 能够更清晰、更准确地表达代码库的结构和功能，从而避免了自然语言的歧义和不一致性。此外，RPG 还能够支持更复杂的依赖关系建模和更高效的规划算法。

**关键设计**：RPG 的具体结构包括节点和边，节点表示代码库中的模块、函数或数据，边表示它们之间的依赖关系。在 ZeroRepo 框架中，使用了图神经网络来处理 RPG，并生成相应的代码。具体的参数设置、损失函数和网络结构等技术细节在论文中进行了详细描述（具体细节未知）。

## 📊 实验亮点

在 RepoCraft 基准测试中，ZeroRepo 生成的代码量平均达到 36K 行，是 Claude Code 的 3.9 倍，其他基线的 68 倍。ZeroRepo 的代码覆盖率达到 81.5%，测试准确率达到 69.7%，分别比 Claude Code 提高了 27.3 和 35.8 个百分点。实验结果表明，RPG 能够有效地提高代码生成的质量和效率。

## 🎯 应用场景

该研究成果可应用于自动化软件开发、代码生成、软件维护和代码理解等领域。通过使用 RPG 和 ZeroRepo 框架，可以显著提高代码生成的效率和质量，降低软件开发的成本。未来，该技术有望应用于更复杂的软件系统，并实现真正的自动化软件开发。

## 📄 摘要（原文）

> Large language models excel at generating individual functions or single files of code, yet generating complete repositories from scratch remains a fundamental challenge. This capability is key to building coherent software systems from high-level specifications and realizing the full potential of automated code generation. The process requires planning at two levels: deciding what features and modules to build (proposal stage) and defining their implementation details (implementation stage). Current approaches rely on natural language planning, which often produces unclear specifications, misaligned components, and brittle designs due to its inherent ambiguity and lack of structure. To address these limitations, we introduce the Repository Planning Graph (RPG), a structured representation that encodes capabilities, file structures, data flows, and functions in a unified graph. By replacing free-form natural language with an explicit blueprint, RPG enables consistent long-horizon planning for repository generation. Building on RPG, we develop ZeroRepo, a graph-driven framework that operates in three stages: proposal-level planning, implementation-level construction, and graph-guided code generation with test validation. To evaluate, we construct RepoCraft, a benchmark of six real-world projects with 1,052 tasks. On RepoCraft, ZeroRepo produces nearly 36K Code Lines and 445K Code Tokens, on average 3.9$\times$ larger than the strongest baseline (Claude Code), and 68$\times$ larger than other baselines. It achieves 81.5% coverage and 69.7% test accuracy, improving over Claude Code by 27.3 and 35.8 points. Further analysis shows that RPG models complex dependencies, enables more sophisticated planning through near-linear scaling, and improves agent understanding of repositories, thus accelerating localization.

