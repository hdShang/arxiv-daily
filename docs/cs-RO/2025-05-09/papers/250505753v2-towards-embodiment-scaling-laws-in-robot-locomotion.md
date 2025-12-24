---
layout: default
title: Towards Embodiment Scaling Laws in Robot Locomotion
---

# Towards Embodiment Scaling Laws in Robot Locomotion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05753" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05753v2</a>
  <a href="https://arxiv.org/pdf/2505.05753.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05753v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05753v2', 'Towards Embodiment Scaling Laws in Robot Locomotion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bo Ai, Liu Dai, Nico Bohlinger, Dichen Li, Tongzhou Mu, Zhanxin Wu, K. Fay, Henrik I. Christensen, Jan Peters, Hao Su

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-05-09 (更新: 2025-08-29)

**备注**: Conference on Robot Learning (CoRL), 2025. Project website: https://embodiment-scaling-laws.github.io/

---

## 💡 一句话要点

**提出体现规模定律以提升机器人运动的泛化能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `机器人运动` `跨体现泛化` `体现规模定律` `自适应控制` `形态共设计` `智能体训练` `迁移学习`

## 📋 核心要点

1. 核心问题：现有方法对跨体现泛化的理解不足，限制了通用体化智能体的构建。
2. 方法要点：通过生成多样化的训练体现，验证增加体现数量对泛化能力的积极影响。
3. 实验或效果：最佳策略在新体现上实现零样本迁移，展示了显著的泛化能力提升。

## 📝 摘要（中文）

跨体现泛化是构建通用体化智能体的愿景基础，但其实现因素尚不清晰。本文研究了体现规模定律，假设增加训练体现的数量可以改善对未见体现的泛化能力，以机器人运动为测试平台。我们程序生成了约1000个具有拓扑、几何和关节运动学变化的体现，并在随机子集上训练策略。观察到支持该假设的积极规模趋势，发现体现规模化显著提升了对固定体现的数据规模化的泛化能力。我们在完整数据集上训练的最佳策略在模拟和现实世界中对新体现实现零样本迁移，包括Unitree Go2和H1。这些结果为通用体化智能的实现迈出了重要一步，具有对可配置机器人自适应控制、形态共设计等领域的相关性。

## 🔬 方法详解

**问题定义**：本文旨在解决跨体现泛化能力不足的问题，现有方法未能充分利用多样化的训练体现，导致智能体在新环境中的表现不佳。

**核心思路**：提出通过生成多样化的训练体现来提升智能体的泛化能力，假设增加训练体现的数量能够改善对未见体现的适应性。

**技术框架**：研究中生成了约1000个不同的体现，涵盖拓扑、几何和关节运动学的变化。训练策略在这些体现的随机子集上进行，评估其泛化能力。

**关键创新**：最重要的创新在于验证了体现规模化的有效性，发现其在泛化能力上优于仅依赖固定体现的数据规模化方法。

**关键设计**：在训练过程中，采用了多样化的体现生成策略，确保了训练数据的丰富性和多样性，优化了策略的迁移能力。

## 📊 实验亮点

实验结果显示，最佳策略在新体现上实现了零样本迁移，成功应用于Unitree Go2和H1等机器人，展现出显著的泛化能力提升。这一成果为通用体化智能的实现提供了重要的实验支持。

## 🎯 应用场景

该研究的潜在应用领域包括可配置机器人、自适应控制系统以及形态共设计等。通过提升机器人在不同环境中的适应能力，能够推动智能体在复杂任务中的应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Cross-embodiment generalization underpins the vision of building generalist embodied agents for any robot, yet its enabling factors remain poorly understood. We investigate embodiment scaling laws, the hypothesis that increasing the number of training embodiments improves generalization to unseen ones, using robot locomotion as a test bed. We procedurally generate ~1,000 embodiments with topological, geometric, and joint-level kinematic variations, and train policies on random subsets. We observe positive scaling trends supporting the hypothesis, and find that embodiment scaling enables substantially broader generalization than data scaling on fixed embodiments. Our best policy, trained on the full dataset, transfers zero-shot to novel embodiments in simulation and the real world, including the Unitree Go2 and H1. These results represent a step toward general embodied intelligence, with relevance to adaptive control for configurable robots, morphology co-design, and beyond.

