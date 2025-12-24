---
layout: default
title: FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation
---

# FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06776" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06776v2</a>
  <a href="https://arxiv.org/pdf/2505.06776.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06776v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06776v2', 'FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanhang Zhang, Yifu Yuan, Prajwal Gurunath, Ishita Gupta, Shayegan Omidshafiei, Ali-akbar Agha-mohammadi, Marcell Vazquez-Chanlatte, Liam Pedersen, Tairan He, Guanya Shi

**分类**: cs.RO

**发布日期**: 2025-05-10 (更新: 2025-11-16)

---

## 💡 一句话要点

**提出FALCON框架以解决人形机器人在复杂环境中的力适应性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人形机器人` `强化学习` `运动操控` `力适应性` `双智能体` `机器人技术` `工业自动化`

## 📋 核心要点

1. 现有方法在复杂环境中难以实现人形机器人精确的全身控制，尤其是在外部力干扰下的运动操控。
2. FALCON框架通过将全身控制分解为下肢和上肢两个智能体，分别负责稳定运动和精确力补偿，从而实现力适应性操控。
3. 实验结果显示，FALCON在上肢关节跟踪精度上提高了2倍，并在多种力干扰下保持稳健的运动能力。

## 📝 摘要（中文）

人形机器人在日常服务和工业任务中具有变革潜力，但在3D末端执行器力交互下实现精确、稳健的全身控制仍然是一个重大挑战。现有方法通常局限于轻量任务或四足/轮式平台。为克服这些限制，本文提出了FALCON，一个基于双智能体强化学习的框架，用于稳健的力适应性人形机器人运动操控。FALCON将全身控制分解为两个专门的智能体：下肢智能体确保在外部力干扰下的稳定运动，上肢智能体则精确跟踪末端执行器位置并进行隐式的适应性力补偿。实验表明，与基线相比，FALCON实现了2倍更准确的上肢关节跟踪，同时在力干扰下保持稳健的运动，并实现更快的训练收敛。

## 🔬 方法详解

**问题定义**：本文旨在解决人形机器人在复杂环境中进行力适应性运动操控的挑战，现有方法往往无法处理外部力干扰，导致控制精度不足。

**核心思路**：FALCON框架通过引入两个专门的智能体，分别负责下肢的稳定运动和上肢的精确力补偿，从而实现对外部力的适应性控制。

**技术框架**：FALCON的整体架构包括两个智能体的协同训练，采用强化学习方法，通过逐步增加施加在末端执行器上的外部力来训练智能体，同时遵循扭矩限制。

**关键创新**：FALCON的主要创新在于其双智能体结构，能够在不依赖于特定奖励或课程调优的情况下，实现跨多个机器人平台的政策训练，显著提升了操控的灵活性和适应性。

**关键设计**：在训练过程中，设置了适应性力补偿机制，采用了特定的损失函数来优化上肢关节的跟踪精度，同时确保下肢运动的稳定性。

## 📊 实验亮点

实验结果表明，FALCON在上肢关节跟踪精度上实现了2倍的提升，同时在外部力干扰下保持了稳健的运动能力。此外，FALCON的训练收敛速度也显著提高，展示了其在多种任务中的有效性。

## 🎯 应用场景

FALCON框架的潜在应用领域包括服务机器人、工业自动化和人机协作等场景，能够有效提升机器人在复杂环境中的操作能力，满足日常任务的需求。未来，该技术可能推动人形机器人在更广泛的领域中应用，提升工作效率和安全性。

## 📄 摘要（原文）

> Humanoid loco-manipulation holds transformative potential for daily service and industrial tasks, yet achieving precise, robust whole-body control with 3D end-effector force interaction remains a major challenge. Prior approaches are often limited to lightweight tasks or quadrupedal/wheeled platforms. To overcome these limitations, we propose FALCON, a dual-agent reinforcement-learning-based framework for robust force-adaptive humanoid loco-manipulation. FALCON decomposes whole-body control into two specialized agents: (1) a lower-body agent ensuring stable locomotion under external force disturbances, and (2) an upper-body agent precisely tracking end-effector positions with implicit adaptive force compensation. These two agents are jointly trained in simulation with a force curriculum that progressively escalates the magnitude of external force exerted on the end effector while respecting torque limits. Experiments demonstrate that, compared to the baselines, FALCON achieves 2x more accurate upper-body joint tracking, while maintaining robust locomotion under force disturbances and achieving faster training convergence. Moreover, FALCON enables policy training without embodiment-specific reward or curriculum tuning. Using the same training setup, we obtain policies that are deployed across multiple humanoids, enabling forceful loco-manipulation tasks such as transporting payloads (0-20N force), cart-pulling (0-100N), and door-opening (0-40N) in the real world.

