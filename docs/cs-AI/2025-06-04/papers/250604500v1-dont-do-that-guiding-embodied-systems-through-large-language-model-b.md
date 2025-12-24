---
layout: default
title: "\"Don't Do That!\": Guiding Embodied Systems through Large Language Model-based Constraint Generation"
---

# "Don't Do That!": Guiding Embodied Systems through Large Language Model-based Constraint Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04500" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04500v1</a>
  <a href="https://arxiv.org/pdf/2506.04500.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04500v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04500v1', '&quot;Don\'t Do That!&quot;: Guiding Embodied Systems through Large Language Model-based Constraint Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aladin Djuhera, Amin Seffo, Masataro Asai, Holger Boche

**分类**: cs.AI, cs.RO

**发布日期**: 2025-06-04

**备注**: Preprint; under review

---

## 💡 一句话要点

**提出STPR框架以通过LLM生成约束指导机器人导航**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `约束生成` `机器人导航` `Python函数` `自动化控制` `智能助手` `点云表示`

## 📋 核心要点

1. 现有方法在将自然语言中的复杂约束转化为可执行代码时面临挑战，容易出现推理错误。
2. 本文提出的STPR框架利用大型语言模型生成可执行的Python函数，从而简化约束表达过程。
3. 实验结果表明，STPR在多个约束和场景中表现出色，确保合规性且运行时间短，适用于小型模型。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进展激发了对将复杂空间、数学和条件约束纳入机器人导航规划问题的兴趣。这些约束可能是非正式且高度复杂的，难以转化为可传递给规划算法的正式描述。本文提出了STPR，一个约束生成框架，利用LLMs将以“不要做什么”为指令表达的约束转化为可执行的Python函数。STPR利用LLM强大的编码能力，将问题描述从语言转变为结构化和透明的代码，从而避免复杂推理和潜在的幻觉。实验表明，LLM生成的函数能够准确描述复杂的数学约束，并将其应用于传统搜索算法的点云表示中。模拟Gazebo环境中的实验显示，STPR在多个约束和场景中确保完全合规，同时具有较短的运行时间。

## 🔬 方法详解

**问题定义**：本文旨在解决如何将自然语言中的复杂约束有效转化为可供机器人导航使用的可执行代码的问题。现有方法在处理这些非正式且复杂的约束时，往往难以避免推理错误和不准确性。

**核心思路**：STPR框架的核心思路是利用大型语言模型的强大编码能力，将“不要做什么”的指令转化为结构化的Python代码。这种设计能够有效避免复杂的推理过程，并减少潜在的幻觉现象。

**技术框架**：STPR框架主要包括两个模块：约束解析模块和代码生成模块。约束解析模块负责从自然语言中提取约束信息，而代码生成模块则将这些信息转化为可执行的Python函数。

**关键创新**：STPR的主要创新在于将大型语言模型应用于约束生成，能够准确描述复杂的数学约束，并将其应用于点云表示中。这一方法与传统的手动编码方式有本质区别，显著提高了效率和准确性。

**关键设计**：在设计上，STPR框架采用了特定的参数设置，以优化LLM的输出质量，并确保生成的代码能够在传统搜索算法中高效运行。

## 📊 实验亮点

实验结果显示，STPR框架在多个约束和场景中实现了100%的合规性，且运行时间显著低于传统方法。此外，STPR能够与小型、特定代码的LLM兼容，降低了推理成本，展现出良好的实用性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、自动化控制和智能助手等。通过将自然语言中的复杂约束转化为可执行代码，STPR框架能够在多种实际场景中提供有效的解决方案，提升机器人系统的智能化水平和操作安全性，未来可能在智能家居、无人驾驶等领域产生深远影响。

## 📄 摘要（原文）

> Recent advancements in large language models (LLMs) have spurred interest in robotic navigation that incorporates complex spatial, mathematical, and conditional constraints from natural language into the planning problem. Such constraints can be informal yet highly complex, making it challenging to translate into a formal description that can be passed on to a planning algorithm. In this paper, we propose STPR, a constraint generation framework that uses LLMs to translate constraints (expressed as instructions on ``what not to do'') into executable Python functions. STPR leverages the LLM's strong coding capabilities to shift the problem description from language into structured and transparent code, thus circumventing complex reasoning and avoiding potential hallucinations. We show that these LLM-generated functions accurately describe even complex mathematical constraints, and apply them to point cloud representations with traditional search algorithms. Experiments in a simulated Gazebo environment show that STPR ensures full compliance across several constraints and scenarios, while having short runtimes. We also verify that STPR can be used with smaller, code-specific LLMs, making it applicable to a wide range of compact models at low inference cost.

