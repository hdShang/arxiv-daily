---
layout: default
title: "InfiAgent: Self-Evolving Pyramid Agent Framework for Infinite Scenarios"
---

# InfiAgent: Self-Evolving Pyramid Agent Framework for Infinite Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22502" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22502v2</a>
  <a href="https://arxiv.org/pdf/2509.22502.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22502v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22502v2', 'InfiAgent: Self-Evolving Pyramid Agent Framework for Infinite Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenglin Yu, Yang Yu, Songmiao Wang, Yucheng Wang, Yifan Yang, Jinjia Li, Ming Li, Hongxia Yang

**分类**: cs.AI, cs.HC

**发布日期**: 2025-09-26 (更新: 2025-09-30)

**备注**: 9 pages of main content and 32 pages of others, 2 figures, under review as a conference paper at ICLR 2026

---

## 💡 一句话要点

**InfiAgent：面向无限场景的自进化金字塔型智能体框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多智能体系统` `智能体自进化` `任务分解` `智能体路由`

## 📋 核心要点

1. 现有LLM智能体依赖手工设计的工作流和提示工程，缺乏可扩展性和成本效益，难以适应广泛的行业应用。
2. InfiAgent提出一种金字塔型DAG多智能体框架，通过智能体自进化、任务分解和双重审计机制，实现无限场景下的高效任务处理。
3. 实验表明，InfiAgent在多个基准测试中优于ADAS 9.9%，并成功应用于AI研究助手InfiHelper，生成的论文获得顶级会议认可。

## 📝 摘要（中文）

大型语言模型（LLM）智能体在组织和执行复杂任务方面表现出卓越的能力，并已广泛应用于各种应用场景。然而，开发这些智能体需要精心设计的工作流程、提示和迭代调整，这需要LLM技术和特定领域的专业知识。这些手工设计的限制阻碍了LLM智能体在广泛行业中的可扩展性和成本效益。为了应对这些挑战，我们提出了InfiAgent，一个基于金字塔型DAG的多智能体框架，可以应用于无限场景。InfiAgent引入了几个关键创新：一种通用的“智能体即工具”机制，可自动将复杂智能体分解为分层多智能体系统；一种双重审计机制，可确保任务完成的质量和稳定性；一种智能体路由功能，可实现高效的任务-智能体匹配；以及一种智能体自进化机制，可根据新任务、不良性能或优化机会自主重构智能体DAG。此外，InfiAgent的原子任务设计支持智能体并行性，从而显着提高执行效率。该框架演变为一个通用的金字塔型多智能体系统，能够解决范围广泛的问题。在多个基准上的评估表明，与ADAS（类似的自动生成智能体框架）相比，InfiAgent的性能提高了9.9％，而AI研究助手InfiHelper的案例研究表明，它生成的科学论文已获得顶级IEEE会议上的人工评审员的认可。

## 🔬 方法详解

**问题定义**：现有的大型语言模型智能体在处理复杂任务时，依赖于人工设计的流程和提示，这限制了它们的可扩展性和在不同领域的应用。手动调整和优化这些智能体既耗时又需要专业知识，使得在各种场景下部署和维护这些智能体变得困难。因此，如何自动地构建和优化LLM智能体，使其能够适应各种复杂任务，是一个亟待解决的问题。

**核心思路**：InfiAgent的核心思路是将复杂的智能体分解为多个更小的、可重用的“智能体即工具”，并通过金字塔型的DAG结构组织这些智能体。这种分解使得任务可以被分配给最合适的智能体，并且可以通过智能体自进化机制自动优化整个智能体系统的结构。双重审计机制确保了任务完成的质量和稳定性。

**技术框架**：InfiAgent的技术框架主要包含以下几个模块：1) 智能体分解模块：将复杂任务分解为原子任务，并为每个任务选择或创建合适的智能体。2) 智能体路由模块：根据任务的特性，将任务分配给最合适的智能体。3) 双重审计模块：对智能体的输出进行验证，确保任务完成的质量。4) 智能体自进化模块：根据任务的完成情况和性能反馈，自动调整智能体DAG的结构，包括添加、删除或修改智能体。整个框架采用金字塔型的DAG结构，顶层是负责全局规划的智能体，底层是执行原子任务的智能体。

**关键创新**：InfiAgent的关键创新在于：1) “智能体即工具”机制，将复杂智能体分解为可重用的组件。2) 双重审计机制，确保任务完成的质量和稳定性。3) 智能体自进化机制，能够根据任务反馈自动优化智能体DAG的结构。与现有方法相比，InfiAgent能够自动构建和优化智能体系统，无需人工干预，从而提高了可扩展性和适应性。

**关键设计**：InfiAgent的关键设计包括：1) 原子任务的定义：原子任务是不可再分的最小任务单元，需要仔细设计以确保智能体能够有效地执行。2) 智能体路由函数的选择：路由函数需要能够准确地将任务分配给最合适的智能体，可以使用基于规则的方法或机器学习模型。3) 自进化机制的实现：自进化机制需要定义合适的奖励函数和优化算法，以确保智能体DAG能够朝着更好的方向发展。4) 双重审计机制的具体实现：例如，可以采用多数投票或者专家评审的方式。

## 📊 实验亮点

InfiAgent在多个基准测试中取得了显著的性能提升，与ADAS相比，性能提高了9.9%。此外，InfiAgent成功应用于AI研究助手InfiHelper，生成的科学论文获得了顶级IEEE会议上人工评审员的认可，证明了InfiAgent在实际应用中的有效性。这些实验结果表明，InfiAgent是一种有前景的自动构建和优化LLM智能体的方法。

## 🎯 应用场景

InfiAgent具有广泛的应用前景，例如可以应用于AI研究助手，帮助研究人员进行文献综述、实验设计和论文撰写；可以应用于智能客服，自动处理用户咨询和投诉；还可以应用于自动化软件开发，自动生成和测试代码。该研究的实际价值在于降低了开发和维护LLM智能体的成本，提高了智能体的可扩展性和适应性。未来，InfiAgent有望成为构建通用人工智能系统的关键技术。

## 📄 摘要（原文）

> Large Language Model (LLM) agents have demonstrated remarkable capabilities in organizing and executing complex tasks, and many such agents are now widely used in various application scenarios. However, developing these agents requires carefully designed workflows, carefully crafted prompts, and iterative tuning, which requires LLM techniques and domain-specific expertise. These hand-crafted limitations hinder the scalability and cost-effectiveness of LLM agents across a wide range of industries. To address these challenges, we propose \textbf{InfiAgent}, a Pyramid-like DAG-based Multi-Agent Framework that can be applied to \textbf{infi}nite scenarios, which introduces several key innovations: a generalized "agent-as-a-tool" mechanism that automatically decomposes complex agents into hierarchical multi-agent systems; a dual-audit mechanism that ensures the quality and stability of task completion; an agent routing function that enables efficient task-agent matching; and an agent self-evolution mechanism that autonomously restructures the agent DAG based on new tasks, poor performance, or optimization opportunities. Furthermore, InfiAgent's atomic task design supports agent parallelism, significantly improving execution efficiency. This framework evolves into a versatile pyramid-like multi-agent system capable of solving a wide range of problems. Evaluations on multiple benchmarks demonstrate that InfiAgent achieves 9.9\% higher performance compared to ADAS (similar auto-generated agent framework), while a case study of the AI research assistant InfiHelper shows that it generates scientific papers that have received recognition from human reviewers at top-tier IEEE conferences.

