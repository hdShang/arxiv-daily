---
layout: default
title: "LLM-First Search: Self-Guided Exploration of the Solution Space"
---

# LLM-First Search: Self-Guided Exploration of the Solution Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05213" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05213v1</a>
  <a href="https://arxiv.org/pdf/2506.05213.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05213v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05213v1', 'LLM-First Search: Self-Guided Exploration of the Solution Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nathan Herr, Tim Rocktäschel, Roberta Raileanu

**分类**: cs.AI, cs.CL

**发布日期**: 2025-06-05

**备注**: 9 main pages, 2 figures, 2 tables, 36 appendix pages

**🔗 代码/项目**: [GITHUB](https://github.com/NathanHerr/LLM-First-Search)

---

## 💡 一句话要点

**提出LLM-First Search以解决搜索策略固定性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自导向搜索` `蒙特卡洛树搜索` `推理与规划` `计算效率` `搜索策略`

## 📋 核心要点

1. 现有搜索方法如MCTS依赖固定的超参数，限制了其在不同任务中的适应性和效率。
2. LLM-First Search（LFS）通过自我引导探索，使LLM能够自主决定搜索路径，提升了灵活性和上下文敏感性。
3. 实验结果显示，LFS在更具挑战性的任务上表现优越，且计算效率高于传统方法，尤其是在强模型支持下。

## 📝 摘要（中文）

大型语言模型（LLMs）在推理和规划方面取得了显著进展，通常通过将问题解决视为搜索过程来实现。现有方法如蒙特卡洛树搜索（MCTS）在某些领域有效，但其对固定探索超参数的依赖限制了其在不同难度任务中的适应性。本文提出了LLM-First Search（LFS），一种新颖的LLM自导向搜索方法，消除了预定义搜索策略的需求，使LLM能够通过自我引导探索自主控制搜索过程。LFS在Countdown和数独任务上与三种经典搜索算法进行了评估，结果表明LFS在更具挑战性的任务上表现更佳，计算效率更高，且在强模型下具有更好的扩展性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有搜索方法在不同任务中适应性差、效率低的问题，尤其是固定超参数导致的局限性。

**核心思路**：LFS通过赋予LLM自主控制搜索过程的能力，消除了对外部启发式或硬编码策略的依赖，允许模型根据内部评分机制自我引导探索。

**技术框架**：LFS的整体架构包括输入处理、内部评分机制和搜索路径选择三个主要模块。输入处理模块负责接收任务信息，内部评分机制用于评估当前路径的有效性，搜索路径选择模块则决定是继续当前路径还是探索新分支。

**关键创新**：LFS的核心创新在于其自我引导的搜索机制，使得模型能够根据上下文动态调整搜索策略，与传统方法的固定策略形成鲜明对比。

**关键设计**：LFS在设计上不需要手动调优参数，且通过强大的LLM模型提升了计算效率，特别是在计算预算增加时，表现出更好的扩展性。该方法的代码已公开，便于后续研究和应用。

## 📊 实验亮点

实验结果表明，LFS在更具挑战性的任务上表现优于传统算法，如Tree-of-Thoughts的广度优先搜索和蒙特卡洛树搜索，且在计算效率上具有显著优势，尤其是在强模型支持下，提升幅度明显。

## 🎯 应用场景

该研究的潜在应用领域包括复杂问题求解、游戏策略优化和自动化决策系统等。通过提升搜索效率和灵活性，LFS能够在多种实际场景中提供更优的解决方案，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable improvements in reasoning and planning through increased test-time compute, often by framing problem-solving as a search process. While methods like Monte Carlo Tree Search (MCTS) have proven effective in some domains, their reliance on fixed exploration hyperparameters limits their adaptability across tasks of varying difficulty, rendering them impractical or expensive in certain settings. In this paper, we propose \textbf{LLM-First Search (LFS)}, a novel \textit{LLM Self-Guided Search} method that removes the need for pre-defined search strategies by empowering the LLM to autonomously control the search process via self-guided exploration. Rather than relying on external heuristics or hardcoded policies, the LLM evaluates whether to pursue the current search path or explore alternative branches based on its internal scoring mechanisms. This enables more flexible and context-sensitive reasoning without requiring manual tuning or task-specific adaptation. We evaluate LFS on Countdown and Sudoku against three classic widely-used search algorithms, Tree-of-Thoughts' Breadth First Search (ToT-BFS), Best First Search (BestFS), and MCTS, each of which have been used to achieve SotA results on a range of challenging reasoning tasks. We found that LFS (1) performs better on more challenging tasks without additional tuning, (2) is more computationally efficient compared to the other methods, especially when powered by a stronger model, (3) scales better with stronger models, due to its LLM-First design, and (4) scales better with increased compute budget. Our code is publicly available at \href{https://github.com/NathanHerr/LLM-First-Search}{LLM-First-Search}.

