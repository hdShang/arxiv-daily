---
layout: default
title: "LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry"
---

# LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19629" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19629v1</a>
  <a href="https://arxiv.org/pdf/2512.19629.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19629v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19629v1', 'LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaqi Peng, Wenzhe Cai, Yuqiang Yang, Tai Wang, Yuan Shen, Jiangmiao Pang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-22

**备注**: Project page:https://steinate.github.io/logoplanner.github.io/

**🔗 代码/项目**: [PROJECT_PAGE](https://steinate.github.io/logoplanner.github.io/)

---

## 💡 一句话要点

**LoGoPlanner：基于度量视觉几何的定位引导端到端导航策略**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `端到端导航` `视觉几何` `定位` `环境感知` `机器人` `轨迹规划` `度量学习` `深度学习`

## 📋 核心要点

1. 传统导航方法依赖模块化pipeline，易受延迟和模块间误差累积的影响，限制了整体性能。
2. LoGoPlanner通过端到端学习，结合视觉几何信息进行定位和环境感知，实现更鲁棒的导航。
3. 实验表明，LoGoPlanner在仿真和真实环境中均优于传统方法，并在不同机器人和环境间具有良好的泛化性。

## 📝 摘要（中文）

本文提出LoGoPlanner，一个定位引导的端到端导航框架，旨在解决移动机器人在非结构化环境中轨迹规划的挑战。传统模块化方法存在延迟和感知、定位、建图和规划模块之间的误差累积问题。现有的端到端学习方法依赖于精确的传感器外参标定进行自定位，限制了其在不同机器人和环境中的泛化能力。LoGoPlanner通过以下方式解决这些限制：（1）微调长时程视觉几何骨干网络，以绝对度量尺度进行预测，从而提供隐式的状态估计以实现精确定位；（2）从历史观测中重建周围场景几何，为可靠的避障提供密集的、细粒度的环境感知；（3）策略以辅助任务引导的隐式几何为条件，从而减少误差传播。在仿真和真实世界环境中的评估表明，LoGoPlanner的完全端到端设计减少了累积误差，而度量感知几何记忆增强了规划一致性和避障能力，与oracle定位基线相比，性能提升超过27.3％，并在不同的机器人和环境中表现出强大的泛化能力。

## 🔬 方法详解

**问题定义**：现有移动机器人的轨迹规划方法，特别是端到端学习方法，依赖于独立的定位模块，而这些模块又依赖于精确的传感器外参标定。这限制了算法在不同机器人平台和环境中的泛化能力。此外，传统模块化pipeline存在延迟和误差累积问题，影响整体导航性能。

**核心思路**：LoGoPlanner的核心思想是将定位融入到端到端的导航策略中，通过学习视觉几何信息来隐式地进行状态估计，从而避免对独立定位模块的依赖。同时，利用历史观测重建环境几何信息，为导航策略提供更丰富的环境感知，增强避障能力。

**技术框架**：LoGoPlanner是一个端到端的导航框架，主要包含以下几个模块：(1) 长时程视觉几何骨干网络：用于提取视觉特征并预测场景的几何信息，通过微调使其具备绝对度量尺度感知能力。(2) 几何记忆模块：利用历史观测重建周围场景的几何信息，提供密集的、细粒度的环境感知。(3) 导航策略模块：以视觉特征和几何记忆作为输入，输出控制信号或轨迹。整个框架通过端到端的方式进行训练，实现定位、环境感知和导航的联合优化。

**关键创新**：LoGoPlanner的关键创新在于将定位融入到端到端的导航策略中，通过学习视觉几何信息来隐式地进行状态估计，避免了对独立定位模块的依赖。此外，利用历史观测重建环境几何信息，为导航策略提供更丰富的环境感知。这种端到端的设计减少了误差传播，提高了导航的鲁棒性和泛化能力。

**关键设计**：LoGoPlanner的关键设计包括：(1) 使用长时程视觉几何骨干网络，例如Transformer或LSTM，来提取视觉特征并预测场景的几何信息。(2) 设计合适的损失函数，例如度量学习损失或几何重建损失，来训练骨干网络使其具备绝对度量尺度感知能力。(3) 使用几何记忆模块，例如占用栅格地图或点云地图，来存储和更新环境几何信息。(4) 设计合适的导航策略网络，例如强化学习或模仿学习，以视觉特征和几何记忆作为输入，输出控制信号或轨迹。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19629v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19629v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19629v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

LoGoPlanner在仿真和真实世界环境中进行了评估，实验结果表明，与依赖oracle定位的基线方法相比，LoGoPlanner的性能提升超过27.3％。此外，LoGoPlanner在不同的机器人和环境中表现出强大的泛化能力，证明了其端到端设计和度量感知几何记忆的有效性。

## 🎯 应用场景

LoGoPlanner适用于各种移动机器人导航场景，尤其是在非结构化和动态环境中，如家庭服务机器人、仓储物流机器人、自动驾驶车辆等。该方法通过端到端学习和视觉几何信息，提高了导航的鲁棒性和泛化能力，降低了对传感器标定的依赖，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Trajectory planning in unstructured environments is a fundamental and challenging capability for mobile robots. Traditional modular pipelines suffer from latency and cascading errors across perception, localization, mapping, and planning modules. Recent end-to-end learning methods map raw visual observations directly to control signals or trajectories, promising greater performance and efficiency in open-world settings. However, most prior end-to-end approaches still rely on separate localization modules that depend on accurate sensor extrinsic calibration for self-state estimation, thereby limiting generalization across embodiments and environments. We introduce LoGoPlanner, a localization-grounded, end-to-end navigation framework that addresses these limitations by: (1) finetuning a long-horizon visual-geometry backbone to ground predictions with absolute metric scale, thereby providing implicit state estimation for accurate localization; (2) reconstructing surrounding scene geometry from historical observations to supply dense, fine-grained environmental awareness for reliable obstacle avoidance; and (3) conditioning the policy on implicit geometry bootstrapped by the aforementioned auxiliary tasks, thereby reducing error propagation.We evaluate LoGoPlanner in both simulation and real-world settings, where its fully end-to-end design reduces cumulative error while metric-aware geometry memory enhances planning consistency and obstacle avoidance, leading to more than a 27.3\% improvement over oracle-localization baselines and strong generalization across embodiments and environments. The code and models have been made publicly available on the \href{https://steinate.github.io/logoplanner.github.io/}{project page}.

