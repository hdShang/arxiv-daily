---
layout: default
title: "GRATE: a Graph transformer-based deep Reinforcement learning Approach for Time-efficient autonomous robot Exploration"
---

# GRATE: a Graph transformer-based deep Reinforcement learning Approach for Time-efficient autonomous robot Exploration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12863" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12863v1</a>
  <a href="https://arxiv.org/pdf/2509.12863.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12863v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12863v1', 'GRATE: a Graph transformer-based deep Reinforcement learning Approach for Time-efficient autonomous robot Exploration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haozhan Ni, Jingsong Liang, Chenyu He, Yuhong Cao, Guillaume Sartoretti

**分类**: cs.RO

**发布日期**: 2025-09-16

---

## 💡 一句话要点

**提出基于图Transformer的深度强化学习方法GRATE，提升机器人自主探索的时间效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自主机器人探索` `深度强化学习` `图Transformer` `时间效率` `路径规划`

## 📋 核心要点

1. 现有基于强化学习的自主探索方法在图结构数据推理能力上存在局限性，且通常只关注距离优化，忽略了时间效率。
2. GRATE利用图Transformer捕获信息图的局部结构和全局依赖，增强了模型在整个环境中的推理能力，并使用卡尔曼滤波平滑路径。
3. 实验结果表明，GRATE在探索效率上优于现有方法，距离上提升高达21.5%，时间上提升高达21.3%，并在真实场景中验证了有效性。

## 📝 摘要（中文）

自主机器人探索（ARE）是指机器人自主导航并绘制未知环境地图的过程。最近基于强化学习（RL）的方法通常将ARE建模为在无碰撞信息图上定义的序列决策问题。然而，这些方法在图结构化数据上的推理能力有限。此外，由于对机器人运动的考虑不足，由此产生的RL策略通常被优化为最小化行驶距离，而忽略了时间效率。为了克服这些限制，我们提出GRATE，一种基于深度强化学习（DRL）的方法，它利用图Transformer来有效地捕获信息图的局部结构模式和全局上下文依赖关系，从而增强模型在整个环境中的推理能力。此外，我们部署卡尔曼滤波器来平滑航路点输出，确保生成的路径在运动学上是机器人可以遵循的。实验结果表明，在各种模拟基准中，我们的方法比最先进的传统和基于学习的基线表现出更好的探索效率（在完成探索的距离上高达21.5%，时间上高达21.3%）。我们还在真实场景中验证了我们的规划器。

## 🔬 方法详解

**问题定义**：自主机器人探索（ARE）旨在使机器人在未知环境中自主导航并构建地图。现有基于强化学习的方法通常将此问题建模为在信息图上的序列决策过程，但这些方法在处理图结构数据时推理能力不足，并且往往只关注路径距离的优化，忽略了时间效率，导致探索速度慢。

**核心思路**：GRATE的核心思路是利用图Transformer来增强模型对环境的理解和推理能力，同时考虑机器人运动学约束以提高时间效率。图Transformer能够有效捕获信息图的局部结构和全局依赖关系，从而做出更明智的探索决策。卡尔曼滤波器的引入则保证了生成路径的平滑性和可行性。

**技术框架**：GRATE的整体框架包括以下几个主要模块：1) 信息图构建模块，用于将环境信息表示为图结构；2) 基于图Transformer的策略网络，用于学习探索策略；3) 卡尔曼滤波器，用于平滑路径；4) 强化学习训练循环，用于优化策略网络。机器人根据策略网络输出的动作选择下一个探索目标，并使用卡尔曼滤波平滑路径，最终完成环境探索。

**关键创新**：GRATE的关键创新在于将图Transformer引入到自主探索任务中，并结合卡尔曼滤波器进行路径平滑。与传统的基于图的强化学习方法相比，图Transformer能够更好地捕捉图的全局信息，从而提高探索效率。卡尔曼滤波器的使用则保证了生成路径的运动学可行性，进一步提升了时间效率。

**关键设计**：GRATE的关键设计包括：1) 图Transformer的网络结构，包括层数、注意力头数等；2) 强化学习的奖励函数，需要平衡探索效率和安全性；3) 卡尔曼滤波器的参数设置，需要根据机器人的运动学特性进行调整。具体的损失函数和网络结构细节在论文中应该有更详细的描述（未知）。

## 📊 实验亮点

实验结果表明，GRATE在多种模拟环境中均优于现有方法，在探索距离上提升高达21.5%，在探索时间上提升高达21.3%。此外，GRATE还在真实场景中进行了验证，证明了其在实际应用中的可行性。这些结果表明GRATE是一种高效且实用的自主探索方法。

## 🎯 应用场景

GRATE具有广泛的应用前景，可用于仓库巡检、灾难救援、自动驾驶等领域。通过提高机器人自主探索的效率和安全性，GRATE可以降低人工干预的需求，提升工作效率，并在复杂环境中实现更可靠的自主导航。

## 📄 摘要（原文）

> Autonomous robot exploration (ARE) is the process of a robot autonomously navigating and mapping an unknown environment. Recent Reinforcement Learning (RL)-based approaches typically formulate ARE as a sequential decision-making problem defined on a collision-free informative graph. However, these methods often demonstrate limited reasoning ability over graph-structured data. Moreover, due to the insufficient consideration of robot motion, the resulting RL policies are generally optimized to minimize travel distance, while neglecting time efficiency. To overcome these limitations, we propose GRATE, a Deep Reinforcement Learning (DRL)-based approach that leverages a Graph Transformer to effectively capture both local structure patterns and global contextual dependencies of the informative graph, thereby enhancing the model's reasoning capability across the entire environment. In addition, we deploy a Kalman filter to smooth the waypoint outputs, ensuring that the resulting path is kinodynamically feasible for the robot to follow. Experimental results demonstrate that our method exhibits better exploration efficiency (up to 21.5% in distance and 21.3% in time to complete exploration) than state-of-the-art conventional and learning-based baselines in various simulation benchmarks. We also validate our planner in real-world scenarios.

