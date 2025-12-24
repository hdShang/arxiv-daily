---
layout: default
title: "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning"
---

# SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09674" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09674v1</a>
  <a href="https://arxiv.org/pdf/2509.09674.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09674v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09674v1', 'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haozhan Li, Yuxin Zuo, Jiale Yu, Yuhao Zhang, Zhaohui Yang, Kaiyan Zhang, Xuekai Zhu, Yuchen Zhang, Tianxing Chen, Ganqu Cui, Dehui Wang, Dingxiang Luo, Yuchen Fan, Youbang Sun, Jia Zeng, Jiangmiao Pang, Shanghang Zhang, Yu Wang, Yao Mu, Bowen Zhou, Ning Ding

**分类**: cs.RO, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-09-11

**🔗 代码/项目**: [GITHUB](https://github.com/PRIME-RL/SimpleVLA-RL)

---

## 💡 一句话要点

**SimpleVLA-RL：通过强化学习扩展VLA模型训练，提升机器人操作性能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `VLA模型` `强化学习` `机器人操作` `长期动作规划` `泛化能力` `轨迹采样` `并行化`

## 📋 核心要点

1. VLA模型依赖大量人工标注的机器人轨迹进行监督微调，数据获取成本高昂且泛化性受限。
2. SimpleVLA-RL利用强化学习，通过VLA特定的轨迹采样和并行化等技术，提升VLA模型的长期动作规划能力。
3. 实验表明，SimpleVLA-RL在机器人操作任务上超越了监督微调，并发现了新的策略模式，提升了泛化能力。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型已成为机器人操作的强大范例。尽管大规模预训练和监督微调(SFT)取得了显著进展，但这些模型面临两个根本挑战：(i)用于SFT扩展的大规模人工操作机器人轨迹的稀缺性和高成本，以及(ii)对涉及分布转移的任务的泛化能力有限。大型推理模型(LRM)的最新突破表明，强化学习(RL)可以显著增强逐步推理能力，这引出了一个自然的问题：RL能否类似地改善VLA的长期逐步动作规划？本文提出了SimpleVLA-RL，这是一个为VLA模型量身定制的高效RL框架。基于veRL，引入了VLA特定的轨迹采样、可扩展的并行化、多环境渲染和优化的损失计算。应用于OpenVLA-OFT时，SimpleVLA-RL在LIBERO上实现了SoTA性能，甚至通过引入的探索增强策略在RoboTwin 1.0和2.0上优于$π_0$。SimpleVLA-RL不仅减少了对大规模数据的依赖，实现了强大的泛化能力，而且在实际任务中显著超越了SFT。此外，还发现了一种新的现象“pushcut”，即策略发现了先前训练过程中未见过的模式。

## 🔬 方法详解

**问题定义**：VLA模型在机器人操作任务中面临数据依赖和泛化性问题。现有方法依赖于大规模人工标注的机器人轨迹进行监督微调，数据获取成本高昂，且模型难以泛化到新的环境和任务。因此，需要一种更有效的方法来训练VLA模型，使其能够更好地进行长期动作规划，并具备更强的泛化能力。

**核心思路**：论文的核心思路是利用强化学习来训练VLA模型，以克服监督微调的局限性。强化学习允许模型通过与环境的交互来学习最优策略，从而减少对大规模人工标注数据的依赖，并提高模型的泛化能力。通过设计合适的奖励函数和探索策略，引导模型学习更有效的长期动作规划。

**技术框架**：SimpleVLA-RL框架基于veRL，并针对VLA模型进行了优化。主要包括以下几个模块：1) VLA特定的轨迹采样：根据VLA模型的特点，设计高效的轨迹采样方法，以提高学习效率。2) 可扩展的并行化：利用并行计算资源，加速强化学习的训练过程。3) 多环境渲染：在多个不同的环境中进行训练，以提高模型的泛化能力。4) 优化的损失计算：设计合适的损失函数，以引导模型学习最优策略。

**关键创新**：SimpleVLA-RL的关键创新在于将强化学习应用于VLA模型的训练，并针对VLA模型的特点进行了优化。通过VLA特定的轨迹采样、可扩展的并行化、多环境渲染和优化的损失计算，显著提高了VLA模型的性能和泛化能力。此外，还发现了一种新的现象“pushcut”，即策略发现了先前训练过程中未见过的模式，表明强化学习可以帮助模型发现新的策略。

**关键设计**：论文中关键的设计包括：1) 奖励函数的设计：设计合适的奖励函数，以引导模型学习期望的动作序列。2) 探索策略的设计：采用合适的探索策略，以鼓励模型探索新的动作空间。3) VLA特定的轨迹采样方法：根据VLA模型的特点，设计高效的轨迹采样方法，例如，优先采样具有挑战性的轨迹。4) 并行化策略：采用数据并行和模型并行等技术，加速强化学习的训练过程。

## 📊 实验亮点

SimpleVLA-RL在LIBERO上实现了SoTA性能，并在RoboTwin 1.0和2.0上优于$π_0$，证明了强化学习在VLA模型训练中的有效性。此外，该方法还发现了一种新的现象“pushcut”，即策略发现了先前训练过程中未见过的模式，表明强化学习可以帮助模型发现新的策略。

## 🎯 应用场景

SimpleVLA-RL具有广泛的应用前景，可应用于各种机器人操作任务，如家庭服务机器人、工业机器人、医疗机器人等。该研究可以降低机器人操作任务对大规模人工标注数据的依赖，提高机器人的自主性和泛化能力，从而推动机器人技术的发展和应用。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have recently emerged as a powerful paradigm for robotic manipulation. Despite substantial progress enabled by large-scale pretraining and supervised fine-tuning (SFT), these models face two fundamental challenges: (i) the scarcity and high cost of large-scale human-operated robotic trajectories required for SFT scaling, and (ii) limited generalization to tasks involving distribution shift. Recent breakthroughs in Large Reasoning Models (LRMs) demonstrate that reinforcement learning (RL) can dramatically enhance step-by-step reasoning capabilities, raising a natural question: Can RL similarly improve the long-horizon step-by-step action planning of VLA? In this work, we introduce SimpleVLA-RL, an efficient RL framework tailored for VLA models. Building upon veRL, we introduce VLA-specific trajectory sampling, scalable parallelization, multi-environment rendering, and optimized loss computation. When applied to OpenVLA-OFT, SimpleVLA-RL achieves SoTA performance on LIBERO and even outperforms $π_0$ on RoboTwin 1.0\&2.0 with the exploration-enhancing strategies we introduce. SimpleVLA-RL not only reduces dependence on large-scale data and enables robust generalization, but also remarkably surpasses SFT in real-world tasks. Moreover, we identify a novel phenomenon ``pushcut'' during RL training, wherein the policy discovers previously unseen patterns beyond those seen in the previous training process. Github: https://github.com/PRIME-RL/SimpleVLA-RL

