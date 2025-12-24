---
layout: default
title: "CoTaP: Compliant Task Pipeline and Reinforcement Learning of Its Controller with Compliance Modulation"
---

# CoTaP: Compliant Task Pipeline and Reinforcement Learning of Its Controller with Compliance Modulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25443" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25443v2</a>
  <a href="https://arxiv.org/pdf/2509.25443.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25443v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25443v2', 'CoTaP: Compliant Task Pipeline and Reinforcement Learning of Its Controller with Compliance Modulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zewen He, Chenyuan Chen, Dilshod Azizov, Yoshihiko Nakamura

**分类**: cs.RO

**发布日期**: 2025-09-29 (更新: 2025-10-06)

**备注**: Submitted to IEEE for possible publication, under review

---

## 💡 一句话要点

**提出CoTaP框架，通过强化学习和柔顺控制实现人型机器人全身运动控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人型机器人` `全身运动控制` `强化学习` `柔顺控制` `知识蒸馏`

## 📋 核心要点

1. 现有基于学习的人型机器人控制方法缺乏力数据，难以在真实环境中实现适当的柔顺性。
2. CoTaP框架结合强化学习和基于模型的柔顺控制，通过两阶段训练实现全身运动控制。
3. 仿真实验验证了CoTaP框架在不同柔顺性设置下对外部扰动的响应，证明了其可行性。

## 📝 摘要（中文）

本文提出了一种名为Compliant Task Pipeline (CoTaP) 的框架，旨在利用柔顺性信息改进人型机器人的基于学习的控制结构。该框架提出了一种两阶段双智能体强化学习方法，并结合基于模型的柔顺控制。在训练过程中，首先训练一个基于位置控制器的基础策略；然后在知识蒸馏阶段，将上半身策略与基于模型的柔顺控制相结合，并由基础策略引导下半身智能体。在上半身控制中，可以通过对称正定 (SPD) 流形上的柔顺性调制来指定可调节的任务空间柔顺性，并将其与其他控制器集成，从而确保系统稳定性。通过仿真验证了该策略的可行性，主要比较了不同柔顺性设置下对外部扰动的响应。

## 🔬 方法详解

**问题定义**：论文旨在解决人型机器人全身运动控制中，由于缺乏力数据和依赖位置控制，难以在与环境交互时实现适当柔顺性的问题。现有方法主要依赖位置控制，无法有效处理外部扰动和实现精确的力控制。

**核心思路**：论文的核心思路是将强化学习与基于模型的柔顺控制相结合，通过两阶段训练策略，使机器人能够学习到具有柔顺性的运动控制策略。通过可调节的任务空间柔顺性，机器人可以更好地适应外部环境的变化，并实现更稳定和自然的运动。

**技术框架**：CoTaP框架包含以下几个主要模块：1) 基于位置控制器的基础策略训练；2) 上半身策略与基于模型的柔顺控制相结合；3) 下半身智能体由基础策略引导；4) 通过SPD流形上的柔顺性调制实现任务空间柔顺性的调整。整体流程是先训练一个基础的运动策略，然后通过知识蒸馏的方式，将柔顺控制融入到上半身的控制中，从而实现全身的柔顺运动控制。

**关键创新**：论文的关键创新在于将强化学习与基于模型的柔顺控制相结合，并提出了一个两阶段的训练策略。通过这种方式，机器人可以在没有大量力数据的情况下，学习到具有柔顺性的运动控制策略。此外，通过SPD流形上的柔顺性调制，可以灵活地调整任务空间的柔顺性，从而适应不同的任务需求。

**关键设计**：论文的关键设计包括：1) 两阶段的强化学习训练策略，分别训练基础策略和柔顺控制策略；2) 基于模型的柔顺控制器的设计，用于实现任务空间的柔顺性控制；3) SPD流形上的柔顺性调制方法，用于灵活地调整柔顺性参数。具体的损失函数和网络结构等细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

论文通过仿真实验验证了CoTaP框架的有效性。实验结果表明，在不同柔顺性设置下，CoTaP框架能够有效地应对外部扰动，并保持系统的稳定性。通过对比不同柔顺性参数下的响应，验证了柔顺性调制方法的有效性。具体的性能数据和提升幅度在论文中进行了详细描述（未知）。

## 🎯 应用场景

该研究成果可应用于人型机器人辅助医疗、康复训练、人机协作等领域。通过柔顺性控制，机器人可以更安全、更自然地与人或环境进行交互，从而提高工作效率和安全性。未来，该技术有望应用于更复杂的机器人系统，例如双臂机器人、移动机器人等。

## 📄 摘要（原文）

> Humanoid whole-body locomotion control is a critical approach for humanoid robots to leverage their inherent advantages. Learning-based control methods derived from retargeted human motion data provide an effective means of addressing this issue. However, because most current human datasets lack measured force data, and learning-based robot control is largely position-based, achieving appropriate compliance during interaction with real environments remains challenging. This paper presents Compliant Task Pipeline (CoTaP): a pipeline that leverages compliance information in the learning-based structure of humanoid robots. A two-stage dual-agent reinforcement learning framework combined with model-based compliance control for humanoid robots is proposed. In the training process, first a base policy with a position-based controller is trained; then in the distillation, the upper-body policy is combined with model-based compliance control, and the lower-body agent is guided by the base policy. In the upper-body control, adjustable task-space compliance can be specified and integrated with other controllers through compliance modulation on the symmetric positive definite (SPD) manifold, ensuring system stability. We validated the feasibility of the proposed strategy in simulation, primarily comparing the responses to external disturbances under different compliance settings.

