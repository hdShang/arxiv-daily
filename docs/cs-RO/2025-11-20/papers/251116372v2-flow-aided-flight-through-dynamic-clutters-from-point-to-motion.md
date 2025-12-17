---
layout: default
title: Flow-Aided Flight Through Dynamic Clutters From Point To Motion
---

# Flow-Aided Flight Through Dynamic Clutters From Point To Motion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.16372" class="toolbar-btn" target="_blank">📄 arXiv: 2511.16372v2</a>
  <a href="https://arxiv.org/pdf/2511.16372.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16372v2" onclick="toggleFavorite(this, '2511.16372v2', 'Flow-Aided Flight Through Dynamic Clutters From Point To Motion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bowen Xu, Zexuan Yan, Minghao Lu, Xiyu Fan, Yi Luo, Youshen Lin, Zhiqiang Chen, Yeke Chen, Qiyuan Qiao, Peng Lu

**分类**: cs.RO

**发布日期**: 2025-11-20 (更新: 2025-12-10)

**备注**: Accepted to IEEE Robotics and Automation Letters (RA-L), November, 2025

---

## 💡 一句话要点

**提出基于点流辅助的强化学习方法，解决动态复杂环境中无人机自主飞行问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `无人机` `自主飞行` `强化学习` `点云处理` `动态环境`

## 📋 核心要点

1. 现有方法依赖于显式建模动态障碍物运动，但在高动态和遮挡场景下，计算成本高且可靠性低。
2. 本文提出一种基于点流辅助的强化学习方法，直接从点云到运动，无需目标检测、跟踪和预测。
3. 实验表明，该方法在成功率和适应性方面优于其他方案，并且能够安全地驱动真实四旋翼飞行器。

## 📝 摘要（中文）

在动态复杂环境中飞行的主要挑战在于有效感知环境动态以及生成规避障碍物的行为，同时需要考虑障碍物的运动。以往的解决方案在显式建模动态障碍物运动以进行规避方面取得了一些进展，但这种决策的关键依赖在具有遮挡的高度动态场景中耗时且不可靠。相反，本文无需引入目标检测、跟踪和预测，而是利用单线激光雷达感知，通过强化学习（RL）实现直接从点到运动的自主飞行系统。对于外部感知，从原始点云编码深度感知距离图，实现固定形状、低分辨率和细节安全。环境变化感知点流被用作从多帧观测中提取的运动特征。这两者被集成到复杂动态环境的轻量级且易于学习的表示中。对于动作生成，通过所提出的变化感知表示隐式地驱动提前避免动态威胁的行为，其中策略优化由相对运动调制的距离场指示。凭借易于部署的感知模拟和动态模型无关的加速控制，所提出的系统显示出优于其他方案的成功率和适应性，并且从模拟器导出的策略可以驱动具有安全机动的真实四旋翼飞行器。

## 🔬 方法详解

**问题定义**：论文旨在解决无人机在动态复杂环境中自主飞行的问题。现有方法通常依赖于对动态障碍物进行检测、跟踪和预测，这在高动态和遮挡环境下计算成本高昂且容易出错，导致飞行策略的不可靠性。

**核心思路**：论文的核心思路是利用强化学习，直接从原始点云数据学习飞行策略，避免了显式地建模障碍物运动。通过设计一种轻量级的环境表示，结合深度距离图和点流信息，使无人机能够感知环境的变化和动态，从而生成规避行为。

**技术框架**：整体框架包括环境感知和动作生成两个主要模块。环境感知模块首先从激光雷达获取原始点云数据，然后编码成深度感知距离图，并提取环境变化感知点流作为运动特征。这两个特征被整合为环境的表示。动作生成模块利用强化学习算法，根据环境表示生成飞行控制指令。策略优化由相对运动调制的距离场指示。

**关键创新**：最重要的技术创新在于使用点流来感知环境的动态变化，并将其与深度距离图结合，形成一种轻量级且易于学习的环境表示。这种表示方法避免了对动态障碍物进行显式建模，从而提高了在高动态环境中的鲁棒性和效率。此外，使用相对运动调制的距离场来指导策略优化，进一步提升了无人机的避障能力。

**关键设计**：论文设计了一种固定形状、低分辨率的深度感知距离图，以保证细节安全并降低计算复杂度。环境变化感知点流通过多帧观测提取，作为运动特征。强化学习算法采用动态模型无关的加速控制。具体的网络结构、损失函数和参数设置在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，该方法在模拟环境中取得了优于其他方案的成功率和适应性。更重要的是，从模拟器导出的策略可以直接驱动真实四旋翼飞行器，并实现安全的飞行机动，验证了该方法在实际应用中的可行性。

## 🎯 应用场景

该研究成果可应用于物流配送、灾害救援、环境监测等领域，使无人机能够在复杂动态环境中安全可靠地执行任务。通过降低对环境感知的计算需求，该方法有望在资源受限的无人机平台上实现更高效的自主飞行。

## 📄 摘要（原文）

> Challenges in traversing dynamic clutters lie mainly in the efficient perception of the environmental dynamics and the generation of evasive behaviors considering obstacle movement. Previous solutions have made progress in explicitly modeling the dynamic obstacle motion for avoidance, but this key dependency of decision-making is time-consuming and unreliable in highly dynamic scenarios with occlusions. On the contrary, without introducing object detection, tracking, and prediction, we empower the reinforcement learning (RL) with single LiDAR sensing to realize an autonomous flight system directly from point to motion. For exteroception, a depth sensing distance map achieving fixed-shape, low-resolution, and detail-safe is encoded from raw point clouds, and an environment change sensing point flow is adopted as motion features extracted from multi-frame observations. These two are integrated into a lightweight and easy-to-learn representation of complex dynamic environments. For action generation, the behavior of avoiding dynamic threats in advance is implicitly driven by the proposed change-aware sensing representation, where the policy optimization is indicated by the relative motion modulated distance field. With the deployment-friendly sensing simulation and dynamics model-free acceleration control, the proposed system shows a superior success rate and adaptability to alternatives, and the policy derived from the simulator can drive a real-world quadrotor with safe maneuvers.

