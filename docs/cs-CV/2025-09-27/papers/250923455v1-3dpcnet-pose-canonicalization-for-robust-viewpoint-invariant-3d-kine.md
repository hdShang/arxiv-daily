---
layout: default
title: "3DPCNet: Pose Canonicalization for Robust Viewpoint-Invariant 3D Kinematic Analysis from Monocular RGB cameras"
---

# 3DPCNet: Pose Canonicalization for Robust Viewpoint-Invariant 3D Kinematic Analysis from Monocular RGB cameras

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23455" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23455v1</a>
  <a href="https://arxiv.org/pdf/2509.23455.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23455v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23455v1', '3DPCNet: Pose Canonicalization for Robust Viewpoint-Invariant 3D Kinematic Analysis from Monocular RGB cameras')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tharindu Ekanayake, Constantino Álvarez Casado, Miguel Bordallo López

**分类**: cs.CV, cs.LG

**发布日期**: 2025-09-27

**备注**: 8 pages, 6 figures, 1 table, 21 references, conference, Code available at: https://github.com/tharindu326/3DPCNet

---

## 💡 一句话要点

**提出3DPCNet以解决单目RGB摄像头下的3D姿态标准化问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `3D姿态估计` `单目摄像头` `运动分析` `自监督学习` `图卷积网络` `变换器` `视角标准化` `健康监测`

## 📋 核心要点

1. 现有的单目3D姿态估计方法生成的骨架依赖于摄像机视角，导致运动信号的比较分析变得复杂。
2. 论文提出的3DPCNet模块能够将输入的3D姿态校正为一致的身体中心标准框架，增强了姿态的可比性。
3. 在MM-Fi基准测试中，3DPCNet显著降低了平均旋转误差和每个关节位置的误差，验证了其有效性。

## 📝 摘要（中文）

单目3D姿态估计器生成以相机为中心的骨架，导致视角依赖的运动信号，给健康和运动科学等应用的比较分析带来困难。我们提出了3DPCNet，这是一个紧凑的、与估计器无关的模块，直接对3D关节坐标进行处理，将任何输入姿态校正为一致的、以身体为中心的标准框架。该模型通过门控交叉注意机制融合了图卷积网络的局部骨架特征和变换器的全局上下文。模型预测的连续6D旋转被映射到SO(3)矩阵以对齐姿态。在MM-Fi数据集上进行自监督训练，使用合成旋转姿态，通过复合损失确保准确的旋转和姿态重建。3DPCNet在MM-Fi基准上将平均旋转误差从20°以上降低到3.4°，每个关节位置的平均误差从约64毫米降低到47毫米。对TotalCapture数据集的定性评估进一步证明了我们的方法能够从视频中生成与真实IMU传感器数据强视觉对应的加速度信号，确认我们的模块消除了视角变异性，从而实现物理上合理的运动分析。

## 🔬 方法详解

**问题定义**：本论文旨在解决单目RGB摄像头下3D姿态估计的视角依赖性问题。现有方法生成的姿态信号难以进行比较分析，尤其在健康和运动科学领域。

**核心思路**：3DPCNet通过将输入的3D关节坐标转换为一致的身体中心标准框架，消除了视角变异性。该方法结合了局部和全局特征，确保了姿态的准确性和一致性。

**技术框架**：3DPCNet的整体架构包括一个混合编码器，利用图卷积网络提取局部骨架特征，并通过变换器获取全局上下文。模型通过门控交叉注意机制融合这些特征，最终预测出6D旋转。

**关键创新**：最重要的创新在于提出了一个估计器无关的模块，能够直接处理3D关节坐标，并通过自监督学习进行训练。这种方法与现有的依赖于特定估计器的技术有本质区别。

**关键设计**：模型使用复合损失函数进行训练，确保了旋转的准确性和姿态的重建。通过合成旋转姿态进行自监督训练，优化了模型的性能。

## 📊 实验亮点

在MM-Fi基准测试中，3DPCNet将平均旋转误差从20°以上降低至3.4°，每个关节位置的平均误差从约64毫米降低至47毫米，显示出显著的性能提升。此外，定性评估表明其生成的加速度信号与真实IMU传感器数据具有强视觉对应性。

## 🎯 应用场景

该研究具有广泛的应用潜力，特别是在健康监测、运动分析和虚拟现实等领域。通过消除视角依赖性，3DPCNet能够提供更一致和可靠的运动分析，帮助研究人员和专业人士更好地理解和评估运动表现。

## 📄 摘要（原文）

> Monocular 3D pose estimators produce camera-centered skeletons, creating view-dependent kinematic signals that complicate comparative analysis in applications such as health and sports science. We present 3DPCNet, a compact, estimator-agnostic module that operates directly on 3D joint coordinates to rectify any input pose into a consistent, body-centered canonical frame. Its hybrid encoder fuses local skeletal features from a graph convolutional network with global context from a transformer via a gated cross-attention mechanism. From this representation, the model predicts a continuous 6D rotation that is mapped to an $SO(3)$ matrix to align the pose. We train the model in a self-supervised manner on the MM-Fi dataset using synthetically rotated poses, guided by a composite loss ensuring both accurate rotation and pose reconstruction. On the MM-Fi benchmark, 3DPCNet reduces the mean rotation error from over 20$^{\circ}$ to 3.4$^{\circ}$ and the Mean Per Joint Position Error from ~64 mm to 47 mm compared to a geometric baseline. Qualitative evaluations on the TotalCapture dataset further demonstrate that our method produces acceleration signals from video that show strong visual correspondence to ground-truth IMU sensor data, confirming that our module removes viewpoint variability to enable physically plausible motion analysis.

