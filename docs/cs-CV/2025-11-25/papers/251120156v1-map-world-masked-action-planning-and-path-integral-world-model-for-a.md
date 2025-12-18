---
layout: default
title: Map-World: Masked Action planning and Path-Integral World Model for Autonomous Driving
---

# Map-World: Masked Action planning and Path-Integral World Model for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.20156" class="toolbar-btn" target="_blank">📄 arXiv: 2511.20156v1</a>
  <a href="https://arxiv.org/pdf/2511.20156.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20156v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.20156v1', 'Map-World: Masked Action planning and Path-Integral World Model for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bin Hu, Zijian Lu, Haicheng Liao, Chengran Yuan, Bin Rao, Yongkang Li, Guofa Li, Zhiyong Cui, Cheng-zhong Xu, Zhenning Li

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-25

---

## 💡 一句话要点

**提出MAP-World，结合掩码动作规划与路径积分世界模型，实现自动驾驶多模态运动规划。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `自动驾驶` `运动规划` `世界模型` `多模态预测` `掩码动作规划`

## 📋 核心要点

1. 现有自动驾驶运动规划方法依赖手工锚点或强化学习选择单一最佳轨迹，忽略了其他可行未来状态的信息。
2. MAP-World将未来自车运动视为掩码序列补全，结合掩码动作规划与路径加权世界模型，实现多模态轨迹预测。
3. 实验表明，MAP-World在NAVSIM上达到与锚点方法相当的性能，并在基于世界模型的方法中取得领先，同时保持实时性。

## 📝 摘要（中文）

自动驾驶的运动规划需要在计算效率高的前提下处理多个可行的未来状态。现有的端到端系统和基于世界模型的规划器虽然可以预测丰富的多模态轨迹，但通常依赖于手工设计的锚点或强化学习来选择单个最佳模式进行训练和控制。这种选择丢弃了关于其他未来状态的信息，并使优化变得复杂。我们提出了MAP-World，一个无先验的多模态规划框架，它将掩码动作规划与路径加权世界模型相结合。掩码动作规划（MAP）模块将未来的自车运动视为掩码序列补全：过去的航点被编码为可见token，未来的航点被表示为掩码token，驾驶意图路径提供了一个粗略的支架。一个紧凑的潜在规划状态通过注入噪声扩展为多个轨迹查询，从而产生多样化的、时间上一致的模式，而无需锚点库或教师策略。然后，一个轻量级的世界模型根据每个候选轨迹展开未来的BEV语义。在训练过程中，语义损失被计算为模式的期望，使用轨迹概率作为离散路径权重，因此规划器可以从所有可能的未来状态分布中学习，而不是单个选定的路径。在NAVSIM上，我们的方法与基于锚点的方法相匹配，并在基于世界模型的方法中实现了最先进的性能，同时避免了强化学习并保持了实时推理延迟。

## 🔬 方法详解

**问题定义**：自动驾驶运动规划需要在复杂环境中预测车辆的未来轨迹，并选择最优的行动方案。现有方法，如基于锚点的方法和强化学习方法，虽然能够生成多模态轨迹，但存在依赖手工设计、训练复杂、忽略其他可行轨迹等问题，导致规划结果的鲁棒性和泛化能力受限。

**核心思路**：MAP-World的核心思路是将未来的自车运动规划问题转化为一个序列补全问题，利用Transformer架构的强大序列建模能力，同时结合世界模型来评估不同轨迹的优劣。通过掩码动作规划（MAP）模块生成多个候选轨迹，并使用路径加权世界模型对这些轨迹进行评估，从而实现多模态运动规划。

**技术框架**：MAP-World框架主要包含两个核心模块：掩码动作规划（MAP）模块和路径加权世界模型。MAP模块负责生成多个候选轨迹，它将过去的航点作为可见token，未来的航点作为掩码token，并利用驾驶意图路径作为引导，生成多样化的轨迹。路径加权世界模型则根据每个候选轨迹展开未来的BEV语义，并计算语义损失，用于训练规划器。

**关键创新**：MAP-World的关键创新在于其无先验的多模态规划方法。它避免了手工设计锚点或使用强化学习，而是通过掩码动作规划和路径加权世界模型，直接从数据中学习多模态轨迹的分布。这种方法能够更好地捕捉环境的不确定性，并生成更鲁棒的规划结果。

**关键设计**：MAP模块使用Transformer架构，将过去和未来的航点作为输入，并利用注意力机制来建模它们之间的关系。通过注入噪声，MAP模块可以生成多个不同的轨迹。路径加权世界模型使用轻量级的卷积神经网络，根据每个轨迹预测未来的BEV语义。训练过程中，语义损失被计算为模式的期望，使用轨迹概率作为离散路径权重，使得规划器可以从所有可能的未来状态分布中学习。

## 📊 实验亮点

MAP-World在NAVSIM仿真平台上进行了评估，实验结果表明，该方法与基于锚点的方法性能相当，并在基于世界模型的方法中取得了领先地位。值得注意的是，MAP-World避免了强化学习的使用，并保持了实时推理延迟，使其更具实用价值。

## 🎯 应用场景

MAP-World可应用于各种自动驾驶场景，例如城市道路、高速公路和停车场等。该方法能够提高自动驾驶系统的安全性和可靠性，尤其是在复杂和不确定的环境中。此外，该方法还可以应用于机器人导航、无人机飞行等领域。

## 📄 摘要（原文）

> Motion planning for autonomous driving must handle multiple plausible futures while remaining computationally efficient. Recent end-to-end systems and world-model-based planners predict rich multi-modal trajectories, but typically rely on handcrafted anchors or reinforcement learning to select a single best mode for training and control. This selection discards information about alternative futures and complicates optimization. We propose MAP-World, a prior-free multi-modal planning framework that couples masked action planning with a path-weighted world model. The Masked Action Planning (MAP) module treats future ego motion as masked sequence completion: past waypoints are encoded as visible tokens, future waypoints are represented as mask tokens, and a driving-intent path provides a coarse scaffold. A compact latent planning state is expanded into multiple trajectory queries with injected noise, yielding diverse, temporally consistent modes without anchor libraries or teacher policies. A lightweight world model then rolls out future BEV semantics conditioned on each candidate trajectory. During training, semantic losses are computed as an expectation over modes, using trajectory probabilities as discrete path weights, so the planner learns from the full distribution of plausible futures instead of a single selected path. On NAVSIM, our method matches anchor-based approaches and achieves state-of-the-art performance among world-model-based methods, while avoiding reinforcement learning and maintaining real-time inference latency.

