---
layout: default
title: Co-Saving: Resource Aware Multi-Agent Collaboration for Software Development
---

# Co-Saving: Resource Aware Multi-Agent Collaboration for Software Development

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21898" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21898v1</a>
  <a href="https://arxiv.org/pdf/2505.21898.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21898v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21898v1', 'Co-Saving: Resource Aware Multi-Agent Collaboration for Software Development')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rennai Qiu, Chen Qian, Ran Li, Yufan Dang, Weize Chen, Cheng Yang, Yingli Zhang, Ye Tian, Xuantang Xiong, Lei Han, Zhiyuan Liu, Maosong Sun

**分类**: cs.CL, cs.AI, cs.MA, cs.SE

**发布日期**: 2025-05-28

**备注**: Work in Progress

---

## 💡 一句话要点

**提出Co-Saving以解决多智能体协作中的资源效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `资源感知` `软件开发` `协作机制` `历史轨迹学习`

## 📋 核心要点

1. 现有的多智能体系统在处理复杂任务时，往往面临资源消耗高和执行时间长的问题，导致效率低下。
2. 本文提出的Co-Saving通过引入资源感知机制和历史成功轨迹的快捷方式，提升了多智能体协作的效率。
3. 实验结果显示，Co-Saving在软件开发任务中相比于现有方法，令牌使用减少了50.85%，代码质量提高了10.06%。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）和自主智能体在多个领域展现了卓越的能力。然而，独立智能体在处理复杂任务时常常面临资源消耗高和执行时间长的问题。尽管多智能体系统（MAS）通过任务分解、迭代通信和角色专业化等协作机制缓解了部分限制，但仍然缺乏资源感知，导致效率低下。为此，本文提出了一种资源感知的多智能体系统——Co-Saving，旨在通过利用经验知识提升操作效率和解决方案质量。我们的核心创新在于引入“快捷方式”，即从历史成功轨迹中学习的指令性过渡，能够绕过冗余推理的智能体，加速集体问题解决过程。实验结果表明，与现有的MAS ChatDev相比，我们的方法在软件开发任务中实现了平均50.85%的令牌使用减少，并提高了整体代码质量10.06%。

## 🔬 方法详解

**问题定义**：本文旨在解决多智能体系统在复杂任务中资源消耗高和执行效率低的问题。现有方法缺乏资源感知，导致高令牌消耗和冗长的执行时间。

**核心思路**：Co-Saving通过引入资源感知机制和历史成功轨迹的“快捷方式”，使多个智能体能够更高效地协作，避免冗余推理，加速问题解决过程。

**技术框架**：该方法的整体架构包括多个智能体的协作模块、资源监测模块和历史轨迹学习模块。智能体通过共享经验和资源信息进行协作，优化任务执行流程。

**关键创新**：最重要的技术创新是引入“快捷方式”，即通过学习历史成功轨迹来指导智能体的决策，从而减少不必要的推理步骤。这一设计显著提高了多智能体系统的效率。

**关键设计**：在参数设置上，本文对智能体的协作频率、资源监测阈值和历史轨迹的学习率进行了优化，确保系统在不同任务中的适应性和效率。

## 📊 实验亮点

在实验中，Co-Saving相较于现有的多智能体系统ChatDev，平均减少了50.85%的令牌使用，并提高了代码质量10.06%。这些结果表明，Co-Saving在资源效率和解决方案质量方面具有显著优势，展示了其在软件开发中的实际应用潜力。

## 🎯 应用场景

Co-Saving的研究成果在软件开发、自动化测试和复杂系统管理等领域具有广泛的应用潜力。通过提升多智能体协作的资源效率，该方法能够显著降低开发成本和时间，提高软件质量，推动智能化软件开发的进程。未来，该技术还可能扩展到其他需要高效协作的领域，如机器人协作和智能制造。

## 📄 摘要（原文）

> Recent advancements in Large Language Models (LLMs) and autonomous agents have demonstrated remarkable capabilities across various domains. However, standalone agents frequently encounter limitations when handling complex tasks that demand extensive interactions and substantial computational resources. Although Multi-Agent Systems (MAS) alleviate some of these limitations through collaborative mechanisms like task decomposition, iterative communication, and role specialization, they typically remain resource-unaware, incurring significant inefficiencies due to high token consumption and excessive execution time. To address these limitations, we propose a resource-aware multi-agent system -- Co-Saving (meaning that multiple agents collaboratively engage in resource-saving activities), which leverages experiential knowledge to enhance operational efficiency and solution quality. Our key innovation is the introduction of "shortcuts" -- instructional transitions learned from historically successful trajectories -- which allows to bypass redundant reasoning agents and expedite the collective problem-solving process. Experiments for software development tasks demonstrate significant advantages over existing methods. Specifically, compared to the state-of-the-art MAS ChatDev, our method achieves an average reduction of 50.85% in token usage, and improves the overall code quality by 10.06%.

