---
layout: default
title: "Deep Reactive Policy: Learning Reactive Manipulator Motion Planning for Dynamic Environments"
---

# Deep Reactive Policy: Learning Reactive Manipulator Motion Planning for Dynamic Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06953" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06953v1</a>
  <a href="https://arxiv.org/pdf/2509.06953.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06953v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06953v1', 'Deep Reactive Policy: Learning Reactive Manipulator Motion Planning for Dynamic Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahui Yang, Jason Jingzhou Liu, Yulong Li, Youssef Khaky, Kenneth Shaw, Deepak Pathak

**分类**: cs.RO, cs.AI, cs.CV, cs.LG, eess.SY

**发布日期**: 2025-09-08

**备注**: Website at \url{deep-reactive-policy.com}

---

## 💡 一句话要点

**提出深度反应策略DRP，解决动态环境中机器人操作臂的反应式运动规划问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `机器人操作臂` `运动规划` `深度学习` `Transformer` `动态环境`

## 📋 核心要点

1. 传统运动规划器需要完全的环境知识，且速度慢，难以适应动态环境；神经运动策略虽然能直接处理原始感官输入，但在复杂或动态环境中泛化能力不足。
2. 论文提出DRP，核心是基于Transformer的神经运动策略IMPACT，通过大量专家轨迹预训练，并结合师生微调和局部反应式目标提议模块DCP-RMP，提升动态环境适应性。
3. DRP在模拟和真实世界的复杂动态环境中表现出色，成功率超越了传统的和神经方法，展示了其强大的泛化能力和反应式运动规划能力。

## 📝 摘要（中文）

本文提出了一种名为深度反应策略（DRP）的视觉-运动神经运动策略，旨在为各种动态环境中的反应式运动生成提供解决方案，该策略直接作用于点云感官输入。DRP的核心是IMPACT，这是一个基于Transformer的神经运动策略，通过在各种模拟场景中生成的1000万条专家轨迹进行预训练。通过迭代的师生微调，进一步提高了IMPACT在静态障碍物规避方面的性能。此外，在推理时，使用DCP-RMP（一个局部反应式目标提议模块）增强了策略在动态障碍物规避方面的能力。在具有杂乱场景、动态移动障碍物和目标阻塞等挑战性任务中对DRP进行了评估。实验结果表明，DRP具有很强的泛化能力，在模拟和真实环境中，其成功率均优于以往的经典方法和神经方法。

## 🔬 方法详解

**问题定义**：在动态、部分可观测的环境中，机器人操作臂生成无碰撞运动轨迹是一个基本挑战。传统运动规划方法虽然可以计算全局最优轨迹，但需要完整的环境信息，并且计算速度通常较慢，难以适应动态场景。现有的神经运动策略虽然可以直接从原始传感器输入进行闭环操作，但往往难以在复杂或动态环境中泛化。

**核心思路**：论文的核心思路是设计一个能够直接从点云数据进行反应式运动规划的神经策略。通过预训练学习通用的运动模式，然后通过微调和局部反应式模块来增强策略在特定环境下的适应性和动态避障能力。这种方法结合了离线学习的泛化能力和在线反应的灵活性。

**技术框架**：DRP的整体框架包含三个主要部分：1) 基于Transformer的神经运动策略IMPACT，用于学习通用的运动模式；2) 迭代的师生微调，用于提高静态障碍物规避能力；3) 局部反应式目标提议模块DCP-RMP，用于增强动态障碍物规避能力。IMPACT首先在大规模模拟数据上进行预训练，然后通过师生学习进行微调，最后在推理时结合DCP-RMP进行动态避障。

**关键创新**：DRP的关键创新在于将Transformer架构应用于神经运动策略，并结合预训练、微调和局部反应式模块，从而实现了在复杂动态环境中具有强大泛化能力和反应能力的运动规划。与传统的运动规划方法相比，DRP可以直接从原始传感器数据进行规划，无需完整的环境模型。与现有的神经运动策略相比，DRP通过预训练和微调提高了泛化能力，并通过DCP-RMP增强了动态避障能力。

**关键设计**：IMPACT使用Transformer编码器-解码器结构，输入为点云数据，输出为操作臂的运动指令。预训练数据包含1000万条专家轨迹，涵盖各种模拟场景。师生微调采用迭代的方式，学生网络学习教师网络的输出，并不断提高自身的性能。DCP-RMP基于距离一致性惩罚（Distance Consistency Penalty）来生成局部目标，引导操作臂避开动态障碍物。

## 📊 实验亮点

DRP在模拟和真实世界的实验中均取得了显著的成果。在模拟环境中，DRP在各种具有挑战性的任务中，其成功率显著优于传统的RRT-Connect和现有的神经运动策略。在真实世界的实验中，DRP也表现出了强大的泛化能力，成功地完成了复杂的物体操作任务，证明了其在实际应用中的潜力。具体性能数据在论文中有详细展示。

## 🎯 应用场景

DRP在机器人操作臂的运动规划领域具有广泛的应用前景，例如在拥挤的仓库环境中进行拣选和放置操作，在动态的生产线上进行装配任务，以及在家庭服务机器人中进行物体操作。该研究的实际价值在于提高了机器人在复杂动态环境中执行任务的效率和可靠性。未来，DRP可以进一步扩展到其他类型的机器人，例如移动机器人和无人机，从而实现更广泛的应用。

## 📄 摘要（原文）

> Generating collision-free motion in dynamic, partially observable environments is a fundamental challenge for robotic manipulators. Classical motion planners can compute globally optimal trajectories but require full environment knowledge and are typically too slow for dynamic scenes. Neural motion policies offer a promising alternative by operating in closed-loop directly on raw sensory inputs but often struggle to generalize in complex or dynamic settings. We propose Deep Reactive Policy (DRP), a visuo-motor neural motion policy designed for reactive motion generation in diverse dynamic environments, operating directly on point cloud sensory input. At its core is IMPACT, a transformer-based neural motion policy pretrained on 10 million generated expert trajectories across diverse simulation scenarios. We further improve IMPACT's static obstacle avoidance through iterative student-teacher finetuning. We additionally enhance the policy's dynamic obstacle avoidance at inference time using DCP-RMP, a locally reactive goal-proposal module. We evaluate DRP on challenging tasks featuring cluttered scenes, dynamic moving obstacles, and goal obstructions. DRP achieves strong generalization, outperforming prior classical and neural methods in success rate across both simulated and real-world settings. Video results and code available at https://deep-reactive-policy.com

