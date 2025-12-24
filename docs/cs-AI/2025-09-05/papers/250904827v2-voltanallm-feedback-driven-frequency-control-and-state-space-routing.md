---
layout: default
title: "VoltanaLLM: Feedback-Driven Frequency Control and State-Space Routing for Energy-Efficient LLM Serving"
---

# VoltanaLLM: Feedback-Driven Frequency Control and State-Space Routing for Energy-Efficient LLM Serving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04827" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04827v2</a>
  <a href="https://arxiv.org/pdf/2509.04827.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04827v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04827v2', 'VoltanaLLM: Feedback-Driven Frequency Control and State-Space Routing for Energy-Efficient LLM Serving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahuan Yu, Aryan Taneja, Junfeng Lin, Minjia Zhang

**分类**: cs.DC, cs.AI, cs.LG

**发布日期**: 2025-09-05 (更新: 2025-09-14)

**🔗 代码/项目**: [GITHUB](https://github.com/Supercomputing-System-AI-Lab/VoltanaLLM)

---

## 💡 一句话要点

**VoltanaLLM：面向节能LLM服务的反馈驱动频率控制与状态空间路由**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `节能服务` `频率控制` `请求路由` `控制理论` `服务水平目标` `状态空间路由`

## 📋 核心要点

1. 现有LLM服务系统面临高昂的能源成本，阻碍了其可持续和经济高效的部署，尤其是在交互式应用中。
2. VoltanaLLM通过控制理论方法，协同设计频率缩放和请求路由，实现细粒度的阶段特定控制，从而优化能源效率。
3. 实验结果表明，VoltanaLLM在保持近乎完美的SLO达成率的同时，实现了高达36.3%的节能效果。

## 📝 摘要（中文）

现代大型语言模型（LLM）服务系统越来越多地支持交互式应用，如实时聊天助手、代码生成工具和智能体工作流。然而，LLM推理的能源成本急剧上升，对可持续和经济高效的部署提出了日益严峻的挑战。本文介绍了一种面向服务水平目标（SLO）感知、节能LLM服务的系统VoltanaLLM，该系统从控制理论的角度构建。VoltanaLLM共同设计了新兴的预填充/解码分离架构中的频率缩放和请求路由，利用它们解耦的执行来实现细粒度的阶段特定控制。它由一个反馈驱动的频率控制器组成，该控制器动态地调整预填充和解码阶段的GPU频率，以及一个状态空间路由器，该路由器探索跨频率缩放实例的路由决策，以在延迟约束下最小化能量。我们在SGLang中实现了VoltanaLLM，并在多个最先进的LLM和真实世界数据集上评估了其性能。结果表明，VoltanaLLM在保持接近完美的SLO达成率的同时，实现了高达36.3%的节能效果，为可持续和智能的LLM服务铺平了道路。VoltanaLLM的代码已在GitHub上开源。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）服务中日益增长的能源消耗问题。现有的LLM服务系统，尤其是在支持交互式应用时，面临着高昂的推理能源成本。传统的频率控制和请求路由方法无法充分利用预填充和解码阶段的解耦特性，导致能源效率低下。

**核心思路**：VoltanaLLM的核心思路是从控制理论的角度出发，将LLM服务系统视为一个可控系统。通过反馈驱动的频率控制和状态空间路由，动态地调整GPU频率和请求路由策略，以在满足延迟约束的前提下最小化能源消耗。这种方法能够实现细粒度的阶段特定控制，从而更有效地利用计算资源。

**技术框架**：VoltanaLLM的整体架构包含两个主要模块：反馈驱动的频率控制器和状态空间路由器。频率控制器负责动态调整预填充和解码阶段的GPU频率，以优化能源效率。状态空间路由器则根据当前系统的状态（如延迟、负载等），选择合适的实例进行请求路由，以满足延迟约束。这两个模块协同工作，共同实现节能的LLM服务。

**关键创新**：VoltanaLLM的关键创新在于其协同设计的频率控制和请求路由机制。传统的频率控制和请求路由通常是独立进行的，无法充分利用预填充和解码阶段的解耦特性。VoltanaLLM通过将这两个模块集成在一起，实现了细粒度的阶段特定控制，从而更有效地优化能源效率。此外，VoltanaLLM还采用了状态空间路由，能够根据系统的实时状态动态地调整路由策略，从而更好地满足延迟约束。

**关键设计**：频率控制器采用PID控制算法，根据延迟反馈动态调整GPU频率。状态空间路由器使用马尔可夫决策过程（MDP）来建模请求路由问题，并使用强化学习算法来学习最优的路由策略。具体的参数设置和损失函数等技术细节在论文中有详细描述。

## 📊 实验亮点

VoltanaLLM在多个最先进的LLM和真实世界数据集上进行了评估。实验结果表明，VoltanaLLM在保持接近完美的SLO达成率的同时，实现了高达36.3%的节能效果。与传统的LLM服务系统相比，VoltanaLLM能够显著降低能源消耗，从而降低运营成本并提高可持续性。

## 🎯 应用场景

VoltanaLLM适用于各种需要高效LLM服务的场景，如实时聊天机器人、代码生成工具、智能体工作流等。该研究成果有助于降低LLM服务的运营成本，提高能源利用率，并促进LLM技术的可持续发展。未来，VoltanaLLM可以进一步扩展到支持更多类型的LLM和硬件平台，并与其他优化技术相结合，以实现更高的能源效率。

## 📄 摘要（原文）

> Modern Large Language Model (LLM) serving systems increasingly support interactive applications, like real-time chat assistants, code generation tools, and agentic workflows. However, the soaring energy cost of LLM inference presents a growing challenge for sustainable and cost-effective deployment. This paper introduces VoltanaLLM, a system for SLO-aware, energy-efficient LLM serving, built from a control theory perspective. VoltanaLLM co-designs frequency scaling and request routing in emerging prefill/decode disaggregated architectures, leveraging their decoupled execution to enable fine-grained phase-specific control. It consists of a feedback-driven frequency controller that dynamically adapts GPU frequency for prefill and decode phases, and a state-space router that explores routing decisions across frequency-scaled instances to minimize energy under latency constraints. We implement VoltanaLLM in SGLang and evaluate its performance over multiple state-of-the-art LLMs and real-world datasets. The results demonstrate that VoltanaLLM achieves up to 36.3% energy savings while maintaining near-perfect SLO attainment rate, paving the way for sustainable and intelligent LLM serving. Code of VoltanaLLM is open-sourced on GitHub: https://github.com/Supercomputing-System-AI-Lab/VoltanaLLM.

