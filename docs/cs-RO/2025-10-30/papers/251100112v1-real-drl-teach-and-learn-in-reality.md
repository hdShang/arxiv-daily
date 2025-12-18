---
layout: default
title: Real-DRL: Teach and Learn in Reality
---

# Real-DRL: Teach and Learn in Reality

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00112" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00112v1</a>
  <a href="https://arxiv.org/pdf/2511.00112.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00112v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.00112v1', 'Real-DRL: Teach and Learn in Reality')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanbing Mao, Yihao Cai, Lui Sha

**分类**: cs.RO, cs.AI

**发布日期**: 2025-10-30

**备注**: 37 pages

---

## 💡 一句话要点

**Real-DRL框架：在真实环境中安全地训练深度强化学习智能体**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `安全自主系统` `Sim2Real` `教学式学习` `物理模型` `四足机器人` `实时控制`

## 📋 核心要点

1. 现有DRL方法在安全攸关系统中应用面临Sim2Real差距和未知风险，难以保证安全。
2. Real-DRL框架通过引入PHY-Teacher进行安全保障，并采用教学式学习范式指导DRL-Student学习。
3. 实验表明，Real-DRL在真实四足机器人和仿真环境中均表现出良好的安全性和性能。

## 📝 摘要（中文）

本文提出了一种名为Real-DRL的框架，用于安全攸关的自主系统，该框架能够在真实环境中运行时学习深度强化学习（DRL）智能体，从而开发安全且高性能的动作策略，同时优先考虑安全性。Real-DRL由三个交互组件组成：DRL-Student、PHY-Teacher和Trigger。DRL-Student是一个DRL智能体，它在双重自学习和教学式学习范式以及实时安全信息批采样方面进行创新。另一方面，PHY-Teacher是一个基于物理模型的动作策略设计，它只关注安全关键功能。PHY-Teacher的新颖之处在于其对两个关键任务的实时补丁：i) 促进DRL-Student的教学式学习范式，以及ii) 支持真实系统的安全。Trigger管理DRL-Student和PHY-Teacher之间的交互。在三个交互组件的支持下，Real-DRL可以有效地解决由未知未知和Sim2Real差距引起的安全挑战。此外，Real-DRL显著的特点包括i) 确保安全，ii) 自动分层学习（即安全优先学习，然后是高性能学习），以及iii) 安全信息批采样，以解决由极端情况引起的学习经验不平衡。对真实四足机器人、NVIDIA Isaac Gym中的四足机器人和倒立摆系统的实验，以及比较和消融研究，证明了Real-DRL的有效性和独特功能。

## 🔬 方法详解

**问题定义**：现有深度强化学习方法在应用于真实物理系统，特别是安全攸关的自主系统时，面临着诸多挑战。Sim2Real差距导致在仿真环境中训练的策略难以直接迁移到真实世界。此外，真实世界中存在许多未知的、难以建模的风险，使得传统的DRL方法难以保证系统的安全性。现有方法通常依赖于大量的试错，这在安全攸关的系统中是不可接受的。

**核心思路**：Real-DRL的核心思路是引入一个基于物理模型的“教师”（PHY-Teacher），该教师专门负责提供安全保障。DRL智能体（DRL-Student）通过与PHY-Teacher的交互进行学习，从而在保证安全的前提下，逐步提升性能。这种“教学式学习”范式能够有效地利用先验知识，加速学习过程，并降低探索风险。

**技术框架**：Real-DRL框架包含三个主要组件：DRL-Student、PHY-Teacher和Trigger。DRL-Student是一个标准的DRL智能体，负责学习高性能的动作策略。PHY-Teacher是一个基于物理模型的控制器，其主要目标是保证系统的安全性。Trigger负责管理DRL-Student和PHY-Teacher之间的交互，决定何时使用PHY-Teacher的策略进行干预，以避免潜在的安全风险。整体流程是DRL-Student在环境中探索，Trigger根据当前状态判断是否需要PHY-Teacher介入，PHY-Teacher执行安全策略，DRL-Student根据PHY-Teacher的反馈进行学习。

**关键创新**：Real-DRL的关键创新在于引入了PHY-Teacher作为安全保障机制，并采用教学式学习范式。与传统的DRL方法相比，Real-DRL能够更好地处理Sim2Real差距和未知风险，从而在真实物理系统中实现安全可靠的自主控制。此外，Real-DRL还采用了安全信息批采样，以解决由极端情况引起的学习经验不平衡问题。

**关键设计**：PHY-Teacher的设计基于物理模型，通常采用PID控制或模型预测控制等方法，以保证系统的稳定性。Trigger的设计需要权衡安全性和性能，通常采用基于规则或基于学习的方法。DRL-Student可以采用各种DRL算法，如PPO、SAC等。安全信息批采样通过对高风险状态的经验进行加权，从而提高智能体对安全问题的敏感性。

## 📊 实验亮点

实验结果表明，Real-DRL在真实四足机器人和NVIDIA Isaac Gym仿真环境中均表现出良好的性能。与传统的DRL方法相比，Real-DRL能够显著提高系统的安全性，并实现更高的性能。消融研究验证了PHY-Teacher和安全信息批采样的有效性。

## 🎯 应用场景

Real-DRL框架可应用于各种安全攸关的自主系统，如自动驾驶汽车、无人机、机器人等。该框架能够有效地解决Sim2Real差距和未知风险，从而在真实环境中实现安全可靠的自主控制。未来，Real-DRL有望在工业自动化、智能交通、医疗健康等领域发挥重要作用。

## 📄 摘要（原文）

> This paper introduces the Real-DRL framework for safety-critical autonomous systems, enabling runtime learning of a deep reinforcement learning (DRL) agent to develop safe and high-performance action policies in real plants (i.e., real physical systems to be controlled), while prioritizing safety! The Real-DRL consists of three interactive components: a DRL-Student, a PHY-Teacher, and a Trigger. The DRL-Student is a DRL agent that innovates in the dual self-learning and teaching-to-learn paradigm and the real-time safety-informed batch sampling. On the other hand, PHY-Teacher is a physics-model-based design of action policies that focuses solely on safety-critical functions. PHY-Teacher is novel in its real-time patch for two key missions: i) fostering the teaching-to-learn paradigm for DRL-Student and ii) backing up the safety of real plants. The Trigger manages the interaction between the DRL-Student and the PHY-Teacher. Powered by the three interactive components, the Real-DRL can effectively address safety challenges that arise from the unknown unknowns and the Sim2Real gap. Additionally, Real-DRL notably features i) assured safety, ii) automatic hierarchy learning (i.e., safety-first learning and then high-performance learning), and iii) safety-informed batch sampling to address the learning experience imbalance caused by corner cases. Experiments with a real quadruped robot, a quadruped robot in NVIDIA Isaac Gym, and a cart-pole system, along with comparisons and ablation studies, demonstrate the Real-DRL's effectiveness and unique features.

