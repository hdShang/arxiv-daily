---
layout: default
title: Joint Design of Embedded Index Coding and Beamforming for MIMO-based Distributed Computing via Multi-Agent Reinforcement Learning
---

# Joint Design of Embedded Index Coding and Beamforming for MIMO-based Distributed Computing via Multi-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20201" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20201v1</a>
  <a href="https://arxiv.org/pdf/2512.20201.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20201v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20201v1', 'Joint Design of Embedded Index Coding and Beamforming for MIMO-based Distributed Computing via Multi-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heekang Song, Wan Choi

**分类**: eess.SY

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出基于多智能体强化学习的嵌入式索引编码与波束成形联合设计方法，优化MIMO分布式计算系统性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `嵌入式索引编码` `波束成形` `MIMO系统` `分布式计算` `无线通信` `数据混洗`

## 📋 核心要点

1. 分布式计算中数据混洗阶段的通信负载过高，现有EIC方法在无线MIMO系统中未充分考虑信道条件和空间复用增益。
2. 提出基于多智能体强化学习(MARL)的EIC和波束成形联合设计方法，分散的智能体根据局部观察进行决策，管理混合动作空间。
3. 仿真结果表明，提出的MARL方法在显著降低复杂性的同时，实现了接近最优的性能，验证了其有效性和实用性。

## 📝 摘要（中文）

在分布式计算系统中，数据混洗阶段的通信负载是关键挑战，过多的节点间传输是主要的性能瓶颈。嵌入式索引编码(EIC)是一种有前景的方法，它利用用户节点缓存的数据来更有效地编码传输。然而，大多数关于EIC的先前工作都集中在有线、无差错环境中最小化代码长度，这对于无线多输入多输出(MIMO)系统来说通常不是最优的，因为必须考虑信道条件和空间复用增益。本文研究了MIMO系统中EIC和发射波束成形的联合设计，以最小化总传输时间，这是一个NP-hard问题。我们首先提出了一种传统的优化方法，通过穷举搜索确定最优EIC。为了解决其过高的复杂性并适应动态无线环境，我们提出了一种新颖的、低复杂度的多智能体强化学习(MARL)框架。所提出的框架使分散的智能体能够根据局部观察采取行动，同时有效地管理离散EIC选择和连续波束成形设计的混合动作空间。仿真结果表明，所提出的基于MARL的方法以显著降低的复杂性实现了接近最优的性能，突出了其在实际无线系统中的有效性和实用性。

## 🔬 方法详解

**问题定义**：论文旨在解决MIMO分布式计算系统中，如何联合优化嵌入式索引编码（EIC）和发射波束成形，以最小化总传输时间的问题。现有方法，特别是针对有线环境设计的EIC方法，无法有效利用无线MIMO系统的信道特性和空间复用增益，导致性能瓶颈。此外，联合优化问题是NP-hard问题，传统优化方法复杂度过高，难以适应动态无线环境。

**核心思路**：论文的核心思路是利用多智能体强化学习（MARL）框架，将EIC选择和波束成形设计分解为多个智能体的决策问题。每个智能体根据局部观察独立行动，通过学习与其他智能体协作，共同优化全局目标，即最小化总传输时间。这种分散式决策方式降低了计算复杂度，并提高了对动态无线环境的适应性。

**技术框架**：整体框架包含多个智能体，每个智能体对应一个用户节点。每个智能体观察局部信道状态信息和缓存数据信息，然后选择EIC方案和设计波束成形向量。所有智能体的行为共同影响系统的总传输时间，该时间作为奖励信号反馈给每个智能体。智能体通过与环境交互，不断学习和优化其策略。

**关键创新**：最重要的技术创新在于将EIC选择（离散动作空间）和波束成形设计（连续动作空间）的联合优化问题，转化为一个多智能体强化学习问题，并设计了相应的MARL框架。与传统的集中式优化方法相比，该方法具有更低的计算复杂度和更好的可扩展性。与单智能体强化学习方法相比，多智能体方法能够更好地处理分布式决策问题。

**关键设计**：论文采用Actor-Critic架构的MARL算法。Actor网络负责选择EIC方案和设计波束成形向量，Critic网络负责评估Actor网络生成的策略的价值。损失函数包括奖励函数和正则化项，用于平衡性能和稳定性。具体参数设置和网络结构在论文中有详细描述，但摘要中未提供具体数值。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20201v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20201v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20201v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

仿真结果表明，所提出的基于MARL的方法在显著降低复杂性的同时，实现了接近最优的性能。与传统的穷举搜索方法相比，MARL方法在性能损失很小的情况下，计算复杂度大幅降低。具体的性能提升幅度和对比基线在摘要中未给出，需要在论文正文中查找。

## 🎯 应用场景

该研究成果可应用于无线分布式计算系统，例如边缘计算、联邦学习等场景。通过优化数据混洗阶段的通信效率，可以显著提升分布式计算的整体性能，降低延迟，提高资源利用率。未来，该方法有望推广到更复杂的无线网络环境，例如异构网络、大规模MIMO系统等。

## 📄 摘要（原文）

> In distributed computing systems, reducing the communication load during the data shuffling phase is a critical challenge, as excessive inter-node transmissions are a major performance bottleneck. One promising approach to alleviate this burden is Embedded Index Coding (EIC), which exploits cached data at user nodes to encode transmissions more efficiently. However, most prior work on EIC has focused on minimizing code length in wired, error-free environments-an objective often suboptimal for wireless multiple-input multiple-output (MIMO) systems, where channel conditions and spatial multiplexing gains must be considered. This paper investigates the joint design of EIC and transmit beamforming in MIMO systems to minimize total transmission time, an NP-hard problem. We first present a conventional optimization method that determines the optimal EIC via exhaustive search. To address its prohibitive complexity and adapt to dynamic wireless environments, we propose a novel, low-complexity multi-agent reinforcement learning (MARL) framework. The proposed framework enables decentralized agents to act on local observations while effectively managing the hybrid action space of discrete EIC selection and continuous beamforming design. Simulation results demonstrate that the proposed MARL-based approach achieves near-optimal performance with significantly reduced complexity, underscoring its effectiveness and practicality for real-world wireless systems.

