---
layout: default
title: "SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence"
---

# SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15672" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15672v1</a>
  <a href="https://arxiv.org/pdf/2506.15672.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15672v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15672v1', 'SwarmAgentic: Towards Fully Automated Agentic System Generation via Swarm Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yao Zhang, Chenyang Lin, Shijie Tang, Haokun Chen, Shijie Zhou, Yunpu Ma, Volker Tresp

**分类**: cs.AI, cs.MA

**发布日期**: 2025-06-18

**备注**: 41 pages

**🔗 代码/项目**: [PROJECT_PAGE](https://yaoz720.github.io/SwarmAgentic/)

---

## 💡 一句话要点

**提出SwarmAgentic以实现完全自动化的智能体系统生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `智能体系统` `自动化生成` `粒子群优化` `自我优化` `协作机制` `高效搜索` `开放性任务`

## 📋 核心要点

1. 现有智能体系统生成框架缺乏完全自主性，无法实现从零开始的智能体生成和自我优化功能，限制了系统的适应性和可扩展性。
2. SwarmAgentic框架通过语言驱动的探索，能够从头构建智能体系统，并共同优化智能体功能与协作，提升系统的整体性能。
3. 在六个真实世界的任务中，SwarmAgentic在TravelPlanner基准上实现了+261.8%的相对提升，显著超越了所有基线方法，展示了其有效性。

## 📝 摘要（中文）

随着大型语言模型的快速发展，智能体系统在决策、协调和任务执行方面取得了进展。然而，现有的智能体系统生成框架缺乏完全自主性，无法从零开始生成智能体、实现自我优化功能和协作，限制了适应性和可扩展性。本文提出了SwarmAgentic框架，能够从头构建智能体系统，并通过语言驱动的探索共同优化智能体功能和协作。SwarmAgentic维护候选系统的种群，并通过反馈引导的更新进行演化，灵感来自粒子群优化（PSO）。在六个真实世界的开放性探索任务中进行评估，SwarmAgentic在TravelPlanner基准上相较于ADAS实现了+261.8%的相对提升，突显了完全自动化在结构不受限任务中的有效性。该框架标志着可扩展和自主智能体系统设计的重要进展。

## 🔬 方法详解

**问题定义**：本文旨在解决现有智能体系统生成框架的不足，特别是缺乏完全自主性和自我优化能力的问题。这些不足限制了智能体系统在复杂任务中的适应性和可扩展性。

**核心思路**：SwarmAgentic框架的核心思想是通过语言驱动的探索实现从零开始的智能体系统生成，并将智能体功能与协作视为相互依赖的组件进行共同优化。这种设计旨在提高系统的灵活性和效率。

**技术框架**：SwarmAgentic的整体架构包括候选系统的种群维护和基于反馈的演化更新。该框架通过模拟粒子群优化（PSO）的方法，进行系统级结构的高效搜索。主要模块包括任务描述解析、目标函数定义、智能体功能优化和协作机制设计。

**关键创新**：SwarmAgentic的主要创新在于实现了完全自动化的智能体系统生成，结合了粒子群优化的思想，使得智能体的生成和优化过程更加高效和灵活。这与现有方法的本质区别在于其自主性和自我优化能力。

**关键设计**：在技术细节上，SwarmAgentic采用了特定的损失函数来评估智能体的功能和协作效果，同时设计了适应性强的参数设置，以确保在不同任务中的有效性和稳定性。

## 📊 实验亮点

在实验中，SwarmAgentic在TravelPlanner基准上实现了+261.8%的相对提升，超越了所有基线方法，展示了其在开放性和探索性任务中的卓越性能。这一结果突显了完全自动化在复杂任务中的有效性。

## 🎯 应用场景

该研究的潜在应用场景包括智能交通系统、自动化物流、智能家居和复杂任务的协作机器人等领域。通过实现完全自动化的智能体系统生成，SwarmAgentic能够大幅提升系统的适应性和效率，具有重要的实际价值和广泛的未来影响。

## 📄 摘要（原文）

> The rapid progress of Large Language Models has advanced agentic systems in decision-making, coordination, and task execution. Yet, existing agentic system generation frameworks lack full autonomy, missing from-scratch agent generation, self-optimizing agent functionality, and collaboration, limiting adaptability and scalability. We propose SwarmAgentic, a framework for fully automated agentic system generation that constructs agentic systems from scratch and jointly optimizes agent functionality and collaboration as interdependent components through language-driven exploration. To enable efficient search over system-level structures, SwarmAgentic maintains a population of candidate systems and evolves them via feedback-guided updates, drawing inspiration from Particle Swarm Optimization (PSO). We evaluate our method on six real-world, open-ended, and exploratory tasks involving high-level planning, system-level coordination, and creative reasoning. Given only a task description and an objective function, SwarmAgentic outperforms all baselines, achieving a +261.8% relative improvement over ADAS on the TravelPlanner benchmark, highlighting the effectiveness of full automation in structurally unconstrained tasks. This framework marks a significant step toward scalable and autonomous agentic system design, bridging swarm intelligence with fully automated system multi-agent generation. Our code is publicly released at https://yaoz720.github.io/SwarmAgentic/.

