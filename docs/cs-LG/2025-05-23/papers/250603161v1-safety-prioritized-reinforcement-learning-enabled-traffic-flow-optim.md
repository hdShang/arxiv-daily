---
layout: default
title: Safety-Prioritized, Reinforcement Learning-Enabled Traffic Flow Optimization in a 3D City-Wide Simulation Environment
---

# Safety-Prioritized, Reinforcement Learning-Enabled Traffic Flow Optimization in a 3D City-Wide Simulation Environment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03161" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03161v1</a>
  <a href="https://arxiv.org/pdf/2506.03161.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03161v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03161v1', 'Safety-Prioritized, Reinforcement Learning-Enabled Traffic Flow Optimization in a 3D City-Wide Simulation Environment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mira Nuthakki

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-05-23

**备注**: 18 pages, figures at end, methods at end. Format/order can be changed if necessary

---

## 💡 一句话要点

**提出基于强化学习的安全优先交通流优化方法以应对城市交通问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `交通流优化` `强化学习` `3D模拟` `安全优先` `碰撞模型` `城市交通` `环境影响`

## 📋 核心要点

1. 现有交通管理方法在应对交通拥堵和碰撞方面效果有限，难以适应复杂的城市交通动态。
2. 本文提出了一种基于3D模拟环境和强化学习的交通流优化方法，优先考虑安全性而非效率。
3. 实验结果显示，该方法显著减少了碰撞事件和行驶距离，同时提高了燃油效率和降低了碳排放。

## 📝 摘要（中文）

交通拥堵和碰撞是全球面临的重大经济、环境和社会挑战。传统的交通管理方法在解决这些复杂动态问题上效果有限。为填补现有研究空白，本文开发了三种工具：一个综合的3D城市模拟环境，整合宏观和微观交通动态；一个碰撞模型；以及一个以安全优先的自定义奖励函数为基础的强化学习框架。使用Unity游戏引擎进行直接碰撞建模。基于自定义奖励的强化学习方法——近端策略优化（PPO）模型，显著改善了基线结果，减少了严重碰撞、车辆间碰撞的数量，以及总行驶距离，提升幅度超过基线的三倍。同时，燃油效率提高了39%，碳排放减少了88%。结果证明了将“零事故”安全原则应用于城市3D交通模拟的可行性。

## 🔬 方法详解

**问题定义**：本文旨在解决城市交通中的拥堵和碰撞问题，现有方法在应对这些复杂动态问题时效果不佳，缺乏有效的安全优先策略。

**核心思路**：论文提出通过构建一个3D城市模拟环境，结合强化学习框架和自定义奖励函数，优先考虑交通安全，以优化交通流。这样的设计旨在更好地模拟真实交通情况，提升安全性。

**技术框架**：整体架构包括三个主要模块：3D城市模拟环境、碰撞模型和强化学习框架。模拟环境使用Unity引擎，碰撞模型用于实时碰撞检测，强化学习框架则通过PPO算法进行训练和优化。

**关键创新**：最重要的技术创新在于将安全优先的自定义奖励函数引入强化学习模型，显著改善了交通流优化效果，与传统方法相比，能够更有效地减少碰撞和优化交通流。

**关键设计**：在模型设计中，使用了基于物理的碰撞建模，设置了适应性强的奖励函数，确保模型在训练过程中能够有效学习到安全优先的策略。

## 📊 实验亮点

实验结果表明，基于PPO的强化学习模型在减少严重碰撞数量、车辆间碰撞数量和总行驶距离方面，提升幅度超过基线的三倍。同时，燃油效率提高了39%，碳排放减少了88%，显示出该方法在实际应用中的显著效果。

## 🎯 应用场景

该研究的潜在应用领域包括城市交通管理、智能交通系统和自动驾驶技术。通过优化交通流和减少碰撞，该方法能够提升城市交通的安全性和效率，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Traffic congestion and collisions represent significant economic, environmental, and social challenges worldwide. Traditional traffic management approaches have shown limited success in addressing these complex, dynamic problems. To address the current research gaps, three potential tools are developed: a comprehensive 3D city-wide simulation environment that integrates both macroscopic and microscopic traffic dynamics; a collision model; and a reinforcement learning framework with custom reward functions prioritizing safety over efficiency. Unity game engine-based simulation is used for direct collision modeling. A custom reward enabled reinforcement learning method, proximal policy optimization (PPO) model, yields substantial improvements over baseline results, reducing the number of serious collisions, number of vehicle-vehicle collisions, and total distance travelled by over 3 times the baseline values. The model also improves fuel efficiency by 39% and reduces carbon emissions by 88%. Results establish feasibility for city-wide 3D traffic simulation applications incorporating the vision-zero safety principles of the Department of Transportation, including physics-informed, adaptable, realistic collision modeling, as well as appropriate reward modeling for real-world traffic signal light control towards reducing collisions, optimizing traffic flow and reducing greenhouse emissions.

