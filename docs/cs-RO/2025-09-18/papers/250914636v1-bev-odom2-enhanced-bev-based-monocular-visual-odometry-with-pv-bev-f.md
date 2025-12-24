---
layout: default
title: "BEV-ODOM2: Enhanced BEV-based Monocular Visual Odometry with PV-BEV Fusion and Dense Flow Supervision for Ground Robots"
---

# BEV-ODOM2: Enhanced BEV-based Monocular Visual Odometry with PV-BEV Fusion and Dense Flow Supervision for Ground Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14636" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14636v1</a>
  <a href="https://arxiv.org/pdf/2509.14636.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14636v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14636v1', 'BEV-ODOM2: Enhanced BEV-based Monocular Visual Odometry with PV-BEV Fusion and Dense Flow Supervision for Ground Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yufei Wei, Wangtao Lu, Sha Lu, Chenxiao Hu, Fuzhang Han, Rong Xiong, Yue Wang

**分类**: cs.RO

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**BEV-ODOM2：面向地面机器人的PV-BEV融合与稠密光流监督单目视觉里程计**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `单目视觉里程计` `鸟瞰图` `PV-BEV融合` `稠密光流监督` `地面机器人` `位姿估计` `深度学习`

## 📋 核心要点

1. 现有BEV方法在单目视觉里程计中面临监督信号稀疏和透视投影信息损失的挑战。
2. BEV-ODOM2通过引入稠密BEV光流监督和PV-BEV融合来增强特征表达，提升位姿估计精度。
3. 实验结果表明，BEV-ODOM2在多个数据集上取得了显著的性能提升，RTE降低了40%。

## 📝 摘要（中文）

本文提出BEV-ODOM2，一个增强的框架，旨在解决基于鸟瞰图（BEV）的单目视觉里程计（MVO）中存在的稀疏监督信号和透视-BEV投影过程中的信息损失问题，且无需额外标注。该方法引入了：（1）从3自由度（3-DoF）位姿真值构建的稠密BEV光流监督，用于像素级指导；（2）PV-BEV融合，在投影前计算相关体积，以保留6自由度（6-DoF）运动线索，同时保持尺度一致性。该框架采用三种仅从位姿数据导出的监督级别：稠密BEV光流、PV分支的5自由度（5-DoF）和最终3自由度（3-DoF）输出。增强的旋转采样进一步平衡了训练中不同的运动模式。在KITTI、NCLT、Oxford和新收集的ZJH-VO多尺度数据集上的大量评估表明，该方法达到了最先进的性能，与之前的BEV方法相比，RTE（旋转平移误差）提高了40%。ZJH-VO数据集涵盖了从地下停车场到室外广场的各种地面车辆场景，现已公开，以促进未来的研究。

## 🔬 方法详解

**问题定义**：现有的基于BEV的单目视觉里程计方法，在将图像从透视视角转换到鸟瞰视角的过程中，会造成信息的损失。同时，由于监督信号的稀疏性，导致模型学习到的特征表达能力不足，从而影响位姿估计的准确性。尤其是在地面机器人应用中，精确的里程计信息至关重要。

**核心思路**：BEV-ODOM2的核心思路是通过引入稠密的光流监督和PV-BEV融合来增强BEV特征的表达能力。稠密光流监督可以提供像素级别的运动信息，从而更有效地指导模型的学习。PV-BEV融合则可以在投影前保留更多的6自由度运动信息，避免信息损失，同时保持尺度一致性。

**技术框架**：BEV-ODOM2框架包含两个主要分支：PV（Perspective View）分支和BEV分支。PV分支处理原始图像，提取特征。BEV分支将PV分支提取的特征投影到BEV空间，并进行特征提取。在投影之前，计算PV特征和BEV特征之间的相关体积，实现PV-BEV融合。最后，利用融合后的BEV特征进行位姿估计。整个框架采用多层次的监督，包括稠密BEV光流监督、PV分支的5自由度位姿监督和最终3自由度位姿输出监督。

**关键创新**：该论文的关键创新在于：（1）提出了稠密BEV光流监督，为BEV特征的学习提供了更精细的指导信号；（2）引入了PV-BEV融合，在投影前计算相关体积，保留了更多的6自由度运动信息，避免了信息损失。与现有方法相比，BEV-ODOM2能够更有效地利用图像信息，提高位姿估计的准确性。

**关键设计**：在PV-BEV融合中，使用了相关体积来衡量PV特征和BEV特征之间的相似度。在损失函数设计中，采用了多层次的监督策略，包括稠密BEV光流损失、PV分支的5自由度位姿损失和最终3自由度位姿损失。此外，还采用了增强的旋转采样策略，以平衡训练数据中不同运动模式的分布。

## 📊 实验亮点

BEV-ODOM2在KITTI、NCLT、Oxford和ZJH-VO数据集上进行了广泛的评估，结果表明其性能优于现有的BEV方法。特别是在RTE指标上，BEV-ODOM2相比之前的BEV方法提高了40%。此外，该论文还公开了新收集的ZJH-VO数据集，为未来的研究提供了宝贵的数据资源。

## 🎯 应用场景

BEV-ODOM2在地面机器人导航、自动驾驶、智能交通系统等领域具有广泛的应用前景。精确的视觉里程计信息是这些应用的基础，可以为路径规划、环境感知和决策提供支持。该研究成果有助于提高地面机器人在复杂环境中的自主导航能力，并推动相关技术的发展。

## 📄 摘要（原文）

> Bird's-Eye-View (BEV) representation offers a metric-scaled planar workspace, facilitating the simplification of 6-DoF ego-motion to a more robust 3-DoF model for monocular visual odometry (MVO) in intelligent transportation systems. However, existing BEV methods suffer from sparse supervision signals and information loss during perspective-to-BEV projection. We present BEV-ODOM2, an enhanced framework addressing both limitations without additional annotations. Our approach introduces: (1) dense BEV optical flow supervision constructed from 3-DoF pose ground truth for pixel-level guidance; (2) PV-BEV fusion that computes correlation volumes before projection to preserve 6-DoF motion cues while maintaining scale consistency. The framework employs three supervision levels derived solely from pose data: dense BEV flow, 5-DoF for the PV branch, and final 3-DoF output. Enhanced rotation sampling further balances diverse motion patterns in training. Extensive evaluation on KITTI, NCLT, Oxford, and our newly collected ZJH-VO multi-scale dataset demonstrates state-of-the-art performance, achieving 40 improvement in RTE compared to previous BEV methods. The ZJH-VO dataset, covering diverse ground vehicle scenarios from underground parking to outdoor plazas, is publicly available to facilitate future research.

