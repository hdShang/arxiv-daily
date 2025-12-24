---
layout: default
title: "CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance"
---

# CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22773" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22773v1</a>
  <a href="https://arxiv.org/pdf/2511.22773.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22773v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.22773v1', 'CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Heng Yang, Xuan Zhao, Leo Maxime Brunswic, Montgomery Alban, Mateo Clemente, Tongtong Cao, Jun Jin, Amir Rasouli

**分类**: cs.RO, cs.AI

**发布日期**: 2025-11-27

**备注**: 4 tables, 9 figures

---

## 💡 一句话要点

**CAPE：基于近端模式扩展的上下文感知扩散策略，用于机器人避障**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散模型` `模仿学习` `机器人避障` `上下文感知` `轨迹生成`

## 📋 核心要点

1. 现有模仿学习方法在避障等复杂任务中，需要大量数据才能保证泛化性，数据采集成本高昂。
2. CAPE通过上下文感知的先验引导迭代细化，扩展轨迹分布模式，从而在推理时生成更优的避障轨迹。
3. CAPE在模拟和真实世界的实验中，相较于现有方法，成功率分别提升了26%和80%，展示了其优越的泛化能力。

## 📝 摘要（中文）

扩散模型能够从演示数据中捕获多模态轨迹，使其成为模仿学习中一种变革性的方法。然而，要达到最佳性能需要大规模数据集，这对于具有挑战性的任务（如避障）而言成本高昂。为了解决这个问题，我们提出了基于近端模式扩展的上下文感知扩散策略（CAPE），该框架通过一种新颖的先验引导迭代细化程序，在推理时利用上下文感知先验和指导来扩展轨迹分布模式。该框架生成初始轨迹规划并执行一个短轨迹前缀，然后将剩余轨迹段扰动到中间噪声水平，形成轨迹先验。这种先验是上下文感知的，并保留了任务意图。通过上下文感知引导去噪重复该过程，迭代地扩展模式支持，从而允许找到更平滑、更少碰撞的轨迹。对于避障，CAPE使用碰撞感知上下文扩展轨迹分布模式，从而能够在以前未见过的环境中采样无碰撞轨迹，同时保持目标一致性。我们在各种杂乱的、未见过的模拟和真实世界环境中评估了CAPE，并表明与SOTA方法相比，成功率分别提高了高达26%和80%，证明了对未见环境的更好泛化。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人避障任务中，模仿学习方法对新环境泛化能力不足的问题。现有方法依赖大量数据，难以覆盖所有可能的障碍物类型和空间配置，导致在未见过的环境中容易发生碰撞。

**核心思路**：论文的核心思路是利用扩散模型生成轨迹，并通过上下文感知的先验信息引导轨迹的生成过程，从而扩展轨迹分布的模式，使其能够覆盖更多安全、无碰撞的轨迹。这种方法能够在少量数据的基础上，提升模型对新环境的泛化能力。

**技术框架**：CAPE框架包含以下几个主要阶段：1) 生成初始轨迹规划；2) 执行轨迹前缀；3) 将剩余轨迹段扰动到中间噪声水平，形成上下文感知的轨迹先验；4) 通过上下文感知引导去噪，迭代地细化轨迹，扩展模式支持。该框架通过不断地迭代，逐步生成更平滑、更少碰撞的轨迹。

**关键创新**：CAPE的关键创新在于提出了上下文感知的先验引导迭代细化程序。该程序利用已执行的轨迹前缀作为上下文信息，生成轨迹先验，并利用该先验引导扩散模型的去噪过程，从而扩展轨迹分布的模式。这种方法能够有效地利用上下文信息，生成更符合任务需求的轨迹。

**关键设计**：CAPE的关键设计包括：1) 使用扩散模型作为轨迹生成器；2) 设计上下文感知的轨迹先验，该先验基于已执行的轨迹前缀生成；3) 设计上下文感知引导去噪过程，该过程利用轨迹先验引导扩散模型的去噪过程。具体的参数设置和网络结构等细节在论文中进行了详细描述，但摘要中未提及具体数值。

## 📊 实验亮点

CAPE在模拟和真实世界的实验中表现出色。在模拟环境中，CAPE的成功率比现有方法提高了26%。在更具挑战性的真实世界环境中，CAPE的成功率更是提高了80%。这些结果表明，CAPE具有很强的泛化能力，能够在未见过的环境中生成安全、有效的避障轨迹。

## 🎯 应用场景

CAPE框架可应用于各种机器人避障场景，例如自动驾驶、无人机导航、工业机器人等。该研究能够降低机器人对环境感知的要求，提高机器人在复杂环境中的安全性和可靠性，具有重要的实际应用价值和广阔的未来发展前景。

## 📄 摘要（原文）

> In robotics, diffusion models can capture multi-modal trajectories from demonstrations, making them a transformative approach in imitation learning. However, achieving optimal performance following this regiment requires a large-scale dataset, which is costly to obtain, especially for challenging tasks, such as collision avoidance. In those tasks, generalization at test time demands coverage of many obstacles types and their spatial configurations, which are impractical to acquire purely via data. To remedy this problem, we propose Context-Aware diffusion policy via Proximal mode Expansion (CAPE), a framework that expands trajectory distribution modes with context-aware prior and guidance at inference via a novel prior-seeded iterative guided refinement procedure. The framework generates an initial trajectory plan and executes a short prefix trajectory, and then the remaining trajectory segment is perturbed to an intermediate noise level, forming a trajectory prior. Such a prior is context-aware and preserves task intent. Repeating the process with context-aware guided denoising iteratively expands mode support to allow finding smoother, less collision-prone trajectories. For collision avoidance, CAPE expands trajectory distribution modes with collision-aware context, enabling the sampling of collision-free trajectories in previously unseen environments while maintaining goal consistency. We evaluate CAPE on diverse manipulation tasks in cluttered unseen simulated and real-world settings and show up to 26% and 80% higher success rates respectively compared to SOTA methods, demonstrating better generalization to unseen environments.

