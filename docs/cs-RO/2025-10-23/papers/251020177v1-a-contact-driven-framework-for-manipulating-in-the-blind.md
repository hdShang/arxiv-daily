---
layout: default
title: A Contact-Driven Framework for Manipulating in the Blind
---

# A Contact-Driven Framework for Manipulating in the Blind

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.20177" target="_blank" class="toolbar-btn">arXiv: 2510.20177v1</a>
    <a href="https://arxiv.org/pdf/2510.20177.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20177v1" 
            onclick="toggleFavorite(this, '2510.20177v1', 'A Contact-Driven Framework for Manipulating in the Blind')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Muhammad Suhail Saleem, Lai Yuan, Maxim Likhachev

**分类**: cs.RO

**发布日期**: 2025-10-23

---

## 💡 一句话要点

**提出基于接触驱动的框架，解决机器人盲操作中的物体操作问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人操作` `盲操作` `接触反馈` `结构先验` `占据估计`

## 📋 核心要点

1. 现有方法在视觉信息不足的环境中，机器人难以区分自由空间和占据空间，从而难以进行有效操作。
2. 该论文提出了一种基于接触反馈和结构先验的框架，使机器人能够在未知环境中进行盲操作。
3. 实验结果表明，该框架能够可靠地解决家庭任务，并且任务完成时间相比基线方法减少了2倍。

## 📝 摘要（中文）

本文提出了一种理论完备且经验有效的盲操作框架，该框架集成了接触反馈和结构先验，以实现在未知环境中稳健操作。该框架包含三个紧密耦合的模块：（i）接触检测和定位模块，利用关节扭矩传感和接触粒子滤波器来检测和定位接触；（ii）占据估计模块，利用接触观测历史构建工作空间的局部占据地图，并通过学习到的预测器将其外推到未探索区域；（iii）规划模块，考虑到接触定位估计和占据预测可能存在噪声，计算避免碰撞并高效完成任务的路径，同时不排除可行的解决方案。在UR10e机械臂上，通过模拟和真实世界的实验，在两个家庭任务中评估了该系统——（i）操作厨房水槽下被管道包围的阀门，以及（ii）从杂乱的架子上检索目标物体。结果表明，该框架能够可靠地解决这些任务，与基线相比，任务完成时间最多可减少2倍，消融实验证实了每个模块的贡献。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人如何在视觉信息不足（例如，杂乱、遮挡或光线不足的环境）的情况下进行物体操作的问题。现有方法在这些情况下表现不佳，因为它们严重依赖视觉信息来感知环境和规划运动。因此，机器人需要像人类一样，依靠接触反馈来区分自由空间和占据空间，并绕过障碍物。

**核心思路**：论文的核心思路是将接触反馈与结构先验知识相结合，以提高机器人在未知环境中的操作能力。通过接触反馈，机器人可以感知周围环境的几何形状和障碍物。结构先验知识可以帮助机器人预测未见区域的结构，从而避免不必要的碰撞。

**技术框架**：该框架包含三个主要模块：（1）接触检测和定位模块：使用关节扭矩传感和接触粒子滤波器来检测和定位接触点。（2）占据估计模块：利用接触观测的历史信息构建工作空间的局部占据地图，并使用学习到的预测器将该地图外推到未探索的区域。（3）规划模块：考虑到接触定位估计和占据预测可能存在噪声，计算避免碰撞并高效完成任务的路径，同时不排除可行的解决方案。

**关键创新**：该论文的关键创新在于将接触反馈、结构先验知识和概率规划相结合，从而实现鲁棒的盲操作。与传统的基于视觉的机器人操作方法相比，该框架能够在视觉信息不足的环境中实现更可靠的操作。此外，该框架还能够利用结构先验知识来预测未见区域的结构，从而提高操作效率。

**关键设计**：接触检测和定位模块使用接触粒子滤波器来估计接触点的位置。占据估计模块使用高斯过程回归来学习结构先验知识，并预测未见区域的占据情况。规划模块使用RRT*算法来生成无碰撞路径，并考虑接触定位估计和占据预测的不确定性。

## 📊 实验亮点

在UR10e机械臂上进行了厨房水槽下阀门操作和杂乱架子上物体检索的实验。结果表明，该框架能够可靠地解决这些任务，与基线方法相比，任务完成时间最多可减少2倍。消融实验验证了每个模块的贡献，证明了框架的有效性。

## 🎯 应用场景

该研究成果可应用于各种视觉受限的机器人操作场景，例如：在拥挤的仓库中拣选物品、在黑暗或烟雾弥漫的环境中进行维修、在水下或太空等极端环境中进行操作。该技术具有重要的实际价值，可以提高机器人在复杂环境中的自主操作能力。

## 📄 摘要（原文）

> Robots often face manipulation tasks in environments where vision is inadequate due to clutter, occlusions, or poor lighting--for example, reaching a shutoff valve at the back of a sink cabinet or locating a light switch above a crowded shelf. In such settings, robots, much like humans, must rely on contact feedback to distinguish free from occupied space and navigate around obstacles. Many of these environments often exhibit strong structural priors--for instance, pipes often span across sink cabinets--that can be exploited to anticipate unseen structure and avoid unnecessary collisions. We present a theoretically complete and empirically efficient framework for manipulation in the blind that integrates contact feedback with structural priors to enable robust operation in unknown environments. The framework comprises three tightly coupled components: (i) a contact detection and localization module that utilizes joint torque sensing with a contact particle filter to detect and localize contacts, (ii) an occupancy estimation module that uses the history of contact observations to build a partial occupancy map of the workspace and extrapolate it into unexplored regions with learned predictors, and (iii) a planning module that accounts for the fact that contact localization estimates and occupancy predictions can be noisy, computing paths that avoid collisions and complete tasks efficiently without eliminating feasible solutions. We evaluate the system in simulation and in the real world on a UR10e manipulator across two domestic tasks--(i) manipulating a valve under a kitchen sink surrounded by pipes and (ii) retrieving a target object from a cluttered shelf. Results show that the framework reliably solves these tasks, achieving up to a 2x reduction in task completion time compared to baselines, with ablations confirming the contribution of each module.

