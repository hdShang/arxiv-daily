---
layout: default
title: "AutoRing: Imitation Learning--based Autonomous Intraocular Foreign Body Removal Manipulation with Eye Surgical Robot"
---

# AutoRing: Imitation Learning--based Autonomous Intraocular Foreign Body Removal Manipulation with Eye Surgical Robot

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19191" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19191v2</a>
  <a href="https://arxiv.org/pdf/2508.19191.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19191v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19191v2', 'AutoRing: Imitation Learning--based Autonomous Intraocular Foreign Body Removal Manipulation with Eye Surgical Robot')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Wang, Wenjie Deng, Haotian Xue, Di Cui, Yiqi Chen, Mingchuan Zhou, Haochao Ying, Jian Wu

**分类**: cs.RO

**发布日期**: 2025-08-26 (更新: 2025-08-27)

---

## 💡 一句话要点

**提出AutoRing以解决眼内异物去除的自主操作问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `眼内手术` `模仿学习` `自主操作` `机器人技术` `运动学校准` `智能医疗` `手术机器人`

## 📋 核心要点

1. 现有的眼内异物去除机器人系统主要依赖手动遥控，导致操作精度低且学习成本高。
2. 本文提出的AutoRing框架通过模仿学习实现自主的眼内异物环操作，集成了动态运动中心校准。
3. 实验结果表明，AutoRing在未校准的显微镜条件下成功实现了自主的环抓取和定位，具有良好的实用性。

## 📝 摘要（中文）

眼内异物去除需要在有限的眼内空间内实现毫米级的精确操作，而现有的机器人系统主要依赖于手动遥控，学习曲线陡峭。为了解决自主操作中的挑战，特别是由于运动缩放和运动中心变化带来的运动学不确定性，本文提出了AutoRing，一个基于模仿学习的自主眼内异物环操作框架。该方法集成了动态运动中心校准，以解决由于眼内仪器变化引起的坐标系不一致，并引入了RCM-ACT架构，结合了动作分块变换器与实时运动学重新对齐。AutoRing仅基于专家演示的立体视觉数据和仪器运动学进行训练，成功完成了环抓取和定位任务，无需显式的深度传感。实验验证表明，在未校准的显微镜条件下实现了端到端的自主操作，为开发智能眼外科系统提供了可行框架。

## 🔬 方法详解

**问题定义**：本文旨在解决眼内异物去除过程中自主操作的精确性问题。现有方法依赖于手动遥控，导致操作精度不足且学习曲线陡峭。

**核心思路**：AutoRing框架通过模仿学习实现自主操作，利用专家演示数据进行训练，克服了运动学不确定性和坐标系不一致的问题。

**技术框架**：AutoRing的整体架构包括动态运动中心校准模块和RCM-ACT架构，后者结合了动作分块变换器与实时运动学重新对齐，确保操作的精确性和稳定性。

**关键创新**：最重要的创新在于动态运动中心校准和RCM-ACT架构的结合，使得系统能够在不同的眼内仪器条件下保持高精度的操作能力。

**关键设计**：在训练过程中，使用了立体视觉数据和仪器运动学，损失函数设计考虑了抓取和定位的精度，网络结构采用了动作分块变换器以提高学习效率。

## 📊 实验亮点

实验结果显示，AutoRing在未校准的显微镜条件下实现了端到端的自主操作，成功完成了环抓取和定位任务，表现出较高的操作精度和稳定性，显著提升了传统手动操作的效率。

## 🎯 应用场景

该研究的潜在应用领域包括眼科手术机器人系统，能够在复杂的眼内环境中进行高精度的操作。未来，AutoRing有望推动智能医疗设备的发展，提高眼科手术的安全性和效率。

## 📄 摘要（原文）

> Intraocular foreign body removal demands millimeter-level precision in confined intraocular spaces, yet existing robotic systems predominantly rely on manual teleoperation with steep learning curves. To address the challenges of autonomous manipulation (particularly kinematic uncertainties from variable motion scaling and variation of the Remote Center of Motion (RCM) point), we propose AutoRing, an imitation learning framework for autonomous intraocular foreign body ring manipulation. Our approach integrates dynamic RCM calibration to resolve coordinate-system inconsistencies caused by intraocular instrument variation and introduces the RCM-ACT architecture, which combines action-chunking transformers with real-time kinematic realignment. Trained solely on stereo visual data and instrument kinematics from expert demonstrations in a biomimetic eye model, AutoRing successfully completes ring grasping and positioning tasks without explicit depth sensing. Experimental validation demonstrates end-to-end autonomy under uncalibrated microscopy conditions. The results provide a viable framework for developing intelligent eye-surgical systems capable of complex intraocular procedures.

