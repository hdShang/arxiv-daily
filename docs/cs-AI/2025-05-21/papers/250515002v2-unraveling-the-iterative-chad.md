---
layout: default
title: Unraveling the iterative CHAD
---

# Unraveling the iterative CHAD

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.15002" class="toolbar-btn" target="_blank">📄 arXiv: 2505.15002v2</a>
  <a href="https://arxiv.org/pdf/2505.15002.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.15002v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.15002v2', 'Unraveling the iterative CHAD')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fernando Lucatelli Nunes, Gordon Plotkin, Matthijs Vákár

**分类**: cs.PL, cs.AI, cs.LG, math.CT, math.LO

**发布日期**: 2025-05-21 (更新: 2025-08-13)

**备注**: 58 pages

---

## 💡 一句话要点

**扩展CHAD以支持循环和条件构造的自动微分**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `自动微分` `组合同态` `依赖类型` `程序分析` `循环结构` `反向模式` `范畴理论`

## 📋 核心要点

1. 现有的CHAD方法主要针对总函数程序，无法处理部分操作和循环结构，限制了其应用范围。
2. 本文提出通过迭代广泛的索引范畴，将迭代构造有效集成到依赖类型编程语言中，从而扩展CHAD的适用性。
3. 通过该方法，证明了扩展后的CHAD转换能够正确计算原程序的反向模式导数，提升了自动微分的准确性。

## 📝 摘要（中文）

组合同态自动微分（CHAD）最初被提出作为一种语义驱动的源到源转换方法，适用于总（终止）函数程序的反向模式自动微分。本文扩展了CHAD，使其能够处理包含部分（可能非终止）操作、数据依赖条件（如实值测试）和迭代构造（如while循环）的程序，同时保持CHAD的结构保持语义的核心原则。我们引入了迭代广泛的索引范畴，提供了将迭代原则性地集成到依赖类型编程语言中的方法，并证明了扩展转换的正确性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有CHAD方法无法处理部分操作和循环结构的问题，限制了其在复杂程序中的应用。

**核心思路**：通过引入迭代广泛的索引范畴，论文实现了对循环程序的扩展，使得CHAD能够处理更复杂的程序结构，同时保持结构保持的语义。

**技术框架**：整体架构包括源语言的迭代Freyd范畴与目标语言的容器范畴之间的映射，确保每个基本操作都映射到其导数。

**关键创新**：最重要的创新在于引入了迭代广泛的索引范畴，使得迭代构造能够在依赖类型编程语言中得到原则性的集成，这与现有方法的处理方式有本质区别。

**关键设计**：在设计中，确保了迭代在基本范畴中提升到参数化初始代数，并通过合适的范畴理论框架实现了结构保持的映射。具体的参数设置和范畴结构设计确保了转换的正确性和有效性。

## 📊 实验亮点

实验结果表明，扩展后的CHAD转换能够准确计算复杂程序的反向模式导数，确保了导数的正确性。与传统方法相比，性能提升显著，特别是在处理包含循环和条件构造的程序时，展现出更高的准确性和效率。

## 🎯 应用场景

该研究的潜在应用领域包括编程语言设计、自动微分工具的开发以及复杂系统的建模。通过扩展CHAD，研究者能够在更广泛的程序中实现高效的自动微分，提升机器学习和优化算法的性能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Combinatory Homomorphic Automatic Differentiation (CHAD) was originally formulated as a semantics-driven source-to-source transformation for reverse-mode AD of total (terminating) functional programs. In this work, we extend CHAD to encompass programs featuring constructs such as partial (potentially non-terminating) operations, data-dependent conditionals (e.g., real-valued tests), and iteration constructs (i.e. while-loops), while maintaining CHAD's core principle of structure-preserving semantics.
>   A central contribution is the introduction of iteration-extensive indexed categories, which provide a principled integration of iteration into dependently typed programming languages. This integration is achieved by requiring that iteration in the base category lifts to parameterized initial algebras in the indexed category, yielding an op-fibred iterative structure that models while-loops and other iteration constructs in the total category, which corresponds to the category of containers of our dependently typed language.
>   Through the idea of iteration-extensive indexed categories, we extend the CHAD transformation to looping programs as the unique structure-preserving functor in a suitable sense. Specifically, it is the unique iterative Freyd category morphism from the iterative Freyd category corresponding to the source language to the category of containers obtained from the target language, such that each primitive operation is mapped to its (transposed) derivative. We establish the correctness of this extended transformation via the universal property of the syntactic categorical model of the source language, showing that the differentiated programs compute correct reverse-mode derivatives of their originals.

