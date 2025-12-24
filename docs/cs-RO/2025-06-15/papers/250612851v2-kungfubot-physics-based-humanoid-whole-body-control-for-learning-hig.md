---
layout: default
title: "KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills"
---

# KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12851" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12851v2</a>
  <a href="https://arxiv.org/pdf/2506.12851.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12851v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12851v2', 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weiji Xie, Jinrui Han, Jiakun Zheng, Huanyu Li, Xinzhe Liu, Jiyuan Shi, Weinan Zhang, Chenjia Bai, Xuelong Li

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-15 (更新: 2025-10-27)

**备注**: NeurIPS 2025. Project Page: https://kungfu-bot.github.io/

---

## 💡 一句话要点

**提出基于物理的人形机器人全身控制框架以学习高动态技能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `人形机器人` `动态技能` `运动模仿` `自适应控制` `物理约束` `策略训练` `双层优化`

## 📋 核心要点

1. 现有算法仅能跟踪低速平滑的人类动作，无法有效处理高动态技能的模仿。
2. 提出了一种基于物理的控制框架，通过多步骤运动处理和自适应跟踪来实现高动态行为的模仿。
3. 实验结果显示，所提方法在跟踪误差上显著优于现有方法，并成功应用于实际机器人中。

## 📝 摘要（中文）

人形机器人在模仿人类行为以获取各种技能方面展现出良好前景。然而，现有算法仅能跟踪平滑、低速的人类动作，即使经过精细的奖励和课程设计。本文提出了一种基于物理的人形控制框架，旨在通过多步骤运动处理和自适应运动跟踪，掌握如功夫和舞蹈等高动态人类行为。我们设计了一条运动处理管道，以提取、过滤、校正和重新定向运动，同时确保最大程度地遵循物理约束。在运动模仿方面，我们构建了一个双层优化问题，根据当前跟踪误差动态调整跟踪精度容忍度，形成自适应课程机制。实验表明，我们的方法在模仿一系列高动态动作时，跟踪误差显著低于现有方法，并成功部署在Unitree G1机器人上，展现出稳定且富有表现力的行为。

## 🔬 方法详解

**问题定义**：本文旨在解决现有算法在模仿高动态人类行为时的不足，特别是在跟踪精度和运动表现方面的挑战。现有方法无法有效处理复杂的动态动作，导致跟踪误差较大。

**核心思路**：论文提出了一种基于物理的控制框架，通过设计运动处理管道和自适应运动跟踪机制，来提高对高动态技能的模仿能力。通过动态调整跟踪精度容忍度，形成自适应课程机制，以适应不同的运动复杂性。

**技术框架**：整体架构包括运动处理、运动模仿和策略训练三个主要模块。运动处理模块负责提取和校正运动，运动模仿模块通过双层优化问题进行跟踪，策略训练模块则使用不对称演员-评论家框架进行政策学习。

**关键创新**：最重要的创新在于提出了自适应课程机制和双层优化问题，能够根据跟踪误差动态调整跟踪精度，这在现有方法中尚未见到。

**关键设计**：在设计中，运动处理管道确保遵循物理约束，损失函数的设计考虑了跟踪误差和运动的动态特性，网络结构采用不对称演员-评论家架构以提高学习效率。

## 📊 实验亮点

实验结果表明，所提方法在模仿高动态动作时，跟踪误差显著低于现有方法，具体表现为跟踪误差降低了XX%（具体数据未知）。该方法成功部署在Unitree G1机器人上，展现出稳定且富有表现力的运动行为，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括人形机器人在娱乐、体育训练和人机交互等场景中的应用。通过学习高动态技能，机器人能够更自然地与人类互动，提升其在复杂环境中的适应能力和表现力。未来，随着技术的进一步发展，该框架可能会在更多领域中发挥重要作用。

## 📄 摘要（原文）

> Humanoid robots are promising to acquire various skills by imitating human behaviors. However, existing algorithms are only capable of tracking smooth, low-speed human motions, even with delicate reward and curriculum design. This paper presents a physics-based humanoid control framework, aiming to master highly-dynamic human behaviors such as Kungfu and dancing through multi-steps motion processing and adaptive motion tracking. For motion processing, we design a pipeline to extract, filter out, correct, and retarget motions, while ensuring compliance with physical constraints to the maximum extent. For motion imitation, we formulate a bi-level optimization problem to dynamically adjust the tracking accuracy tolerance based on the current tracking error, creating an adaptive curriculum mechanism. We further construct an asymmetric actor-critic framework for policy training. In experiments, we train whole-body control policies to imitate a set of highly-dynamic motions. Our method achieves significantly lower tracking errors than existing approaches and is successfully deployed on the Unitree G1 robot, demonstrating stable and expressive behaviors. The project page is https://kungfu-bot.github.io.

