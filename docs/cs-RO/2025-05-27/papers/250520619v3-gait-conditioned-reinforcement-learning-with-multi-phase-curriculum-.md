---
layout: default
title: Gait-Conditioned Reinforcement Learning with Multi-Phase Curriculum for Humanoid Locomotion
---

# Gait-Conditioned Reinforcement Learning with Multi-Phase Curriculum for Humanoid Locomotion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20619" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20619v3</a>
  <a href="https://arxiv.org/pdf/2505.20619.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20619v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20619v3', 'Gait-Conditioned Reinforcement Learning with Multi-Phase Curriculum for Humanoid Locomotion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianhu Peng, Lingfan Bao, Chengxu Zhou

**分类**: cs.RO

**发布日期**: 2025-05-27 (更新: 2025-09-15)

---

## 💡 一句话要点

**提出基于步态条件的强化学习框架以实现类人机器人多模式运动**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `步态条件强化学习` `类人机器人` `运动控制` `动态奖励机制` `结构化课程`

## 📋 核心要点

1. 现有方法在类人机器人运动控制中面临步态多样性和奖励干扰的问题，导致学习效率低下。
2. 本文提出了一种步态条件强化学习框架，利用动态奖励路由和结构化课程逐步引入复杂步态，提升学习稳定性。
3. 实验结果表明，该方法在仿真和真实机器人上均成功实现了多种运动模式，验证了其有效性和稳定性。

## 📝 摘要（中文）

本文提出了一种统一的步态条件强化学习框架，使类人机器人能够在单一递归策略下执行站立、行走、奔跑及平滑过渡。通过动态激活步态特定目标的紧凑奖励路由机制，减轻了奖励干扰，支持稳定的多步态学习。人类启发的奖励项促进了生物力学自然的运动，如直膝站立和协调的手腿摆动，而无需运动捕捉数据。结构化的课程逐步引入步态复杂性，并在多个阶段扩展指令空间。在仿真中，该策略成功实现了稳健的站立、行走、奔跑及步态过渡。在真实的Unitree G1类人机器人上，我们验证了站立、行走及行走到站立的过渡，展示了稳定且协调的运动控制。这项工作为在多样化模式和环境中实现灵活自然的类人控制提供了可扩展的无参考解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决类人机器人在多步态运动控制中的学习效率低下及奖励干扰问题。现有方法往往无法有效处理多样化的步态，导致运动控制不稳定。

**核心思路**：提出的框架通过步态条件强化学习，结合动态激活的奖励机制，促进多步态的稳定学习。设计上，利用人类启发的奖励项来引导机器人学习自然的运动模式。

**技术框架**：整体架构包括步态条件输入、动态奖励路由和结构化课程三个主要模块。步态条件输入通过一热编码传递步态信息，动态奖励路由根据当前步态激活相应的奖励目标，结构化课程则逐步增加学习的复杂性。

**关键创新**：最重要的创新在于紧凑的奖励路由机制和结构化课程设计，这与现有方法的静态奖励和单一学习阶段形成鲜明对比，显著提升了多步态学习的稳定性和效率。

**关键设计**：在技术细节上，采用了适应性损失函数来平衡不同步态的学习，网络结构设计为递归神经网络，以处理时间序列数据，确保运动的连贯性和自然性。具体参数设置和训练策略在实验中进行了优化。

## 📊 实验亮点

实验结果显示，所提出的框架在仿真环境中成功实现了稳健的站立、行走和奔跑，且在真实Unitree G1类人机器人上验证了站立、行走及行走到站立的过渡，展示了稳定的运动控制。与基线方法相比，运动的协调性和自然性有显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人及娱乐机器人等，能够在复杂环境中实现灵活的运动控制。其无参考的控制方法为未来类人机器人在多样化任务中的应用提供了新的思路，具有广泛的实际价值和影响力。

## 📄 摘要（原文）

> We present a unified gait-conditioned reinforcement learning framework that enables humanoid robots to perform standing, walking, running, and smooth transitions within a single recurrent policy. A compact reward routing mechanism dynamically activates gait-specific objectives based on a one-hot gait ID, mitigating reward interference and supporting stable multi-gait learning. Human-inspired reward terms promote biomechanically natural motions, such as straight-knee stance and coordinated arm-leg swing, without requiring motion capture data. A structured curriculum progressively introduces gait complexity and expands command space over multiple phases. In simulation, the policy successfully achieves robust standing, walking, running, and gait transitions. On the real Unitree G1 humanoid, we validate standing, walking, and walk-to-stand transitions, demonstrating stable and coordinated locomotion. This work provides a scalable, reference-free solution toward versatile and naturalistic humanoid control across diverse modes and environments.

