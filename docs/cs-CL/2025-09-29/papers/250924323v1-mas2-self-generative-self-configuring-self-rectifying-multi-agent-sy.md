---
layout: default
title: "MAS$^2$: Self-Generative, Self-Configuring, Self-Rectifying Multi-Agent Systems"
---

# MAS$^2$: Self-Generative, Self-Configuring, Self-Rectifying Multi-Agent Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24323" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24323v1</a>
  <a href="https://arxiv.org/pdf/2509.24323.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24323v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24323v1', 'MAS$^2$: Self-Generative, Self-Configuring, Self-Rectifying Multi-Agent Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kun Wang, Guibin Zhang, ManKit Ye, Xinyu Deng, Dongxia Wang, Xiaobin Hu, Jinyang Guo, Yang Liu, Yufei Guo

**分类**: cs.MA, cs.CL

**发布日期**: 2025-09-29

**🔗 代码/项目**: [GITHUB](https://github.com/yeyeyeah2/MAS2)

---

## 💡 一句话要点

**提出MAS$^2$，一种自生成、自配置、自校正的多智能体系统，提升复杂任务性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `自生成` `自配置` `自校正` `大语言模型` `协同树优化` `智能体协作`

## 📋 核心要点

1. 现有自动多智能体系统通常采用“一次生成并部署”的模式，难以适应现实世界环境的动态性和不确定性。
2. MAS$^2$的核心思想是递归自生成，通过“生成器-执行器-校正器”三智能体团队动态构建和调整目标智能体系统。
3. 实验结果表明，MAS$^2$在多个基准测试中优于现有方法，且具有良好的跨骨干泛化能力和成本效益。

## 📝 摘要（中文）

本文提出MAS$^2$，一种基于递归自生成原则的多智能体系统范式，能够自主地为不同的问题构建定制化的多智能体系统。该系统包含一个“生成器-执行器-校正器”三智能体团队，能够动态地组合和自适应地校正目标智能体系统，以响应实时的任务需求。论文提出了协同树优化方法来训练和专门化这些元智能体。在七个基准测试上的广泛评估表明，MAS$^2$在深度研究和代码生成等复杂场景中，相比最先进的多智能体系统，性能提升高达19.6%。此外，MAS$^2$表现出卓越的跨骨干泛化能力，能够有效地利用先前未见过的LLM，产生高达15.1%的改进。重要的是，这些收益是在没有产生过多token成本的情况下获得的，因为MAS$^2$始终位于成本-性能权衡的帕累托前沿。源代码已公开。

## 🔬 方法详解

**问题定义**：现有的大语言模型驱动的多智能体系统（MAS）通常采用预先设计好的角色、工具和通信协议，缺乏对动态环境的适应能力。即使是自动化的MAS，也往往遵循“一次生成并部署”的模式，无法根据实时任务需求进行调整，导致系统脆弱且难以应对真实世界的复杂性和不确定性。

**核心思路**：MAS$^2$的核心思路是引入递归自生成的概念，让一个多智能体系统能够自主地为不同的问题构建定制化的多智能体系统。通过一个元智能体团队（生成器、执行器、校正器）来动态地组合和自适应地校正目标智能体系统，从而实现对环境变化的实时响应。这种设计使得系统能够根据任务需求进行自我调整和优化，提高了系统的鲁棒性和适应性。

**技术框架**：MAS$^2$的技术框架包含三个关键模块：生成器（Generator）、执行器（Implementer）和校正器（Rectifier）。生成器负责根据任务需求生成目标智能体系统的配置，包括角色、工具和通信协议等。执行器负责根据生成器的配置部署和运行目标智能体系统。校正器负责监控目标智能体系统的运行状态，并根据实时反馈进行调整和优化。这三个模块形成一个闭环反馈系统，能够不断地改进和完善目标智能体系统。

**关键创新**：MAS$^2$最重要的技术创新在于其递归自生成的范式。与传统的“一次生成并部署”的模式不同，MAS$^2$能够根据实时任务需求动态地构建和调整目标智能体系统。这种自适应性使得系统能够更好地应对真实世界的复杂性和不确定性。此外，协同树优化（Collaborative Tree Optimization）方法也是一个关键创新，用于训练和专门化元智能体，使其能够更好地完成生成、执行和校正的任务。

**关键设计**：协同树优化方法用于训练生成器、执行器和校正器这三个元智能体。具体的技术细节包括：使用特定的提示工程（prompt engineering）来指导元智能体的行为；设计合适的奖励函数来鼓励元智能体之间的协作；以及使用强化学习算法来优化元智能体的策略。此外，在目标智能体系统的配置方面，需要仔细选择角色、工具和通信协议，以确保系统能够有效地完成任务。

## 📊 实验亮点

实验结果表明，MAS$^2$在七个基准测试中取得了显著的性能提升。在深度研究和代码生成等复杂场景中，MAS$^2$相比最先进的多智能体系统，性能提升高达19.6%。此外，MAS$^2$表现出卓越的跨骨干泛化能力，能够有效地利用先前未见过的LLM，产生高达15.1%的改进。重要的是，这些收益是在没有产生过多token成本的情况下获得的，MAS$^2$始终位于成本-性能权衡的帕累托前沿。

## 🎯 应用场景

MAS$^2$具有广泛的应用前景，例如在自动化研究、软件开发、智能客服、金融分析等领域。它可以用于构建能够自主解决复杂问题的智能系统，提高工作效率和决策质量。未来，MAS$^2$有望成为构建通用人工智能的重要基石。

## 📄 摘要（原文）

> The past two years have witnessed the meteoric rise of Large Language Model (LLM)-powered multi-agent systems (MAS), which harness collective intelligence and exhibit a remarkable trajectory toward self-evolution. This paradigm has rapidly progressed from manually engineered systems that require bespoke configuration of prompts, tools, roles, and communication protocols toward frameworks capable of automated orchestration. Yet, dominant automatic multi-agent systems, whether generated by external modules or a single LLM agent, largely adhere to a rigid ``\textit{generate-once-and-deploy}'' paradigm, rendering the resulting systems brittle and ill-prepared for the dynamism and uncertainty of real-world environments. To transcend this limitation, we introduce MAS$^2$, a paradigm predicated on the principle of recursive self-generation: a multi-agent system that autonomously architects bespoke multi-agent systems for diverse problems. Technically, we devise a ``\textit{generator-implementer-rectifier}'' tri-agent team capable of dynamically composing and adaptively rectifying a target agent system in response to real-time task demands. Collaborative Tree Optimization is proposed to train and specialize these meta-agents. Extensive evaluation across seven benchmarks reveals that MAS$^2$ achieves performance gains of up to $19.6\%$ over state-of-the-art MAS in complex scenarios such as deep research and code generation. Moreover, MAS$^2$ exhibits superior cross-backbone generalization, effectively leveraging previously unseen LLMs to yield improvements of up to $15.1\%$. Crucially, these gains are attained without incurring excessive token costs, as MAS$^2$ consistently resides on the Pareto frontier of cost-performance trade-offs. The source codes are available at https://github.com/yeyeyeah2/MAS2.

