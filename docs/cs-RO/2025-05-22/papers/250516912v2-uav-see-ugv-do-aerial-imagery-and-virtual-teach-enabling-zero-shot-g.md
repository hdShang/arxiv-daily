---
layout: default
title: "UAV See, UGV Do: Aerial Imagery and Virtual Teach Enabling Zero-Shot Ground Vehicle Repeat"
---

# UAV See, UGV Do: Aerial Imagery and Virtual Teach Enabling Zero-Shot Ground Vehicle Repeat

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.16912" class="toolbar-btn" target="_blank">📄 arXiv: 2505.16912v2</a>
  <a href="https://arxiv.org/pdf/2505.16912.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.16912v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.16912v2', 'UAV See, UGV Do: Aerial Imagery and Virtual Teach Enabling Zero-Shot Ground Vehicle Repeat')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Desiree Fisker, Alexander Krawciw, Sven Lilge, Melissa Greeff, Timothy D. Barfoot

**分类**: cs.RO

**发布日期**: 2025-05-22 (更新: 2025-07-30)

**备注**: 8 pages, 8 figures, accepted to IROS 2025

---

## 💡 一句话要点

**提出VirT&R框架以解决GPS缺失下的UGV自主导航问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `无人驾驶` `自主导航` `神经辐射场` `环境模拟` `路径跟踪` `虚拟教学` `零-shot学习`

## 📋 核心要点

1. 现有的自主导航方法在GPS缺失的环境中表现不佳，限制了地面车辆的应用。
2. VirT&R框架通过航拍图像训练NeRF模型，生成高保真环境模拟，实现UGV的虚拟路径定义与执行。
3. 实验结果显示，VirT&R在路径跟踪精度上与LT&R相当，且无需人工教学，提升了自主性。

## 📝 摘要（中文）

本文提出了虚拟教学与重复（VirT&R）框架，这是对传统教学与重复（T&R）框架的扩展，旨在实现GPS缺失情况下的零-shot自主地面车辆导航。VirT&R利用目标环境的航拍图像训练神经辐射场（NeRF）模型，从中提取密集点云和照片纹理网格。通过NeRF生成的高保真环境模拟，UGV能够虚拟定义所需路径，并在实际环境中执行任务。实验结果表明，VirT&R在超过12公里的自主驾驶数据中表现出良好的重复性，RMSE分别为19.5厘米和18.4厘米，显示出与传统LT&R方法相似的路径跟踪性能。

## 🔬 方法详解

**问题定义**：本文旨在解决在GPS缺失环境中，地面车辆（UGV）自主导航的挑战。现有的教学与重复（T&R）方法依赖于GPS和人工路径教学，限制了其在未知环境中的应用。

**核心思路**：VirT&R框架的核心思想是利用航拍图像训练神经辐射场（NeRF）模型，生成环境的高保真模拟，从而使UGV能够在未探索的环境中自主导航，而无需人工干预。

**技术框架**：VirT&R的整体架构包括三个主要模块：首先，通过航拍图像训练NeRF模型，提取环境的点云和纹理；其次，利用生成的NeRF网格创建环境的高保真模拟；最后，UGV在模拟环境中虚拟定义路径，并在实际环境中执行任务。

**关键创新**：VirT&R的最大创新在于其实现了在GPS缺失情况下的零-shot导航能力，且无需人工路径教学，显著提高了UGV的自主性和灵活性。

**关键设计**：在技术细节上，VirT&R使用NeRF生成的教导地图进行路径规划，采用了特定的损失函数以优化点云的生成质量，并通过物理标记进行路径跟踪误差的评估。

## 📊 实验亮点

实验结果显示，VirT&R在两种不同环境中实现了19.5厘米和18.4厘米的均方根误差（RMSE），与LT&R方法相当，且最大误差分别为39.4厘米和47.6厘米。这表明VirT&R在路径跟踪精度上具有竞争力，且无需人工干预，提升了自主性。

## 🎯 应用场景

该研究的潜在应用领域包括无人驾驶汽车、农业机器人、灾后救援等场景，尤其是在GPS信号弱或缺失的环境中，VirT&R框架能够显著提升地面车辆的自主导航能力，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> This paper presents Virtual Teach and Repeat (VirT&R): an extension of the Teach and Repeat (T&R) framework that enables GPS-denied, zero-shot autonomous ground vehicle navigation in untraversed environments. VirT&R leverages aerial imagery captured for a target environment to train a Neural Radiance Field (NeRF) model so that dense point clouds and photo-textured meshes can be extracted. The NeRF mesh is used to create a high-fidelity simulation of the environment for piloting an unmanned ground vehicle (UGV) to virtually define a desired path. The mission can then be executed in the actual target environment by using NeRF-generated point cloud submaps associated along the path and an existing LiDAR Teach and Repeat (LT&R) framework. We benchmark the repeatability of VirT&R on over 12 km of autonomous driving data using physical markings that allow a sim-to-real lateral path-tracking error to be obtained and compared with LT&R. VirT&R achieved measured root mean squared errors (RMSE) of 19.5 cm and 18.4 cm in two different environments, which are slightly less than one tire width (24 cm) on the robot used for testing, and respective maximum errors were 39.4 cm and 47.6 cm. This was done using only the NeRF-derived teach map, demonstrating that VirT&R has similar closed-loop path-tracking performance to LT&R but does not require a human to manually teach the path to the UGV in the actual environment.

