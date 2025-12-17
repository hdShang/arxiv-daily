---
layout: default
title: Bayesian Ego-graph Inference for Networked Multi-Agent Reinforcement Learning
---

# Bayesian Ego-graph Inference for Networked Multi-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16606" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16606</a>
  <a href="https://arxiv.org/pdf/2509.16606.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16606" onclick="toggleFavorite(this, '2509.16606', 'Bayesian Ego-graph Inference for Networked Multi-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Duan, Jie Lu, Junyu Xuan

**分类**: cs.MA, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出BayesG，通过贝叶斯推断学习稀疏交互结构，解决网络化多智能体强化学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `网络化学习` `贝叶斯推断` `变分推断` `图神经网络`

## 📋 核心要点

1. 现有网络化多智能体强化学习方法依赖静态邻域，难以适应动态异构环境，集中式方法又不适用于去中心化系统。
2. BayesG通过贝叶斯变分推断学习稀疏的、上下文感知的交互结构，每个智能体基于自我图采样通信掩码。
3. BayesG在交通控制任务中优于现有MARL基线，证明了其可扩展性、效率和性能优势。

## 📝 摘要（中文）

在网络化多智能体强化学习（Networked-MARL）中，去中心化的智能体必须在局部可观测性和固定物理图上的受限通信下行动。现有方法通常假设静态邻域，限制了对动态或异构环境的适应性。集中式框架虽然可以学习动态图，但它们依赖于全局状态访问和集中式基础设施，这在实际的去中心化系统中是不切实际的。我们提出了一种基于随机图策略的Networked-MARL方法，其中每个智能体根据其局部物理邻域上的采样子图来决定其决策。在此基础上，我们引入了BayesG，一个去中心化的actor框架，它通过贝叶斯变分推断学习稀疏的、上下文感知的交互结构。每个智能体在其自我图上运行，并采样一个潜在的通信掩码来指导消息传递和策略计算。变分分布使用证据下界（ELBO）目标与策略一起进行端到端训练，使智能体能够联合学习交互拓扑和决策策略。在多达167个智能体的大规模交通控制任务中，BayesG优于强大的MARL基线，展示了卓越的可扩展性、效率和性能。

## 🔬 方法详解

**问题定义**：论文旨在解决网络化多智能体强化学习中，智能体如何在局部观测和受限通信条件下，学习动态变化的交互拓扑结构的问题。现有方法要么假设静态邻域，限制了适应性；要么依赖全局信息，不适用于去中心化场景。因此，如何在去中心化的环境中，让智能体自主学习并适应动态的交互关系是核心挑战。

**核心思路**：论文的核心思路是利用贝叶斯变分推断，让每个智能体学习一个关于其邻域交互结构的概率分布。通过对该分布进行采样，智能体可以动态地选择与其进行通信的邻居，从而适应环境的变化。这种方法的关键在于，它允许智能体在局部信息的基础上，推断出全局的交互模式。

**技术框架**：BayesG是一个去中心化的actor框架，每个智能体维护一个自我图（ego-graph），表示其局部邻域。框架包含以下主要模块：1) 变分推断模块：用于学习邻域交互结构的概率分布；2) 采样模块：从变分分布中采样通信掩码；3) 消息传递模块：根据通信掩码进行消息传递，聚合邻居信息；4) 策略网络：基于聚合后的信息，输出智能体的动作。整个框架通过端到端的方式进行训练。

**关键创新**：最重要的技术创新点在于使用贝叶斯变分推断来学习稀疏的、上下文感知的交互结构。与现有方法相比，BayesG不需要预先定义固定的邻域关系，而是允许智能体根据环境的变化，动态地调整其交互模式。此外，通过变分推断，BayesG可以学习到邻域交互结构的不确定性，从而提高鲁棒性。

**关键设计**：变分推断模块使用神经网络来参数化变分分布，通常是高斯分布。证据下界（ELBO）被用作训练目标，它平衡了策略的性能和交互结构的稀疏性。通信掩码通常是二元的，表示是否与某个邻居进行通信。策略网络可以使用任何标准的强化学习算法，如Actor-Critic或PPO。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.16606/Fig/BayesG.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.16606/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.16606/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

BayesG在包含多达167个智能体的大规模交通控制任务中，显著优于现有的MARL基线方法。实验结果表明，BayesG能够有效地学习稀疏的交互结构，提高智能体的协作效率和系统的整体性能。具体的性能提升数据在论文中进行了详细的展示和分析。

## 🎯 应用场景

该研究成果可应用于大规模交通控制、无线通信网络资源分配、社交网络影响力最大化等领域。通过学习动态交互结构，智能体能够更好地适应复杂环境，提高协作效率和系统性能。未来，该方法有望扩展到更广泛的多智能体系统，例如机器人集群、传感器网络等。

## 📄 摘要（原文）

> In networked multi-agent reinforcement learning (Networked-MARL), decentralized agents must act under local observability and constrained communication over fixed physical graphs. Existing methods often assume static neighborhoods, limiting adaptability to dynamic or heterogeneous environments. While centralized frameworks can learn dynamic graphs, their reliance on global state access and centralized infrastructure is impractical in real-world decentralized systems. We propose a stochastic graph-based policy for Networked-MARL, where each agent conditions its decision on a sampled subgraph over its local physical neighborhood. Building on this formulation, we introduce BayesG, a decentralized actor-framework that learns sparse, context-aware interaction structures via Bayesian variational inference. Each agent operates over an ego-graph and samples a latent communication mask to guide message passing and policy computation. The variational distribution is trained end-to-end alongside the policy using an evidence lower bound (ELBO) objective, enabling agents to jointly learn both interaction topology and decision-making strategies. BayesG outperforms strong MARL baselines on large-scale traffic control tasks with up to 167 agents, demonstrating superior scalability, efficiency, and performance.

