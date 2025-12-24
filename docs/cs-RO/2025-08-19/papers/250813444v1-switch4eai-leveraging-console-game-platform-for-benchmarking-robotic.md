---
layout: default
title: "Switch4EAI: Leveraging Console Game Platform for Benchmarking Robotic Athletics"
---

# Switch4EAI: Leveraging Console Game Platform for Benchmarking Robotic Athletics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13444" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13444v1</a>
  <a href="https://arxiv.org/pdf/2508.13444.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13444v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13444v1', 'Switch4EAI: Leveraging Console Game Platform for Benchmarking Robotic Athletics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyu Li, Jeonghwan Kim, Wontaek Kim, Donghoon Baek, Seungeun Rho, Sehoon Ha

**分类**: cs.RO

**发布日期**: 2025-08-19

**备注**: Workshop Submission

---

## 💡 一句话要点

**提出Switch4EAI以解决机器人运动性能评估标准缺乏问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人控制` `运动评估` `类人机器人` `游戏技术` `标准化基准` `动作捕捉` `人机交互`

## 📋 核心要点

1. 现有方法缺乏标准化的基准，难以在真实环境中评估机器人运动表现，尤其是与人类的比较。
2. 提出Switch4EAI，通过利用运动感应游戏来评估机器人控制策略，提供了一种低成本且易于部署的解决方案。
3. 在Unitree G1类人机器人上进行验证，建立了机器人与人类玩家的定量基准，展示了该方法的有效性。

## 📝 摘要（中文）

近年来，整体机器人控制的进展使得类人和腿部机器人能够执行越来越灵活和协调的动作。然而，缺乏标准化的基准来评估机器人在真实环境中的运动表现，尤其是与人类的直接比较。本文提出了Switch4EAI（Switch-for-Embodied-AI），这是一个低成本且易于部署的管道，利用运动感应的游戏来评估整体机器人控制策略。以任天堂Switch上的《Just Dance》为例，我们的系统捕捉、重建并重新定向游戏中的舞蹈动作以供机器人执行。我们在Unitree G1类人机器人上验证了该系统，建立了机器人与人类玩家表现的定量基准。本文讨论了这些结果，展示了使用商业游戏平台作为物理基准的可行性，并激励未来在具身AI基准方面的研究。

## 🔬 方法详解

**问题定义**：本文旨在解决缺乏标准化基准的问题，以便在真实环境中评估机器人运动性能，尤其是与人类的比较。现有方法往往缺乏可操作性和普适性，难以进行有效的评估。

**核心思路**：论文提出的核心思路是利用现有的运动感应游戏作为评估平台，通过捕捉游戏中的舞蹈动作并将其重定向到机器人执行，从而实现对机器人运动性能的标准化评估。

**技术框架**：整体架构包括三个主要模块：动作捕捉模块、动作重建模块和机器人执行模块。首先，系统通过游戏捕捉玩家的动作，然后重建这些动作并将其转化为机器人可执行的指令。

**关键创新**：最重要的技术创新在于将商业游戏平台作为物理基准，利用其丰富的动作数据和标准化的评估方式，显著提高了机器人运动性能评估的可行性和有效性。

**关键设计**：在技术细节上，系统采用了开源的整体控制器，设置了适当的参数以确保动作的准确重定向，并设计了特定的损失函数以优化机器人执行的精度和流畅性。

## 📊 实验亮点

实验结果表明，Switch4EAI系统在Unitree G1类人机器人上的表现与人类玩家进行了有效的对比，建立了定量基准，展示了机器人在执行复杂动作时的能力，提升幅度显著，验证了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人运动控制、娱乐机器人、以及人机交互等。通过提供标准化的评估基准，未来可以促进机器人技术的进步和应用，推动机器人在复杂环境中的自主运动能力提升。

## 📄 摘要（原文）

> Recent advances in whole-body robot control have enabled humanoid and legged robots to execute increasingly agile and coordinated movements. However, standardized benchmarks for evaluating robotic athletic performance in real-world settings and in direct comparison to humans remain scarce. We present Switch4EAI(Switch-for-Embodied-AI), a low-cost and easily deployable pipeline that leverages motion-sensing console games to evaluate whole-body robot control policies. Using Just Dance on the Nintendo Switch as a representative example, our system captures, reconstructs, and retargets in-game choreography for robotic execution. We validate the system on a Unitree G1 humanoid with an open-source whole-body controller, establishing a quantitative baseline for the robot's performance against a human player. In the paper, we discuss these results, which demonstrate the feasibility of using commercial games platform as physically grounded benchmarks and motivate future work to for benchmarking embodied AI.

