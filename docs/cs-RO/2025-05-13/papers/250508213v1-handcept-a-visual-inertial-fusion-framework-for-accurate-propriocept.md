---
layout: default
title: "HandCept: A Visual-Inertial Fusion Framework for Accurate Proprioception in Dexterous Hands"
---

# HandCept: A Visual-Inertial Fusion Framework for Accurate Proprioception in Dexterous Hands

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08213" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08213v1</a>
  <a href="https://arxiv.org/pdf/2505.08213.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08213v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08213v1', 'HandCept: A Visual-Inertial Fusion Framework for Accurate Proprioception in Dexterous Hands')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junda Huang, Jianshu Zhou, Honghao Guo, Yunhui Liu

**分类**: cs.RO

**发布日期**: 2025-05-13

**备注**: 8 pages, 7 figures, journal

---

## 💡 一句话要点

**提出HandCept以解决灵巧手的本体感知问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `本体感知` `灵巧手` `视觉-惯性融合` `扩展卡尔曼滤波器` `零样本学习` `机器人操作` `人机交互`

## 📋 核心要点

1. 灵巧手的本体感知面临体积和通用性限制，传统关节角度估计方法在动态环境中难以实现准确性和鲁棒性。
2. HandCept框架结合了视觉和惯性传感器，采用零样本学习和扩展卡尔曼滤波器，实时融合数据以提高关节角度估计的准确性。
3. 实验结果显示，HandCept的关节角度估计误差在2°到4°之间，且无明显漂移，显著优于现有的视觉或惯性单一方法。

## 📝 摘要（中文）

随着机器人技术向通用操作发展，灵巧手的本体感知变得愈发重要。然而，灵巧手的本体感知仍然是一个瓶颈，主要由于体积和通用性限制。本文提出了HandCept，一个新颖的视觉-惯性本体感知框架，旨在克服传统关节角度估计方法的挑战。HandCept利用零样本学习方法，结合腕部RGB-D相机和9轴IMU，通过无延迟的扩展卡尔曼滤波器实时融合，解决了动态环境中视觉和惯性测量噪声和漂移的问题。实验结果表明，HandCept的关节角度估计误差在2°到4°之间，且无明显漂移，优于仅使用视觉或惯性的方法。此外，我们验证了IMU系统的稳定性和一致性，展示了IMU之间的共同基准框架简化了系统校准。为支持模拟到现实的迁移，我们还开源了高保真渲染管道，便于在没有真实世界基准的情况下进行训练。

## 🔬 方法详解

**问题定义**：本研究旨在解决灵巧手的本体感知问题，现有方法在动态环境中面临视觉和惯性测量噪声及漂移的挑战，导致关节角度估计不准确。

**核心思路**：HandCept框架通过结合视觉和惯性传感器，采用零样本学习方法，旨在提高动态环境下的关节角度估计精度和鲁棒性。

**技术框架**：整体架构包括一个腕部安装的RGB-D相机和9轴IMU，数据通过无延迟的扩展卡尔曼滤波器进行实时融合，形成一个高效的本体感知系统。

**关键创新**：最重要的技术创新在于采用零样本学习和扩展卡尔曼滤波器的结合，显著提高了关节角度估计的准确性，避免了传统方法中的漂移问题。

**关键设计**：在设计中，IMU系统的稳定性和一致性得到了验证，采用共同基准框架简化了系统校准，确保了高精度的传感器融合。

## 📊 实验亮点

实验结果表明，HandCept在关节角度估计中实现了2°到4°的误差范围，且无明显漂移，显著优于仅使用视觉或惯性的方法，展示了其在动态环境下的优越性能。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、医疗机器人、以及人机交互等。通过提高灵巧手的本体感知能力，HandCept能够显著提升机器人在复杂环境中的操作能力，推动智能机器人技术的发展。

## 📄 摘要（原文）

> As robotics progresses toward general manipulation, dexterous hands are becoming increasingly critical. However, proprioception in dexterous hands remains a bottleneck due to limitations in volume and generality. In this work, we present HandCept, a novel visual-inertial proprioception framework designed to overcome the challenges of traditional joint angle estimation methods. HandCept addresses the difficulty of achieving accurate and robust joint angle estimation in dynamic environments where both visual and inertial measurements are prone to noise and drift. It leverages a zero-shot learning approach using a wrist-mounted RGB-D camera and 9-axis IMUs, fused in real time via a latency-free Extended Kalman Filter (EKF). Our results show that HandCept achieves joint angle estimation errors between $2^{\circ}$ and $4^{\circ}$ without observable drift, outperforming visual-only and inertial-only methods. Furthermore, we validate the stability and uniformity of the IMU system, demonstrating that a common base frame across IMUs simplifies system calibration. To support sim-to-real transfer, we also open-sourced our high-fidelity rendering pipeline, which is essential for training without real-world ground truth. This work offers a robust, generalizable solution for proprioception in dexterous hands, with significant implications for robotic manipulation and human-robot interaction.

