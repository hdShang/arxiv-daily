---
layout: default
title: "NaviAgent: Bilevel Planning on Tool Navigation Graph for Large-Scale Orchestration"
---

# NaviAgent: Bilevel Planning on Tool Navigation Graph for Large-Scale Orchestration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19500" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19500v2</a>
  <a href="https://arxiv.org/pdf/2506.19500.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19500v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19500v2', 'NaviAgent: Bilevel Planning on Tool Navigation Graph for Large-Scale Orchestration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yan Jiang, Hao Zhou, LiZhong GU, Ai Han, TianLong Li

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-06-24 (更新: 2025-10-31)

---

## 💡 一句话要点

**提出NaviAgent以解决大规模工具导航中的规划与执行问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `工具导航` `任务规划` `双层架构` `图模型` `闭环优化` `自适应导航` `大型语言模型` `工具链编排`

## 📋 核心要点

1. 现有的工具调用代理在处理复杂任务时缺乏全局视图，导致错误累积和可扩展性不足。
2. NaviAgent通过双层架构将任务规划与工具执行解耦，采用图模型对工具生态系统进行建模。
3. 实验结果显示，NaviAgent在任务成功率上优于其他模型，复杂任务性能提升最高可达17个百分点。

## 📝 摘要（中文）

大型语言模型（LLMs）最近展示了作为功能调用代理的能力，通过调用外部工具来解决超出其静态知识范围的任务。然而，现有代理通常逐步调用工具，缺乏对任务结构的全局视图。这导致错误累积和可扩展性有限，尤其是在扩展到数千个工具时。为了解决这些问题，本文提出了NaviAgent，一种新颖的双层架构，通过图模型对工具生态系统进行建模，将任务规划与工具执行解耦。在任务规划层，基于LLM的代理决定直接响应、澄清用户意图、调用工具链或执行工具输出，从而确保在不依赖工具间复杂性的情况下广泛覆盖交互场景。在执行层，持续演变的工具世界导航模型（TWNM）编码工具之间的结构和行为关系，引导代理生成可扩展且稳健的调用序列。通过结合真实工具交互的反馈，NaviAgent支持规划和执行的闭环优化，超越了简单的工具调用，朝着大规模工具生态系统的自适应导航发展。实验表明，NaviAgent在各模型和任务中实现了最佳任务成功率，集成TWMN进一步提升了复杂任务的性能，最高可达17个百分点，突显了其在工具链编排中的关键作用。

## 🔬 方法详解

**问题定义**：本文旨在解决现有工具调用代理在处理复杂任务时的局限性，特别是缺乏全局视图导致的错误累积和可扩展性问题。

**核心思路**：NaviAgent通过双层架构设计，将任务规划与工具执行分开，利用图模型来表示工具之间的关系，从而实现更高效的任务处理和工具调用。

**技术框架**：NaviAgent的整体架构包括任务规划层和执行层。在任务规划层，代理根据用户意图选择响应方式；在执行层，TWNM模型编码工具间的关系，指导代理生成调用序列。

**关键创新**：NaviAgent的主要创新在于引入了TWNM，通过对工具生态系统的动态建模，支持闭环优化，显著提高了工具调用的灵活性和准确性。

**关键设计**：在设计上，TWNM不断更新以反映工具间的结构和行为关系，确保代理能够生成适应性强的调用序列，此外，采用了反馈机制来优化规划与执行过程。

## 📊 实验亮点

实验结果表明，NaviAgent在各类任务中均实现了最佳的任务成功率，尤其是在复杂任务上，集成TWNM后性能提升最高可达17个百分点，显著优于现有模型，展示了其在工具链编排中的重要性。

## 🎯 应用场景

NaviAgent的研究成果在多个领域具有潜在应用价值，包括智能助手、自动化任务处理和复杂系统管理等。其自适应导航能力能够有效提升工具链的使用效率，推动智能系统的进一步发展与应用。

## 📄 摘要（原文）

> Large language models (LLMs) have recently demonstrated the ability to act as function call agents by invoking external tools, enabling them to solve tasks beyond their static knowledge. However, existing agents typically call tools step by step at a time without a global view of task structure. As tools depend on each other, this leads to error accumulation and limited scalability, particularly when scaling to thousands of tools. To address these limitations, we propose NaviAgent, a novel bilevel architecture that decouples task planning from tool execution through graph-based modeling of the tool ecosystem. At the task-planning level, the LLM-based agent decides whether to respond directly, clarify user intent, invoke a toolchain, or execute tool outputs, ensuring broad coverage of interaction scenarios independent of inter-tool complexity. At the execution level, a continuously evolving Tool World Navigation Model (TWNM) encodes structural and behavioral relations among tools, guiding the agent to generate scalable and robust invocation sequences. By incorporating feedback from real tool interactions, NaviAgent supports closed-loop optimization of planning and execution, moving beyond tool calling toward adaptive navigation of large-scale tool ecosystems. Experiments show that NaviAgent achieves the best task success rates across models and tasks, and integrating TWMN further boosts performance by up to 17 points on complex tasks, underscoring its key role in toolchain orchestration.

