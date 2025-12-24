---
layout: default
title: A Tightly Coupled IMU-Based Motion Capture Approach for Estimating Multibody Kinematics and Kinetics
---

# A Tightly Coupled IMU-Based Motion Capture Approach for Estimating Multibody Kinematics and Kinetics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08193" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08193v1</a>
  <a href="https://arxiv.org/pdf/2505.08193.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08193v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08193v1', 'A Tightly Coupled IMU-Based Motion Capture Approach for Estimating Multibody Kinematics and Kinetics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hassan Osman, Daan de Kanter, Jelle Boelens, Manon Kok, Ajay Seth

**分类**: cs.RO, eess.SY

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出紧耦合IMU运动捕捉方法以解决多体动力学估计问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `惯性测量单元` `运动捕捉` `多体动力学` `迭代扩展卡尔曼滤波器` `状态估计` `康复治疗` `机器人控制`

## 📋 核心要点

1. 现有IMU运动捕捉方法面临磁干扰和漂移误差等挑战，限制了其在临床和家庭环境中的应用。
2. 本文提出的紧耦合运动捕捉方法通过IEKF将IMU测量与多体动态模型直接集成，提升了运动学和动力学的估计精度。
3. 实验结果表明，该方法在摆和Kuka机器人上的关节角度最大均方根差分别为3.75度和3.24度，显示出显著的性能提升。

## 📝 摘要（中文）

惯性测量单元（IMU）使得在实验室之外的多体运动捕捉成为可能，适用于诊断运动障碍和支持康复。然而，IMU测量中的磁干扰和漂移误差等挑战限制了其更广泛的应用。本文提出了一种紧耦合的运动捕捉方法，通过迭代扩展卡尔曼滤波器（IEKF）直接将IMU测量与多体动态模型集成，以同时估计系统的运动学和动力学。该方法仅利用加速度计和陀螺仪数据，显著提高了基于IMU的状态估计精度，并允许整合其他传感器数据以进一步提升准确性。通过与高精度的真实数据进行验证，结果显示该方法在多个实验中表现出色。

## 🔬 方法详解

**问题定义**：本文旨在解决IMU在多体运动捕捉中的应用问题，尤其是由于磁干扰和漂移误差导致的测量不准确。现有方法在动态环境中的表现不佳，限制了其临床应用。

**核心思路**：论文提出的紧耦合方法通过IEKF将IMU数据与多体动态模型结合，利用运动学和动力学特性来提高状态估计的准确性。此设计允许在不依赖于复杂传感器的情况下，提升IMU的使用效果。

**技术框架**：整体架构包括IMU数据采集、IEKF状态估计、运动学和动力学约束的应用，以及与其他传感器数据的整合。主要模块包括数据预处理、状态预测、状态更新和结果输出。

**关键创新**：最重要的创新在于将IMU测量与多体动态模型紧耦合，通过IEKF实现了运动学和动力学的同时估计，显著提高了估计精度。与传统方法相比，该方法更有效地处理了IMU测量中的误差。

**关键设计**：关键设计包括IEKF的参数设置和运动学、动力学约束的实现。损失函数的设计确保了估计结果的准确性，并允许灵活整合其他传感器数据，如光学运动捕捉和关节扭矩读数。

## 📊 实验亮点

实验结果显示，摆的关节角度计算最大均方根差为3.75度，相较于光学运动捕捉的逆运动学标准，Kuka机器人关节角度的最大均方根差为3.24度，显示出该方法在动态环境中具有优越的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括运动医学、康复治疗和运动训练等。通过提供更准确的运动捕捉数据，该方法能够帮助医生和治疗师更好地评估患者的运动能力，并制定个性化的康复计划。此外，未来可能扩展到机器人控制和人机交互等领域，提升智能系统的运动理解能力。

## 📄 摘要（原文）

> Inertial Measurement Units (IMUs) enable portable, multibody motion capture (MoCap) in diverse environments beyond the laboratory, making them a practical choice for diagnosing mobility disorders and supporting rehabilitation in clinical or home settings. However, challenges associated with IMU measurements, including magnetic distortions and drift errors, complicate their broader use for MoCap. In this work, we propose a tightly coupled motion capture approach that directly integrates IMU measurements with multibody dynamic models via an Iterated Extended Kalman Filter (IEKF) to simultaneously estimate the system's kinematics and kinetics. By enforcing kinematic and kinetic properties and utilizing only accelerometer and gyroscope data, our method improves IMU-based state estimation accuracy. Our approach is designed to allow for incorporating additional sensor data, such as optical MoCap measurements and joint torque readings, to further enhance estimation accuracy. We validated our approach using highly accurate ground truth data from a 3 Degree of Freedom (DoF) pendulum and a 6 DoF Kuka robot. We demonstrate a maximum Root Mean Square Difference (RMSD) in the pendulum's computed joint angles of 3.75 degrees compared to optical MoCap Inverse Kinematics (IK), which serves as the gold standard in the absence of internal encoders. For the Kuka robot, we observe a maximum joint angle RMSD of 3.24 degrees compared to the Kuka's internal encoders, while the maximum joint angle RMSD of the optical MoCap IK compared to the encoders was 1.16 degrees. Additionally, we report a maximum joint torque RMSD of 2 Nm in the pendulum compared to optical MoCap Inverse Dynamics (ID), and 3.73 Nm in the Kuka robot relative to its internal torque sensors.

