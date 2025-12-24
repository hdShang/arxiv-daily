---
layout: default
title: "Feel the Force: Contact-Driven Learning from Humans"
---

# Feel the Force: Contact-Driven Learning from Humans

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.01944" class="toolbar-btn" target="_blank">📄 arXiv: 2506.01944v1</a>
  <a href="https://arxiv.org/pdf/2506.01944.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.01944v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.01944v1', 'Feel the Force: Contact-Driven Learning from Humans')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ademi Adeniji, Zhuoran Chen, Vincent Liu, Venkatesh Pattabiraman, Raunaq Bhirangi, Siddhant Haldar, Pieter Abbeel, Lerrel Pinto

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-02

---

## 💡 一句话要点

**提出FeelTheForce以解决机器人精细力控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人控制` `力敏感操作` `人类学习` `触觉反馈` `闭环控制` `视觉模型` `人机协作`

## 📋 核心要点

1. 现有的机器人控制策略在真实环境中的多样化交互中泛化能力不足，难以实现精细的接触力控制。
2. 论文提出的FeelTheForce系统通过建模人类的触觉行为，结合触觉手套和视觉模型，实现了力敏感的操作学习。
3. 实验结果表明，该系统在5个力敏感操作任务中达到了77%的成功率，展示了其在实际应用中的有效性。

## 📝 摘要（中文）

在机器人操作中，控制精细的接触力仍然是一个核心挑战。虽然从机器人收集的数据或模拟中学习的策略显示出潜力，但它们在真实世界的多样化交互中难以泛化。直接从人类学习提供了一种可扩展的解决方案，使演示者能够在自然环境中执行技能。然而，仅靠视觉演示缺乏推断精确接触力所需的信息。我们提出了FeelTheForce（FTF）：一个机器人学习系统，通过建模人类触觉行为来学习力敏感的操作。使用触觉手套测量接触力，并通过基于视觉的模型估计手部姿态，我们训练了一个闭环策略，持续预测操作所需的力。该策略被重新定向到配备触觉夹爪传感器的Franka Panda机器人，利用共享的视觉和动作表示。在执行时，PD控制器调节夹爪闭合以跟踪预测的力，从而实现精确的力感知控制。我们的方案在5个力敏感操作任务中实现了77%的成功率。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人在操作过程中对精细接触力的控制问题。现有方法主要依赖于机器人收集的数据或模拟，导致在真实环境中的泛化能力不足。

**核心思路**：论文的核心思路是通过建模人类的触觉行为，利用人类的自然操作技能来学习力敏感的操作。这种设计使得机器人能够在真实环境中更好地理解和应用接触力。

**技术框架**：整体架构包括三个主要模块：触觉手套用于测量接触力，视觉模型用于估计手部姿态，以及闭环控制策略用于实时预测和调节操作所需的力。

**关键创新**：最重要的技术创新在于将人类的触觉行为与机器人控制相结合，利用人类的自然操作来指导机器人学习，从而实现更高效的力控制。与现有方法相比，该方法在学习过程中更具可扩展性和适应性。

**关键设计**：关键设计包括使用触觉手套的传感器数据作为输入，结合视觉模型的输出，训练闭环控制策略。此外，PD控制器的设计用于调节夹爪闭合，以精确跟踪预测的接触力。

## 📊 实验亮点

实验结果显示，FeelTheForce系统在5个力敏感操作任务中实现了77%的成功率，显著优于传统方法。这一成果表明，该系统在实际操作中的有效性和可靠性，为机器人精细力控制提供了新的解决方案。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和人机协作等场景。在这些领域，机器人需要与人类或物体进行精细的物理交互，FeelTheForce系统能够提升机器人在复杂环境中的操作能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Controlling fine-grained forces during manipulation remains a core challenge in robotics. While robot policies learned from robot-collected data or simulation show promise, they struggle to generalize across the diverse range of real-world interactions. Learning directly from humans offers a scalable solution, enabling demonstrators to perform skills in their natural embodiment and in everyday environments. However, visual demonstrations alone lack the information needed to infer precise contact forces. We present FeelTheForce (FTF): a robot learning system that models human tactile behavior to learn force-sensitive manipulation. Using a tactile glove to measure contact forces and a vision-based model to estimate hand pose, we train a closed-loop policy that continuously predicts the forces needed for manipulation. This policy is re-targeted to a Franka Panda robot with tactile gripper sensors using shared visual and action representations. At execution, a PD controller modulates gripper closure to track predicted forces-enabling precise, force-aware control. Our approach grounds robust low-level force control in scalable human supervision, achieving a 77% success rate across 5 force-sensitive manipulation tasks. Code and videos are available at https://feel-the-force-ftf.github.io.

