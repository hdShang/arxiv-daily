---
layout: default
title: "Reinforcement Learning Foundations for Deep Research Systems: A Survey"
---

# Reinforcement Learning Foundations for Deep Research Systems: A Survey

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06733" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06733v2</a>
  <a href="https://arxiv.org/pdf/2509.06733.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06733v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06733v2', 'Reinforcement Learning Foundations for Deep Research Systems: A Survey')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenjun Li, Zhi Chen, Jingru Lin, Hannan Cao, Wei Han, Sheng Liang, Zhi Zhang, Kuicai Dong, Dexun Li, Chen Zhang, Yong Liu

**分类**: cs.AI, cs.CL, cs.IR

**发布日期**: 2025-09-08 (更新: 2025-11-05)

**备注**: 39 pages, second version

---

## 💡 一句话要点

**综述：基于强化学习的深度研究系统，解决智能体工具交互与长期信用分配问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `深度研究系统` `智能体` `工具交互` `信用分配` `多目标优化` `综述`

## 📋 核心要点

1. 现有深度研究系统依赖SFT和DPO，存在模仿偏差、暴露偏差，且难以进行长程信用分配和多目标权衡。
2. 本研究强调强化学习在深度研究系统中的应用，通过优化轨迹级策略，实现探索和有原则的信用分配。
3. 该综述系统地整理了数据合成、强化学习方法和训练系统，并涵盖了智能体架构、评估和基准。

## 📝 摘要（中文）

深度研究系统，即通过协调推理、网络搜索和用户文件访问以及工具使用来解决复杂多步骤任务的智能体AI，正朝着具有规划器、协调器和执行器的分层部署发展。端到端训练整个堆栈仍然不切实际，因此大多数工作训练连接到搜索、浏览和代码等核心工具的单个规划器。虽然SFT赋予了协议保真度，但它存在模仿和暴露偏差，并且未能充分利用环境反馈。偏好对齐方法（如DPO）依赖于模式和代理，是离线策略，并且在长程信用分配和多目标权衡方面表现不佳。SFT和DPO的另一个局限性在于它们依赖于人类定义的决策点和子技能。强化学习通过优化轨迹级策略，实现探索、恢复行为和有原则的信用分配，从而与闭环、工具交互研究保持一致，并减少对人类先验和评分者偏差的依赖。本综述是首个专门针对深度研究系统的强化学习基础的综述。它沿着三个轴系统化了最近的工作：（i）数据合成和管理；（ii）用于智能体研究的强化学习方法，涵盖稳定性、样本效率、长上下文处理、奖励和信用设计、多目标优化和多模态集成；（iii）智能体强化学习训练系统和框架。我们还涵盖了智能体架构和协调，以及评估和基准，包括最近的QA、VQA、长格式合成和领域相关的工具交互任务。我们提炼出反复出现的模式，揭示基础设施瓶颈，并为使用强化学习训练稳健、透明的深度研究智能体提供实用指导。

## 🔬 方法详解

**问题定义**：深度研究系统旨在解决复杂、多步骤的任务，需要智能体具备推理、搜索、工具使用等能力。现有方法，如SFT和DPO，在训练过程中存在模仿偏差、暴露偏差，难以进行长程信用分配，并且过度依赖人工定义的决策点和子技能。这些问题限制了智能体的探索能力和泛化性能。

**核心思路**：本综述的核心思路是强调强化学习（RL）在深度研究系统中的重要性。RL能够通过优化轨迹级别的策略，实现智能体与环境的闭环交互，从而克服SFT和DPO的局限性。通过奖励函数的设计，RL可以鼓励智能体进行探索，学习恢复行为，并实现有原则的信用分配。

**技术框架**：该综述将深度研究系统的RL方法分为三个主要部分：数据合成与管理、智能体研究的RL方法以及智能体RL训练系统和框架。数据合成与管理关注如何生成高质量的训练数据。智能体研究的RL方法涵盖了稳定性、样本效率、长上下文处理、奖励和信用设计、多目标优化和多模态集成等关键技术。训练系统和框架则提供了实际训练智能体的工具和平台。此外，综述还讨论了智能体架构和协调，以及评估和基准。

**关键创新**：该综述的关键创新在于它是首个专门针对深度研究系统的强化学习基础的综述。它系统地整理了该领域的研究进展，并提炼出反复出现的模式和基础设施瓶颈。通过对现有方法的分析和总结，该综述为使用强化学习训练稳健、透明的深度研究智能体提供了实用指导。

**关键设计**：综述中讨论的关键设计包括奖励函数的设计、信用分配策略、长上下文处理方法、多目标优化策略以及多模态集成技术。奖励函数的设计需要能够准确地反映任务目标，并鼓励智能体进行探索。信用分配策略需要能够将奖励分配给对最终结果有贡献的步骤。长上下文处理方法需要能够有效地利用历史信息。多目标优化策略需要能够平衡不同的任务目标。多模态集成技术需要能够将不同模态的信息融合在一起。

## 📊 实验亮点

该综述系统地整理了深度研究系统中强化学习的应用，总结了数据合成、RL方法和训练系统三个方面的研究进展。它强调了RL在解决长程信用分配、多目标优化和减少人工干预方面的优势，并为未来研究提供了方向。

## 🎯 应用场景

该研究成果可应用于智能客服、自动化报告生成、科学研究辅助等领域。通过强化学习训练的智能体能够更好地理解用户意图，自主进行信息检索和工具调用，从而提高工作效率和决策质量。未来，该技术有望推动人工智能在各个领域的应用。

## 📄 摘要（原文）

> Deep research systems, agentic AI that solve complex, multi-step tasks by coordinating reasoning, search across the open web and user files, and tool use, are moving toward hierarchical deployments with a Planner, Coordinator, and Executors. In practice, training entire stacks end-to-end remains impractical, so most work trains a single planner connected to core tools such as search, browsing, and code. While SFT imparts protocol fidelity, it suffers from imitation and exposure biases and underuses environment feedback. Preference alignment methods such as DPO are schema and proxy-dependent, off-policy, and weak for long-horizon credit assignment and multi-objective trade-offs. A further limitation of SFT and DPO is their reliance on human defined decision points and subskills through schema design and labeled comparisons. Reinforcement learning aligns with closed-loop, tool-interaction research by optimizing trajectory-level policies, enabling exploration, recovery behaviors, and principled credit assignment, and it reduces dependence on such human priors and rater biases.
>   This survey is, to our knowledge, the first dedicated to the RL foundations of deep research systems. It systematizes recent work along three axes: (i) data synthesis and curation; (ii) RL methods for agentic research covering stability, sample efficiency, long context handling, reward and credit design, multi-objective optimization, and multimodal integration; and (iii) agentic RL training systems and frameworks. We also cover agent architecture and coordination, as well as evaluation and benchmarks, including recent QA, VQA, long-form synthesis, and domain-grounded, tool-interaction tasks. We distill recurring patterns, surface infrastructure bottlenecks, and offer practical guidance for training robust, transparent deep research agents with RL.

