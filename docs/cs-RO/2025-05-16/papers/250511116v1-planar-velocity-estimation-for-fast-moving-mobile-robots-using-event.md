---
layout: default
title: Planar Velocity Estimation for Fast-Moving Mobile Robots Using Event-Based Optical Flow
---

# Planar Velocity Estimation for Fast-Moving Mobile Robots Using Event-Based Optical Flow

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11116" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11116v1</a>
  <a href="https://arxiv.org/pdf/2505.11116.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11116v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11116v1', 'Planar Velocity Estimation for Fast-Moving Mobile Robots Using Event-Based Optical Flow')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liam Boyle, Jonas Kühne, Nicolas Baumann, Niklas Bastuck, Michele Magno

**分类**: cs.RO, cs.CV

**发布日期**: 2025-05-16

---

## 💡 一句话要点

**提出基于事件相机的平面速度估计方法以解决移动机器人速度估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `速度估计` `事件相机` `光流` `移动机器人` `自动驾驶` `平面运动学` `鲁棒性`

## 📋 核心要点

1. 现有的速度估计方法依赖于轮子里程计和IMU数据，通常需要强假设，难以适应复杂环境。
2. 本文提出通过事件相机获取光流，结合平面运动学进行速度估计，解耦了轮子与地面之间的牵引假设。
3. 实验结果表明，该方法在横向误差上提高了38.3%，并在高速条件下表现出色，具有实际应用潜力。

## 📝 摘要（中文）

准确的速度估计在移动机器人中至关重要，尤其是在驾驶辅助系统和自动驾驶中。传统的轮子里程计与惯性测量单元（IMU）数据融合的方法通常依赖于非滑动转向等强假设，或复杂的车辆动力学模型，这在滑溜的环境条件下往往不成立。本文提出了一种速度估计方法，该方法通过结合平面运动学与垂直于地面的事件相机光流，解耦了轮子与地面之间的牵引假设。事件相机的微秒级异步延迟和高动态范围使其在运动模糊这一常见挑战下表现出色。通过在1:10比例的自主赛车平台上进行实地实验，并与精确的运动捕捉数据进行比较，结果显示该方法不仅与现有的Event-VIO方法性能相当，还在横向误差上提高了38.3%。在高速（最高32 m/s）的定性实验进一步确认了该方法的有效性，显示出其在实际应用中的巨大潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决移动机器人速度估计中的不确定性，现有方法依赖于轮子与地面之间的牵引假设，难以适应不同环境条件下的复杂动态。

**核心思路**：通过结合事件相机获取的光流与平面运动学，本文提出了一种新的速度估计方法，避免了对轮子与地面之间牵引的假设，从而提高了在复杂环境下的适应性。

**技术框架**：该方法的整体架构包括事件相机数据的获取、光流计算、平面运动学模型的应用以及最终的速度估计输出。主要模块包括数据预处理、光流提取和速度计算。

**关键创新**：最重要的创新在于利用事件相机的高动态范围和微秒级延迟，显著提高了在高速运动下的速度估计精度，与传统方法相比，减少了对复杂动力学模型的依赖。

**关键设计**：在技术细节上，本文采用了特定的光流计算算法，并对事件相机的参数进行了优化设置，以确保在不同速度下的鲁棒性和准确性。

## 📊 实验亮点

实验结果显示，提出的方法在横向误差上提高了38.3%，与现有的Event-VIO方法性能相当。此外，在高速条件下（最高32 m/s）的定性实验进一步验证了该方法的有效性，显示出其在实际应用中的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、无人机导航和移动机器人等，能够在复杂和动态的环境中提供更为准确的速度估计。这将极大提升自动驾驶系统的安全性和可靠性，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> Accurate velocity estimation is critical in mobile robotics, particularly for driver assistance systems and autonomous driving. Wheel odometry fused with Inertial Measurement Unit (IMU) data is a widely used method for velocity estimation; however, it typically requires strong assumptions, such as non-slip steering, or complex vehicle dynamics models that do not hold under varying environmental conditions like slippery surfaces. We introduce an approach to velocity estimation that is decoupled from wheel-to-surface traction assumptions by leveraging planar kinematics in combination with optical flow from event cameras pointed perpendicularly at the ground. The asynchronous micro-second latency and high dynamic range of event cameras make them highly robust to motion blur, a common challenge in vision-based perception techniques for autonomous driving. The proposed method is evaluated through in-field experiments on a 1:10 scale autonomous racing platform and compared to precise motion capture data, demonstrating not only performance on par with the state-of-the-art Event-VIO method but also a 38.3 % improvement in lateral error. Qualitative experiments at highway speeds of up to 32 m/s further confirm the effectiveness of our approach, indicating significant potential for real-world deployment.

