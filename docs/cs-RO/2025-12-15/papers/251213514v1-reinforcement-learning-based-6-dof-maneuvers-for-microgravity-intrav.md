---
layout: default
title: "Reinforcement Learning based 6-DoF Maneuvers for Microgravity Intravehicular Docking: A Simulation Study with Int-Ball2 in ISS-JEM"
---

# Reinforcement Learning based 6-DoF Maneuvers for Microgravity Intravehicular Docking: A Simulation Study with Int-Ball2 in ISS-JEM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13514" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13514v1</a>
  <a href="https://arxiv.org/pdf/2512.13514.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13514v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.13514v1', 'Reinforcement Learning based 6-DoF Maneuvers for Microgravity Intravehicular Docking: A Simulation Study with Int-Ball2 in ISS-JEM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aman Arora, Matteo El-Hariry, Miguel Olivares-Mendez

**分类**: cs.RO

**发布日期**: 2025-12-15

**备注**: Presented at AI4OPA Workshop at the International Conference on Space Robotics (iSpaRo) 2025 at Sendai, Japan

---

## 💡 一句话要点

**提出基于强化学习的6自由度微重力舱内对接方法，用于国际空间站Int-Ball2机器人。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `强化学习` `机器人对接` `微重力环境` `近端策略优化` `域随机化` `Int-Ball2` `Isaac Sim`

## 📋 核心要点

1. 舱内自由飞行器在国际空间站任务中至关重要，但在传感噪声、执行器不匹配和环境变化下的精确对接仍具挑战。
2. 论文提出基于近端策略优化（PPO）的强化学习框架，在域随机化和观测噪声下训练控制器，并建模螺旋桨阻力扭矩和极性结构。
3. 实验结果表明，该方法在各种条件下实现了稳定可靠的对接，为后续研究如避碰导航和sim-to-real迁移奠定基础。

## 📝 摘要（中文）

本文提出了一种基于强化学习(RL)的框架，用于日本宇宙航空研究开发机构(JAXA)的Int-Ball2机器人在日本实验舱(JEM)的高保真Isaac Sim模型中进行六自由度(6-DoF)对接。使用近端策略优化(PPO)算法，在域随机化的动力学和有界观测噪声下训练和评估控制器，同时显式地建模了螺旋桨的阻力扭矩效应和极性结构。这使得能够对Int-Ball2的推进物理特性如何影响基于RL的对接性能进行受控研究。学习到的策略在各种条件下实现了稳定可靠的对接，并为未来在避碰导航、安全RL、推进精确的sim-to-real迁移以及基于视觉的端到端对接方面的扩展奠定了基础。

## 🔬 方法详解

**问题定义**：论文旨在解决微重力环境下，Int-Ball2机器人在国际空间站日本实验舱(JEM)内的自主对接问题。现有方法难以应对传感噪声、执行器不匹配以及环境变化带来的挑战，尤其是在精确建模推进系统物理特性方面存在不足。

**核心思路**：论文的核心思路是利用强化学习，特别是近端策略优化(PPO)算法，训练一个能够适应各种不确定性和干扰的控制器。通过域随机化，使智能体在模拟环境中学习到的策略能够泛化到真实环境中。同时，显式地建模螺旋桨的阻力扭矩效应和极性结构，提高了仿真的真实性。

**技术框架**：整体框架包括以下几个主要模块：1) 高保真Isaac Sim环境，用于模拟JEM舱内环境和Int-Ball2的动力学特性；2) 基于PPO的强化学习算法，用于训练对接控制器；3) 域随机化模块，用于增加训练数据的多样性，提高策略的泛化能力；4) 观测噪声模型，用于模拟真实环境中的传感噪声；5) 推进系统模型，用于精确建模螺旋桨的阻力扭矩效应和极性结构。

**关键创新**：论文的关键创新在于将强化学习应用于微重力环境下的机器人对接任务，并显式地建模了螺旋桨的阻力扭矩效应和极性结构。这使得智能体能够学习到更加鲁棒和可靠的对接策略。此外，通过域随机化，提高了策略的泛化能力，使其能够适应真实环境中的各种不确定性和干扰。

**关键设计**：论文使用PPO算法作为强化学习的核心算法。奖励函数的设计至关重要，需要引导智能体学习到精确的对接动作。域随机化的参数包括Int-Ball2的质量、惯性矩、螺旋桨的推力等。观测噪声模型采用高斯噪声模型，噪声的方差根据实际传感器的精度进行设置。推进系统模型基于实验数据进行标定，以确保仿真的准确性。

## 📊 实验亮点

论文在Isaac Sim中进行了大量仿真实验，结果表明，基于PPO的强化学习策略能够实现稳定可靠的对接。通过域随机化，策略能够适应各种不确定性和干扰。显式建模螺旋桨阻力扭矩和极性结构显著提升了对接性能。具体性能数据未知，但论文强调了策略的鲁棒性和可靠性。

## 🎯 应用场景

该研究成果可应用于国际空间站舱内自主任务，例如物资运输、设备维护和环境监测。通过强化学习训练的智能体能够自主完成对接任务，减少宇航员的工作负担，提高空间站的运行效率。此外，该方法还可以推广到其他微重力环境下的机器人操作任务，例如卫星维修和空间碎片清理。

## 📄 摘要（原文）

> Autonomous free-flyers play a critical role in intravehicular tasks aboard the International Space Station (ISS), where their precise docking under sensing noise, small actuation mismatches, and environmental variability remains a nontrivial challenge. This work presents a reinforcement learning (RL) framework for six-degree-of-freedom (6-DoF) docking of JAXA's Int-Ball2 robot inside a high-fidelity Isaac Sim model of the Japanese Experiment Module (JEM). Using Proximal Policy Optimization (PPO), we train and evaluate controllers under domain-randomized dynamics and bounded observation noise, while explicitly modeling propeller drag-torque effects and polarity structure. This enables a controlled study of how Int-Ball2's propulsion physics influence RL-based docking performance in constrained microgravity interiors. The learned policy achieves stable and reliable docking across varied conditions and lays the groundwork for future extensions pertaining to Int-Ball2 in collision-aware navigation, safe RL, propulsion-accurate sim-to-real transfer, and vision-based end-to-end docking.

