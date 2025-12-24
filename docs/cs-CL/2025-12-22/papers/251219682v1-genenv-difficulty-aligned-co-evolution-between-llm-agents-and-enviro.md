---
layout: default
title: "GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators"
---

# GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19682" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19682v1</a>
  <a href="https://arxiv.org/pdf/2512.19682.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19682v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19682v1', 'GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiacheng Guo, Ling Yang, Peter Chen, Qixin Xiao, Yinjie Wang, Xinzhe Juan, Jiahao Qiu, Ke Shen, Mengdi Wang

**分类**: cs.CL

**发布日期**: 2025-12-22

**备注**: Our codes are available at https://github.com/Gen-Verse/GenEnv

---

## 💡 一句话要点

**GenEnv：通过LLM智能体与环境模拟器的难度对齐协同进化，提升智能体性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM智能体` `环境模拟器` `协同进化` `课程学习` `难度对齐` `数据高效` `自适应学习`

## 📋 核心要点

1. 现有LLM智能体训练受限于真实世界交互数据的高成本和静态性，难以有效提升智能体能力。
2. GenEnv通过构建智能体与环境模拟器的协同进化机制，动态生成难度与智能体能力相匹配的任务。
3. 实验表明，GenEnv在多个基准测试中显著提升了智能体性能，且数据效率优于离线数据增强方法。

## 📝 摘要（中文）

本文提出GenEnv框架，旨在解决训练高性能大语言模型（LLM）智能体时，真实世界交互数据成本高昂且静态的问题。GenEnv建立了一个智能体与可扩展的生成式环境模拟器之间难度对齐的协同进化博弈。与在静态数据集上进化模型的传统方法不同，GenEnv实现了数据进化：模拟器充当动态课程策略，持续生成专门为智能体的“近端发展区”量身定制的任务。这一过程由一个简单而有效的α-课程奖励引导，该奖励将任务难度与智能体的当前能力对齐。在API-Bank、ALFWorld、BFCL、Bamboogle和TravelPlanner五个基准测试中，GenEnv将智能体性能提高了高达+40.3％，并达到或超过了更大模型的平均性能。与基于Gemini 2.5 Pro的离线数据增强相比，GenEnv在数据使用量减少3.3倍的情况下实现了更好的性能。通过从静态监督转向自适应模拟，GenEnv为扩展智能体能力提供了一条数据高效的途径。

## 🔬 方法详解

**问题定义**：现有的大语言模型智能体训练方法依赖于静态的、成本高昂的真实世界交互数据，这限制了智能体能力的扩展和泛化能力。如何以更低的成本、更高效的方式训练出更强大的LLM智能体是一个关键问题。

**核心思路**：GenEnv的核心思路是建立一个智能体和环境模拟器之间的协同进化关系。环境模拟器根据智能体的能力动态生成任务，智能体在这些任务中学习和进化。通过难度对齐的课程学习，智能体可以逐步提升自身能力。

**技术框架**：GenEnv框架包含两个主要组成部分：LLM智能体和生成式环境模拟器。智能体负责执行任务，环境模拟器负责生成任务并评估智能体的表现。框架通过α-课程奖励机制来调节任务难度，使其与智能体的能力相匹配。整个过程是一个循环迭代的过程，智能体和环境模拟器相互促进，共同进化。

**关键创新**：GenEnv的关键创新在于将环境模拟器视为一个动态的课程策略，能够根据智能体的能力自适应地生成任务。这种方法摆脱了对静态数据集的依赖，实现了数据的高效利用。此外，α-课程奖励机制能够有效地将任务难度与智能体的能力对齐，避免了智能体在过于简单或过于困难的任务中浪费时间。

**关键设计**：α-课程奖励是GenEnv中的一个关键设计。它通过一个参数α来控制任务难度的调整。具体来说，α根据智能体在任务上的表现进行调整，如果智能体表现良好，则增加任务难度；如果智能体表现不佳，则降低任务难度。这种自适应的难度调整机制能够确保智能体始终处于“近端发展区”，从而实现最佳的学习效果。具体的损失函数和网络结构取决于具体的智能体和环境模拟器的选择，论文中没有给出统一的定义。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19682v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19682v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19682v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

GenEnv在五个基准测试中表现出色，相较于7B参数的基线模型，性能提升高达40.3%。GenEnv的性能与更大的模型相当甚至超过，并且比基于Gemini 2.5 Pro的离线数据增强方法节省了3.3倍的数据量。这些结果表明，GenEnv是一种数据高效且有效的智能体训练方法。

## 🎯 应用场景

GenEnv框架具有广泛的应用前景，可以应用于各种需要智能体与环境交互的任务中，例如机器人控制、游戏AI、自动驾驶等。通过GenEnv，可以更高效地训练出能够在复杂环境中执行任务的智能体，从而推动人工智能技术的发展。

## 📄 摘要（原文）

> Training capable Large Language Model (LLM) agents is critically bottlenecked by the high cost and static nature of real-world interaction data. We address this by introducing GenEnv, a framework that establishes a difficulty-aligned co-evolutionary game between an agent and a scalable, generative environment simulator. Unlike traditional methods that evolve models on static datasets, GenEnv instantiates a dataevolving: the simulator acts as a dynamic curriculum policy, continuously generating tasks specifically tailored to the agent's ``zone of proximal development''. This process is guided by a simple but effective $α$-Curriculum Reward, which aligns task difficulty with the agent's current capabilities. We evaluate GenEnv on five benchmarks, including API-Bank, ALFWorld, BFCL, Bamboogle, and TravelPlanner. Across these tasks, GenEnv improves agent performance by up to \textbf{+40.3\%} over 7B baselines and matches or exceeds the average performance of larger models. Compared to Gemini 2.5 Pro-based offline data augmentation, GenEnv achieves better performance while using 3.3$\times$ less data. By shifting from static supervision to adaptive simulation, GenEnv provides a data-efficient pathway for scaling agent capabilities.

