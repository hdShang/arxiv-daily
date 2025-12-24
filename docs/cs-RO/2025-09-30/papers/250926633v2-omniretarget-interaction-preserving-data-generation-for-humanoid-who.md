---
layout: default
title: "OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction"
---

# OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26633" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26633v2</a>
  <a href="https://arxiv.org/pdf/2509.26633.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26633v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26633v2', 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lujie Yang, Xiaoyu Huang, Zhen Wu, Angjoo Kanazawa, Pieter Abbeel, Carmelo Sferrazza, C. Karen Liu, Rocky Duan, Guanya Shi

**分类**: cs.RO, cs.AI, cs.LG, eess.SY

**发布日期**: 2025-09-30 (更新: 2025-10-08)

**备注**: Project website: https://omniretarget.github.io

---

## 💡 一句话要点

**OmniRetarget：交互保持的人形机器人全身运动操作与场景交互数据生成引擎**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `人形机器人` `运动重定向` `交互保持` `数据生成` `强化学习`

## 📋 核心要点

1. 现有动作重定向方法难以弥合人与机器人之间的差异，导致不真实的运动伪影，且忽略了人与环境的交互。
2. OmniRetarget基于交互网格建模智能体与环境的交互关系，通过优化拉普拉斯形变和施加运动学约束生成可行轨迹。
3. 实验表明，OmniRetarget生成的数据能够训练人形机器人执行长时程的跑酷和运动操作技能，且训练过程简单高效。

## 📝 摘要（中文）

本文提出OmniRetarget，一个交互保持的数据生成引擎，用于解决人形机器人复杂技能学习中，人类动作重定向到机器人时遇到的问题。现有方法难以处理人与机器人之间的巨大差异，导致足部滑动和穿透等不真实的伪影，并且忽略了人与物体及环境之间丰富的交互。OmniRetarget基于交互网格，显式地建模并保持了智能体、地形和被操作物体之间关键的空间和接触关系。通过最小化人类和机器人网格之间的拉普拉斯形变，并强制执行运动学约束，OmniRetarget生成运动学上可行的轨迹。此外，保持任务相关的交互能够实现高效的数据增强，从单个演示扩展到不同的机器人形态、地形和物体配置。实验表明，OmniRetarget生成的轨迹在运动学约束满足和接触保持方面优于现有方法，并成功训练了Unitree G1人形机器人在长时程（最长30秒）的跑酷和运动操作技能，仅使用5个奖励项和简单的领域随机化，无需任何学习课程。

## 🔬 方法详解

**问题定义**：现有的人形机器人技能学习方法依赖于将人类动作重定向到机器人作为运动学参考。然而，由于人类和机器人之间存在显著的形态差异，现有的重定向方法常常产生不真实的运动伪影，例如足部滑动和穿透。更重要的是，这些方法通常忽略了人类与物体和环境之间丰富的交互，而这些交互对于表达性的运动和运动操作至关重要。

**核心思路**：OmniRetarget的核心思路是通过显式地建模和保持智能体、地形和被操作物体之间的关键空间和接触关系来解决上述问题。它使用一个交互网格来表示这些关系，并通过优化人类和机器人网格之间的形变，同时强制执行运动学约束，来生成运动学上可行的轨迹。

**技术框架**：OmniRetarget的整体框架包括以下几个主要步骤：1) 使用交互网格显式建模人与环境的交互关系；2) 将人类动作重定向到机器人，同时最小化人类和机器人网格之间的拉普拉斯形变；3) 强制执行运动学约束，确保生成的轨迹在运动学上可行；4) 利用保持的交互关系进行数据增强，生成适用于不同机器人形态、地形和物体配置的数据。

**关键创新**：OmniRetarget的关键创新在于引入了交互网格的概念，并将其用于显式地建模和保持智能体与环境之间的交互关系。这与现有方法忽略交互关系的做法形成了鲜明对比。通过保持这些交互关系，OmniRetarget能够生成更真实、更可用的机器人运动轨迹。

**关键设计**：OmniRetarget的关键设计包括：1) 使用拉普拉斯形变来最小化人类和机器人网格之间的差异，同时保持网格的局部结构；2) 使用运动学约束来确保生成的轨迹在运动学上可行，例如关节角度限制和自碰撞避免；3) 设计损失函数来鼓励保持交互关系，例如接触点的位置和方向。

## 📊 实验亮点

OmniRetarget在OMOMO、LAFAN1和自研MoCap数据集上进行了评估，生成了超过8小时的轨迹数据。实验结果表明，OmniRetarget在运动学约束满足和接触保持方面优于现有方法。使用OmniRetarget生成的数据，成功训练了Unitree G1人形机器人在长时程（最长30秒）的跑酷和运动操作技能，且仅使用了5个奖励项和简单的领域随机化。

## 🎯 应用场景

OmniRetarget具有广泛的应用前景，可用于生成高质量的机器人训练数据，从而提升机器人在复杂环境中的运动和操作能力。例如，可应用于人形机器人跑酷、物体操作、搜救等任务，也可用于虚拟现实和游戏等领域，生成更逼真的人体动画。该研究有助于推动人形机器人技术的发展，使其能够更好地适应和融入人类社会。

## 📄 摘要（原文）

> A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration. More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. We comprehensively evaluate OmniRetarget by retargeting motions from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

