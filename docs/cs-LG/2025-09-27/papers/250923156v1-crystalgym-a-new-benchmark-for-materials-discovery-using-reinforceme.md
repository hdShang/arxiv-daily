---
layout: default
title: "CrystalGym: A New Benchmark for Materials Discovery Using Reinforcement Learning"
---

# CrystalGym: A New Benchmark for Materials Discovery Using Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23156" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23156v1</a>
  <a href="https://arxiv.org/pdf/2509.23156.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23156v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23156v1', 'CrystalGym: A New Benchmark for Materials Discovery Using Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prashant Govindarajan, Mathieu Reymond, Antoine Clavaud, Mariano Phielipp, Santiago Miret, Sarath Chandar

**分类**: cs.LG

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**提出 CrystalGym：一个用于强化学习材料发现的新基准测试环境**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `材料发现` `密度泛函理论` `晶体结构` `基准测试` `材料设计` `机器学习` `奖励函数`

## 📋 核心要点

1. 现有材料设计方法依赖高精度原子模拟，但计算成本高昂，限制了直接使用DFT信号进行训练。
2. CrystalGym提供了一个强化学习环境，允许直接使用DFT计算的属性作为奖励信号，优化材料设计。
3. 实验评估了多种强化学习算法在CrystalGym上的性能，并探索了使用强化学习微调大型语言模型的潜力。

## 📝 摘要（中文）

本研究提出了 CrystalGym，一个用于晶体材料发现的开源强化学习（RL）环境，旨在促进直接使用密度泛函理论（DFT）信号进行材料设计。由于DFT计算成本高昂，现有机器学习方法主要采用生成式方法，缺乏利用DFT信号作为反馈来改进训练和生成。CrystalGym通过基准测试常见的基于价值和基于策略的强化学习算法，来设计具有目标属性的各种晶体，例如带隙、体积模量和密度，这些属性直接从环境中的DFT计算获得。实验结果表明，不同的算法在样本效率和收敛性方面表现各异。此外，还研究了使用强化学习微调大型语言模型以改善基于DFT的奖励。CrystalGym旨在为强化学习研究人员和材料科学家提供一个测试平台，以解决具有实际应用意义的真实设计问题。

## 🔬 方法详解

**问题定义**：现有材料设计主要依赖于高精度的原子模拟，特别是密度泛函理论（DFT）计算。然而，DFT计算成本非常高昂，导致机器学习方法难以直接利用DFT信号作为反馈来改进材料设计过程。现有的机器学习方法大多是生成式的，无法充分利用DFT提供的精确信息。因此，如何在高计算成本下，有效利用DFT信号指导材料设计，是一个亟待解决的问题。

**核心思路**：本研究的核心思路是构建一个强化学习环境 CrystalGym，将材料设计过程建模为一个序列决策问题。通过强化学习算法，智能体可以与环境交互，探索不同的材料结构，并根据DFT计算得到的材料属性（如带隙、体积模量、密度）获得奖励。智能体通过不断试错和学习，优化材料结构，最终设计出满足特定目标属性的材料。

**技术框架**：CrystalGym 的整体框架包含以下几个主要模块：1) 材料结构表示模块：将晶体材料的结构信息编码为智能体可以理解的状态表示。2) 动作空间定义模块：定义智能体可以采取的动作，例如添加、删除或替换原子。3) DFT计算模块：使用 DFT 模拟器计算材料的属性，并将其作为奖励信号反馈给智能体。4) 强化学习算法模块：使用各种强化学习算法（如基于价值的方法和基于策略的方法）训练智能体，使其能够根据当前状态选择最优动作。5) 评估模块：评估智能体设计的材料的性能，并与现有材料进行比较。

**关键创新**：本研究的关键创新在于构建了一个能够直接使用 DFT 信号作为奖励的强化学习环境 CrystalGym。这使得强化学习算法能够直接优化材料的物理属性，而无需依赖于间接的代理模型。此外，CrystalGym 提供了一个标准化的测试平台，方便研究人员比较不同强化学习算法在材料设计任务上的性能。

**关键设计**：CrystalGym 的关键设计包括：1) 使用开源材料基因组项目（Materials Project）的数据集作为初始状态空间。2) 定义了一组常用的材料设计动作，例如添加、删除或替换原子。3) 使用 GPAW (Grid-based Projector-Augmented Wave) 代码进行 DFT 计算。4) 实现了多种常用的强化学习算法，例如 Deep Q-Network (DQN) 和 Proximal Policy Optimization (PPO)。5) 提供了灵活的奖励函数设计，允许用户根据不同的目标属性定制奖励信号。

## 📊 实验亮点

实验结果表明，不同的强化学习算法在 CrystalGym 上表现出不同的性能。例如，某些算法在样本效率方面表现更好，而另一些算法则更容易收敛到最优解。此外，研究还发现，使用强化学习微调大型语言模型可以提高基于 DFT 的奖励。虽然没有一种算法能够解决所有的 CrystalGym 任务，但实验结果为选择合适的强化学习算法和环境设置提供了有价值的指导。

## 🎯 应用场景

CrystalGym 的潜在应用领域包括新材料发现、材料优化和材料定制。通过使用 CrystalGym，研究人员可以加速新材料的发现过程，设计具有特定性能的材料，并优化现有材料的性能。这对于能源、电子、化工等领域具有重要意义，例如可以用于设计高性能电池材料、高效太阳能电池材料和新型催化剂。

## 📄 摘要（原文）

> In silico design and optimization of new materials primarily relies on high-accuracy atomic simulators that perform density functional theory (DFT) calculations. While recent works showcase the strong potential of machine learning to accelerate the material design process, they mostly consist of generative approaches that do not use direct DFT signals as feedback to improve training and generation mainly due to DFT's high computational cost. To aid the adoption of direct DFT signals in the materials design loop through online reinforcement learning (RL), we propose CrystalGym, an open-source RL environment for crystalline material discovery. Using CrystalGym, we benchmark common value- and policy-based reinforcement learning algorithms for designing various crystals conditioned on target properties. Concretely, we optimize for challenging properties like the band gap, bulk modulus, and density, which are directly calculated from DFT in the environment. While none of the algorithms we benchmark solve all CrystalGym tasks, our extensive experiments and ablations show different sample efficiencies and ease of convergence to optimality for different algorithms and environment settings. Additionally, we include a case study on the scope of fine-tuning large language models with reinforcement learning for improving DFT-based rewards. Our goal is for CrystalGym to serve as a test bed for reinforcement learning researchers and material scientists to address these real-world design problems with practical applications. We therefore introduce a novel class of challenges for reinforcement learning methods dealing with time-consuming reward signals, paving the way for future interdisciplinary research for machine learning motivated by real-world applications.

