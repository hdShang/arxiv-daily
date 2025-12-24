---
layout: default
title: "Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids"
---

# Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12252" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12252v2</a>
  <a href="https://arxiv.org/pdf/2508.12252.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12252v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12252v2', 'Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaizhe Hu, Haochen Shi, Yao He, Weizhuo Wang, C. Karen Liu, Shuran Song

**分类**: cs.RO

**发布日期**: 2025-08-17 (更新: 2025-08-26)

**备注**: Accepted to The Conference on Robot Learning (CoRL) 2025

---

## 💡 一句话要点

**提出Robot-Trains-Robot框架以解决人形机器人现实世界学习问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人形机器人` `强化学习` `仿真与现实` `自动化学习` `机器人教师` `动态编码` `学习效率` `安全性`

## 📋 核心要点

1. 现有的仿真基础强化学习方法在现实世界应用中面临安全性和效率等挑战，限制了人形机器人的学习能力。
2. 提出Robot-Trains-Robot框架，通过机器人教师指导学生机器人，提供多种支持以优化现实世界学习过程。
3. 在两个复杂的现实世界任务中验证了方法的有效性，显示出在行走策略微调和从零开始学习摆动任务方面的显著进步。

## 📝 摘要（中文）

基于仿真的强化学习（RL）在提升人形机器人行走任务方面取得了显著进展，但从零开始的现实世界RL或从预训练策略的适应仍然较为稀缺，限制了人形机器人的潜力。现实世界学习在克服仿真与现实之间的差距时面临安全性、奖励设计和学习效率等重大挑战。为了解决这些问题，我们提出了Robot-Trains-Robot（RTR）框架，其中一个机器人手臂教师积极支持和指导人形机器人学生。RTR系统提供保护、学习计划、奖励、扰动、失败检测和自动重置，能够在最小人类干预下实现高效的长期现实世界人形训练。此外，我们提出了一种新的RL管道，通过优化一个在现实世界中的单一动态编码潜变量来促进和稳定仿真到现实的转移。我们通过两个具有挑战性的现实世界人形任务验证了我们的方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决人形机器人在现实世界中学习的挑战，尤其是仿真与现实之间的差距，以及安全性和学习效率的问题。现有方法往往无法有效适应真实环境，导致学习效果不佳。

**核心思路**：我们提出的Robot-Trains-Robot框架通过一个机器人教师主动支持人形机器人学生，提供必要的保护和指导，从而提高学习效率和安全性。这样的设计使得机器人能够在复杂环境中进行自主学习，同时减少人类干预。

**技术框架**：RTR系统包括多个模块：教师机器人负责提供指导和保护，学习计划模块优化学习进度，奖励机制设计用于激励学生机器人，扰动和失败检测模块确保学习过程的稳定性，自动重置功能则在出现失败时迅速恢复学习状态。

**关键创新**：本研究的主要创新在于引入了一个动态编码的潜变量优化机制，能够在现实世界中有效促进仿真到现实的转移。这一机制与传统的直接RL方法相比，显著提高了学习的稳定性和效率。

**关键设计**：在设计中，我们设置了多种参数以适应不同的学习任务，包括奖励函数的设计、扰动强度的调节以及教师机器人与学生机器人之间的交互策略。这些设计确保了学习过程的灵活性和适应性。

## 📊 实验亮点

在实验中，RTR框架在两个现实世界任务中表现出色：在行走策略微调任务中，机器人实现了精确的速度跟踪，而在摆动任务中，从零开始学习的效率显著提升，展示了与传统方法相比的明显优势。

## 🎯 应用场景

该研究的潜在应用领域包括人形机器人在复杂环境中的自主导航、任务执行和人机协作等场景。通过优化现实世界学习过程，RTR框架能够提升机器人在实际应用中的表现，推动智能机器人技术的发展与普及。

## 📄 摘要（原文）

> Simulation-based reinforcement learning (RL) has significantly advanced humanoid locomotion tasks, yet direct real-world RL from scratch or adapting from pretrained policies remains rare, limiting the full potential of humanoid robots. Real-world learning, despite being crucial for overcoming the sim-to-real gap, faces substantial challenges related to safety, reward design, and learning efficiency. To address these limitations, we propose Robot-Trains-Robot (RTR), a novel framework where a robotic arm teacher actively supports and guides a humanoid robot student. The RTR system provides protection, learning schedule, reward, perturbation, failure detection, and automatic resets. It enables efficient long-term real-world humanoid training with minimal human intervention. Furthermore, we propose a novel RL pipeline that facilitates and stabilizes sim-to-real transfer by optimizing a single dynamics-encoded latent variable in the real world. We validate our method through two challenging real-world humanoid tasks: fine-tuning a walking policy for precise speed tracking and learning a humanoid swing-up task from scratch, illustrating the promising capabilities of real-world humanoid learning realized by RTR-style systems. See https://robot-trains-robot.github.io/ for more info.

