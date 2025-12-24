---
layout: default
title: "SHaRe-RL: Structured, Interactive Reinforcement Learning for Contact-Rich Industrial Assembly Tasks"
---

# SHaRe-RL: Structured, Interactive Reinforcement Learning for Contact-Rich Industrial Assembly Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13949" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13949v1</a>
  <a href="https://arxiv.org/pdf/2509.13949.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13949v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13949v1', 'SHaRe-RL: Structured, Interactive Reinforcement Learning for Contact-Rich Industrial Assembly Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jannick Stranghöner, Philipp Hartmann, Marco Braun, Sebastian Wrede, Klaus Neumann

**分类**: cs.RO

**发布日期**: 2025-09-17

**备注**: 8 pages, 5 figures, submitted to the IEEE International Conference on Robotics and Automation (ICRA) 2026

---

## 💡 一句话要点

**SHaRe-RL：面向高柔性工业装配的结构化交互式强化学习**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `工业机器人` `人机交互` `接触密集型任务` `装配自动化`

## 📋 核心要点

1. 现有机器人系统在高柔性工业装配中面临适应性差、样本效率低和探索不安全等问题。
2. SHaRe-RL通过结构化技能、融合人类知识和限制交互力，实现高效安全的在线强化学习。
3. 在工业连接器插入实验中，SHaRe-RL在实际时间预算内实现了可靠的性能，验证了其有效性。

## 📝 摘要（中文）

针对中小企业常见的高柔性、小批量工业装配需求，现有机器人系统难以兼顾精度、安全性和灵活性。人工编程适应性差且成本高昂，而基于学习的方法在接触密集型任务中样本效率低且探索不安全。为此，我们提出了SHaRe-RL，一种利用多源先验知识的强化学习框架。通过(i)将技能结构化为操作原语，(ii)结合人类演示和在线修正，以及(iii)使用每轴柔顺性限制交互力，SHaRe-RL能够为长时程、接触密集型工业装配任务实现高效且安全的在线学习。在间隙为0.2-0.4毫米的工业Harting连接器模块插入实验中，证明了SHaRe-RL在实际时间预算内实现了可靠的性能。结果表明，无需机器人或强化学习知识的工艺专业知识，可以有意义地促进学习，从而为工业装配中强化学习的更安全、更稳健和更经济的部署提供可能。

## 🔬 方法详解

**问题定义**：论文旨在解决高柔性、小批量工业装配任务中，机器人难以高效、安全地学习接触密集型操作的问题。现有方法如人工编程难以适应产品变化，而传统强化学习方法样本效率低，且在探索过程中容易造成设备损坏或人员伤害。

**核心思路**：论文的核心思路是结合结构化技能表示、人类知识和力控制，构建一个更安全、更高效的强化学习框架。通过将复杂任务分解为可复用的操作原语，并利用人类演示和在线修正来引导学习过程，同时使用力控制来限制交互力，从而提高学习效率和安全性。

**技术框架**：SHaRe-RL框架包含以下主要模块：(1) 技能结构化模块，将装配任务分解为一系列操作原语；(2) 人机交互模块，允许人类提供演示和在线修正；(3) 强化学习模块，使用结构化的动作空间和奖励函数进行策略学习；(4) 力控制模块，通过调整每轴的柔顺性来限制交互力。整体流程是：首先，人类提供少量演示数据，然后，强化学习智能体在人机交互和力控制的辅助下进行在线学习，不断优化策略。

**关键创新**：SHaRe-RL的关键创新在于将结构化技能表示、人机交互和力控制有机结合，从而显著提高了强化学习在接触密集型工业装配任务中的效率和安全性。与传统强化学习方法相比，SHaRe-RL能够利用先验知识，减少探索空间，避免不安全的操作。

**关键设计**：论文中，操作原语的设计需要根据具体的装配任务进行定义，例如插入、旋转、抓取等。人机交互模块允许操作员通过示教或在线调整来修正机器人的动作。强化学习模块使用Actor-Critic算法，奖励函数的设计需要考虑任务完成度、时间和力的大小。力控制模块通过调整每轴的柔顺性参数来限制交互力，防止过大的力对设备造成损坏。

## 📊 实验亮点

实验结果表明，SHaRe-RL在工业Harting连接器模块插入任务中，能够在实际时间预算内实现可靠的性能。与传统的强化学习方法相比，SHaRe-RL能够显著提高学习效率和安全性，并允许操作员通过人机交互来指导学习过程。该方法在间隙为0.2-0.4毫米的连接器插入任务中表现出良好的鲁棒性。

## 🎯 应用场景

SHaRe-RL可应用于各种高柔性、小批量的工业装配场景，例如电子产品组装、精密仪器制造、汽车零部件装配等。该方法能够降低机器人编程的难度和成本，提高生产效率和产品质量，并为中小企业实现自动化生产提供了一种经济可行的解决方案。未来，该方法有望扩展到更复杂的装配任务和更广泛的机器人应用领域。

## 📄 摘要（原文）

> High-mix low-volume (HMLV) industrial assembly, common in small and medium-sized enterprises (SMEs), requires the same precision, safety, and reliability as high-volume automation while remaining flexible to product variation and environmental uncertainty. Current robotic systems struggle to meet these demands. Manual programming is brittle and costly to adapt, while learning-based methods suffer from poor sample efficiency and unsafe exploration in contact-rich tasks. To address this, we present SHaRe-RL, a reinforcement learning framework that leverages multiple sources of prior knowledge. By (i) structuring skills into manipulation primitives, (ii) incorporating human demonstrations and online corrections, and (iii) bounding interaction forces with per-axis compliance, SHaRe-RL enables efficient and safe online learning for long-horizon, contact-rich industrial assembly tasks. Experiments on the insertion of industrial Harting connector modules with 0.2-0.4 mm clearance demonstrate that SHaRe-RL achieves reliable performance within practical time budgets. Our results show that process expertise, without requiring robotics or RL knowledge, can meaningfully contribute to learning, enabling safer, more robust, and more economically viable deployment of RL for industrial assembly.

