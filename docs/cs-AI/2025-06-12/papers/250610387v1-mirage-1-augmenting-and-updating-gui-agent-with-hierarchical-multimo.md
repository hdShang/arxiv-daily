---
layout: default
title: "Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills"
---

# Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10387" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10387v1</a>
  <a href="https://arxiv.org/pdf/2506.10387.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10387v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10387v1', 'Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuquan Xie, Zaijing Li, Rui Shao, Gongwei Chen, Kaiwen Zhou, Yinchuan Li, Dongmei Jiang, Liqiang Nie

**分类**: cs.AI

**发布日期**: 2025-06-12

**备注**: 20 pages, 5 figures, 5 tables

**🔗 代码/项目**: [PROJECT_PAGE](https://cybertronagent.github.io/Mirage-1.github.io/)

---

## 💡 一句话要点

**提出层次化多模态技能模块以解决GUI代理知识不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `长时间任务` `GUI代理` `层次化技能` `蒙特卡洛树搜索` `知识结构` `在线学习` `智能助手`

## 📋 核心要点

1. 现有的多模态GUI代理在处理长时间任务时面临知识不足和离线与在线领域之间的差距等挑战。
2. 本文提出层次化多模态技能模块（HMS）和技能增强蒙特卡洛树搜索算法（SA-MCTS），以提升代理的知识结构和任务规划能力。
3. 实验结果表明，Mirage-1在多个基准测试中超越了之前的代理，性能提升幅度最高达79%。

## 📝 摘要（中文）

近年来，利用多模态大语言模型（MLLM）作为GUI代理的研究取得了良好进展。然而，这些代理在在线环境中的长时间任务中仍面临知识不足和离线与在线领域之间的固有差距等挑战。为此，本文提出了层次化多模态技能（HMS）模块，通过将轨迹逐步抽象为执行技能、核心技能和元技能，构建了一个层次化的知识结构，以支持长时间任务规划。此外，提出的技能增强蒙特卡洛树搜索（SA-MCTS）算法有效利用离线环境中获得的技能，减少在线树搜索过程中的动作搜索空间。基于HMS，本文提出了Mirage-1，一个多模态、跨平台的即插即用GUI代理，并通过构建新的基准AndroidLH验证其在实际长时间场景中的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态GUI代理在长时间任务中知识不足的问题，尤其是在在线环境中面临的挑战。现有方法在离线和在线领域之间存在显著差距，导致代理无法有效执行复杂任务。

**核心思路**：论文提出的层次化多模态技能模块（HMS）通过将任务轨迹逐步抽象为执行技能、核心技能和元技能，构建了一个层次化的知识结构。这种设计灵感来源于人类在开放环境中对知识的泛化能力，旨在提升代理的任务规划能力。

**技术框架**：整体架构包括HMS模块和SA-MCTS算法。HMS模块负责知识的层次化抽象，而SA-MCTS算法则在在线环境中利用这些技能进行高效的动作搜索。整个流程从离线学习开始，逐步过渡到在线任务执行。

**关键创新**：最重要的技术创新在于HMS模块的设计和SA-MCTS算法的提出。HMS模块通过层次化技能的构建，显著提升了代理在复杂任务中的知识表达能力，而SA-MCTS则有效缩小了在线搜索空间，提升了搜索效率。

**关键设计**：在HMS模块中，技能的抽象层次分为执行技能、核心技能和元技能，具体的参数设置和损失函数设计尚未详细披露。SA-MCTS算法通过结合离线学习的技能，优化了在线搜索过程中的决策效率。整体架构的设计确保了模块之间的高效协同。

## 📊 实验亮点

实验结果显示，Mirage-1在AndroidWorld、MobileMiniWob++、Mind2Web-Live和AndroidLH等多个基准测试中分别提升了32%、19%、15%和79%的性能，显著超越了之前的代理。这表明该方法在实际长时间任务中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化测试和人机交互等场景。通过提升GUI代理在复杂任务中的表现，Mirage-1能够在实际应用中提供更高效的用户体验，推动智能系统的进一步发展。未来，该技术可能在更多领域中得到广泛应用，提升自动化水平和用户满意度。

## 📄 摘要（原文）

> Recent efforts to leverage the Multi-modal Large Language Model (MLLM) as GUI agents have yielded promising outcomes. However, these agents still struggle with long-horizon tasks in online environments, primarily due to insufficient knowledge and the inherent gap between offline and online domains. In this paper, inspired by how humans generalize knowledge in open-ended environments, we propose a Hierarchical Multimodal Skills (HMS) module to tackle the issue of insufficient knowledge. It progressively abstracts trajectories into execution skills, core skills, and ultimately meta-skills, providing a hierarchical knowledge structure for long-horizon task planning. To bridge the domain gap, we propose the Skill-Augmented Monte Carlo Tree Search (SA-MCTS) algorithm, which efficiently leverages skills acquired in offline environments to reduce the action search space during online tree exploration. Building on HMS, we propose Mirage-1, a multimodal, cross-platform, plug-and-play GUI agent. To validate the performance of Mirage-1 in real-world long-horizon scenarios, we constructed a new benchmark, AndroidLH. Experimental results show that Mirage-1 outperforms previous agents by 32\%, 19\%, 15\%, and 79\% on AndroidWorld, MobileMiniWob++, Mind2Web-Live, and AndroidLH, respectively. Project page: https://cybertronagent.github.io/Mirage-1.github.io/

