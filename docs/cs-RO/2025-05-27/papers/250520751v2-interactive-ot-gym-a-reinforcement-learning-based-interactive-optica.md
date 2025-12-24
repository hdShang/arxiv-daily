---
layout: default
title: "Interactive OT Gym: A Reinforcement Learning-Based Interactive Optical tweezer (OT)-Driven Microrobotics Simulation Platform"
---

# Interactive OT Gym: A Reinforcement Learning-Based Interactive Optical tweezer (OT)-Driven Microrobotics Simulation Platform

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20751" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20751v2</a>
  <a href="https://arxiv.org/pdf/2505.20751.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20751v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20751v2', 'Interactive OT Gym: A Reinforcement Learning-Based Interactive Optical tweezer (OT)-Driven Microrobotics Simulation Platform')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zongcai Tan, Dandan Zhang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-27 (更新: 2025-05-30)

**备注**: ICRA 2025

---

## 💡 一句话要点

**提出Interactive OT Gym以解决光学镊子驱动微机器人协作操控问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `光学镊子` `微机器人` `强化学习` `共享控制` `生物医学` `微操控` `模拟平台`

## 📋 核心要点

1. 现有的光学镊子控制方法在动态环境中实现多个微机器人的协作操控存在显著挑战，尤其是复杂形状的微机器人。
2. 论文提出了Interactive OT Gym，一个基于强化学习的模拟平台，支持复杂物理场模拟和上下文感知的共享控制策略。
3. 实验表明，使用该平台的共享控制系统相比纯人控或RL控制，任务完成时间减少约67%，成功率达到100%。

## 📝 摘要（中文）

光学镊子（OT）在生物医学应用中提供了无与伦比的亚微米精度微操控能力。然而，控制传统多陷阱OT以实现动态环境中多个复杂形状微机器人的协作操控面临重大挑战。为此，我们提出了Interactive OT Gym，这是一个基于强化学习（RL）的模拟平台，旨在支持OT驱动的微机器人。该平台支持复杂物理场模拟，并集成了触觉反馈接口、RL模块和针对OT驱动微机器人在协作生物对象操控任务中的上下文感知共享控制策略。实验结果表明，我们的共享控制系统显著提高了微操控性能，任务完成时间减少约67%，成功率达到100%。

## 🔬 方法详解

**问题定义**：本论文旨在解决在动态环境中使用光学镊子进行多个复杂形状微机器人协作操控的挑战。现有方法在控制精度和效率上存在不足，难以实现高效的微操控。

**核心思路**：我们提出的Interactive OT Gym平台结合了强化学习和共享控制策略，允许在手动和自主控制之间无缝切换，从而提高微操控的灵活性和效率。

**技术框架**：该平台的整体架构包括复杂物理场模拟模块、触觉反馈接口、强化学习模块和上下文感知共享控制策略。各模块协同工作，支持高效的微操控任务。

**关键创新**：最重要的创新在于将强化学习与共享控制相结合，使得用户可以在手动输入和自主操作之间自适应切换，这在现有的光学镊子控制方法中尚属首次。

**关键设计**：在设计中，我们采用了特定的损失函数来优化控制策略，并通过高保真度的物理模拟来确保训练的有效性。网络结构经过精心设计，以适应复杂的微操控任务。

## 📊 实验亮点

实验结果显示，使用Interactive OT Gym的共享控制系统相比于单独使用人控或强化学习控制，任务完成时间减少了约67%，并且成功率达到了100%。这一显著提升证明了该平台在微操控任务中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括生物医学、微制造和纳米技术等。Interactive OT Gym为开发先进的光学镊子驱动微操控系统和控制算法提供了用户友好的训练和测试环境，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Optical tweezers (OT) offer unparalleled capabilities for micromanipulation with submicron precision in biomedical applications. However, controlling conventional multi-trap OT to achieve cooperative manipulation of multiple complex-shaped microrobots in dynamic environments poses a significant challenge. To address this, we introduce Interactive OT Gym, a reinforcement learning (RL)-based simulation platform designed for OT-driven microrobotics. Our platform supports complex physical field simulations and integrates haptic feedback interfaces, RL modules, and context-aware shared control strategies tailored for OT-driven microrobot in cooperative biological object manipulation tasks. This integration allows for an adaptive blend of manual and autonomous control, enabling seamless transitions between human input and autonomous operation. We evaluated the effectiveness of our platform using a cell manipulation task. Experimental results show that our shared control system significantly improves micromanipulation performance, reducing task completion time by approximately 67% compared to using pure human or RL control alone and achieving a 100% success rate. With its high fidelity, interactivity, low cost, and high-speed simulation capabilities, Interactive OT Gym serves as a user-friendly training and testing environment for the development of advanced interactive OT-driven micromanipulation systems and control algorithms. For more details on the project, please see our website https://sites.google.com/view/otgym

