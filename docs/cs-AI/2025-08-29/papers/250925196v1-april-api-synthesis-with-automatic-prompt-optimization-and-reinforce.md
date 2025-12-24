---
layout: default
title: "APRIL: API Synthesis with Automatic Prompt Optimization and Reinforcement Learning"
---

# APRIL: API Synthesis with Automatic Prompt Optimization and Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25196" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25196v1</a>
  <a href="https://arxiv.org/pdf/2509.25196.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25196v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25196v1', 'APRIL: API Synthesis with Automatic Prompt Optimization and Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hua Zhong, Shan Jiang, Sarfraz Khurshid

**分类**: cs.SE, cs.AI, cs.LG, cs.PL

**发布日期**: 2025-08-29

---

## 💡 一句话要点

**提出APRIL以解决API合成中的搜索空间问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `API合成` `自动提示优化` `强化学习` `大型语言模型` `软件开发` `功能正确性` `代码生成`

## 📋 核心要点

1. 现有方法在API合成中面临指数级搜索空间的挑战，导致生成的代码常常不正确。
2. APRIL通过结合自动提示优化和强化学习，优化提示并微调策略，从而提高API合成的准确性和效率。
3. 在对真实世界API的评估中，APRIL显著优于传统方法，展示了其在功能正确性和合成效率上的提升。

## 📝 摘要（中文）

API在现代软件开发中至关重要，但从大型库中组合新API面临指数级搜索空间的挑战。传统的组件合成方法依赖于昂贵的探索和手工编写的规范。尽管大型语言模型（LLMs）能够从自然语言生成实现，但由于幻觉和对最新上下文信息的有限访问，往往会产生错误的代码。本文提出APRIL，一种结合了基于LLM的合成、自动提示优化（APO）和基于可验证奖励的强化学习（RLVR）的方法。APO对冻结模型的提示进行迭代优化，而RLVR则微调策略以实现功能正确性，形成高效的合成管道。通过对81个来自广泛使用的科学Python库的真实API进行评估，并与专家提示指导下的未微调指令调优LLMs进行基准测试，APRIL取得了显著的改进。这些结果表明，集成APO和RLVR为大型库中的组件API合成提供了一条稳健、可扩展的路径。

## 🔬 方法详解

**问题定义**：本文旨在解决从大型API库中合成新API时面临的指数级搜索空间问题。现有的组件合成方法往往依赖于昂贵的探索过程和手工编写的规范，导致生成的代码准确性不足。

**核心思路**：APRIL的核心思路是结合大型语言模型（LLMs）与自动提示优化（APO）和基于可验证奖励的强化学习（RLVR）。APO通过迭代优化提示来提高模型的输出质量，而RLVR则通过微调策略来确保生成代码的功能正确性。

**技术框架**：APRIL的整体架构包括两个主要模块：APO和RLVR。APO负责对输入提示进行优化，RLVR则在生成的代码上进行强化学习，以确保其功能的正确性。整个流程是一个迭代的优化过程，旨在提高合成的效率和准确性。

**关键创新**：APRIL的主要创新在于将APO与RLVR相结合，形成了一种新的合成管道。这种方法与传统的基于规则的合成方法有本质区别，后者往往依赖于手工规范和固定的搜索策略。

**关键设计**：在APRIL中，APO的参数设置和提示优化策略是关键设计之一。此外，RLVR的损失函数设计也至关重要，以确保生成的代码不仅符合语法，还能实现预期的功能。

## 📊 实验亮点

在对81个真实世界API的评估中，APRIL显著优于传统的未微调指令调优LLMs，展示了在功能正确性和合成效率上的显著提升。这表明集成APO和RLVR的策略在API合成中具有强大的潜力。

## 🎯 应用场景

APRIL的研究成果在软件开发、API设计和自动化编程等领域具有广泛的应用潜力。通过提高API合成的效率和准确性，APRIL可以帮助开发者更快速地构建和维护复杂的软件系统，降低开发成本，并提升软件的可靠性。未来，APRIL可能会在更大规模的API库中得到应用，推动智能编程工具的发展。

## 📄 摘要（原文）

> APIs are central to modern software development, yet composing new APIs from large libraries is difficult due to the exponential search space; traditional component-based synthesis relies on costly exploration and hand-crafted specifications. While large language models (LLMs) can generate implementations from natural language, hallucinations and limited access to up-to-date contextual information often yield incorrect code. In this paper, we present APRIL, an approach that combines LLM-based synthesis with Automatic Prompt Optimization (APO) and Reinforcement Learning from Verifiable Rewards (RLVR): APO iteratively refines prompts for a frozen model, while RLVR fine-tunes the policy toward functional correctness, producing an efficient synthesis pipeline. Evaluated on 81 real-world APIs from widely used scientific Python libraries and benchmarked against instruction-tuned but unfine-tuned LLMs guided by expert prompts, APRIL achieves substantial improvements. These results indicate that integrating APO and RLVR provides a robust, scalable path for component-based API synthesis in large libraries.

