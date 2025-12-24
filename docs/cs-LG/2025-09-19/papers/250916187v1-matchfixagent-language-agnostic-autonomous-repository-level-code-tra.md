---
layout: default
title: "MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Translation Validation and Repair"
---

# MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Translation Validation and Repair

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16187" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16187v1</a>
  <a href="https://arxiv.org/pdf/2509.16187.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16187v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16187v1', 'MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Translation Validation and Repair')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ali Reza Ibrahimzada, Brandon Paulsen, Reyhaneh Jabbarvand, Joey Dodds, Daniel Kroening

**分类**: cs.SE, cs.LG

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**提出MatchFixAgent，实现语言无关的仓库级代码翻译验证与修复**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码翻译` `等价性验证` `代码修复` `大型语言模型` `多智能体系统`

## 📋 核心要点

1. 现有代码翻译验证与修复方法工程开销大，且依赖不足的测试集，导致验证不准确和修复效果差。
2. MatchFixAgent利用多智能体架构，对翻译进行语义分析，生成测试用例，并进行修复，实现语言无关的验证与修复。
3. 实验表明，MatchFixAgent在验证准确性和修复能力上均优于现有方法，尤其在多种编程语言对上表现出更强的适应性。

## 📝 摘要（中文）

代码翻译是将源代码从一种编程语言（PL）转换为另一种编程语言。验证翻译的功能等价性并在必要时进行修复是代码翻译中的关键步骤。现有的自动化验证和修复方法难以推广到多种编程语言，因为工程开销高，并且它们依赖于现有且通常不足的测试套件，这导致错误的等价性声明和无效的翻译修复。我们开发了MatchFixAgent，这是一个基于大型语言模型（LLM）的、与编程语言无关的框架，用于翻译的等价性验证和修复。MatchFixAgent具有多智能体架构，该架构将等价性验证划分为多个子任务，以确保对翻译进行彻底和一致的语义分析。然后，它将此分析反馈给测试智能体以编写和执行测试。在观察到测试失败后，修复智能体会尝试修复翻译错误。最终的（非）等价性决策由裁决智能体做出，该智能体会考虑语义分析和测试执行结果。

## 🔬 方法详解

**问题定义**：代码翻译的验证与修复是保证翻译质量的关键环节。现有方法的痛点在于对特定编程语言的依赖性强，难以泛化到多种语言，同时依赖于质量不高的现有测试集，导致验证结果不准确，修复效果不佳。因此，需要一种语言无关且能有效生成测试用例的验证与修复方法。

**核心思路**：MatchFixAgent的核心思路是利用大型语言模型（LLM）的强大语义理解和生成能力，构建一个多智能体系统，将验证与修复任务分解为多个子任务，每个智能体负责不同的功能，协同完成整个过程。通过语义分析指导测试用例生成，并利用测试结果驱动翻译修复，从而实现更准确、更有效的验证与修复。

**技术框架**：MatchFixAgent采用多智能体架构，主要包含以下几个模块：
1. **语义分析智能体**：负责对源程序和目标程序进行语义分析，提取关键信息。
2. **测试智能体**：根据语义分析结果，生成测试用例，并执行测试。
3. **修复智能体**：在测试失败时，尝试修复翻译中的错误。
4. **裁决智能体**：综合语义分析和测试结果，做出最终的等价性判断。

**关键创新**：MatchFixAgent最重要的技术创新在于其语言无关性和多智能体架构。语言无关性使得该方法可以应用于多种编程语言对的翻译验证与修复，而多智能体架构则将复杂的验证与修复任务分解为多个子任务，提高了效率和准确性。与现有方法相比，MatchFixAgent不再依赖于特定语言的工具和现有测试集，而是通过LLM自主生成测试用例，从而避免了对现有资源的依赖。

**关键设计**：MatchFixAgent的关键设计包括：
1. **语义分析策略**：如何有效地利用LLM进行语义分析，提取关键信息。
2. **测试用例生成策略**：如何根据语义分析结果生成高质量的测试用例。
3. **修复策略**：如何利用LLM进行代码修复，并保证修复后的代码的正确性。
4. **智能体之间的协作机制**：如何协调各个智能体的工作，保证整个系统的稳定性和效率。具体参数设置和损失函数等细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

MatchFixAgent在2219个翻译对上进行了评估，覆盖6种编程语言对。实验结果表明，MatchFixAgent对99.2%的翻译对给出了（非）等价性判断，与现有方法相比，在72.8%的翻译对上结果一致。在结果不一致的情况下，MatchFixAgent的判断正确率高达60.7%。此外，MatchFixAgent能够修复50.6%的不等价翻译，而现有方法仅能修复18.5%。

## 🎯 应用场景

MatchFixAgent可应用于各种代码翻译场景，例如遗留系统迁移、跨平台应用开发、代码库现代化等。该研究的实际价值在于提高代码翻译的质量和效率，降低开发成本，并促进不同编程语言之间的互操作性。未来，该技术有望进一步发展，实现更智能、更自动化的代码翻译与维护。

## 📄 摘要（原文）

> Code translation transforms source code from one programming language (PL) to another. Validating the functional equivalence of translation and repairing, if necessary, are critical steps in code translation. Existing automated validation and repair approaches struggle to generalize to many PLs due to high engineering overhead, and they rely on existing and often inadequate test suites, which results in false claims of equivalence and ineffective translation repair. We develop MatchFixAgent, a large language model (LLM)-based, PL-agnostic framework for equivalence validation and repair of translations. MatchFixAgent features a multi-agent architecture that divides equivalence validation into several sub-tasks to ensure thorough and consistent semantic analysis of the translation. Then it feeds this analysis to test agent to write and execute tests. Upon observing a test failure, the repair agent attempts to fix the translation bug. The final (in)equivalence decision is made by the verdict agent, considering semantic analyses and test execution results.
>   We compare MatchFixAgent's validation and repair results with four repository-level code translation techniques. We use 2,219 translation pairs from their artifacts, which cover 6 PL pairs, and are collected from 24 GitHub projects totaling over 900K lines of code. Our results demonstrate that MatchFixAgent produces (in)equivalence verdicts for 99.2% of translation pairs, with the same equivalence validation result as prior work on 72.8% of them. When MatchFixAgent's result disagrees with prior work, we find that 60.7% of the time MatchFixAgent's result is actually correct. In addition, we show that MatchFixAgent can repair 50.6% of inequivalent translation, compared to prior work's 18.5%. This demonstrates that MatchFixAgent is far more adaptable to many PL pairs than prior work, while producing highly accurate validation results.

