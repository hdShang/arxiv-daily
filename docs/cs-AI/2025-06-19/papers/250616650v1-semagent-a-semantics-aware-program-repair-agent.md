---
layout: default
title: "SemAgent: A Semantics Aware Program Repair Agent"
---

# SemAgent: A Semantics Aware Program Repair Agent

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16650" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16650v1</a>
  <a href="https://arxiv.org/pdf/2506.16650.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16650v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16650v1', 'SemAgent: A Semantics Aware Program Repair Agent')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anvith Pabba, Alex Mathai, Anindya Chakraborty, Baishakhi Ray

**分类**: cs.SE, cs.AI, cs.MA

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出SemAgent以解决程序修复中的语义理解问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `程序修复` `语义理解` `大型语言模型` `自动化修复` `软件工程` `深度学习`

## 📋 核心要点

1. 现有的程序修复方法往往局限于局部代码，缺乏对问题和代码语义的全面理解，导致修复效果不佳。
2. SemAgent通过引入问题、代码和执行语义，采用工作流方法生成完整的修复补丁，提升了修复的准确性和有效性。
3. 在SWEBench-Lite基准测试中，SemAgent的解决率为44.66%，相比基线提升了7.66%，特别在多行推理和边缘案例处理上表现突出。

## 📝 摘要（中文）

大型语言模型（LLMs）在自动化程序修复（APR）等软件工程任务中展现了卓越的能力。然而，现有的修复系统往往过于关注代码中明显可疑的行，缺乏对问题语义、代码语义和执行语义的深入理解，导致生成的补丁往往过拟合于特定用户问题。为了解决这一局限，本文提出了SemAgent，一个基于工作流的程序修复代理，利用问题、代码和执行语义生成完整的补丁。通过创新的管道设计，SemAgent能够识别并修复与问题相关的所有代码行。实验结果表明，SemAgent在SWEBench-Lite基准测试中实现了44.66%的解决率，超越了所有其他基于工作流的方法，并且相比于缺乏深层语义理解的基线提升了7.66%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有程序修复系统在处理用户问题时的局限性，尤其是它们对问题语义和代码上下文的缺乏理解，导致生成的补丁往往不够全面和有效。

**核心思路**：SemAgent的核心思路是通过综合考虑问题、代码和执行语义，采用工作流方法生成完整的修复补丁，确保修复过程不仅关注局部代码，还能理解整体问题背景。

**技术框架**：SemAgent的整体架构包括四个主要模块：首先，利用执行语义检索相关上下文；其次，通过广义抽象理解问题语义；接着，在该抽象的上下文中隔离代码语义；最后，采用两阶段架构进行修复：第一阶段提出细粒度修复，第二阶段根据推断的问题语义筛选相关修复。

**关键创新**：SemAgent的主要创新在于其深层语义理解能力，通过综合考虑多种语义信息，生成的补丁不仅解决特定问题，还具备更广泛的适用性，避免了过拟合现象。

**关键设计**：在设计上，SemAgent采用了两阶段的修复流程，第一阶段关注细粒度修复，第二阶段则通过语义推断进行修复筛选，确保最终生成的补丁既准确又全面。

## 📊 实验亮点

SemAgent在SWEBench-Lite基准测试中实现了44.66%的解决率，超越了所有其他基于工作流的方法，并且相比于缺乏深层语义理解的基线提升了7.66%。该方法在处理需要多行推理和边缘案例的修复问题时表现尤为突出，显示出其强大的实用性和有效性。

## 🎯 应用场景

SemAgent在软件开发和维护领域具有广泛的应用潜力，尤其是在需要自动化程序修复的场景中。其深层语义理解能力可以提高修复的准确性和效率，减少开发者的工作负担，促进软件质量的提升。未来，该方法还可以扩展到其他软件工程任务，如代码重构和优化等。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown impressive capabilities in downstream software engineering tasks such as Automated Program Repair (APR). In particular, there has been a lot of research on repository-level issue-resolution benchmarks such as SWE-Bench. Although there has been significant progress on this topic, we notice that in the process of solving such issues, existing agentic systems tend to hyper-localize on immediately suspicious lines of code and fix them in isolation, without a deeper understanding of the issue semantics, code semantics, or execution semantics. Consequently, many existing systems generate patches that overfit to the user issue, even when a more general fix is preferable. To address this limitation, we introduce SemAgent, a novel workflow-based procedure that leverages issue, code, and execution semantics to generate patches that are complete - identifying and fixing all lines relevant to the issue. We achieve this through a novel pipeline that (a) leverages execution semantics to retrieve relevant context, (b) comprehends issue-semantics via generalized abstraction, (c) isolates code-semantics within the context of this abstraction, and (d) leverages this understanding in a two-stage architecture: a repair stage that proposes fine-grained fixes, followed by a reviewer stage that filters relevant fixes based on the inferred issue-semantics. Our evaluations show that our methodology achieves a solve rate of 44.66% on the SWEBench-Lite benchmark beating all other workflow-based approaches, and an absolute improvement of 7.66% compared to our baseline, which lacks such deep semantic understanding. We note that our approach performs particularly well on issues requiring multi-line reasoning (and editing) and edge-case handling, suggesting that incorporating issue and code semantics into APR pipelines can lead to robust and semantically consistent repairs.

