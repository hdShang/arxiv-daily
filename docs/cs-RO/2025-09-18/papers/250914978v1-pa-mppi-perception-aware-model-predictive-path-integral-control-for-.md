---
layout: default
title: "PA-MPPI: Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments"
---

# PA-MPPI: Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14978" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14978v1</a>
  <a href="https://arxiv.org/pdf/2509.14978.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14978v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14978v1', 'PA-MPPI: Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Zhai, Rudolf Reiter, Davide Scaramuzza

**分类**: cs.RO

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**提出感知驱动的MPPI算法，提升四旋翼无人机在未知环境中的导航能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `四旋翼无人机` `未知环境导航` `模型预测控制` `路径积分` `感知驱动` `运动规划` `自主探索`

## 📋 核心要点

1. 传统MPPI在未知环境中受阻时，缺乏探索未知区域的能力，限制了其导航性能。
2. PA-MPPI通过在线调整轨迹，使其能够根据感知目标进行自适应调整，从而实现对未知区域的探索。
3. 实验结果表明，PA-MPPI在复杂环境中显著优于传统MPPI，并可作为导航基础模型的安全策略。

## 📝 摘要（中文）

本文提出了一种感知驱动的模型预测路径积分控制（PA-MPPI）方法，用于解决四旋翼无人机在未知环境中导航的问题。该问题面临三大挑战：障碍物导致的非凸自由空间、四旋翼特有的动力学和目标，以及探索未知区域以寻找通往目标的路径的需求。PA-MPPI通过引入感知代价，偏向于能够感知未知区域的轨迹，从而扩展已知的可通行空间，提高找到通往目标的替代路径的可能性。硬件实验表明，PA-MPPI在具有挑战性的环境中，性能比最先进的MPPI算法提升高达100%，并且可以作为导航基础模型的安全且鲁棒的动作策略。

## 🔬 方法详解

**问题定义**：四旋翼无人机在未知环境中导航，需要解决由障碍物引起的非凸优化问题，同时考虑无人机自身的动力学约束和能量消耗等因素。现有MPPI方法虽然能处理非凸空间和动力学约束，但在遇到大型障碍物遮挡目标时，无法有效探索未知区域，导致导航失败。

**核心思路**：PA-MPPI的核心在于引入“感知驱动”的概念，即在MPPI的代价函数中加入与感知相关的项。当目标被遮挡时，该项会引导无人机探索能够提供更多环境信息的区域，从而扩展地图，寻找新的可行路径。

**技术框架**：PA-MPPI的整体框架仍然基于MPPI，但增加了感知模块。该模块负责评估不同轨迹对未知区域的探索能力，并将其转化为代价函数中的一项。具体流程为：首先，利用传感器获取环境信息并构建地图；然后，基于当前地图和目标位置，利用MPPI生成候选轨迹；接着，感知模块评估每条轨迹对未知区域的探索潜力，并计算感知代价；最后，将感知代价加入到MPPI的总体代价函数中，选择最优轨迹执行。

**关键创新**：PA-MPPI最重要的创新在于将感知信息融入到运动规划中，使其能够主动探索未知环境。与传统的MPPI相比，PA-MPPI不再仅仅依赖于已知的地图信息，而是能够根据感知目标动态调整轨迹，从而更好地适应未知环境。

**关键设计**：感知代价的设计是PA-MPPI的关键。论文中感知代价的具体形式未知，但其核心思想是鼓励无人机探索那些能够提供更多未知区域信息的轨迹。这可能涉及到计算轨迹附近未知区域的面积、信息增益等指标，并将这些指标转化为代价函数中的一项。此外，感知模块的效率也很重要，需要保证PA-MPPI能够以较高的频率运行（论文中为50Hz）。

## 📊 实验亮点

硬件实验表明，PA-MPPI在具有挑战性的环境中，性能比最先进的MPPI算法提升高达100%。在这些环境中，传统MPPI由于无法探索未知区域而导航失败，而PA-MPPI能够通过感知驱动的轨迹规划找到通往目标的路径。此外，PA-MPPI能够以50Hz的频率运行，保证了其在实际应用中的实时性。

## 🎯 应用场景

PA-MPPI在搜索救援、灾后评估、未知环境探索等领域具有广泛的应用前景。它可以使无人机在复杂、未知的环境中自主导航，完成各种任务。此外，PA-MPPI还可以作为导航基础模型的安全策略，提高其在实际应用中的鲁棒性和可靠性，使其能够安全地执行由基础模型生成的导航指令。

## 📄 摘要（原文）

> Quadrotor navigation in unknown environments is critical for practical missions such as search-and-rescue. Solving it requires addressing three key challenges: the non-convexity of free space due to obstacles, quadrotor-specific dynamics and objectives, and the need for exploration of unknown regions to find a path to the goal. Recently, the Model Predictive Path Integral (MPPI) method has emerged as a promising solution that solves the first two challenges. By leveraging sampling-based optimization, it can effectively handle non-convex free space while directly optimizing over the full quadrotor dynamics, enabling the inclusion of quadrotor-specific costs such as energy consumption. However, its performance in unknown environments is limited, as it lacks the ability to explore unknown regions when blocked by large obstacles. To solve this issue, we introduce Perception-Aware MPPI (PA-MPPI). Here, perception-awareness is defined as adapting the trajectory online based on perception objectives. Specifically, when the goal is occluded, PA-MPPI's perception cost biases trajectories that can perceive unknown regions. This expands the mapped traversable space and increases the likelihood of finding alternative paths to the goal. Through hardware experiments, we demonstrate that PA-MPPI, running at 50 Hz with our efficient perception and mapping module, performs up to 100% better than the baseline in our challenging settings where the state-of-the-art MPPI fails. In addition, we demonstrate that PA-MPPI can be used as a safe and robust action policy for navigation foundation models, which often provide goal poses that are not directly reachable.

