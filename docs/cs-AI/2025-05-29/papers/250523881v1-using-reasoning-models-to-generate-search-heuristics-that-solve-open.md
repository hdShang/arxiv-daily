---
layout: default
title: Using Reasoning Models to Generate Search Heuristics that Solve Open Instances of Combinatorial Design Problems
---

# Using Reasoning Models to Generate Search Heuristics that Solve Open Instances of Combinatorial Design Problems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23881" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23881v1</a>
  <a href="https://arxiv.org/pdf/2505.23881.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23881v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23881v1', 'Using Reasoning Models to Generate Search Heuristics that Solve Open Instances of Combinatorial Design Problems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christopher D. Rosin

**分类**: cs.AI, cs.CL, math.CO

**发布日期**: 2025-05-29

**备注**: arXiv admin note: text overlap with arXiv:2501.17725

---

## 💡 一句话要点

**利用推理模型生成搜索启发式以解决组合设计问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `组合设计` `推理模型` `搜索启发式` `超参数调优` `大型语言模型` `数学优化` `代码生成`

## 📋 核心要点

1. 组合设计领域存在许多开放实例，其存在性尚未确定，现有方法难以有效解决这些问题。
2. 本文提出的CPro1协议利用LLMs生成搜索启发式，通过文本定义和有效性验证器指导模型选择策略。
3. 实验结果显示，CPro1成功解决了7个组合设计问题中的开放实例，包括3个新解实例，且在多个新问题上也取得了突破。

## 📝 摘要（中文）

本文探讨了如何利用具有推理能力的大型语言模型（LLMs）来生成和优化搜索启发式，以解决组合设计领域中的开放实例问题。通过构造协议CPro1，LLMs能够在特定设计类型的文本定义和有效性验证器的指导下，选择和实施策略，并进行自动超参数调优和执行反馈。研究表明，CPro1成功解决了2006年《组合设计手册》中16个组合设计问题中的7个长期未解实例，并为多个最近文献中的问题生成了新的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决组合设计领域中的开放实例问题，现有方法在处理这些问题时常常面临效率低下和解的准确性不足的挑战。

**核心思路**：CPro1协议通过利用具有推理能力的LLMs，生成和优化搜索启发式，从而提高解决开放实例的能力。该设计旨在通过引导模型选择有效策略来提升解的质量和效率。

**技术框架**：CPro1的整体架构包括文本定义、有效性验证器、策略选择模块、超参数调优模块和执行反馈模块。该框架通过迭代生成和优化过程，逐步逼近问题的解决方案。

**关键创新**：CPro1的主要创新在于结合了推理能力的LLMs与组合设计问题的特定需求，显著提升了模型在解决开放实例时的表现，区别于传统的非推理LLMs。

**关键设计**：在参数设置上，CPro1采用了自动超参数调优机制，损失函数设计上注重解的有效性和准确性，网络结构则基于当前最先进的LLMs架构进行优化。通过这些设计，CPro1能够在复杂的组合设计问题中实现更高效的搜索。

## 📊 实验亮点

实验结果显示，CPro1成功解决了7个组合设计问题中的开放实例，包括3个新解实例，且在多个新问题上生成了新的覆盖序列、约翰逊团覆盖、删除码和均匀嵌套斯坦纳四元组系统，展示了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括组合设计、优化算法、以及相关的数学问题求解。通过生成有效的搜索启发式，CPro1能够为科学研究和工程应用提供新的解决方案，推动组合设计领域的进一步发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) with reasoning are trained to iteratively generate and refine their answers before finalizing them, which can help with applications to mathematics and code generation. We apply code generation with reasoning LLMs to a specific task in the mathematical field of combinatorial design. This field studies diverse types of combinatorial designs, many of which have lists of open instances for which existence has not yet been determined. The Constructive Protocol CPro1 uses LLMs to generate search heuristics that have the potential to construct solutions to small open instances. Starting with a textual definition and a validity verifier for a particular type of design, CPro1 guides LLMs to select and implement strategies, while providing automated hyperparameter tuning and execution feedback. CPro1 with reasoning LLMs successfully solves long-standing open instances for 7 of 16 combinatorial design problems selected from the 2006 Handbook of Combinatorial Designs, including new solved instances for 3 of these (Bhaskar Rao Designs, Symmetric Weighing Matrices, Balanced Ternary Designs) that were unsolved by CPro1 with non-reasoning LLMs. It also solves open instances for several problems from recent (2025) literature, generating new Covering Sequences, Johnson Clique Covers, Deletion Codes, and a Uniform Nested Steiner Quadruple System.

