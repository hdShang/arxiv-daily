---
layout: default
title: Gödel's Poetry
---

# Gödel's Poetry

**arXiv**: [2512.14252v1](https://arxiv.org/abs/2512.14252) | [PDF](https://arxiv.org/pdf/2512.14252.pdf)

**作者**: Kelly J. Davis

**分类**: cs.AI, cs.LG

**发布日期**: 2025-12-16

**备注**: 24 pages, 1 figure

**🔗 代码/项目**: [GITHUB](https://github.com/KellyJDavis/goedels-poetry)

---

## 💡 一句话要点

**提出基于多智能体架构和递归分解的定理证明系统，显著提升Lean4自动证明性能**

**关键词**: `自动定理证明` `Lean4证明生成` `递归分解` `多智能体架构` `抽象语法树解析` `形式化验证` `语言模型` `数学推理`

## 📋 核心要点

1. 核心问题：形式化自动定理证明面临困难定理难以直接证明的挑战，现有方法在复杂场景下性能有限。
2. 方法要点：采用多智能体架构协调语言模型生成Lean4证明，并递归分解困难定理为简单命题以提升证明成功率。
3. 实验或效果：在miniF2F基准测试中，无分解时通过率达90.4%，引入分解后性能显著提升。

## 📝 摘要（中文）

形式化自动定理证明长期以来被视为人工智能的挑战。本文介绍了一种新的计算机定理证明方法，该方法采用专门的语言模型生成Lean4证明，并结合递归分解将困难定理分解为更简单的蕴含命题。这些模型通过多智能体架构协调，组织自动形式化（如果需要）、证明生成、困难定理分解为简单蕴含命题，以及这些命题的递归证明（和/或分解）。在没有分解的情况下，我们在miniF2F上实现了90.4%的通过率。通过分解，这一性能得到显著提升。一个关键的技术贡献在于我们扩展了Kimina Lean Server，增加了抽象语法树（AST）解析能力，以促进自动递归证明分解。该系统已在PyPI上作为goedels-poetry（https://pypi.org/project/goedels-poetry）提供，开源实现KellyJDavis/goedels-poetry（https://github.com/KellyJDavis/goedels-poetry）便于适应替代语言模型和扩展自定义功能。

## 🔬 方法详解

论文提出一个多智能体架构系统，整体框架包括自动形式化、证明生成、定理分解和递归证明等模块。关键技术创新点在于扩展Kimina Lean Server以支持AST解析，实现自动递归证明分解，这允许系统将复杂定理拆解为更易处理的子命题。与现有方法的主要区别在于结合了语言模型生成和结构化分解策略，而非单纯依赖端到端模型或传统符号推理，从而提高了处理困难定理的灵活性和成功率。

## 📊 实验亮点

在miniF2F基准测试中，系统无分解时通过率已达90.4%，引入递归分解后性能得到显著提升，具体提升幅度未知，但强调了分解策略对处理困难定理的有效性。

## 🎯 应用场景

该研究可应用于数学定理自动证明、形式化验证、教育辅助工具和人工智能推理系统等领域，提升自动化证明的效率和可靠性，具有推动AI在逻辑推理方面发展的实际价值。

## 📄 摘要（原文）

> Formal, automated theorem proving has long been viewed as a challenge to artificial intelligence. We introduce here a new approach to computer theorem proving, one that employs specialized language models for Lean4 proof generation combined with recursive decomposition of difficult theorems into simpler entailing propositions. These models are coordinated through a multi-agent architecture that orchestrates autoformalization (if required), proof generation, decomposition of difficult theorems into simpler entailing propositions, and recursive proof (and/or decomposition) of these propositions. Without decomposition, we achieve a 90.4% pass rate on miniF2F. With decomposition, this is significantly improved. A key technical contribution lies in our extension of the Kimina Lean Server with abstract syntax tree (AST) parsing capabilities to facilitate automated, recursive proof decomposition. The system is made available on PyPI as goedels-poetry (at https://pypi.org/project/goedels-poetry ), and the open-source implementation KellyJDavis/goedels-poetry (at https://github.com/KellyJDavis/goedels-poetry ) facilitates both adaptation to alternative language models and extension with custom functionality.

