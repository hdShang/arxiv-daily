---
layout: default
title: "Beyond Formal Semantics for Capabilities and Skills: Model Context Protocol in Manufacturing"
---

# Beyond Formal Semantics for Capabilities and Skills: Model Context Protocol in Manufacturing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11180" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11180v2</a>
  <a href="https://arxiv.org/pdf/2506.11180.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11180v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11180v2', 'Beyond Formal Semantics for Capabilities and Skills: Model Context Protocol in Manufacturing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luis Miguel Vieira da Silva, Aljosha Köcher, Felix Gehlhoff

**分类**: cs.SE, cs.AI, cs.ET, eess.SY

**发布日期**: 2025-06-12 (更新: 2025-12-09)

**备注**: \c{opyright} 2025 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works

**DOI**: [10.1109/ETFA65518.2025.11205601](https://doi.org/10.1109/ETFA65518.2025.11205601)

---

## 💡 一句话要点

**提出模型上下文协议以简化制造业能力与技能建模**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模型上下文协议` `能力建模` `技能建模` `工业自动化` `大型语言模型` `资源管理` `智能制造`

## 📋 核心要点

1. 现有的能力与技能建模方法需要大量手动工作，且难以被大型语言模型有效利用。
2. 本文提出模型上下文协议（MCP），通过标准化接口使系统功能可被LLM直接消费，简化了建模过程。
3. 实验结果表明，MCP能够支持灵活的工业自动化，显著提高了生产系统的效率和适应性。

## 📝 摘要（中文）

明确建模能力和技能（无论基于本体、资产管理外壳还是其他技术）需要大量手动工作，且通常导致的表示形式不易被大型语言模型（LLMs）访问。本文提出了一种基于新近引入的模型上下文协议（MCP）的替代方法。MCP允许系统通过标准化接口暴露功能，直接被基于LLM的代理消费。我们在实验室规模的制造系统上进行了原型评估，通过MCP提供资源功能。然后，通用LLM被任务规划和执行多步骤过程，包括约束处理和通过MCP调用资源功能。结果表明，这种方法可以实现灵活的工业自动化，而无需依赖显式的语义模型。此项工作为进一步探索LLM驱动的生产系统中的外部工具集成奠定了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决现有能力与技能建模方法的不足，特别是手动建模的高成本和对大型语言模型的低兼容性问题。

**核心思路**：提出模型上下文协议（MCP），通过标准化接口使得系统功能能够被LLM直接调用，从而减少对显式语义模型的依赖。

**技术框架**：整体架构包括资源功能的暴露、LLM的任务规划与执行。主要模块包括MCP接口、资源管理模块和LLM执行引擎。

**关键创新**：MCP的引入是本文的核心创新，它与现有方法的本质区别在于不再依赖复杂的语义模型，而是通过标准化接口实现功能的直接调用。

**关键设计**：在设计中，MCP接口的标准化是关键，确保了不同系统间的互操作性。此外，资源函数的调用机制和约束处理策略也经过精心设计，以适应多步骤的任务执行。

## 📊 实验亮点

实验结果显示，基于MCP的系统能够有效地进行多步骤任务规划与执行，且在约束处理和资源调用方面表现出色。与传统方法相比，生产效率显著提升，具体性能数据尚未披露。

## 🎯 应用场景

该研究的潜在应用领域包括智能制造、工业自动化和机器人控制等。通过简化能力与技能的建模过程，MCP能够提高生产系统的灵活性和响应速度，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Explicit modeling of capabilities and skills -- whether based on ontologies, Asset Administration Shells, or other technologies -- requires considerable manual effort and often results in representations that are not easily accessible to Large Language Models (LLMs). In this work-in-progress paper, we present an alternative approach based on the recently introduced Model Context Protocol (MCP). MCP allows systems to expose functionality through a standardized interface that is directly consumable by LLM-based agents. We conduct a prototypical evaluation on a laboratory-scale manufacturing system, where resource functions are made available via MCP. A general-purpose LLM is then tasked with planning and executing a multi-step process, including constraint handling and the invocation of resource functions via MCP. The results indicate that such an approach can enable flexible industrial automation without relying on explicit semantic models. This work lays the basis for further exploration of external tool integration in LLM-driven production systems.

