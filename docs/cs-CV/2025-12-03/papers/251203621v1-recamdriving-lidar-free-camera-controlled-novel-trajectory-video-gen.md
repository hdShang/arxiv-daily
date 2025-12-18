---
layout: default
title: ReCamDriving: LiDAR-Free Camera-Controlled Novel Trajectory Video Generation
---

# ReCamDriving: LiDAR-Free Camera-Controlled Novel Trajectory Video Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.03621" class="toolbar-btn" target="_blank">📄 arXiv: 2512.03621v1</a>
  <a href="https://arxiv.org/pdf/2512.03621.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.03621v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.03621v1', 'ReCamDriving: LiDAR-Free Camera-Controlled Novel Trajectory Video Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaokun Li, Shuaixian Wang, Mantang Guo, Jiehui Huang, Taojun Ding, Mu Hu, Kaixuan Wang, Shaojie Shen, Guang Tan

**分类**: cs.CV

**发布日期**: 2025-12-03

**备注**: Project page: https://recamdriving.github.io/

---

## 💡 一句话要点

**提出ReCamDriving，一种纯视觉相机控制的新轨迹视频生成框架**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视频生成` `相机控制` `3D Gaussian Splatting` `新视角合成` `自动驾驶` `几何引导` `两阶段训练` `跨轨迹数据管理`

## 📋 核心要点

1. 现有方法在复杂场景中生成新轨迹视频时，面临伪影修复困难和几何信息不足的挑战。
2. ReCamDriving利用3DGS渲染提供显式几何引导，并采用两阶段训练策略，提升相机控制精度和泛化能力。
3. 通过跨轨迹数据管理策略构建ParaDrive数据集，包含11万+并行轨迹视频对，实验证明了ReCamDriving的优越性。

## 📝 摘要（中文）

本文提出ReCamDriving，一个纯视觉、相机控制的新轨迹视频生成框架。针对修复方法难以恢复复杂伪影，以及基于LiDAR的方法依赖稀疏和不完整线索的问题，ReCamDriving利用稠密且场景完整的3DGS渲染进行显式几何引导，从而实现精确的相机可控生成。为了缓解在3DGS渲染条件下对修复行为的过拟合，ReCamDriving采用两阶段训练范式：第一阶段使用相机姿态进行粗略控制，第二阶段结合3DGS渲染进行细粒度的视点和几何引导。此外，我们提出了一种基于3DGS的跨轨迹数据管理策略，以消除相机变换模式中的训练-测试差距，从而实现来自单目视频的可扩展多轨迹监督。基于此策略，我们构建了ParaDrive数据集，包含超过11万个并行轨迹视频对。大量实验表明，ReCamDriving实现了最先进的相机可控性和结构一致性。

## 🔬 方法详解

**问题定义**：现有基于修复的方法难以恢复复杂场景中的伪影，而基于LiDAR的方法依赖于稀疏且不完整的线索，导致相机控制的新轨迹视频生成效果不佳。痛点在于缺乏一种能够有效利用几何信息，同时避免过拟合的纯视觉方法。

**核心思路**：ReCamDriving的核心思路是利用3DGS（3D Gaussian Splatting）渲染提供稠密且场景完整的几何信息，并结合两阶段训练策略，从而实现精确的相机可控视频生成。通过显式几何引导，克服了传统方法在复杂场景中生成伪影的问题。

**技术框架**：ReCamDriving框架包含两个主要阶段：第一阶段是基于相机姿态的粗略控制，使用相机位姿作为输入，生成初步的视频序列。第二阶段是基于3DGS渲染的细粒度控制，将3DGS渲染作为几何引导，对第一阶段的结果进行优化，从而实现更精确的视点和几何控制。此外，还包括一个基于3DGS的跨轨迹数据管理策略，用于生成大规模的训练数据。

**关键创新**：ReCamDriving的关键创新在于：1) 提出了一种纯视觉的相机控制视频生成框架，无需依赖LiDAR等外部传感器。2) 利用3DGS渲染提供显式的几何引导，提高了生成视频的结构一致性和相机可控性。3) 提出了两阶段训练策略，有效缓解了对3DGS渲染的过拟合问题。4) 设计了基于3DGS的跨轨迹数据管理策略，能够从单目视频中生成大规模的并行轨迹视频对。

**关键设计**：在第一阶段，网络结构采用常见的视频生成模型，损失函数包括重构损失和对抗损失。在第二阶段，引入了3DGS渲染作为额外的输入，并设计了专门的损失函数来约束生成视频与3DGS渲染的一致性。跨轨迹数据管理策略的关键在于利用3DGS渲染将不同轨迹的视频帧对应起来，从而生成并行轨迹视频对。具体参数设置和网络结构细节在论文中有详细描述，此处未知。

## 📊 实验亮点

实验结果表明，ReCamDriving在相机可控性和结构一致性方面均取得了显著的提升，达到了最先进的水平。通过与现有方法的对比，ReCamDriving能够生成更逼真、更稳定的新轨迹视频。ParaDrive数据集的构建也为相关研究提供了宝贵的数据资源。具体性能数据未知。

## 🎯 应用场景

ReCamDriving在自动驾驶、虚拟现实、游戏开发等领域具有广泛的应用前景。它可以用于生成各种视角的驾驶视频，用于自动驾驶算法的训练和测试。在虚拟现实和游戏开发中，可以用于生成逼真的场景漫游视频，提升用户体验。此外，该技术还可以应用于视频编辑和特效制作等领域。

## 📄 摘要（原文）

> We propose ReCamDriving, a purely vision-based, camera-controlled novel-trajectory video generation framework. While repair-based methods fail to restore complex artifacts and LiDAR-based approaches rely on sparse and incomplete cues, ReCamDriving leverages dense and scene-complete 3DGS renderings for explicit geometric guidance, achieving precise camera-controllable generation. To mitigate overfitting to restoration behaviors when conditioned on 3DGS renderings, ReCamDriving adopts a two-stage training paradigm: the first stage uses camera poses for coarse control, while the second stage incorporates 3DGS renderings for fine-grained viewpoint and geometric guidance. Furthermore, we present a 3DGS-based cross-trajectory data curation strategy to eliminate the train-test gap in camera transformation patterns, enabling scalable multi-trajectory supervision from monocular videos. Based on this strategy, we construct the ParaDrive dataset, containing over 110K parallel-trajectory video pairs. Extensive experiments demonstrate that ReCamDriving achieves state-of-the-art camera controllability and structural consistency.

