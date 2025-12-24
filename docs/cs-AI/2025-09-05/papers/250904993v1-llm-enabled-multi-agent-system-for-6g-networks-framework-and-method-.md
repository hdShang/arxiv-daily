---
layout: default
title: "LLM Enabled Multi-Agent System for 6G Networks: Framework and Method of Dual-Loop Edge-Terminal Collaboration"
---

# LLM Enabled Multi-Agent System for 6G Networks: Framework and Method of Dual-Loop Edge-Terminal Collaboration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04993" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04993v1</a>
  <a href="https://arxiv.org/pdf/2509.04993.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04993v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04993v1', 'LLM Enabled Multi-Agent System for 6G Networks: Framework and Method of Dual-Loop Edge-Terminal Collaboration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zheyan Qu, Wenbo Wang, Zitong Yu, Boquan Sun, Yang Li, Xing Zhang

**分类**: cs.MA, cs.AI

**发布日期**: 2025-09-05

**备注**: This paper has been accepted by IEEE Communications Magazine

---

## 💡 一句话要点

**提出基于LLM的多智能体双环协同框架，提升6G网络边缘终端任务处理效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `6G网络` `边缘计算` `LLM` `任务分解` `双环协同` `智能体协作`

## 📋 核心要点

1. 现有LLM智能体在6G网络中面临设备资源限制，复杂工具调用效率低下，难以满足多样化的用户需求。
2. 论文提出双环协同框架，通过边缘-终端多智能体协作，分解复杂任务，并行执行子任务，提升整体效率。
3. 案例研究表明，该方法在6G支持的城市安全治理中，有效提升了任务规划和执行效率，验证了框架的有效性。

## 📝 摘要（中文）

本文提出了一种基于LLM的多智能体系统框架和双环终端-边缘协同方法，用于6G网络。该框架旨在解决单个网络设备资源有限，难以高效运行复杂工具调用的LLM智能体的问题。外环由全局智能体与部署在边缘服务器和终端上的多个子智能体迭代协作构成，通过任务分解和并行子任务分配来增强规划能力。内环利用具有专门角色的子智能体循环推理、执行和重新规划子任务，并结合卸载策略的并行工具调用生成来提高效率。通过在6G支持的城市安全治理案例研究中验证了改进的任务规划能力和任务执行效率。最后，分析了6G网络中面临的开放挑战和未来发展方向，以加速6G时代的到来。

## 🔬 方法详解

**问题定义**：论文旨在解决6G网络中，单个网络设备资源有限，导致LLM智能体无法高效运行复杂工具调用，从而限制了其在多样化环境和用户意图下的应用。现有方法难以充分利用边缘和终端的计算资源进行协同，导致任务处理效率低下。

**核心思路**：论文的核心思路是构建一个基于LLM的多智能体系统，通过双环协同机制，将复杂任务分解为多个子任务，并分配给边缘服务器和终端上的子智能体并行处理。外环负责任务分解和子任务分配，内环负责子任务的循环推理、执行和重新规划，从而提高整体任务处理效率。

**技术框架**：该框架包含一个全局智能体和多个子智能体。全局智能体部署在云端或边缘服务器上，负责接收用户请求，进行任务分解，并将子任务分配给边缘服务器和终端上的子智能体。子智能体具有专门的角色，负责执行分配到的子任务，并进行循环推理、执行和重新规划。外环是全局智能体与子智能体之间的迭代协作，内环是子智能体内部的循环推理、执行和重新规划。

**关键创新**：该论文的关键创新在于提出了双环协同机制，实现了边缘和终端的计算资源协同利用，提高了LLM智能体的任务处理效率。此外，论文还提出了基于卸载策略的并行工具调用生成方法，进一步提高了子智能体的执行效率。

**关键设计**：论文中，全局智能体和子智能体都基于LLM构建，并配备了辅助模块和规划核心。全局智能体使用任务分解算法将复杂任务分解为多个子任务。子智能体使用循环推理、执行和重新规划机制来执行子任务。论文还设计了卸载策略，用于决定哪些工具调用应该在本地执行，哪些应该卸载到边缘服务器执行。

## 📊 实验亮点

论文通过在6G支持的城市安全治理案例研究中验证了所提出的框架和方法。实验结果表明，该方法能够有效提升任务规划能力和任务执行效率。具体的性能数据和对比基线在论文中进行了详细的展示和分析。（具体数值未知，需查阅原文）

## 🎯 应用场景

该研究成果可应用于6G网络支持的各种场景，如城市安全治理、智能交通、远程医疗等。通过多智能体协同，可以更高效地处理复杂任务，提升服务质量，并为用户提供更智能化的服务。未来，该框架可以进一步扩展到更多的应用领域，并与其他技术相结合，实现更强大的功能。

## 📄 摘要（原文）

> The ubiquitous computing resources in 6G networks provide ideal environments for the fusion of large language models (LLMs) and intelligent services through the agent framework. With auxiliary modules and planning cores, LLM-enabled agents can autonomously plan and take actions to deal with diverse environment semantics and user intentions. However, the limited resources of individual network devices significantly hinder the efficient operation of LLM-enabled agents with complex tool calls, highlighting the urgent need for efficient multi-level device collaborations. To this end, the framework and method of the LLM-enabled multi-agent system with dual-loop terminal-edge collaborations are proposed in 6G networks. Firstly, the outer loop consists of the iterative collaborations between the global agent and multiple sub-agents deployed on edge servers and terminals, where the planning capability is enhanced through task decomposition and parallel sub-task distribution. Secondly, the inner loop utilizes sub-agents with dedicated roles to circularly reason, execute, and replan the sub-task, and the parallel tool calling generation with offloading strategies is incorporated to improve efficiency. The improved task planning capability and task execution efficiency are validated through the conducted case study in 6G-supported urban safety governance. Finally, the open challenges and future directions are thoroughly analyzed in 6G networks, accelerating the advent of the 6G era.

