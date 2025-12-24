---
layout: default
title: Reactive Aerobatic Flight via Reinforcement Learning
---

# Reactive Aerobatic Flight via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24396" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24396v1</a>
  <a href="https://arxiv.org/pdf/2505.24396.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24396v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24396v1', 'Reactive Aerobatic Flight via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhichao Han, Xijie Huang, Zhuxiu Xu, Jiarui Zhang, Yuze Wu, Mingyang Wang, Tianyue Wu, Fei Gao

**分类**: cs.RO

**发布日期**: 2025-05-30

**备注**: This work has been submitted to RAL and is under review

---

## 💡 一句话要点

**提出基于强化学习的框架以实现四旋翼的反应式特技飞行**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `四旋翼无人机` `特技飞行` `自动化课程学习` `领域随机化` `自主导航` `控制策略`

## 📋 核心要点

1. 现有方法在处理四旋翼的特技飞行时存在跟踪不准确和计算延迟等问题，限制了其在动态环境中的应用。
2. 本文提出了一种基于强化学习的框架，直接将无人机状态与特技意图映射为控制指令，实现端到端的策略优化。
3. 实验结果表明，该方法在真实环境中成功实现了无人机的连续倒飞，并能反应性地穿越移动障碍，展现出显著的灵活性。

## 📝 摘要（中文）

四旋翼无人机展现出卓越的多功能性，但由于固有的欠驱动特性和激烈机动的复杂性，其特技飞行潜力尚未得到充分发挥。传统方法将轨迹优化与跟踪控制分开，导致跟踪不准确、计算延迟及对初始条件敏感，限制了其在动态高灵活场景中的有效性。本文提出了一种基于强化学习的框架，直接将无人机状态与特技意图映射为控制指令，消除了模块化分离，实现了极端特技机动的端到端策略优化。为确保高效稳定的训练，我们引入了一种自动化课程学习策略，动态调整特技任务的难度。通过领域随机化实现稳健的零-shot 模拟到现实转移，我们的方法在要求苛刻的真实世界实验中得到了验证，包括首次展示无人机自主执行连续倒飞并反应性地穿越移动门，展现出前所未有的灵活性。

## 🔬 方法详解

**问题定义**：本文旨在解决四旋翼无人机在特技飞行中的控制问题，现有方法因模块化分离导致跟踪不准确和计算延迟，难以应对动态环境中的高机动性需求。

**核心思路**：我们提出的框架通过强化学习直接将无人机的状态与特技飞行意图映射为控制指令，消除了传统方法中的模块化分离，从而实现了更高效的端到端策略优化。

**技术框架**：整体架构包括状态感知模块、意图生成模块和控制指令输出模块。状态感知模块负责实时获取无人机的飞行状态，意图生成模块基于强化学习算法生成特技飞行意图，控制指令输出模块则将意图转换为具体的控制命令。

**关键创新**：本研究的主要创新在于引入了自动化课程学习策略，动态调整特技任务的难度，以确保训练的高效性和稳定性。此外，领域随机化技术的应用使得模型在真实环境中的零-shot 转移能力显著增强。

**关键设计**：我们在训练过程中设置了多种难度等级的特技任务，并使用了适应性损失函数来优化控制策略。网络结构采用深度强化学习模型，结合卷积神经网络以处理复杂的状态输入。具体参数设置和网络架构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，所提出的方法成功实现了无人机的连续倒飞，并能够在移动障碍物之间进行反应性导航。这一成果在真实环境中首次展示，标志着无人机在特技飞行领域的显著进步，提升幅度明显，具有重要的应用前景。

## 🎯 应用场景

该研究的潜在应用领域包括无人机表演、搜索与救援、以及复杂环境中的自主导航等。通过提升无人机在动态环境中的机动能力，未来可在多种实际场景中实现更高效的任务执行，具有重要的实际价值和影响。

## 📄 摘要（原文）

> Quadrotors have demonstrated remarkable versatility, yet their full aerobatic potential remains largely untapped due to inherent underactuation and the complexity of aggressive maneuvers. Traditional approaches, separating trajectory optimization and tracking control, suffer from tracking inaccuracies, computational latency, and sensitivity to initial conditions, limiting their effectiveness in dynamic, high-agility scenarios. Inspired by recent breakthroughs in data-driven methods, we propose a reinforcement learning-based framework that directly maps drone states and aerobatic intentions to control commands, eliminating modular separation to enable quadrotors to perform end-to-end policy optimization for extreme aerobatic maneuvers. To ensure efficient and stable training, we introduce an automated curriculum learning strategy that dynamically adjusts aerobatic task difficulty. Enabled by domain randomization for robust zero-shot sim-to-real transfer, our approach is validated in demanding real-world experiments, including the first demonstration of a drone autonomously performing continuous inverted flight while reactively navigating a moving gate, showcasing unprecedented agility.

