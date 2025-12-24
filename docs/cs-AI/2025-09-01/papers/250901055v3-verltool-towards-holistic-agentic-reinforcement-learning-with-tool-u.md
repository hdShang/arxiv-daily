---
layout: default
title: "VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use"
---

# VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01055" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01055v3</a>
  <a href="https://arxiv.org/pdf/2509.01055.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01055v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01055v3', 'VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dongfu Jiang, Yi Lu, Zhuofeng Li, Zhiheng Lyu, Ping Nie, Haozhe Wang, Alex Su, Hui Chen, Kai Zou, Chao Du, Tianyu Pang, Wenhu Chen

**分类**: cs.AI, cs.CL, cs.CV

**发布日期**: 2025-09-01 (更新: 2025-10-17)

**备注**: 32 pages, 5 figures, 13 tables

**🔗 代码/项目**: [GITHUB](https://github.com/TIGER-AI-Lab/verl-tool)

---

## 💡 一句话要点

**提出VerlTool以解决多轮工具交互的强化学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `工具使用` `多模态交互` `模块化设计` `异步执行`

## 📋 核心要点

1. 现有的ARLT方法在多轮工具交互中存在碎片化和执行瓶颈，限制了其扩展性和社区采用。
2. VerlTool通过统一的模块化框架，提供标准化API和异步执行，解决了现有方法的不足。
3. 在数学推理、知识问答、SQL生成等6个领域的实验中，VerlTool表现出与专用系统相当的性能，且训练基础设施统一。

## 📝 摘要（中文）

强化学习与可验证奖励（RLVR）在增强大型语言模型（LLM）推理能力方面取得了一定成功，但仍局限于单轮交互且未整合工具。近期的代理强化学习与工具使用（ARLT）方法虽然应运而生，但存在任务特定代码库的碎片化、同步执行瓶颈和跨领域扩展性有限等问题，阻碍了更广泛的社区采用和算法创新。本文提出了VerlTool，一个统一且模块化的框架，通过系统设计原则解决这些局限性。VerlTool的四大贡献包括：与VeRL的上游对齐、统一的工具管理、异步执行实现近2倍的速度提升，以及在6个ARLT领域的竞争性评估。我们的代码已开源于https://github.com/TIGER-AI-Lab/verl-tool。

## 🔬 方法详解

**问题定义**：本文旨在解决现有ARLT方法在多轮工具交互中的碎片化、同步执行瓶颈及扩展性不足的问题。这些问题限制了算法的创新和社区的广泛应用。

**核心思路**：VerlTool的核心思路是通过统一和模块化的设计，提供标准化的API和异步执行机制，从而提高工具使用的效率和灵活性。这样的设计使得不同工具的集成变得更加简单和高效。

**技术框架**：VerlTool的整体架构包括四个主要模块：工具管理模块、异步执行模块、评估模块和训练模块。工具管理模块负责不同工具的统一管理，异步执行模块消除同步瓶颈，评估模块用于性能比较，训练模块则提供统一的训练基础设施。

**关键创新**：VerlTool的关键创新在于其模块化插件架构，允许快速集成新工具，且只需轻量级的Python定义。这与现有方法的固定和复杂集成方式形成鲜明对比。

**关键设计**：在参数设置上，VerlTool采用了标准化的API设计，支持多种模态的工具使用，如代码执行、搜索、SQL数据库和视觉处理。损失函数和网络结构方面，具体细节在论文中进行了详细描述。整体设计旨在降低开发开销并提供可扩展的基础。

## 📊 实验亮点

在实验中，VerlTool在数学推理、知识问答、SQL生成、视觉推理、网页搜索和软件工程等6个领域表现出色，达到了与专用系统相当的性能，且通过异步执行实现了近2倍的速度提升，显著提高了效率。

## 🎯 应用场景

VerlTool的潜在应用领域包括智能助手、自动化软件开发、数据分析和多模态交互系统等。其模块化设计和高效的工具集成能力，使得研究人员和开发者能够快速构建和测试新的工具增强型强化学习模型，推动相关领域的技术进步和应用落地。

## 📄 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has demonstrated success in enhancing LLM reasoning capabilities, but remains limited to single-turn interactions without tool integration. While recent Agentic Reinforcement Learning with Tool use (ARLT) approaches have emerged to address multi-turn tool interactions, existing works develop task-specific codebases that suffer from fragmentation, synchronous execution bottlenecks, and limited extensibility across domains. These inefficiencies hinder broader community adoption and algorithmic innovation. We introduce VerlTool, a unified and modular framework that addresses these limitations through systematic design principles. VerlTool provides four key contributions: (1) upstream alignment with VeRL ensuring compatibility and simplified maintenance, (2) unified tool management via standardized APIs supporting diverse modalities including code execution, search, SQL databases, and vision processing, (3) asynchronous rollout execution achieving near 2$\times$ speedup by eliminating synchronization bottlenecks, and (4) comprehensive evaluation demonstrating competitive performance across 6 ARLT domains. Our framework formalizes ARLT as multi-turn trajectories with multi-modal observation tokens (text/image/video), extending beyond single-turn RLVR paradigms. We train and evaluate models on mathematical reasoning, knowledge QA, SQL generation, visual reasoning, web search, and software engineering tasks, achieving results comparable to specialized systems while providing unified training infrastructure. The modular plugin architecture enables rapid tool integration requiring only lightweight Python definitions, significantly reducing development overhead and providing a scalable foundation for tool-augmented RL research. Our code is open-sourced at https://github.com/TIGER-AI-Lab/verl-tool.

