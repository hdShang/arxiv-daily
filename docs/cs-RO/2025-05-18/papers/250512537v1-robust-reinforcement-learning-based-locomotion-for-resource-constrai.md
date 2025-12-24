---
layout: default
title: Robust Reinforcement Learning-Based Locomotion for Resource-Constrained Quadrupeds with Exteroceptive Sensing
---

# Robust Reinforcement Learning-Based Locomotion for Resource-Constrained Quadrupeds with Exteroceptive Sensing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12537" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12537v1</a>
  <a href="https://arxiv.org/pdf/2505.12537.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12537v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12537v1', 'Robust Reinforcement Learning-Based Locomotion for Resource-Constrained Quadrupeds with Exteroceptive Sensing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Davide Plozza, Patricia Apostol, Paul Joseph, Simon Schläpfer, Michele Magno

**分类**: cs.RO, eess.SY

**发布日期**: 2025-05-18

**备注**: This paper has been accepted for publication at the IEEE International Conference on Robotics and Automation (ICRA), Atlanta 2025. The code is available at github.com/ETH-PBL/elmap-rl-controller

---

## 💡 一句话要点

**提出基于强化学习的稳健步态控制以解决资源受限四足机器人在复杂地形中的行走问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `四足机器人` `强化学习` `步态控制` `高程映射` `资源受限` `深度传感器` `视觉惯性里程计` `动态性能`

## 📋 核心要点

1. 现有方法在复杂地形上行走时计算需求高，导致资源受限的四足机器人难以实时感知地形。
2. 本文提出的控制器结合强化学习与实时高程映射，能够在资源受限的环境中有效进行步态控制。
3. 实验结果显示，该控制器在不同高度的台阶上均表现出色，成功率高达80%，并且在速度跟踪方面也达到了良好效果。

## 📝 摘要（中文）

紧凑型四足机器人在现实场景中的应用越来越广泛，但在不平坦地形上的实时行走仍然面临挑战，尤其是地形感知的高计算需求。本文提出了一种基于强化学习的外部感知步态控制器，专为资源受限的小型四足机器人设计，能够在复杂地形中实时利用高程映射。我们同时训练策略和状态估计器，为高程映射提供里程计信息，并可与视觉惯性里程计（VIO）融合。实验表明，所提控制器能够顺利跨越17.5厘米高的台阶，并在22.5厘米高的台阶上实现80%的成功率，且在有无VIO的情况下均表现良好。该控制器在前进和偏航速度跟踪方面也表现出色，分别可达1.0米/秒和1.5弧度/秒。我们已将训练代码开源于github.com/ETH-PBL/elmap-rl-controller。

## 🔬 方法详解

**问题定义**：本文旨在解决资源受限的四足机器人在复杂地形上实时行走的挑战，现有方法在地形感知上计算需求过高，影响了机器人的行走能力。

**核心思路**：提出一种基于强化学习的步态控制器，结合实时高程映射和深度传感器选择，能够在资源有限的情况下实现稳健的行走。

**技术框架**：整体架构包括策略训练和状态估计器的并行训练，提供高程映射所需的里程计信息，支持与视觉惯性里程计（VIO）的融合。

**关键创新**：最重要的创新在于通过额外的飞行时间传感器来增强系统的鲁棒性，即使在没有VIO的情况下也能保持稳定，释放计算资源。

**关键设计**：在参数设置上，选择合适的深度传感器以优化高程映射，同时设计损失函数以平衡策略和状态估计的训练效果。

## 📊 实验亮点

实验结果显示，所提控制器能够顺利跨越高达17.5厘米的台阶，并在22.5厘米的台阶上实现80%的成功率，表现出色。此外，前进和偏航速度的跟踪精度分别达到了1.0米/秒和1.5弧度/秒，显示出良好的动态性能。

## 🎯 应用场景

该研究的潜在应用领域包括搜索与救援、环境监测以及人机协作等场景。通过提高四足机器人在复杂环境中的行走能力，能够更好地适应实际应用需求，推动机器人技术的进一步发展。

## 📄 摘要（原文）

> Compact quadrupedal robots are proving increasingly suitable for deployment in real-world scenarios. Their smaller size fosters easy integration into human environments. Nevertheless, real-time locomotion on uneven terrains remains challenging, particularly due to the high computational demands of terrain perception. This paper presents a robust reinforcement learning-based exteroceptive locomotion controller for resource-constrained small-scale quadrupeds in challenging terrains, which exploits real-time elevation mapping, supported by a careful depth sensor selection. We concurrently train both a policy and a state estimator, which together provide an odometry source for elevation mapping, optionally fused with visual-inertial odometry (VIO). We demonstrate the importance of positioning an additional time-of-flight sensor for maintaining robustness even without VIO, thus having the potential to free up computational resources. We experimentally demonstrate that the proposed controller can flawlessly traverse steps up to 17.5 cm in height and achieve an 80% success rate on 22.5 cm steps, both with and without VIO. The proposed controller also achieves accurate forward and yaw velocity tracking of up to 1.0 m/s and 1.5 rad/s respectively. We open-source our training code at github.com/ETH-PBL/elmap-rl-controller.

